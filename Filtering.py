# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filtering.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sdfae = QtWidgets.QTabWidget(self.centralwidget)
        self.sdfae.setGeometry(QtCore.QRect(30, 20, 891, 541))
        self.sdfae.setObjectName("sdfae")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_filters_load = QtWidgets.QPushButton(self.tab)
        self.pushButton_filters_load.setGeometry(QtCore.QRect(20, 100, 121, 61))
        self.pushButton_filters_load.setObjectName("pushButton_filters_load")
        self.label_filters_input = QtWidgets.QLabel(self.tab)
        self.label_filters_input.setGeometry(QtCore.QRect(150, 60, 251, 151))
        self.label_filters_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_filters_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_filters_input.setObjectName("label_filters_input")
        self.label_filters_output = QtWidgets.QLabel(self.tab)
        self.label_filters_output.setGeometry(QtCore.QRect(410, 60, 291, 151))
        self.label_filters_output.setFrameShape(QtWidgets.QFrame.Box)
        self.label_filters_output.setTextFormat(QtCore.Qt.PlainText)
        self.label_filters_output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_filters_output.setObjectName("label_filters_output")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 270, 691, 101))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 311, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 20, 361, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.KernelSize = QtWidgets.QTextEdit(self.groupBox_2)
        self.KernelSize.setEnabled(True)
        self.KernelSize.setGeometry(QtCore.QRect(0, 30, 71, 41))
        self.KernelSize.setObjectName("KernelSize")
        self.Std = QtWidgets.QTextEdit(self.groupBox_2)
        self.Std.setEnabled(True)
        self.Std.setGeometry(QtCore.QRect(100, 30, 71, 41))
        self.Std.setObjectName("Std")
        self.filterBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.filterBtn.setEnabled(False)
        self.filterBtn.setGeometry(QtCore.QRect(210, 30, 91, 31))
        self.filterBtn.setObjectName("filterBtn")
        self.sdfae.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_histograms_input_2 = QtWidgets.QLabel(self.tab_4)
        self.label_histograms_input_2.setGeometry(QtCore.QRect(320, 80, 241, 171))
        self.label_histograms_input_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_histograms_input_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_histograms_input_2.setObjectName("label_histograms_input_2")
        self.label_histograms_hinput_2 = QtWidgets.QLabel(self.tab_4)
        self.label_histograms_hinput_2.setGeometry(QtCore.QRect(320, 260, 241, 191))
        self.label_histograms_hinput_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_histograms_hinput_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_histograms_hinput_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_histograms_hinput_2.setObjectName("label_histograms_hinput_2")
        self.pushButton_histograms_load_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_histograms_load_2.setGeometry(QtCore.QRect(90, 190, 121, 81))
        self.pushButton_histograms_load_2.setObjectName("pushButton_histograms_load_2")
        self.sdfae.addTab(self.tab_4, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton_equalize_load_3 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_equalize_load_3.setGeometry(QtCore.QRect(60, 100, 121, 81))
        self.pushButton_equalize_load_3.setObjectName("pushButton_equalize_load_3")
        self.label_equalize_output_3 = QtWidgets.QLabel(self.tab_7)
        self.label_equalize_output_3.setGeometry(QtCore.QRect(550, 100, 271, 201))
        self.label_equalize_output_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_equalize_output_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_equalize_output_3.setObjectName("label_equalize_output_3")
        self.label_equalize_input_3 = QtWidgets.QLabel(self.tab_7)
        self.label_equalize_input_3.setGeometry(QtCore.QRect(260, 100, 261, 201))
        self.label_equalize_input_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_equalize_input_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_equalize_input_3.setObjectName("label_equalize_input_3")
        self.pushButton_equalize_3 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_equalize_3.setGeometry(QtCore.QRect(60, 200, 121, 81))
        self.pushButton_equalize_3.setObjectName("pushButton_equalize_3")
        self.sdfae.addTab(self.tab_7, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_Hyprid_input_3 = QtWidgets.QLabel(self.tab_2)
        self.label_Hyprid_input_3.setGeometry(QtCore.QRect(250, 250, 231, 181))
        self.label_Hyprid_input_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Hyprid_input_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Hyprid_input_3.setObjectName("label_Hyprid_input_3")
        self.pushButton_Hyprid_load_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Hyprid_load_3.setGeometry(QtCore.QRect(20, 90, 171, 81))
        self.pushButton_Hyprid_load_3.setObjectName("pushButton_Hyprid_load_3")
        self.label_Hyprid_input_4 = QtWidgets.QLabel(self.tab_2)
        self.label_Hyprid_input_4.setGeometry(QtCore.QRect(250, 50, 231, 171))
        self.label_Hyprid_input_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Hyprid_input_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Hyprid_input_4.setObjectName("label_Hyprid_input_4")
        self.label_Hyprid_output_2 = QtWidgets.QLabel(self.tab_2)
        self.label_Hyprid_output_2.setGeometry(QtCore.QRect(550, 110, 321, 261))
        self.label_Hyprid_output_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Hyprid_output_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Hyprid_output_2.setObjectName("label_Hyprid_output_2")
        self.pushButton_Hyprid_load_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Hyprid_load_4.setGeometry(QtCore.QRect(20, 240, 171, 81))
        self.pushButton_Hyprid_load_4.setObjectName("pushButton_Hyprid_load_4")
        self.pushButton_Hyprid_load_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Hyprid_load_5.setGeometry(QtCore.QRect(30, 390, 151, 61))
        self.pushButton_Hyprid_load_5.setObjectName("pushButton_Hyprid_load_5")
        self.sdfae.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_Normalize_load_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Normalize_load_2.setGeometry(QtCore.QRect(40, 100, 161, 71))
        self.pushButton_Normalize_load_2.setObjectName("pushButton_Normalize_load_2")
        self.label_Normalize_input_2 = QtWidgets.QLabel(self.tab_3)
        self.label_Normalize_input_2.setGeometry(QtCore.QRect(290, 120, 231, 201))
        self.label_Normalize_input_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_input_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_input_2.setObjectName("label_Normalize_input_2")
        self.pushButton_Normalize_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Normalize_2.setGeometry(QtCore.QRect(40, 230, 161, 71))
        self.pushButton_Normalize_2.setObjectName("pushButton_Normalize_2")
        self.label_Normalize_output_2 = QtWidgets.QLabel(self.tab_3)
        self.label_Normalize_output_2.setGeometry(QtCore.QRect(610, 120, 231, 201))
        self.label_Normalize_output_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_output_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_output_2.setObjectName("label_Normalize_output_2")
        self.sdfae.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_Normalize_load_3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_Normalize_load_3.setGeometry(QtCore.QRect(30, 120, 161, 71))
        self.pushButton_Normalize_load_3.setObjectName("pushButton_Normalize_load_3")
        self.label_Normalize_output_3 = QtWidgets.QLabel(self.tab_5)
        self.label_Normalize_output_3.setGeometry(QtCore.QRect(230, 270, 241, 211))
        self.label_Normalize_output_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_output_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_output_3.setObjectName("label_Normalize_output_3")
        self.label_Normalize_input_3 = QtWidgets.QLabel(self.tab_5)
        self.label_Normalize_input_3.setGeometry(QtCore.QRect(230, 40, 241, 211))
        self.label_Normalize_input_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_input_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_input_3.setObjectName("label_Normalize_input_3")
        self.label_Normalize_output_4 = QtWidgets.QLabel(self.tab_5)
        self.label_Normalize_output_4.setGeometry(QtCore.QRect(530, 40, 241, 211))
        self.label_Normalize_output_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_output_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_output_4.setObjectName("label_Normalize_output_4")
        self.label_Normalize_output_6 = QtWidgets.QLabel(self.tab_5)
        self.label_Normalize_output_6.setGeometry(QtCore.QRect(530, 270, 241, 211))
        self.label_Normalize_output_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_output_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_output_6.setObjectName("label_Normalize_output_6")
        self.layoutWidget = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 300, 181, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Noise_label = QtWidgets.QLabel(self.layoutWidget)
        self.Noise_label.setObjectName("Noise_label")
        self.horizontalLayout_4.addWidget(self.Noise_label)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Filters_label = QtWidgets.QLabel(self.layoutWidget)
        self.Filters_label.setObjectName("Filters_label")
        self.horizontalLayout_2.addWidget(self.Filters_label)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(3, "")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Edges_label = QtWidgets.QLabel(self.layoutWidget)
        self.Edges_label.setObjectName("Edges_label")
        self.horizontalLayout_3.addWidget(self.Edges_label)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.sdfae.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_Normalize_load_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_Normalize_load_4.setGeometry(QtCore.QRect(50, 110, 161, 71))
        self.pushButton_Normalize_load_4.setObjectName("pushButton_Normalize_load_4")
        self.label_Normalize_output_5 = QtWidgets.QLabel(self.tab_6)
        self.label_Normalize_output_5.setGeometry(QtCore.QRect(620, 130, 231, 201))
        self.label_Normalize_output_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_output_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_output_5.setObjectName("label_Normalize_output_5")
        self.pushButton_Normalize_3 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_Normalize_3.setGeometry(QtCore.QRect(50, 240, 161, 71))
        self.pushButton_Normalize_3.setObjectName("pushButton_Normalize_3")
        self.label_Normalize_input_4 = QtWidgets.QLabel(self.tab_6)
        self.label_Normalize_input_4.setGeometry(QtCore.QRect(300, 130, 231, 201))
        self.label_Normalize_input_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Normalize_input_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Normalize_input_4.setObjectName("label_Normalize_input_4")
        self.pushButton_Normalize_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_Normalize_4.setGeometry(QtCore.QRect(50, 320, 161, 71))
        self.pushButton_Normalize_4.setObjectName("pushButton_Normalize_4")
        self.sdfae.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sdfae.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_filters_load.setText(_translate("MainWindow", "Load Image"))
        self.label_filters_input.setText(_translate("MainWindow", "Input Image"))
        self.label_filters_output.setText(_translate("MainWindow", "Output image"))
        self.groupBox.setTitle(_translate("MainWindow", "Filter Setting"))
        self.label_3.setText(_translate("MainWindow", "Select Filter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-"))
        self.comboBox.setItemText(1, _translate("MainWindow", "LP-Filter"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HP-Filter"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Additional Parameters"))
        self.KernelSize.setToolTip(_translate("MainWindow", "<html><head/><body><p>Window Size</p></body></html>"))
        self.KernelSize.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Std.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.filterBtn.setText(_translate("MainWindow", "Filter"))
        self.sdfae.setTabText(self.sdfae.indexOf(self.tab), _translate("MainWindow", "Filters"))
        self.label_histograms_input_2.setText(_translate("MainWindow", "Input Image"))
        self.label_histograms_hinput_2.setText(_translate("MainWindow", "Input Histogram"))
        self.pushButton_histograms_load_2.setText(_translate("MainWindow", "Load Image"))
        self.sdfae.setTabText(self.sdfae.indexOf(self.tab_4), _translate("MainWindow", "Histograms"))
        self.pushButton_equalize_load_3.setText(_translate("MainWindow", "Load Image"))
        self.label_equalize_output_3.setText(_translate("MainWindow", "Output Image"))
        self.label_equalize_input_3.setText(_translate("MainWindow", "Input Image"))
        self.pushButton_equalize_3.setText(_translate("MainWindow", "equalize"))
        self.sdfae.setTabText(self.sdfae.indexOf(self.tab_7), _translate("MainWindow", "equalize"))
        self.label_Hyprid_input_3.setText(_translate("MainWindow", "Input Image2"))
        self.pushButton_Hyprid_load_3.setText(_translate("MainWindow", "Load Image1"))
        self.label_Hyprid_input_4.setText(_translate("MainWindow", "Input Image1"))
        self.label_Hyprid_output_2.setText(_translate("MainWindow", "Output Image"))
        self.pushButton_Hyprid_load_4.setText(_translate("MainWindow", "Load Image2"))
        self.pushButton_Hyprid_load_5.setText(_translate("MainWindow", "Hyprid"))
        self.sdfae.setTabText(self.sdfae.indexOf(self.tab_2), _translate("MainWindow", " Hyprid"))
        self.pushButton_Normalize_load_2.setText(_translate("MainWindow", "Load Image"))
        self.label_Normalize_input_2.setText(_translate("MainWindow", "Input Image"))
        self.pushButton_Normalize_2.setText(_translate("MainWindow", "Normalize"))
        self.label_Normalize_output_2.setText(_translate("MainWindow", "Output Image"))
        self.sdfae.setTabText(self.sdfae.indexOf(self.tab_3), _translate("MainWindow", "Normalize"))
        self.pushButton_Normalize_load_3.setText(_translate("MainWindow", "Load Image"))
        self.label_Normalize_output_3.setText(_translate("MainWindow", "Without Noise"))
        self.label_Normalize_input_3.setText(_translate("MainWindow", "Input Image"))
        self.label_Normalize_output_4.setText(_translate("MainWindow", "With Noise"))
        self.label_Normalize_output_6.setText(_translate("MainWindow", "Edge Detection"))
        self.Noise_label.setText(_translate("MainWindow", "Noise"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Uniform"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Gaussian"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Salt- Pepper"))
        self.Filters_label.setText(_translate("MainWindow", "Filters"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Gussion"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "AVG"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Median"))
        self.Edges_label.setText(_translate("MainWindow", "Edges"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Sobel"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Roberts"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Prewitt"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Canny"))
        self.sdfae.setTabText(self.sdfae.indexOf(self.tab_5), _translate("MainWindow", "Noise"))
        self.pushButton_Normalize_load_4.setText(_translate("MainWindow", "Load Image"))
        self.label_Normalize_output_5.setText(_translate("MainWindow", "Output Image"))
        self.pushButton_Normalize_3.setText(_translate("MainWindow", "Local"))
        self.label_Normalize_input_4.setText(_translate("MainWindow", "Input Image"))
        self.pushButton_Normalize_4.setText(_translate("MainWindow", "Global"))
        self.sdfae.setTabText(self.sdfae.indexOf(self.tab_6), _translate("MainWindow", "Thresholding"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
