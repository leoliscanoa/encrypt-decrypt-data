"""
Main entry point for the encryption/decryption application.

This application provides a graphical user interface for encrypting and decrypting 
6-digit numbers using a simple algorithm. It is built with PyQt6 to provide a modern 
and responsive user experience.

The application consists of three main screens:
1. Main screen - Allows the user to choose between encryption and decryption
2. Encryption screen - Allows the user to enter a 6-digit number to encrypt
3. Decryption screen - Allows the user to enter a 6-digit encrypted number to decrypt

Results are displayed in a modal dialog with copy-to-clipboard functionality.
"""
import sys
from PyQt6.QtWidgets import QApplication
from windows.main_window import MainWindow

if __name__ == "__main__":
    # Initialize the PyQt application
    app = QApplication(sys.argv)

    # Set a global stylesheet for the application
    # This ensures consistent styling across all components
    app.setStyleSheet("""
        /* Context menu styling for right-click menus */
        QMenu {
            background-color: #f5f5f5;  /* Light gray background */
            color: #212121;             /* Dark gray text for readability */
            border: 1px solid #cccccc;  /* Light gray border */
        }
        /* Styling for selected menu items */
        QMenu::item:selected {
            background-color: #e0e0e0;  /* Slightly darker gray for hover state */
        }

        /* Message box styling for error and information dialogs */
        QMessageBox {
            background-color: #f5f5f5;  /* Light gray background */
            color: #212121;             /* Dark gray text */
        }

        /* Styling for labels within message boxes */
        QMessageBox QLabel {
            color: #212121;             /* Dark gray text for readability */
            font-size: 14px;            /* Larger font size for better visibility */
        }

        /* Styling for buttons within message boxes */
        QMessageBox QPushButton {
            background-color: #FF0000;  /* Red background for buttons */
            color: black;               /* Black text for contrast */
            border: 1px solid #cccccc;  /* Light gray border */
            border-radius: 5px;         /* Rounded corners */
            padding: 10px 20px;         /* Padding for better clickability */
            min-width: 100px;           /* Minimum width for better appearance */
            font-size: 14px;            /* Larger font size */
            font-weight: bold;          /* Bold text for emphasis */
        }

        /* Hover state for buttons within message boxes */
        QMessageBox QPushButton:hover {
            background-color: #CC0000;  /* Darker red for hover state */
        }
    """)

    # Create and show the main application window
    window = MainWindow()
    window.show()

    # Start the application event loop and exit when it's done
    sys.exit(app.exec())
