# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTBudget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 814)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWorkArea = QTabWidget(self.centralwidget)
        self.tabWorkArea.setObjectName(u"tabWorkArea")
        self.tabWorkArea.setGeometry(QRect(40, 70, 661, 661))
        self.tabWorkArea.setTabPosition(QTabWidget.North)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout_2 = QFormLayout(self.tab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.leTransDate = QLineEdit(self.tab)
        self.leTransDate.setObjectName(u"leTransDate")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.leTransDate)

        self.leTransAmount = QLineEdit(self.tab)
        self.leTransAmount.setObjectName(u"leTransAmount")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.leTransAmount)

        self.pbTransSave = QPushButton(self.tab)
        self.pbTransSave.setObjectName(u"pbTransSave")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.pbTransSave)

        self.cbTransAccount = QComboBox(self.tab)
        self.cbTransAccount.setObjectName(u"cbTransAccount")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cbTransAccount)

        self.pbClearTransactionForm = QPushButton(self.tab)
        self.pbClearTransactionForm.setObjectName(u"pbClearTransactionForm")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.pbClearTransactionForm)

        self.tabWorkArea.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayout = QFormLayout(self.tab_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.leBudgetAmount = QLineEdit(self.tab_2)
        self.leBudgetAmount.setObjectName(u"leBudgetAmount")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leBudgetAmount)

        self.leAutoPayAmount = QLineEdit(self.tab_2)
        self.leAutoPayAmount.setObjectName(u"leAutoPayAmount")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.leAutoPayAmount)

        self.leIcomeExpenseFlag = QLineEdit(self.tab_2)
        self.leIcomeExpenseFlag.setObjectName(u"leIcomeExpenseFlag")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.leIcomeExpenseFlag)

        self.pbSaveAccount = QPushButton(self.tab_2)
        self.pbSaveAccount.setObjectName(u"pbSaveAccount")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.pbSaveAccount)

        self.cbAccount = QComboBox(self.tab_2)
        self.cbAccount.setObjectName(u"cbAccount")
        self.cbAccount.setEditable(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cbAccount)

        self.cbCategory = QComboBox(self.tab_2)
        self.cbCategory.setObjectName(u"cbCategory")
        self.cbCategory.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cbCategory)

        self.pbClearAccountForm = QPushButton(self.tab_2)
        self.pbClearAccountForm.setObjectName(u"pbClearAccountForm")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.pbClearAccountForm)

        self.tabWorkArea.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pbAccountsReport = QPushButton(self.tab_3)
        self.pbAccountsReport.setObjectName(u"pbAccountsReport")
        self.pbAccountsReport.setGeometry(QRect(10, 10, 181, 28))
        self.pbThisPeriodReport = QPushButton(self.tab_3)
        self.pbThisPeriodReport.setObjectName(u"pbThisPeriodReport")
        self.pbThisPeriodReport.setGeometry(QRect(200, 10, 181, 28))
        self.pbSalesbyPeriodReport = QPushButton(self.tab_3)
        self.pbSalesbyPeriodReport.setObjectName(u"pbSalesbyPeriodReport")
        self.pbSalesbyPeriodReport.setGeometry(QRect(390, 10, 181, 28))
        self.teReport = QTextEdit(self.tab_3)
        self.teReport.setObjectName(u"teReport")
        self.teReport.setGeometry(QRect(10, 50, 561, 541))
        self.tabWorkArea.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.leNewPeriod = QLineEdit(self.tab_4)
        self.leNewPeriod.setObjectName(u"leNewPeriod")
        self.leNewPeriod.setGeometry(QRect(40, 40, 113, 22))
        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 91, 16))
        self.pbCreateNewPeriod = QPushButton(self.tab_4)
        self.pbCreateNewPeriod.setObjectName(u"pbCreateNewPeriod")
        self.pbCreateNewPeriod.setGeometry(QRect(40, 80, 131, 28))
        self.tabWorkArea.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.pbImportAccounts = QPushButton(self.tab_5)
        self.pbImportAccounts.setObjectName(u"pbImportAccounts")
        self.pbImportAccounts.setGeometry(QRect(40, 30, 121, 28))
        self.pbImportSales = QPushButton(self.tab_5)
        self.pbImportSales.setObjectName(u"pbImportSales")
        self.pbImportSales.setGeometry(QRect(40, 70, 121, 28))
        self.pbImportTrans = QPushButton(self.tab_5)
        self.pbImportTrans.setObjectName(u"pbImportTrans")
        self.pbImportTrans.setGeometry(QRect(40, 110, 124, 28))
        self.pbImport = QProgressBar(self.tab_5)
        self.pbImport.setObjectName(u"pbImport")
        self.pbImport.setGeometry(QRect(50, 180, 551, 23))
        self.pbImport.setValue(0)
        self.tabWorkArea.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.formLayout_3 = QFormLayout(self.tab_6)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.tab_6)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lePeriod = QLineEdit(self.tab_6)
        self.lePeriod.setObjectName(u"lePeriod")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lePeriod)

        self.pbsaveSettings = QPushButton(self.tab_6)
        self.pbsaveSettings.setObjectName(u"pbsaveSettings")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.pbsaveSettings)

        self.tabWorkArea.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWorkArea.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.pbTransSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pbClearTransactionForm.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWorkArea.setTabText(self.tabWorkArea.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Trans", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Auto Pay Amount", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Income/expense", None))
        self.pbSaveAccount.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pbClearAccountForm.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWorkArea.setTabText(self.tabWorkArea.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.pbAccountsReport.setText(QCoreApplication.translate("MainWindow", u"Accounts Report", None))
        self.pbThisPeriodReport.setText(QCoreApplication.translate("MainWindow", u"This Period Report", None))
        self.pbSalesbyPeriodReport.setText(QCoreApplication.translate("MainWindow", u"Sales by Period Report", None))
        self.tabWorkArea.setTabText(self.tabWorkArea.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Report", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"New Period", None))
        self.pbCreateNewPeriod.setText(QCoreApplication.translate("MainWindow", u"Create New Period", None))
        self.tabWorkArea.setTabText(self.tabWorkArea.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Month End", None))
        self.pbImportAccounts.setText(QCoreApplication.translate("MainWindow", u"Import Accounts", None))
        self.pbImportSales.setText(QCoreApplication.translate("MainWindow", u"Import Sales", None))
        self.pbImportTrans.setText(QCoreApplication.translate("MainWindow", u"Import Transactions", None))
        self.tabWorkArea.setTabText(self.tabWorkArea.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Period", None))
        self.pbsaveSettings.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWorkArea.setTabText(self.tabWorkArea.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

