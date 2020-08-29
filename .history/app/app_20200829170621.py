from PySide2 import QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devises")

    def setup_ui(self):
        pass


app = QtWidgets.QApplication([])
win = App()
win.show()


app.exec_()
