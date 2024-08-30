import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layouts
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        # Labels
        self.input_label = QLabel('Enter value:')
        self.result_label = QLabel('Result:')
        
        # Input field
        self.input_field = QLineEdit(self)
        
        # Units
        self.units = ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Feet', 'Inches']
        
        # Combo Boxes
        self.from_unit = QComboBox(self)
        self.from_unit.addItems(self.units)
        self.to_unit = QComboBox(self)
        self.to_unit.addItems(self.units)

        # Convert Button
        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_units)
        
        # Result field
        self.result_field = QLineEdit(self)
        self.result_field.setReadOnly(True)

        # Adding widgets to layout
        hbox.addWidget(self.input_label)
        hbox.addWidget(self.input_field)
        hbox.addWidget(self.from_unit)
        hbox.addWidget(self.to_unit)
        hbox.addWidget(self.convert_button)

        vbox.addLayout(hbox)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.result_field)

        self.setLayout(vbox)

        # Window settings
        self.setWindowTitle('Unit Converter')
        self.setGeometry(100, 100, 400, 200)
        
        # Apply dark and teal theme
        self.setStyleSheet("""
            QWidget {
                background-color: #2E2E2E;  # Dark background
                color: #E0E0E0;            # Light text
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                color: #E0E0E0;
            }
            QLineEdit {
                background-color: #3D3D3D;  # Darker input background
                color: #E0E0E0;
                border: 1px solid #008080;  # Teal border
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #008080;  # Teal background
                color: #E0E0E0;
                border: 1px solid #006666;  # Darker teal border
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #004d4d;  # Darker teal on hover
            }
            QComboBox {
                background-color: #3D3D3D;  # Dark background
                color: #E0E0E0;
                border: 1px solid #008080;  # Teal border
                border-radius: 5px;
                padding: 5px;
            }
        """)

    def convert_units(self):
        try:
            value = float(self.input_field.text())
            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()

            # Conversion factors
            conversion_factors = {
                ('Meters', 'Kilometers'): 0.001,
                ('Meters', 'Centimeters'): 100,
                ('Meters', 'Millimeters'): 1000,
                ('Meters', 'Feet'): 3.28084,
                ('Meters', 'Inches'): 39.3701,
                # Add other conversion factors as needed
            }
            
            # Unit conversion
            if from_unit == to_unit:
                result = value
            else:
                key = (from_unit, to_unit)
                if key in conversion_factors:
                    result = value * conversion_factors[key]
                else:
                    result = value / conversion_factors[(to_unit, from_unit)]

            self.result_field.setText(f"{result:.2f}")

        except ValueError:
            self.result_field.setText("Invalid input")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec_())
