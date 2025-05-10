# Number encryption and decryption

A desktop application for encrypting and decrypting 6-digit numbers using a simple algorithm. Built with PyQt6 for a modern and responsive user interface.

![Application Demo](assets/app-demo.gif)

## Features

- **Encryption**: Convert a 6-digit number into an encrypted form using a simple algorithm
- **Decryption**: Recover the original number from its encrypted form
- **User-friendly Interface**: Modern UI with clear navigation and instructions
- **Copy to Clipboard**: Copy results with a single click
- **Input Validation**: Ensures only valid 6-digit numbers are processed

## Encryption algorithm

The application uses a simple encryption algorithm:

1. **For encryption**:
   - Add 7 to each digit and take the remainder when divided by 10
   - Swap the first digit with the third
   - Swap the second digit with the fourth
   - Swap the fifth digit with the sixth

2. **For decryption**:
   - Reverse the digit swaps
   - Subtract 7 from each digit (or add 3, which is equivalent to mod 10)

## Requirements

- Python 3.6 or higher
- PyQt6 6.0.0 or higher
- pyperclip 1.8.2 or higher

## Installation

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. The main screen will appear with two options:
   - **Encrypt**: Click to encrypt a 6-digit number
   - **Decrypt**: Click to decrypt a previously encrypted number

3. **To encrypt a number**:
   - Enter a 6-digit number in the input field
   - Click the "Encrypt" button
   - The encrypted result will appear in a modal dialog
   - Click the "Copy" button to copy the result to the clipboard
   - Click anywhere on the dialog to close it

4. **To decrypt a number**:
   - Enter a 6-digit encrypted number in the input field
   - Click the "Decrypt" button
   - The original number will appear in a modal dialog
   - Click the "Copy" button to copy the result to the clipboard
   - Click anywhere on the dialog to close it

## Project structure

```
encrypt-decrypt-data/
├── assets/
│   └── PlaygroundImage.png  # Background image for the main screen
├── functions/
│   ├── __init__.py
│   ├── crypto.py            # Encryption and decryption algorithms
│   └── utils.py             # Utility functions for UI components
├── windows/
│   ├── __init__.py
│   ├── main_window.py       # Main application window
│   ├── encrypt_window.py    # Encryption page
│   ├── decrypt_window.py    # Decryption page
│   └── result_window.py     # Result dialog
├── main.py                  # Application entry point
└── requirements.txt         # Required packages
```

### Key elements

- **main.py**: Entry point for the application, sets up the PyQt application and global stylesheet
- **main_window.py**: Defines the MainWindow class, which contains the stacked widget for navigation
- **encrypt_window.py**: Defines the EncryptPage class for encrypting numbers
- **decrypt_window.py**: Defines the DecryptPage class for decrypting numbers
- **result_window.py**: Defines the ResultDialog class for displaying results
- **crypto.py**: Contains the encryption and decryption algorithms
- **utils.py**: Contains utility functions for UI components, such as centering windows and dialogs

## Troubleshooting

### Common Issues

1. **Application doesn't start**:
   - Ensure you have Python 3.6 or higher installed
   - Verify that all required packages are installed with `pip list`
   - Check for error messages in the console

2. **Copy to clipboard doesn't work**:
   - Ensure pyperclip is properly installed
   - Some Linux systems may require additional packages for clipboard functionality:
     ```
     sudo apt-get install xclip
     ```

3. **UI elements appear incorrectly**:
   - Ensure you have PyQt6 6.0.0 or higher installed
   - Try resizing the window to see if elements adjust properly

4. **Background image doesn't appear**:
   - Verify that the assets directory contains the PlaygroundImage.png file
   - Check file permissions to ensure the application can read the image

## License
This repository is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](http://creativecommons.org/licenses/by-nc-sa/4.0/).
### You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

### Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial** — You may not use the material for commercial purposes.
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

See the [LICENSE.md](LICENSE.md) file for more details.

## Author

- Andrés Leonardo Liscano (aliscano20@unisalle.edu.co)

## Referencias
- Riverbank Computing. (s.f.). PyQt6 Reference Guide. Recuperado el 9 de mayo de 2025, de https://www.riverbankcomputing.com/static/Docs/PyQt6/
