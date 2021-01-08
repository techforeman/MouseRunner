
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon

from handlers.mouse_handler import Mouse_Handler


class UI_Input:
    def __init__(self, config):
        # Construct UI input object to be pass to mouse_handler
        self.delay = config["mouse_movement"]["delay"]
        self.offset = config["mouse_movement"]["offset"]
        self.random_movement_enabled = False
        self.random_delay_enabled = False
        self.random_movement = [
            config["mouse_movement"]["min_random_movement"],
            config["mouse_movement"]["max_random_movement"]
        ]
        self.random_delay = [
            config["mouse_movement"]["min_random_delay"],
            config["mouse_movement"]["max_random_delay"]
        ]


class UI_Handler:
    def __init__(self, ui, MainWindow, config):
        # Initialize input value
        self.ui = ui
        self.tray_minimize_enabled = False
        self.mouse_handler = Mouse_Handler()
        self.ui_input = UI_Input(config)

        # Iinitialize minimize to tray handler
        self.MainWindow = MainWindow
        self.MainWindow.closeEvent = self.closeEvent
        self.tray_icon = QSystemTrayIcon(self.MainWindow)
        self.tray_icon.setIcon(QIcon('ui/images/icon256.png'))
        show_action = QAction("Restore", self.MainWindow)
        quit_action = QAction("Exit", self.MainWindow)
        show_action.triggered.connect(self.MainWindow.show)
        quit_action.triggered.connect(qApp.quit)
        quit_action.triggered.connect(self.tray_icon.hide)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.MainWindow.show)



    def enable_tray_minimize(self, element):
        # Enable the program to be minimize to system tray
        if element.isChecked():
            self.tray_minimize_enabled = True
        else:
            self.tray_minimize_enabled = False

    def start_mouse_movement(self, element):
        # Start mouse movement
        element.setEnabled(False)
        self.ui.stopButton.setEnabled(True)

        self.mouse_handler.start_mouse_movement(self.ui_input)
        self.start_timer()


    def stop_mouse_movement(self):
        # Stop mouse movement
        self.ui.stopButton.setEnabled(False)
        self.ui.startButton.setEnabled(True)


        self.mouse_handler.stop_mouse_movement()
        self.ui.currentTimerValue.setText("00:00:00")

    def start_timer(self):
        max_sec_to_run = 86400
        self.mouse_handler.start_timer(max_sec_to_run, self)


    def closeEvent(self, event):
        # Will trigger when user pressed close button on the UI window
        if self.tray_minimize_enabled:
            event.ignore()
            self.MainWindow.hide()
            self.tray_icon.showMessage(
              "Mouse Mover",
              "Minimized to tray",
              QSystemTrayIcon.Information,
              2000
             )
        else:
            self.stop_mouse_movement()
            self.tray_icon.hide()
