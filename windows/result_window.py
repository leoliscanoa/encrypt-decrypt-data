"""
Result dialog for displaying encryption/decryption results.

This module defines the ResultDialog class, which creates a modal dialog to display
the results of encryption or decryption operations. It includes a copy-to-clipboard
functionality and can be closed by clicking anywhere on the dialog.
"""
import pyperclip
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFrame, QLabel, QPushButton, QApplication
from functions.utils import center_on_parent


class ResultDialog(QDialog):
    """
    Modal dialog to display encryption/decryption results.

    This class creates a dialog that shows the result of an encryption or decryption
    operation in a large, readable format. It provides a button to copy the result
    to the clipboard and can be closed by clicking anywhere on the dialog.
    """
    def __init__(self, parent=None, result=""):
        """
        Initialize the result dialog.

        Args:
            parent: The parent widget that created this dialog.
                   Used for positioning the dialog relative to the parent.
            result: The encryption/decryption result to display.
        """
        super().__init__(parent)
        self.setWindowTitle("Result")  # Dialog title
        self.setFixedSize(400, 200)  # Fixed size for a consistent appearance
        self.setStyleSheet("background-color: #f5f5f5;")  # Light gray background

        # Main layout with padding
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)  # Add padding around the edges

        # Result frame with a semi-transparent background
        result_frame = QFrame()
        result_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);  /* Semi-transparent white */
                border-radius: 5px;  /* Rounded corners */
            }
        """)
        result_layout = QVBoxLayout(result_frame)

        # Result label displaying the encryption/decryption result
        result_label = QLabel(result)
        result_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))  # Large, bold font
        result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        result_label.setStyleSheet("color: #212121;")  # Dark gray text for readability
        result_layout.addWidget(result_label)

        # Copy button with the clipboard icon
        copy_button = QPushButton("📋 Copy")
        copy_button.setFont(QFont("Arial", 14))
        copy_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;  /* Blue background */
                color: white;  /* White text */
                border: none;  /* No border */
                border-radius: 5px;  /* Rounded corners */
                padding: 10px 20px;  /* Add padding for better clickability */
            }
            QPushButton:hover {
                background-color: #0b7dda;  /* Darker blue when hovered */
            }
        """)
        # Connect button click to copy function
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(result))
        result_layout.addWidget(copy_button)

        # Add the result frame to the main layout
        layout.addWidget(result_frame)

        # Allow closing the dialog by clicking anywhere on it
        self.mousePressEvent = lambda event: self.close()

    def copy_to_clipboard(self, text):
        """
        Copy the provided text to the clipboard and close the dialog.

        Uses both pyperclip and QApplication.clipboard() for maximum compatibility
        across different platforms.

        Args:
            text: The text to copy to the clipboard.
        """
        # Use pyperclip for better cross-platform support
        pyperclip.copy(text)
        # Also use Qt's clipboard for redundancy
        QApplication.clipboard().setText(text)
        # Close the dialog after copying
        self.close()

    def center_dialog(self):
        """
        Center the dialog relative to its parent window.

        Uses the center_on_parent utility function to center the dialog relative to its parent,
        or on the screen if there is no parent.
        """
        center_on_parent(self)
