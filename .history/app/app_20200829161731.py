from PySide2 import QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


app = QtWidgets.QApplication([])
app.exec_()