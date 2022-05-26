import sys

from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.resize(360, 160)

widget.setWindowTitle("Pyqt5 测试")

widget.show()

sys.exit(app.exec_())