# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './acq4/analysis/old/UncagingControlTemplate.ui'
#
# Created: Tue Dec 24 01:49:15 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_UncagingControlWidget(object):
    def setupUi(self, UncagingControlWidget):
        UncagingControlWidget.setObjectName(_fromUtf8("UncagingControlWidget"))
        UncagingControlWidget.resize(442, 354)
        self.gridLayout_4 = QtGui.QGridLayout(UncagingControlWidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(UncagingControlWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.thresholdSpin = QtGui.QDoubleSpinBox(UncagingControlWidget)
        self.thresholdSpin.setObjectName(_fromUtf8("thresholdSpin"))
        self.gridLayout.addWidget(self.thresholdSpin, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(UncagingControlWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.directTimeSpin = QtGui.QDoubleSpinBox(UncagingControlWidget)
        self.directTimeSpin.setObjectName(_fromUtf8("directTimeSpin"))
        self.gridLayout.addWidget(self.directTimeSpin, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(UncagingControlWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.poststimTimeSpin = QtGui.QDoubleSpinBox(UncagingControlWidget)
        self.poststimTimeSpin.setObjectName(_fromUtf8("poststimTimeSpin"))
        self.gridLayout.addWidget(self.poststimTimeSpin, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(UncagingControlWidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gradientRadio = QtGui.QRadioButton(self.groupBox_2)
        self.gradientRadio.setObjectName(_fromUtf8("gradientRadio"))
        self.gridLayout_3.addWidget(self.gradientRadio, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.colorSpin1 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.colorSpin1.setObjectName(_fromUtf8("colorSpin1"))
        self.horizontalLayout_2.addWidget(self.colorSpin1)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.colorSpin3 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.colorSpin3.setMaximum(100.0)
        self.colorSpin3.setObjectName(_fromUtf8("colorSpin3"))
        self.horizontalLayout_3.addWidget(self.colorSpin3)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.gradientWidget = GradientWidget(self.groupBox_2)
        self.gradientWidget.setObjectName(_fromUtf8("gradientWidget"))
        self.gridLayout_3.addWidget(self.gradientWidget, 3, 0, 2, 2)
        self.rgbRadio = QtGui.QRadioButton(self.groupBox_2)
        self.rgbRadio.setObjectName(_fromUtf8("rgbRadio"))
        self.gridLayout_3.addWidget(self.rgbRadio, 5, 0, 1, 2)
        self.colorTracesCheck = QtGui.QCheckBox(self.groupBox_2)
        self.colorTracesCheck.setObjectName(_fromUtf8("colorTracesCheck"))
        self.gridLayout_3.addWidget(self.colorTracesCheck, 7, 0, 1, 2)
        self.svgCheck = QtGui.QCheckBox(self.groupBox_2)
        self.svgCheck.setObjectName(_fromUtf8("svgCheck"))
        self.gridLayout_3.addWidget(self.svgCheck, 8, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lowClipSpin = QtGui.QSpinBox(self.groupBox_2)
        self.lowClipSpin.setObjectName(_fromUtf8("lowClipSpin"))
        self.horizontalLayout_4.addWidget(self.lowClipSpin)
        self.highClipSpin = QtGui.QSpinBox(self.groupBox_2)
        self.highClipSpin.setObjectName(_fromUtf8("highClipSpin"))
        self.horizontalLayout_4.addWidget(self.highClipSpin)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 9, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.downsampleSpin = QtGui.QSpinBox(self.groupBox_2)
        self.downsampleSpin.setObjectName(_fromUtf8("downsampleSpin"))
        self.horizontalLayout_5.addWidget(self.downsampleSpin)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 10, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 2, 1)
        self.groupBox = QtGui.QGroupBox(UncagingControlWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.eventFindRadio = QtGui.QRadioButton(self.groupBox)
        self.eventFindRadio.setObjectName(_fromUtf8("eventFindRadio"))
        self.gridLayout_2.addWidget(self.eventFindRadio, 0, 0, 1, 1)
        self.chargeTransferRadio = QtGui.QRadioButton(self.groupBox)
        self.chargeTransferRadio.setObjectName(_fromUtf8("chargeTransferRadio"))
        self.gridLayout_2.addWidget(self.chargeTransferRadio, 1, 0, 1, 1)
        self.useSpontActCheck = QtGui.QCheckBox(self.groupBox)
        self.useSpontActCheck.setObjectName(_fromUtf8("useSpontActCheck"))
        self.gridLayout_2.addWidget(self.useSpontActCheck, 2, 0, 1, 1)
        self.medianCheck = QtGui.QCheckBox(self.groupBox)
        self.medianCheck.setObjectName(_fromUtf8("medianCheck"))
        self.gridLayout_2.addWidget(self.medianCheck, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.recolorBtn = QtGui.QPushButton(UncagingControlWidget)
        self.recolorBtn.setObjectName(_fromUtf8("recolorBtn"))
        self.gridLayout_4.addWidget(self.recolorBtn, 2, 0, 1, 2)

        self.retranslateUi(UncagingControlWidget)
        QtCore.QMetaObject.connectSlotsByName(UncagingControlWidget)

    def retranslateUi(self, UncagingControlWidget):
        UncagingControlWidget.setWindowTitle(_translate("UncagingControlWidget", "Form", None))
        self.label.setText(_translate("UncagingControlWidget", "Noise Threshold", None))
        self.label_3.setText(_translate("UncagingControlWidget", "Direct Time", None))
        self.label_2.setText(_translate("UncagingControlWidget", "Post-Stim. Time", None))
        self.groupBox_4.setTitle(_translate("UncagingControlWidget", "Coloring Scheme:", None))
        self.gradientRadio.setText(_translate("UncagingControlWidget", "Gradient", None))
        self.label_4.setText(_translate("UncagingControlWidget", "Low % Cutoff", None))
        self.label_5.setText(_translate("UncagingControlWidget", "High % Cutoff", None))
        self.rgbRadio.setText(_translate("UncagingControlWidget", "RGB", None))
        self.colorTracesCheck.setText(_translate("UncagingControlWidget", "Color Traces by Laser Power", None))
        self.svgCheck.setText(_translate("UncagingControlWidget", "Prepare for SVG", None))
        self.label_6.setText(_translate("UncagingControlWidget", "Clip:", None))
        self.label_7.setText(_translate("UncagingControlWidget", "Downsample:", None))
        self.groupBox.setTitle(_translate("UncagingControlWidget", "Analysis Method:", None))
        self.eventFindRadio.setText(_translate("UncagingControlWidget", "Event Finding", None))
        self.chargeTransferRadio.setText(_translate("UncagingControlWidget", "Total Charge Transfer", None))
        self.useSpontActCheck.setText(_translate("UncagingControlWidget", "Use Spont. Activity", None))
        self.medianCheck.setText(_translate("UncagingControlWidget", "Use Median", None))
        self.recolorBtn.setText(_translate("UncagingControlWidget", "Re-Color", None))

from acq4.pyqtgraph.GradientWidget import GradientWidget
