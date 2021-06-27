import QTBudgetGui
from sqlalchemy.sql.coercions import cls
from sqlalchemy import update, values, func
from models import engine, Account, Session, Transaction, Account_Period, Setting
import csv
from datetime import date
from copy import copy
from decimal import Decimal

class Utility():
    def __init__(self):
        pass

    def countRows(self, field):
        session=Session()
        count=session.query(func.count(field)).scalar()
        return count

    def accounts(self):
        session=Session()
        accountsDict={}
        for account in session.query(Account).order_by(Account.name):
            accountsDict[account.account_id]=account
        return accountsDict

    def insertTransaction(self, trans):
        session=Session()
        session.add(trans)
        session.commit()

    def updateTransaction(self, trans):
        pass

    def updateAccount(self, account):
        session=Session()
        session.query(Account).filter(Account.account_id==account.account_id).update({
            Account.name: account.name,
            Account.budget: account.budget,
            Account.auto_post: account.auto_post,
            Account.ie_type: account.ie_type,
            Account.category: account.category
        })
        session.commit()

    def insertAccount(self, account):
        session=Session()
        session.add(account)
        session.commit()

    def insertSales(self, account):

        period=Period('2000-01')
        current_period=period.current()

        sales=Account_Period()
        sales.amount=0.00
        sales.budget=account.budget
        sales.period=current_period
        sales.account_id=None

        session=Session()
        for accountx in session.query(Account).filter(Account.name==account.name):
            sales.account_id=accountx.account_id

        session.add(sales)
        session.commit()

    def updateSales(self, trans):
        session=Session()
        for sales in session.query(Account_Period).filter(Account_Period.account_id==trans.account_id, Account_Period.period==trans.period):
            sales.amount+=Decimal(trans.amount)
        session.add(trans)
        session.commit()


class Settings():
    def __init__(self):
        self.lePeriod=None

    def updatePeriod(self, current_period):
        session=Session()
        setting=Setting()
        session.query(Setting).filter(Setting.key=='current_period').update({Setting.value: current_period})
        session.commit()

    def form(self, lePeriod):
        self.lePeriod=lePeriod
        period=Period('2000-01')
        self.lePeriod.setText(period.current())

    def saveSettings(self):
        new_period=self.lePeriod.text()
        self.updatePeriod(new_period)

class MonthEnd():
    def __init__(self):
        self.leNextPeriod=None
        self.nextPeriod=None
    def form(self, leNextPeriod):
        self.leNextPeriod=leNextPeriod
        period=Period('2000-01')
        period=Period(period.current())
        period.next()
        self.nextPeriod=period.period
        self.leNextPeriod.setText(self.nextPeriod)

    def execute(self):
        utility=Utility()
        accountsDict=utility.accounts()

        session=Session()
        # for all accounts, create sales files
        for (account_id, account) in accountsDict.items():
            sales=Account_Period()
            sales.budget=account.budget
            sales.period=self.nextPeriod
            sales.amount=account.auto_post
            sales.account_id=account_id

            session.add(sales)
            session.commit()
        # for all accounts with auto pay, create transactions
            if account.auto_post!=0:
                trans=Transaction()
                trans.trans_date=date.today()
                trans.period=self.nextPeriod
                trans.amount=account.auto_post
                trans.account_id=account_id

                session.add(trans)
                session.commit()

        # update settings with new period
        setting=Setting()
        setting.updatePeriod(self.nextPeriod)


class Form():
    def __init__(self, statusBar):
        self.SB=statusBar
        self.cbAccount=None
        self.cbCategory=None
        self.leBudgetAmount=None
        self.leAutoPayAmount=None
        self.leIncomeExpenseFlag=None
        self.leDate=None
        self.leAmount=0
        self.account_id=None

    def newAccount(self, cbAccount,
                            cbCategory,
                            leBudgetAmount,
                            leAutoPayAmount,
                            leIncomeExpenseFlag):

        self.cbAccount=cbAccount
        self.cbCategory=cbCategory
        self.leBudgetAmount=leBudgetAmount
        self.leAutoPayAmount=leAutoPayAmount
        self.leIncomeExpenseFlag=leIncomeExpenseFlag

        self.SB.clearMessage()
        self.initializeAccountForm()

    def initializeAccountForm(self):

        utility=Utility()
        accountsDict=utility.accounts()
        categories=[]
        self.cbAccount.clear()
        for account in accountsDict.values():
            self.cbAccount.addItem(account.name)
            if account.category not in categories:
                categories.append(account.category)
        for category in categories:
            self.cbCategory.addItem(category)
        self.leBudgetAmount.setText('0.00')
        self.leAutoPayAmount.setText('0.00')
        self.leIncomeExpenseFlag.setText('E')
        self.account_id=None

    def Account(self, name):
        print(name)
        session=Session()
        account=Account()
        for account in session.query(Account).filter(Account.name==name):
            print(account)
        self.account_id=account.account_id
        self.cbAccount.clear()
        self.cbAccount.addItem(account.name)
        self.cbCategory.clear()
        self.cbCategory.addItem(account.category)
        self.leBudgetAmount.setText(str(account.budget))
        self.leAutoPayAmount.setText(str(account.auto_post))
        self.leIncomeExpenseFlag.setText(account.ie_type)

    def validateAccount(self, account):
        if not (account.ie_type=='E' or account.ie_type=='I'):
            return (False, 'Must be Income or Expense type')

        return (True, '')

    def saveAccount(self):
        account=Account()
        account.account_id=self.account_id
        account.name=self.cbAccount.currentText()
        account.category=self.cbCategory.currentText()
        account.budget=self.leBudgetAmount.text()
        account.auto_post=self.leAutoPayAmount.text()
        account.ie_type=self.leIncomeExpenseFlag.text()

        (result, message)=self.validateAccount(account)
        if result==False:
            self.SB.showMessage(message)
        else:

            accountx=copy(account)

            utility=Utility()
            if account.account_id==None:
                utility.insertAccount(account)
                utility.insertSales(accountx)
            else:
                utility.updateAccount(account)

            self.initializeAccountForm()
            self.SB.showMessage('Account was saved')

    def newTransaction(self,
                       cbAccount,
                       leDate,
                       leAmount):
        self.cbAccount=cbAccount
        self.leDate=leDate
        self.leAmount=leAmount

        self.initializeTransactionForm()

    def initializeTransactionForm(self):

        utility=Utility()
        accountsDict=utility.accounts()
        for account in accountsDict.values():
            self.cbAccount.addItem(account.name)
        self.leDate.setText(str(date.today()))
        self.leAmount.setText('0.00')

    def Transaction(self):
        pass

    def validateTransaction(self, trans):
        if float(trans.amount)==0:
            return (False, 'Please enter a non-zero amount')

        return (True, '')

    def saveTransaction(self):

        period=Period('2000-01')
        current_period=period.current()

        session=Session()
        trans=Transaction()
        for account in session.query(Account).filter(Account.name==self.cbAccount.currentText()):
            trans.account_id=account.account_id

        trans.trans_date=self.leDate.text()
        trans.period=current_period
        trans.amount=self.leAmount.text()

        (result, message)=self.validateTransaction(trans)
        if result:

            transx=copy(trans)

            utility=Utility()
            utility.insertTransaction(trans)

            utility.updateSales(transx)

            self.initializeTransactionForm()
            self.SB.showMessage('Transaction was saved')

        else:
            self.SB.showMessage(message)

class Report():
    def __init__(self):
        pass
    def accountReport(self, reportWidget):

        rows=[]
        session=Session()
        hdr='<table class="table">'
        rows.append(hdr)
        hdr=f"<tr><th>{'Account':<20}</th><th>{'Category':<20}</th><th>{'Budget':>12}</th><th>{'Auto Post':>12}</th><th>{'Income/Expense':<10}</th></tr>"
        rows.append(hdr)
        for account in session.query(Account).order_by(Account.name):
            #line=f"{account.name:<20}{account.category:<20}{account.budget:>12}{account.auto_post:>12} {account.ie_type:<10}"
            line=f"<tr><td>{account.name}</td><td>{account.category}</td><td>{account.budget:.2f}</td><td>{account.auto_post:.2f}</td><td>{account.ie_type}</td></tr>"
            rows.append(line)
        rows.append("</table>")
        reportWidget.setHtml('\n'.join(rows))

    def periodReport(self, reportWidget):
        utility=Utility()
        accountsDict=utility.accounts()
        period=Period('2000-01')
        current_period=period.current()
        session=Session()
        rows=[]
        rows.append('<table>')
        hdr="<tr><th>Account Name</th><th>Amount Spent</th><th>Budget Amount</th><th>Net Balance</th></tr>"
        rows.append(hdr)
        for sales in session.query(Account_Period).filter(Account_Period.period==current_period).order_by(Account_Period.account_id.name):
            account_id=sales.account_id
            account=accountsDict[account_id]
            line=f"<tr><td>{account.name}</td><td>{sales.amount:.2f}</td><td>{sales.budget:.2f}</td><td>{-sales.amount+sales.budget:.2f}</td></tr>"
            rows.append(line)
        rows.append('</table>')
        reportWidget.setHtml('\n'.join(rows))

    def salesReport(self, reportWidget):
        rows=[]
        session=Session()
        hdr='<table>'
        rows.append(hdr)
        hdr="<tr><th>Accounting Period</th><th>Amount Spent</th><th>Budget Amount</th><th>Net Balance</th></tr>"
        rows.append(hdr)
        periodTotal=0
        budgetTotal=0
        currPeriod="xx"
        for sales in session.query(Account_Period).order_by(Account_Period.period.desc()):
            period=sales.period
            if period!=currPeriod:
                if currPeriod!='xx':
                    line=f"<tr><td>{currPeriod}</td><td>{periodTotal:.2f}</td><td>{budgetTotal:.2f}</td><td>{-periodTotal+budgetTotal:.2f}</td></tr>"
                    rows.append(line)
                currPeriod=period
                periodTotal=0
                budgetTotal=0
            periodTotal+=sales.amount
            budgetTotal+=sales.budget
        line = f"<tr><td>{currPeriod}</td><td>{periodTotal:.2f}</td><td>{budgetTotal:.2f}</td><td>{periodTotal - budgetTotal:.2f}</td></tr>"
        rows.append(line)
        rows.append("</table>")
        reportWidget.setHtml('\n'.join(rows))


class Period():
    def __init__(self, period):
        self._period=period

    def current(self):
        session=Session()
        setting=Setting()
        for setting in session.query(Setting).filter(Setting.key=='current_period'):
            current_period=setting.value
        return current_period
    def next(self):
        (year, _, month)=self.period.partition('-')
        month=int(month)+1
        if month>12:
            month=1
            year=int(year)+1
        self.period=f"{year}-{month:02}"
    def month(self):
        (year, _, month) = self.period.partition('-')
        return int(month)
    def year(self):
        (year, _, month) = self.period.partition('-')
        return int(year)
    @property
    def period(self):
        return self._period
    @period.setter
    def period(self, value):
        self._period=value

class Import():
    DIR="CSV"
    def __init__(self, pbImport):
        self.pbImport=pbImport
    def importAccounts(self):
        utility = Utility()
        if utility.countRows(Account.account_id) > 0:
            return
        print('importing accounts...')
        self.pbImport.setValue(0)
        n=0
        with open('CSV\\accounts.csv', 'r') as file:
            reader = csv.reader(file)
            csvList = list(reader)
            increment = 100 / len(csvList)
            for row in csvList:
                n+=1
                self.pbImport.setValue(n*increment)
                if n==1:
                    continue
                session=Session()
                account=Account()
                account.name=row[1]
                account.ie_type='E'
                account.budget=row[2]
                account.auto_post=0.00
                account.category=''
                session.add(account)
                session.commit()
        print(n, 'accounts were imported')
    def importSales(self):
        utility = Utility()
        if utility.countRows(Account_Period.id) > 0:
            return
        print('importing sales...')
        self.pbImport.setValue(0)
        n = 0
        with open('CSV\\sales.csv', 'r') as file:
            reader = csv.reader(file)
            csvList = list(reader)
            increment = 100 / len(csvList)
            for row in csvList:
                n += 1
                self.pbImport.setValue(n*increment)
                if n == 1:
                    continue
                session = Session()
                sales = Account_Period()
                name = row[0]
                for account in session.query(Account).filter(Account.name == name):
                    sales.account_id=account.account_id
                sales.period=row[1]
                sales.amount=float(row[3])
                sales.budget=float(row[2])
                session.add(sales)
                session.commit()
        print(n, 'sales were imported')
    def importTrans(self):
        utility=Utility()
        count=utility.countRows(Transaction.trans_id)
        if count>0:
            return
        print('importing transactions...')
        self.pbImport.setValue(0)

        n = 0
        with open('CSV\\trans.csv', 'r') as file:
            reader = csv.reader(file)
            csvList=list(reader)
            increment=100/len(csvList)
            for row in csvList:
                n += 1
                self.pbImport.setValue(n*increment)
                if n == 1:
                    continue
                session = Session()
                trans = Transaction()
                name = row[0]
                for account in session.query(Account).filter(Account.name==name):
                    trans.account_id=account.account_id
                trans.period=row[1]
                trans.amount=float(row[3])
                trans.trans_date=row[2]
                session.add(trans)
                session.commit()
        print(n, 'transactions were imported')
    def buildPath(self):
        path=cls.DIR
        return path