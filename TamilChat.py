# Form implementation generated from reading ui file 'chatUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
# - *- coding: utf- 8 - *-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from textblob import TextBlob
from PyQt5 import QtCore, QtGui, QtWidgets

chatbot = ChatBot('Tamil Chat', logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Im sorry, I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
		'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
		])
trainer = ListTrainer(chatbot)
conv = open('chat.txt', 'r').readlines()
trainer.train(conv)
conv2 = open('chat2.txt', 'r').readlines()
trainer.train(conv2)
conv3 = open('chat3.txt', 'r').readlines()
trainer.train(conv3)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(15, 11, 761, 441))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(13, 470, 591, 61))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 470, 151, 61))
        self.pushButton.setObjectName("pushButton")
        #On click
        self.pushButton.clicked.connect(self.on_click)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "அருவி "))
        self.pushButton.setText(_translate("MainWindow", "Send"))

    def on_click(self):
        textInp = self.textEdit.toPlainText()
        self.textEdit.setText('')

        userInp = str(textInp)
        userInp = TextBlob(userInp)
        userInp =str( userInp.translate(from_lang='ta', to='en'))
        print(userInp)
        botResp = chatbot.get_response(userInp)
        botResp = TextBlob(str(botResp))
        botResp =str( botResp.translate(from_lang='en', to='ta'))
        self.textBrowser.append('You: '+ textInp)
        self.textBrowser.append('Bot: '+ botResp)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

