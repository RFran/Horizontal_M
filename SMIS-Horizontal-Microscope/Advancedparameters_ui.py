# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Advancedparameters.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Advanced_parameters_window(object):
    def setupUi(self, Advanced_parameters_window):
        Advanced_parameters_window.setObjectName(_fromUtf8("Advanced_parameters_window"))
        Advanced_parameters_window.resize(963, 214)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Logo/SMISlogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Advanced_parameters_window.setWindowIcon(icon)
        self.gridLayoutWidget = QtGui.QWidget(Advanced_parameters_window)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 671, 131))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_35 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_35.setFrameShape(QtGui.QFrame.HLine)
        self.line_35.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_35.setObjectName(_fromUtf8("line_35"))
        self.gridLayout.addWidget(self.line_35, 10, 8, 1, 1)
        self.largeDecNew = QtGui.QLineEdit(self.gridLayoutWidget)
        self.largeDecNew.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.largeDecNew.setAlignment(QtCore.Qt.AlignCenter)
        self.largeDecNew.setObjectName(_fromUtf8("largeDecNew"))
        self.gridLayout.addWidget(self.largeDecNew, 9, 6, 1, 1)
        self.line_29 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_29.setFrameShape(QtGui.QFrame.VLine)
        self.line_29.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_29.setObjectName(_fromUtf8("line_29"))
        self.gridLayout.addWidget(self.line_29, 1, 7, 1, 1)
        self.xyzDecNew = QtGui.QLineEdit(self.gridLayoutWidget)
        self.xyzDecNew.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.xyzDecNew.setAlignment(QtCore.Qt.AlignCenter)
        self.xyzDecNew.setObjectName(_fromUtf8("xyzDecNew"))
        self.gridLayout.addWidget(self.xyzDecNew, 5, 6, 1, 1)
        self.line_23 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_23.setFrameShape(QtGui.QFrame.VLine)
        self.line_23.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_23.setObjectName(_fromUtf8("line_23"))
        self.gridLayout.addWidget(self.line_23, 7, 1, 1, 1)
        self.line_24 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_24.setFrameShape(QtGui.QFrame.VLine)
        self.line_24.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_24.setObjectName(_fromUtf8("line_24"))
        self.gridLayout.addWidget(self.line_24, 9, 1, 1, 1)
        self.line_16 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.gridLayout.addWidget(self.line_16, 2, 6, 1, 1)
        self.largeAccNew = QtGui.QLineEdit(self.gridLayoutWidget)
        self.largeAccNew.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.largeAccNew.setAlignment(QtCore.Qt.AlignCenter)
        self.largeAccNew.setObjectName(_fromUtf8("largeAccNew"))
        self.gridLayout.addWidget(self.largeAccNew, 9, 4, 1, 1)
        self.line_5 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 2, 4, 1, 1)
        self.line_20 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_20.setFrameShape(QtGui.QFrame.VLine)
        self.line_20.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_20.setObjectName(_fromUtf8("line_20"))
        self.gridLayout.addWidget(self.line_20, 3, 3, 1, 1)
        self.line_21 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_21.setFrameShape(QtGui.QFrame.VLine)
        self.line_21.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_21.setObjectName(_fromUtf8("line_21"))
        self.gridLayout.addWidget(self.line_21, 3, 1, 1, 1)
        self.line_14 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.gridLayout.addWidget(self.line_14, 2, 2, 1, 1)
        self.line_25 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_25.setFrameShape(QtGui.QFrame.HLine)
        self.line_25.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_25.setObjectName(_fromUtf8("line_25"))
        self.gridLayout.addWidget(self.line_25, 8, 2, 1, 1)
        self.line_26 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_26.setFrameShape(QtGui.QFrame.HLine)
        self.line_26.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_26.setObjectName(_fromUtf8("line_26"))
        self.gridLayout.addWidget(self.line_26, 4, 2, 1, 1)
        self.line_22 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_22.setFrameShape(QtGui.QFrame.VLine)
        self.line_22.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_22.setObjectName(_fromUtf8("line_22"))
        self.gridLayout.addWidget(self.line_22, 5, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.line_18 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_18.setFrameShape(QtGui.QFrame.VLine)
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_18.setObjectName(_fromUtf8("line_18"))
        self.gridLayout.addWidget(self.line_18, 7, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)
        self.line_10 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout.addWidget(self.line_10, 6, 2, 1, 1)
        self.line_11 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.gridLayout.addWidget(self.line_11, 6, 6, 1, 1)
        self.line_13 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.gridLayout.addWidget(self.line_13, 2, 0, 1, 1)
        self.line_8 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 6, 4, 1, 1)
        self.line_9 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout.addWidget(self.line_9, 6, 8, 1, 1)
        self.line_7 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout.addWidget(self.line_7, 6, 10, 1, 1)
        self.line_6 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 6, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 5, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 7, 2, 1, 1)
        self.line_28 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_28.setFrameShape(QtGui.QFrame.VLine)
        self.line_28.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_28.setObjectName(_fromUtf8("line_28"))
        self.gridLayout.addWidget(self.line_28, 1, 5, 1, 1)
        self.xyzAccAct = QtGui.QLineEdit(self.gridLayoutWidget)
        self.xyzAccAct.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.xyzAccAct.setAlignment(QtCore.Qt.AlignCenter)
        self.xyzAccAct.setObjectName(_fromUtf8("xyzAccAct"))
        self.gridLayout.addWidget(self.xyzAccAct, 3, 4, 1, 1)
        self.line_27 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_27.setFrameShape(QtGui.QFrame.VLine)
        self.line_27.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_27.setObjectName(_fromUtf8("line_27"))
        self.gridLayout.addWidget(self.line_27, 1, 3, 1, 1)
        self.line_30 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_30.setFrameShape(QtGui.QFrame.VLine)
        self.line_30.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_30.setObjectName(_fromUtf8("line_30"))
        self.gridLayout.addWidget(self.line_30, 1, 9, 1, 1)
        self.line_17 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_17.setFrameShape(QtGui.QFrame.VLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.gridLayout.addWidget(self.line_17, 9, 3, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 9, 2, 1, 1)
        self.line_19 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_19.setFrameShape(QtGui.QFrame.VLine)
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_19.setObjectName(_fromUtf8("line_19"))
        self.gridLayout.addWidget(self.line_19, 5, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 1, 8, 1, 1)
        self.largeDecAct = QtGui.QLineEdit(self.gridLayoutWidget)
        self.largeDecAct.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.largeDecAct.setAlignment(QtCore.Qt.AlignCenter)
        self.largeDecAct.setObjectName(_fromUtf8("largeDecAct"))
        self.gridLayout.addWidget(self.largeDecAct, 7, 6, 1, 1)
        self.largeSpeedNew = QtGui.QLineEdit(self.gridLayoutWidget)
        self.largeSpeedNew.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.largeSpeedNew.setAlignment(QtCore.Qt.AlignCenter)
        self.largeSpeedNew.setObjectName(_fromUtf8("largeSpeedNew"))
        self.gridLayout.addWidget(self.largeSpeedNew, 9, 8, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 6, 1, 1)
        self.xyzSpeedAct = QtGui.QLineEdit(self.gridLayoutWidget)
        self.xyzSpeedAct.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.xyzSpeedAct.setAlignment(QtCore.Qt.AlignCenter)
        self.xyzSpeedAct.setObjectName(_fromUtf8("xyzSpeedAct"))
        self.gridLayout.addWidget(self.xyzSpeedAct, 3, 8, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        self.line_15 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.gridLayout.addWidget(self.line_15, 2, 8, 1, 1)
        self.line_31 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_31.setFrameShape(QtGui.QFrame.HLine)
        self.line_31.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_31.setObjectName(_fromUtf8("line_31"))
        self.gridLayout.addWidget(self.line_31, 10, 0, 1, 1)
        self.largeSpeedAct = QtGui.QLineEdit(self.gridLayoutWidget)
        self.largeSpeedAct.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.largeSpeedAct.setAlignment(QtCore.Qt.AlignCenter)
        self.largeSpeedAct.setObjectName(_fromUtf8("largeSpeedAct"))
        self.gridLayout.addWidget(self.largeSpeedAct, 7, 8, 1, 1)
        self.xyzAccNew = QtGui.QLineEdit(self.gridLayoutWidget)
        self.xyzAccNew.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.xyzAccNew.setAlignment(QtCore.Qt.AlignCenter)
        self.xyzAccNew.setObjectName(_fromUtf8("xyzAccNew"))
        self.gridLayout.addWidget(self.xyzAccNew, 5, 4, 1, 1)
        self.largeAccAct = QtGui.QLineEdit(self.gridLayoutWidget)
        self.largeAccAct.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.largeAccAct.setAlignment(QtCore.Qt.AlignCenter)
        self.largeAccAct.setObjectName(_fromUtf8("largeAccAct"))
        self.gridLayout.addWidget(self.largeAccAct, 7, 4, 1, 1)
        self.xyzDecAct = QtGui.QLineEdit(self.gridLayoutWidget)
        self.xyzDecAct.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.xyzDecAct.setAlignment(QtCore.Qt.AlignCenter)
        self.xyzDecAct.setObjectName(_fromUtf8("xyzDecAct"))
        self.gridLayout.addWidget(self.xyzDecAct, 3, 6, 1, 1)
        self.line_39 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_39.setFrameShape(QtGui.QFrame.HLine)
        self.line_39.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_39.setObjectName(_fromUtf8("line_39"))
        self.gridLayout.addWidget(self.line_39, 0, 8, 1, 1)
        self.line_12 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.gridLayout.addWidget(self.line_12, 2, 10, 1, 1)
        self.line_36 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_36.setFrameShape(QtGui.QFrame.HLine)
        self.line_36.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_36.setObjectName(_fromUtf8("line_36"))
        self.gridLayout.addWidget(self.line_36, 10, 10, 1, 1)
        self.xyzSpeedNew = QtGui.QLineEdit(self.gridLayoutWidget)
        self.xyzSpeedNew.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.xyzSpeedNew.setAlignment(QtCore.Qt.AlignCenter)
        self.xyzSpeedNew.setObjectName(_fromUtf8("xyzSpeedNew"))
        self.gridLayout.addWidget(self.xyzSpeedNew, 5, 8, 1, 1)
        self.line_34 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_34.setFrameShape(QtGui.QFrame.HLine)
        self.line_34.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_34.setObjectName(_fromUtf8("line_34"))
        self.gridLayout.addWidget(self.line_34, 10, 6, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.line_40 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_40.setFrameShape(QtGui.QFrame.HLine)
        self.line_40.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_40.setObjectName(_fromUtf8("line_40"))
        self.gridLayout.addWidget(self.line_40, 0, 10, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.line_32 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_32.setFrameShape(QtGui.QFrame.HLine)
        self.line_32.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_32.setObjectName(_fromUtf8("line_32"))
        self.gridLayout.addWidget(self.line_32, 10, 2, 1, 1)
        self.line_38 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_38.setFrameShape(QtGui.QFrame.HLine)
        self.line_38.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_38.setObjectName(_fromUtf8("line_38"))
        self.gridLayout.addWidget(self.line_38, 0, 6, 1, 1)
        self.line_33 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_33.setFrameShape(QtGui.QFrame.HLine)
        self.line_33.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_33.setObjectName(_fromUtf8("line_33"))
        self.gridLayout.addWidget(self.line_33, 10, 4, 1, 1)
        self.line_37 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_37.setFrameShape(QtGui.QFrame.HLine)
        self.line_37.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_37.setObjectName(_fromUtf8("line_37"))
        self.gridLayout.addWidget(self.line_37, 0, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.btnSaveparam = QtGui.QPushButton(Advanced_parameters_window)
        self.btnSaveparam.setGeometry(QtCore.QRect(350, 10, 241, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Logo/document-save-3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveparam.setIcon(icon1)
        self.btnSaveparam.setIconSize(QtCore.QSize(25, 25))
        self.btnSaveparam.setObjectName(_fromUtf8("btnSaveparam"))
        self.btnSeeparam = QtGui.QPushButton(Advanced_parameters_window)
        self.btnSeeparam.setGeometry(QtCore.QRect(100, 10, 241, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Logo/478027-glasses-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSeeparam.setIcon(icon2)
        self.btnSeeparam.setIconSize(QtCore.QSize(40, 35))
        self.btnSeeparam.setObjectName(_fromUtf8("btnSeeparam"))
        self.line = QtGui.QFrame(Advanced_parameters_window)
        self.line.setGeometry(QtCore.QRect(690, 0, 16, 211))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.btnposition = QtGui.QPushButton(Advanced_parameters_window)
        self.btnposition.setGeometry(QtCore.QRect(820, 100, 121, 23))
        self.btnposition.setIcon(icon2)
        self.btnposition.setObjectName(_fromUtf8("btnposition"))
        self.step = QtGui.QLineEdit(Advanced_parameters_window)
        self.step.setGeometry(QtCore.QRect(730, 120, 41, 20))
        self.step.setAlignment(QtCore.Qt.AlignCenter)
        self.step.setObjectName(_fromUtf8("step"))
        self.label_3 = QtGui.QLabel(Advanced_parameters_window)
        self.label_3.setGeometry(QtCore.QRect(780, 120, 47, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnplus = QtGui.QPushButton(Advanced_parameters_window)
        self.btnplus.setGeometry(QtCore.QRect(730, 80, 41, 41))     # Abs,Ord,Largeur,Hauteur
        self.btnplus.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Logo/flecheplus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnplus.setIcon(icon3)
        self.btnplus.setIconSize(QtCore.QSize(35, 35))
        self.btnplus.setObjectName(_fromUtf8("btnplus"))
        self.btnmoins = QtGui.QPushButton(Advanced_parameters_window)
        self.btnmoins.setGeometry(QtCore.QRect(730, 140, 41, 41))
        self.btnmoins.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Logo/flechemoinss.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnmoins.setIcon(icon4)
        self.btnmoins.setIconSize(QtCore.QSize(35, 35))
        self.btnmoins.setObjectName(_fromUtf8("btnmoins"))
        self.position = QtGui.QLineEdit(Advanced_parameters_window)
        self.position.setGeometry(QtCore.QRect(820, 130, 121, 20))
        self.position.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.position.setObjectName(_fromUtf8("position"))
        self.comboBox = QtGui.QComboBox(Advanced_parameters_window)
        self.comboBox.setGeometry(QtCore.QRect(750, 30, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(Advanced_parameters_window)
        self.label.setGeometry(QtCore.QRect(760, 10, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Advanced_parameters_window)
        QtCore.QMetaObject.connectSlotsByName(Advanced_parameters_window)

    def retranslateUi(self, Advanced_parameters_window):
        Advanced_parameters_window.setWindowTitle(_translate("Advanced_parameters_window", "Advanced Parameters", None))
        self.label_14.setText(_translate("Advanced_parameters_window", "  Long range ", None))
        self.label_13.setText(_translate("Advanced_parameters_window", "SYZ", None))
        self.label_12.setText(_translate("Advanced_parameters_window", "  Current  ", None))
        self.label_15.setText(_translate("Advanced_parameters_window", "New", None))
        self.label_16.setText(_translate("Advanced_parameters_window", "Current", None))
        self.label_18.setText(_translate("Advanced_parameters_window", "New", None))
        self.label_10.setText(_translate("Advanced_parameters_window", "Speed", None))
        self.label_9.setText(_translate("Advanced_parameters_window", "Deceleration", None))
        self.label_6.setText(_translate("Advanced_parameters_window", "Acceleration", None))
        self.label_5.setText(_translate("Advanced_parameters_window", "Long range", None))
        self.label_4.setText(_translate("Advanced_parameters_window", "SYZ", None))
        self.label_7.setText(_translate("Advanced_parameters_window", "Motor group", None))
        self.btnSaveparam.setText(_translate("Advanced_parameters_window", "   Save New parameters", None))
        self.btnSeeparam.setText(_translate("Advanced_parameters_window", "     Get current parameters", None))
        self.btnposition.setText(_translate("Advanced_parameters_window", "Get current position", None))
        self.step.setText(_translate("Advanced_parameters_window", "10", None))
        self.label_3.setText(_translate("Advanced_parameters_window", "Step", None))
        self.comboBox.setItemText(0, _translate("Advanced_parameters_window", "Long range Raman", None))
        self.comboBox.setItemText(1, _translate("Advanced_parameters_window", "Long range IR", None))
        self.comboBox.setItemText(2, _translate("Advanced_parameters_window", "Long range DAC", None))
        self.comboBox.setItemText(3, _translate("Advanced_parameters_window", "DAC / S", None))
        self.comboBox.setItemText(4, _translate("Advanced_parameters_window", "DAC / Y", None))
        self.comboBox.setItemText(5, _translate("Advanced_parameters_window", "DAC / Z", None))
        self.label.setText(_translate("Advanced_parameters_window", "Select a motor to move", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Advanced_parameters_window = QtGui.QDialog()
    ui = Ui_Advanced_parameters_window()
    ui.setupUi(Advanced_parameters_window)
    Advanced_parameters_window.show()
    sys.exit(app.exec_())

