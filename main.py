
from busrules import Import, Report, Form, Settings, MonthEnd

import sys

#

from PySide2.QtWidgets import QApplication, QMainWindow

from QTBudgetGui import Ui_MainWindow


#

class MainWindow(QMainWindow, Ui_MainWindow):

    #

    def __init__(self):
        #

        QMainWindow.__init__(self)

        #

        self.setupUi(self)

        self.importClass = Import(self.pbImport)
        self.reportClass=Report()
        self.formClass=Form(self.statusbar)
        self.monthendClass=MonthEnd()
        self.settingClass=Settings()

        self.connectMe()

        #

        self.setWindowTitle("QT Budget Expenses Tracker")

    #

    def connectMe(self):
        self.actionExit.triggered.connect(self.close)
        self.pbImportAccounts.clicked.connect(self.importClass.importAccounts)
        self.pbImportSales.clicked.connect(self.importClass.importSales)
        self.pbImportTrans.clicked.connect(self.importClass.importTrans)
        self.pbAccountsReport.clicked.connect(lambda: self.reportClass.accountReport(self.teReport))
        self.pbThisPeriodReport.clicked.connect(lambda: self.reportClass.periodReport(self.teReport))
        self.pbSalesbyPeriodReport.clicked.connect(lambda: self.reportClass.salesReport(self.teReport))
        self.tabWorkArea.currentChanged.connect(self.tabSelected)
        self.pbSaveAccount.clicked.connect(self.formClass.saveAccount)
        self.pbTransSave.clicked.connect(self.formClass.saveTransaction)
        self.pbCreateNewPeriod.clicked.connect(self.monthendClass.execute)
        self.pbsaveSettings.clicked.connect(self.settingClass.saveSettings)
        self.cbAccount.textActivated.connect(self.formClass.Account)
        self.pbClearAccountForm.clicked.connect(self.formClass.initializeAccountForm)
        self.pbClearTransactionForm.clicked.connect(self.formClass.initializeTransactionForm)



    #

    def tabSelected(self,ndx):
        if ndx==0:
            self.formClass.newTransaction(self.cbTransAccount,
                                          self.leTransDate,
                                          self.leTransAmount)
        elif ndx==1:
            self.formClass.newAccount(self.cbAccount,
                                      self.cbCategory,
                                      self.leBudgetAmount,
                                      self.leAutoPayAmount,
                                      self.leIcomeExpenseFlag)
        elif ndx==2:
            self.reportClass.accountReport(self.teReport)
        elif ndx==3:
            self.monthendClass.form(self.leNewPeriod)
        elif ndx==4:
            pass # import
        elif ndx==5:
            self.settingClass.form(self.lePeriod)

#

if (__name__ == '__main__'):
    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.show()

    sys.exit(app.exec_())