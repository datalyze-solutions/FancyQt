import sys

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
from PyQt4 import (
    QtCore,
    QtGui
)
from PyQt4.QtCore import Qt

import fancyqt.firefox

from dummy import Ui_DummyWidget

class DummyWidget(QtGui.QWidget, Ui_DummyWidget):
    
    def __init__(self, app, parent=None):
        super(DummyWidget, self).__init__(parent)
        self.setupUi(self)
        self._app = app
        
        self._menu = QtGui.QMenu(self)
        self.toolButton_2.setMenu(self._menu)
        self._menu.addAction(self.actionReloadStyle)
        
        self.toolButton.clicked.connect(self._reloadStyle)
        self.actionReloadStyle.triggered.connect(self._reloadStyle)
        self._reloadStyle()
        
        self.setModels()
        
    def _reloadStyle(self):
        module_name = "fancyqt.firefox.stylesheet"
        if module_name in sys.modules:
            reload(sys.modules[module_name])
        else:
            __import__(module_name, fromlist=[module_name])
        
        self._app.setStyleSheet(fancyqt.firefox.stylesheet.style) 
        
    def setModels(self):
        model = QtGui.QStandardItemModel()
        foods = [
            'Cookie dough', # Must be store-bought
            'Hummus', # Must be homemade
            'Spaghetti', # Must be saucy
            'Dal makhani', # Must be spicy
            'Chocolate whipped cream' # Must be plentiful
        ]
        
        for food in foods:
            item = QtGui.QStandardItem(food)
            item.setCheckable(True)
            model.appendRow(item)
        
        self.listView.setModel(model)
        self.tableView.setModel(model)
        self.treeView.setModel(model)
        self.comboBox.setModel(model)

class App(QtGui.QApplication):
    
    def __init__(self, argv):
        super(App, self).__init__(argv)
        self.setStyle("Cleanlooks")
        self.setStyleSheet(fancyqt.firefox.stylesheet.style)
        self.mainWindow = DummyWidget(self)
        self.mainWindow.show()

def main(argv):
    app = App(argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv)