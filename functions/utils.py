"""
Utility functions for the application's UI.

This module contains utility functions that are used by multiple UI components
to avoid code duplication and ensure consistent behavior across the application.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit
)


def center_on_screen(widget):
    """
    Center a widget on the screen.

    Calculates the center position based on the screen's available geometry and
    the widget's size, then moves the widget to that position.

    Args:
        widget (QWidget): The widget to center on the screen.
    """
    # Get the screen geometry (available area)
    screen = widget.screen()
    screen_geometry = screen.availableGeometry()

    # Calculate the center position
    x = (screen_geometry.width() - widget.width()) // 2
    y = (screen_geometry.height() - widget.height()) // 2

    # Move the widget to the calculated center position
    widget.move(x, y)


def center_on_parent(widget):
    """
    Center a widget relative to its parent window.

    If the widget has a parent, it will be centered relative to the parent's window.
    Otherwise, it will be centered on the screen using center_on_screen.

    Args:
        - widget (QWidget): The widget to center relative to its parent.
    """
    if widget.parent():
        # Get the parent window's geometry
        parent_geometry = widget.parent().window().geometry()

        # Calculate the center position relative to parent
        x = parent_geometry.x() + (parent_geometry.width() - widget.width()) // 2
        y = parent_geometry.y() + (parent_geometry.height() - widget.height()) // 2

        # Move the widget to the calculated center position
        widget.move(x, y)
    else:
        # Fallback to screen centering if no parent
        center_on_screen(widget)


def create_back_button(main_window, action_button, button_layout, main_frame_layout):
    """
    Create a back button with standard styling and add it to the layouts.

    This function creates a gray "Back" button that navigates to the main page when clicked.
    It adds both the action button and back button to the button layout and then adds
    the button layout to the main frame layout with appropriate spacing.

    Args:
        - main_window: The main window instance that contains the show_main_page method.
        - action_button (QPushButton): The primary action button (encrypt/decrypt) to add alongside the back button.
        - button_layout (QHBoxLayout): The horizontal layout to add the buttons to.
        - main_frame_layout (QVBoxLayout): The main frame layout to add the button layout to.

    Returns:
        QPushButton: The created back button.
    """
    # Back button to return to the main page
    back_button = QPushButton("Back")
    back_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
    back_button.setStyleSheet("""
        QPushButton {
            background-color: #808080;  /* Gray background */
            color: white;  /* White text */
            border: none;  /* No border */
            border-radius: 5px;  /* Rounded corners */
            padding: 10px 20px;  /* Add padding for better clickability */
            min-width: 150px;  /* Minimum width for better appearance */
        }
        QPushButton:hover {
            background-color: #606060;  /* Darker gray when hovered */
        }
    """)
    back_button.clicked.connect(main_window.show_main_page)  # Connect to navigation method

    # Add buttons to the horizontal layout
    button_layout.addWidget(action_button)
    button_layout.addWidget(back_button)

    # Add the button layout to the main frame layout
    main_frame_layout.addLayout(button_layout)
    main_frame_layout.addSpacing(20)  # Add some space at the bottom

    return back_button


def create_input_field(label_text, main_frame_layout):
    """
    Create an input label and entry field with standard styling and add them to the layout.

    This function creates a label with the provided text and a QLineEdit for input.
    Both are styled consistently with the application's design and added to the provided layout.
    The entry field is configured to accept only 6-digit numbers.

    Args:
        - label_text (str): The text to display in the label above the input field.
        - main_frame_layout (QVBoxLayout): The layout to add the label and input field to.

    Returns:
        QLineEdit: The created entry field, which should be assigned to an instance variable.
    """
    # Input section with instructions
    input_label = QLabel(label_text)
    input_label.setFont(QFont("Arial", 14))
    input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    input_label.setStyleSheet("color: #212121;")  # Dark gray text
    main_frame_layout.addWidget(input_label)

    # Entry field with improved visibility and styling
    entry_field = QLineEdit()
    entry_field.setFont(QFont("Arial", 16))  # Larger font for better readability
    entry_field.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
    entry_field.setStyleSheet("""
        QLineEdit {
            background-color: white;  /* White background */
            color: #212121;  /* Dark gray text */
            border: 2px solid #000000;  /* Black border */
            border-radius: 5px;  /* Rounded corners */
            padding: 5px;  /* Inner padding */
            margin: 10px 50px;  /* Margin around the field */
        }
    """)
    entry_field.setFixedHeight(60)  # Fixed height for better appearance
    entry_field.setMaxLength(6)  # Limit input to 6 characters
    # Add validator to only accept numbers between 0 and 999,999
    entry_field.setValidator(QIntValidator(0, 999999))
    main_frame_layout.addWidget(entry_field)
    main_frame_layout.addSpacing(20)  # Add vertical space

    return entry_field
