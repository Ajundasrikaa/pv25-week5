import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox,
    QPushButton, QFormLayout, QMessageBox, QShortcut
)
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtCore import Qt

class FormValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ajundasrika Anugrahanti TS (F1D022108)')
        self.setFixedSize(400, 450)

        layout = QFormLayout()
        font = QFont("Segoe UI", 10)

        self.nameInput = QLineEdit()
        self.nameInput.setFont(font)

        self.emailInput = QLineEdit()
        self.emailInput.setFont(font)

        self.ageInput = QLineEdit()
        self.ageInput.setFont(font)

        self.phoneInput = QLineEdit()
        self.phoneInput.setFont(font)
        self.phoneInput.setInputMask('+62 999 9999 9999')

        self.addressInput = QTextEdit()
        self.addressInput.setFont(font)
        self.addressInput.setFixedHeight(60)

        self.genderInput = QComboBox()
        self.genderInput.setFont(font)
        self.genderInput.addItems(['', 'Male', 'Female', 'Other'])
        self.genderInput.setFixedWidth(150)

        self.educationInput = QComboBox()
        self.educationInput.setFont(font)
        self.educationInput.addItems(['', 'High School', 'Diploma', 'Bachelor', 'Master', 'Doctorate'])
        self.educationInput.setFixedWidth(180)

        self.saveButton = QPushButton('💾 Save')
        self.saveButton.setFont(font)
        self.saveButton.clicked.connect(self.validateForm)

        self.clearButton = QPushButton('🧹 Clear')
        self.clearButton.setFont(font)
        self.clearButton.clicked.connect(self.clearFields)

        layout.setVerticalSpacing(15)
        layout.setFormAlignment(Qt.AlignTop)
        layout.addRow('Name:', self.nameInput)
        layout.addRow('Email:', self.emailInput)
        layout.addRow('Age:', self.ageInput)
        layout.addRow('Phone Number:', self.phoneInput)
        layout.addRow('Address:', self.addressInput)
        layout.addRow('Gender:', self.genderInput)
        layout.addRow('Education:', self.educationInput)
        layout.addRow(self.saveButton, self.clearButton)

        self.setLayout(layout)

        QShortcut(QKeySequence("Q"), self, activated=self.close)

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI';
            }

            QLineEdit, QTextEdit, QComboBox {
                background-color: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 6px;
            }

            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
                border: 1.5px solid #0078D7;
                background-color: #e9f5ff;
            }

            QPushButton {
                padding: 8px 12px;
                border-radius: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                opacity: 0.9;
            }

            QPushButton:pressed {
                padding-left: 10px;
                padding-top: 9px;
            }

            QPushButton:nth-child(1) {
                background-color: #0078D7;
                color: white;
            }

            QPushButton:nth-child(2) {
                background-color: #f44336;
                color: white;
            }

            QComboBox {
                min-width: 100px;
            }

            QComboBox::drop-down {
                border-left: 1px solid #ced4da;
                background-color: #0078D7;
                width: 25px;
                border-top-right-radius: 6px;
                border-bottom-right-radius: 6px;
            }

            QComboBox::down-arrow {
                image: none;
                border: none;
                width: 0;
                height: 0;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 8px solid white;
                margin: 6px;
            }
        """)

    def validateForm(self):
        name = self.nameInput.text().strip()
        email = self.emailInput.text().strip()
        age = self.ageInput.text().strip()
        phone = self.phoneInput.text().replace(' ', '')
        address = self.addressInput.toPlainText().strip()
        gender = self.genderInput.currentText()
        education = self.educationInput.currentText()

        if not name:
            self.showWarning('All fields are required.')
            return

        if not re.match(r"^[A-Za-z\s]+$", name):
            self.showWarning('Name can only contain letters and spaces.')
            return

        if len(name) < 3:
            self.showWarning('Name must be at least 3 characters.')
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.showWarning('Please enter a valid email address.')
            return

        if not age.isdigit():
            self.showWarning('Please enter a valid age (integer value).')
            return

        if len(phone) != 14:
            self.showWarning('Please enter a valid 13 digit phone number.')
            return

        if not address:
            self.showWarning('Address is required.')
            return

        if gender == '':
            self.showWarning('Please select a gender.')
            return

        if education == '':
            self.showWarning('Please select an education level.')
            return

        QMessageBox.information(self, 'Success', 'Profile saved successfully!')
        self.clearFields()

    def showWarning(self, message):
        QMessageBox.warning(self, 'Validation Error', message)

    def clearFields(self):
        self.nameInput.clear()
        self.emailInput.clear()
        self.ageInput.clear()
        self.phoneInput.clear()
        self.addressInput.clear()
        self.genderInput.setCurrentIndex(0)
        self.educationInput.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormValidator()
    window.show()
    sys.exit(app.exec_())
