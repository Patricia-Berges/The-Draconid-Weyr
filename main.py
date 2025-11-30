import sys
from PyQt5.QtWidgets import QApplication
from data.db_handler import create_db
from screens.main_screen import MainScreen


def main():
    # Initialize database
    create_db()

    # Initialize Qt app
    app = QApplication(sys.argv)

    # Create and show main screen
    main_window = MainScreen()
    main_window.show()

    # Run event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
