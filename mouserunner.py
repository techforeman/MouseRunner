import ctypes
import sys
import time
import yaml
import os

from handlers import ui_handler
from handlers.ui_handler import UI_Handler
from ui.ui_mainWindow import *


os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


def get_file_path(filename):
    main_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_file = os.path.abspath(os.path.join(main_path, filename))
    return path_to_file


def main():
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # Fix to appear in Taskbar ##############
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Load config file
    with open(get_file_path('config.yml'), 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    # Initialized UI #######################
    app_icon = get_file_path(config["icon_path"])
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(app_icon))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ########################################

    ui_handler = UI_Handler(ui, MainWindow, config)

    # Attach UI elements to event handlers
    ui.minimizeToTrayEnabled.stateChanged.connect(lambda: ui_handler.enable_tray_minimize(ui.minimizeToTrayEnabled))
    ui.startButton.clicked.connect(lambda: ui_handler.start_mouse_movement(ui.startButton))
    #ui.stopButton.clicked.connect(lambda: ui_handler.stop_mouse_movement(ui.stopButton))
    ui.stopButton.clicked.connect(ui_handler.stop_mouse_movement)




    main()