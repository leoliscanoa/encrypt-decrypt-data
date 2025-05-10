"""
Encryption page for the application.

This module defines the EncryptPage class, which provides the user interface for
encrypting 6-digit numbers. It allows users to input a number, encrypt it using
the algorithm defined in the crypto module, and view the result in a modal dialog.

The page includes:
- A title
- An input field for entering a 6-digit number
- Buttons for encrypting the number and returning to the main page
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFrame, QMessageBox
)

from functions.crypto import encrypt_number
from functions.utils import create_back_button, create_input_field
from windows.result_window import ResultDialog


class EncryptPage(QWidget):
    """
    Page for encrypting 6-digit numbers.

    This class provides a user interface for entering a 6-digit number,
    encrypting it using the algorithm defined in the crypto module,
    and displaying the result in a modal dialog.
    """
    def __init__(self, main_window):
        """
        Initialize the encryption page.

        Args:
            main_window: The parent MainWindow instance that contains this page.
                         Used for navigation back to the main page.
        """
        super().__init__()
        self.number_entry = None
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the user interface components for the encryption page.

        Creates the layout, frame, title, input field, and buttons.
        Configures styling and connects signals to slots.
        """
        # Create the main layout with padding
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Add padding around the edges

        # Create the main frame with a semi-transparent background
        main_frame = QFrame()
        main_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);  /* Semi-transparent white */
                border-radius: 5px;  /* Rounded corners */
            }
        """)
        main_frame_layout = QVBoxLayout(main_frame)
        main_frame_layout.setContentsMargins(20, 20, 20, 20)  # Add padding inside the frame

        # Window title
        title_label = QLabel("Number Encryption")
        title_label.setFont(QFont("Arial", 22, QFont.Weight.Bold))  # Large, bold font
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        title_label.setStyleSheet("color: #212121;")  # Dark gray text for readability
        main_frame_layout.addWidget(title_label)
        main_frame_layout.addSpacing(20)  # Add vertical space

        # Create input field with label
        self.number_entry = create_input_field(
            "Enter a 6-digit number:",
            main_frame_layout
        )

        # Spacer to push buttons to the bottom of the frame
        main_frame_layout.addStretch()

        # Action buttons at the bottom, arranged horizontally and centered
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the buttons

        # Encrypt button with lock emoji
        encrypt_action_button = QPushButton("🔒 Encrypt")
        encrypt_action_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        encrypt_action_button.setStyleSheet("""
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
        encrypt_action_button.clicked.connect(self.perform_encrypt)  # Connect to encryption method

        # Create a back button and add both buttons to layouts
        create_back_button(self.main_window, encrypt_action_button, button_layout, main_frame_layout)

        # Add the main frame to the page's main layout
        main_layout.addWidget(main_frame)

    def perform_encrypt(self):
        """
        Process the encryption request when the Encrypt button is clicked.

        Gets the number from the input field, validates it, encrypts it using the
        encrypt_number function from the crypto module, and displays the result
        in a modal dialog. If the input is invalid, it shows an error message.

        The input field is cleared after either successful encryption or an error.
        """
        # Get the number from the input field
        number_to_encrypt = self.number_entry.text()

        # Encrypt the number using the algorithm from the crypto module
        encrypted_result = encrypt_number(number_to_encrypt)

        if encrypted_result:
            # If encryption was successful, show the result in a modal dialog
            dialog = ResultDialog(self, encrypted_result)
            dialog.center_dialog()  # Center the dialog relative to the parent window
            dialog.exec()  # Show the dialog modally (blocks interaction with a parent window)

            # Clear the input field after successful encryption
            self.number_entry.clear()
        else:
            # If encryption failed (invalid input), show an error message
            QMessageBox.critical(
                self,  # Parent widget
                "Input Error",  # Dialog title
                "Please enter a 6-digit number."  # Error message
            )

            # Clear the input field to allow the user to try again
            self.number_entry.clear()
