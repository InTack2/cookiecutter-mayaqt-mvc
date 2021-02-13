# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_{{cookiecutter.tool_name}}UI(object):
    def setupUi(self, {{cookiecutter.tool_name}}UI):
        {{cookiecutter.tool_name}}UI.setObjectName("{{cookiecutter.tool_name}}UI")
        {{cookiecutter.tool_name}}UI.resize(265, 168)
        self.centralwidget = QtWidgets.QWidget({{cookiecutter.tool_name}}UI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.printSelectedObjectNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.printSelectedObjectNameButton.setObjectName("printSelectedObjectNameButton")
        self.gridLayout.addWidget(self.printSelectedObjectNameButton, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        {{cookiecutter.tool_name}}UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar({{cookiecutter.tool_name}}UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 21))
        self.menubar.setObjectName("menubar")
        {{cookiecutter.tool_name}}UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar({{cookiecutter.tool_name}}UI)
        self.statusbar.setObjectName("statusbar")
        {{cookiecutter.tool_name}}UI.setStatusBar(self.statusbar)

        self.retranslateUi({{cookiecutter.tool_name}}UI)
        QtCore.QMetaObject.connectSlotsByName({{cookiecutter.tool_name}}UI)

    def retranslateUi(self, {{cookiecutter.tool_name}}UI):
        {{cookiecutter.tool_name}}UI.setWindowTitle(QtWidgets.QApplication.translate("{{cookiecutter.tool_name}}UI", "{{cookiecutter.tool_name}}", None, -1))
        self.printSelectedObjectNameButton.setText(QtWidgets.QApplication.translate("{{cookiecutter.tool_name}}UI", "Output the selected object name.", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("{{cookiecutter.tool_name}}UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks for installing template!</p></body></html>", None, -1))
