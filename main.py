from __future__ import annotations
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
import qdarkstyle

from services.settings import AppSettings
from gui.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    settings = AppSettings()
    if settings.dark_mode:
        app.setStyleSheet(qdarkstyle.load_stylesheet())

    splash = QSplashScreen(QPixmap(str(Path(__file__).parent / "resources/splash.png")))
    splash.show()

    win = MainWindow(settings)
    splash.finish(win)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()