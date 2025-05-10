"""
Main window for the encryption/decryption application.

This module defines the MainWindow class, which is the primary container for the application's
user interface. It creates a window with a stacked widget that can display different pages:
- Main page: Shows the application title, author information, and buttons to navigate to the encryption and decryption pages.
- Encryption page: Allows the user to enter a 6-digit number to encrypt.
- Decryption page: Allows the user to enter a 6-digit encrypted number to decrypt.

The main window also handles navigation between these pages and ensures the window is
properly centered on the screen.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QStackedWidget, QFrame,
    QGraphicsOpacityEffect
)

from windows.decrypt_window import DecryptPage
# Import pages
from windows.encrypt_window import EncryptPage
from functions.utils import center_on_screen


class MainWindow(QMainWindow):
    """
    Main Application Window using PyQt6.

    This class represents the main window of the application. It contains a stacked widget
    that allows switching between different pages (main, encryption, and decryption).
    The window is styled with a light gray background and has a semi-transparent background image.
    """
    def __init__(self):
        """
        Initialize the main window with all UI components.

        Sets up the window properties, creates the central widget, stacked widget for page
        navigation, and initializes all pages (main, encryption, and decryption).
        """
        super().__init__()
        # Set the window title (will be translated to English in UI)
        self.setWindowTitle("Encryption Application")
        # Set the initial window size
        self.resize(400, 300)
        # Set the background color to light gray
        self.setStyleSheet("background-color: #f5f5f5;")

        # Center the window on the screen for a better user experience
        self.center_window()

        # Create a central widget to hold all UI elements
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a stacked widget to manage multiple pages/screens
        self.stacked_widget = QStackedWidget()

        # Create the main layout for the central widget
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Add some padding around the edges

        # Create the main page widget
        self.main_page = QWidget()
        self.main_page.setStyleSheet("background-color: #f5f5f5;")  # Light gray background
        self.main_page_layout = QVBoxLayout(self.main_page)
        # Center all elements in the layout
        self.main_page_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Load and set up the background image
        background_image = QPixmap("assets/PlaygroundImage.png")
        background_label = QLabel(self.main_page)
        background_label.setPixmap(background_image)
        background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        background_label.setScaledContents(True)  # Scale image to fit the label

        # Create a semi-transparent effect for the background image
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.3)  # 30% opacity (70% transparent)
        background_label.setGraphicsEffect(opacity_effect)

        # Make the background image fill the entire widget
        background_label.setGeometry(0, 0, self.width(), self.height())

        # Ensure the background image is behind all other widgets
        background_label.lower()

        # Store the background label as an instance variable to prevent garbage collection
        self.background_label = background_label

        # Update the background image size when a window is resized
        self.resized = lambda event: self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.resizeEvent = self.resized

        # Create the main content frame with a semi-transparent background
        main_frame = QFrame()
        main_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);  /* Semi-transparent white */
                border-radius: 5px;  /* Rounded corners */
            }
        """)
        main_frame_layout = QVBoxLayout(main_frame)
        main_frame_layout.setContentsMargins(20, 20, 20, 20)  # Add padding inside the frame

        # Application title - will be displayed in English
        title_label = QLabel("Encryption Application")
        title_label.setFont(QFont("Arial", 22, QFont.Weight.Bold))  # Large, bold font
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        title_label.setStyleSheet("color: #212121;")  # Dark gray text for readability
        main_frame_layout.addWidget(title_label)

        # Author information with prominent styling
        author_label = QLabel("Author: Andrés Leonardo Liscano")
        author_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        author_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        author_label.setStyleSheet("""
            color: #000000;  /* Black text */
            background-color: #f5f5f5;  /* Light gray background */
            border-radius: 5px;  /* Rounded corners */
            padding: 5px 10px;  /* Add some padding */
        """)
        main_frame_layout.addWidget(author_label)
        main_frame_layout.addSpacing(20)  # Add vertical space

        # Instructions for the user
        info_label = QLabel("Select an option:")
        info_label.setFont(QFont("Arial", 16))
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label.setStyleSheet("color: #212121;")  # Dark gray text
        main_frame_layout.addWidget(info_label)
        main_frame_layout.addSpacing(10)  # Add a bit of vertical space

        # Navigation buttons in a horizontal layout
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the buttons

        # Encrypt button with lock emoji
        encrypt_button = QPushButton("🔒 Encrypt")
        encrypt_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        encrypt_button.setStyleSheet("""
            QPushButton {
                background-color: #FF0000;  /* Red background */
                color: white;  /* White text */
                border: none;  /* No border */
                border-radius: 5px;  /* Rounded corners */
                padding: 10px 20px;  /* Add padding for better clickability */
                min-width: 150px;  /* Minimum width for better appearance */
            }
            QPushButton:hover {
                background-color: #CC0000;  /* Darker red when hovered */
            }
        """)
        encrypt_button.clicked.connect(self.show_encrypt_page)  # Connect to navigation method
        button_layout.addWidget(encrypt_button)

        # Decrypt button with unlocked emoji
        decrypt_button = QPushButton("🔓 Decrypt")
        decrypt_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        decrypt_button.setStyleSheet("""
            QPushButton {
                background-color: #008080;  /* Teal background */
                color: white;  /* White text */
                border: none;  /* No border */
                border-radius: 5px;  /* Rounded corners */
                padding: 10px 20px;  /* Add padding for better clickability */
                min-width: 150px;  /* Minimum width for better appearance */
            }
            QPushButton:hover {
                background-color: #006666;  /* Darker teal when hovered */
            }
        """)
        decrypt_button.clicked.connect(self.show_decrypt_page)  # Connect to navigation method
        button_layout.addWidget(decrypt_button)

        # Add the button layout to the main frame
        main_frame_layout.addLayout(button_layout)
        # Add the main frame to the main page layout
        self.main_page_layout.addWidget(main_frame)

        # Initialize encrypt and decrypt pages
        self.encrypt_page = EncryptPage(self)  # Page for encryption functionality
        self.decrypt_page = DecryptPage(self)  # Page for decryption functionality

        # Add all pages to the stacked widget in order
        # Index 0: Main page
        self.stacked_widget.addWidget(self.main_page)
        # Index 1: Encryption page
        self.stacked_widget.addWidget(self.encrypt_page)
        # Index 2: Decryption page
        self.stacked_widget.addWidget(self.decrypt_page)

        # Add the stacked widget to the main layout
        main_layout.addWidget(self.stacked_widget)

        # Show the main page by default (index 0)
        self.stacked_widget.setCurrentIndex(0)

    def show_main_page(self):
        """
        Navigate to the main page.

        Sets the stacked widget's current index to 0, which corresponds to the main page.
        This method is called when the user clicks the "Back" button on the encrypt or decrypt pages.
        """
        self.stacked_widget.setCurrentIndex(0)

    def show_encrypt_page(self):
        """
        Navigate to the encryption page.

        Sets the stacked widget's current index to 1, which corresponds to the encryption page.
        This method is called when the user clicks the "Encrypt" button on the main page.
        """
        self.stacked_widget.setCurrentIndex(1)

    def show_decrypt_page(self):
        """
        Navigate to the decryption page.

        Sets the stacked widget's current index to 2, which corresponds to the decryption page.
        This method is called when the user clicks the "Decrypt" button on the main page.
        """
        self.stacked_widget.setCurrentIndex(2)

    def center_window(self):
        """
        Center the window on the screen.

        Uses the center_on_screen utility function to center the window.
        """
        center_on_screen(self)
