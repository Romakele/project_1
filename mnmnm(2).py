
from PyQt5 import uic
# from PyQt5 import *
from PyQt5.QtWidgets import *
# from pyqtgraph import *

import sys

class MonitoringApp(QMainWindow):
    def __int__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)

        self.totalData = {}
        self.data = []
        self.listStations = set()
        self.selectedItemListWidget = None

        self.navTab = {
            'Загрузка данных': [self.btnDownloadTab.clicked.connect(self.navigate), 1],
            'Визулизация данных': [self.btnVisualTab.clicked.connect(self.navigate), 2],
            'Анализ данных': [self.btnAnalizeTab.clicked.connect(self.navigate), 3],
            'Прогноз': [self.btnPredicTab.clicked.connect(self.navigate), 4],
            'Мониторинг': [self.btnMonitoringTab.clicked.connect(self.navigate), 5],
            'Экспорт': [self.btnExportTab.clicked.connect(self.navigate), None]
        }
        self.homeBtnDowloadTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnAnalisTab.clicked.connect(self.homeGo)
        self.homeBtnPredictTab.clicked.connect(self.homeGo)
        self.homeBtnMonitoringtab.clicked.connect(self.homeGo)

    def navigate(self):
        print(self.sender().text(), self.navTab[self.sender().text()][1])
        self.tabWidget.setCurrentindex(self.navTab[self.sender().text()][1])


    def homeGo(self):
        self.tabWidget.setCurrentindex(0)




app = QApplication(sys.argv)
ex = MonitoringApp()
ex.show()
sys.exit(app.exec())
