import logging
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer

import connection
import roomsmenu



class MainWindow(QWidget) :
    
    def __init__(self) :
        super().__init__()

        # Задаем имя главному меню, чтобы потом использовать его в css файле
        self.setObjectName("MainWindow")

        # Устанавливаем иконку приложения
        # self.setWindowIcon(QIcon(os.path.join(os.getcwd(), args.path, "images/icon3.png")))
        # Устанавливаем размеры и расположение окна приложения
        self.setGeometry(200, 200, 400, 300)
        # Создание строки которое пишется в рамке приложения
        self.setWindowTitle("BrainlyHome")
    
        # Инициализируем logging
        logging.basicConfig(filename="brainlyhome.log", level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

        # Подключаемся к mqtt серверу
        mqtt = connection.Mqtt("192.168.1.112", "base")
        mqtt.connect()
        
        # Подключаемся к помошнику с дополнительными функциями для mqtt
        self.mqtt_helper = connection.MqttHelper(mqtt)

        # Инициализируем виджет окна комнат и клиентов
        self.rm = roomsmenu.RoomsMenu()
        

        self.mainVLay = QVBoxLayout()
        self.mainVLay.addWidget(self.rm)

        self.setLayout(self.mainVLay)

        self.show()

        timer = QTimer(self)
        timer.setInterval(1000)
        timer.setSingleShot(False)
        timer.timeout.connect(self.get_name)
        timer.start(1000)
    


    def get_name(self):
        self.clients = self.mqtt_helper.get_devices()
        if len(self.clients) > 0:
            print(self.clients[0].get_name())



def main() :
    # Инициализируем основной класс приложения
    qApp = QApplication(sys.argv)
    # Инициализируем основной класс окна меню
    mw = MainWindow()
    
    # Открываем и установливаем файл css для приложения
    # with open("/home/whoman/wrk/development/arduino/CompAdmiss/Application/style.css") as f :
    #     qApp.setStyleSheet(f.read())

    sys.exit(qApp.exec_())


if __name__ == '__main__':
    main()
