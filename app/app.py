from PySide2 import QtWidgets, QtGui, QtCore
import currency_converter


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()
        self.set_defaults_values()
        self.setup_connections()
        self.setup_css()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesForm = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")

        self.layout.addWidget(self.cbb_devisesForm)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)

    def set_defaults_values(self):
        self.cbb_devisesForm.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesForm.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("USD")

        self.spn_montant.setRange(1, 100000)
        self.spn_montantConverti.setRange(1, 100000)
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)

    def setup_connections(self):
        self.cbb_devisesForm.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)

    def setup_css(self):
        self.setStyleSheet(""" 
        background-color : rgb(30 , 30 ,30) ;
        color : rgb(240,240,240) ;
        border : none ;
        
        """)

    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesForm.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        try:
            resultat = self.c.convert(montant, devise_from, devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print("La conversin n'a pas fonctionné")
        else:
            self.spn_montantConverti.setValue(resultat)

    def inverser_devise(self):
        devise_from = self.cbb_devisesForm.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        self.cbb_devisesForm.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)

        self.compute()


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
