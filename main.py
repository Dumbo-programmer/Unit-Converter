import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main Layout
        layout = QVBoxLayout()

        # Input Fields Layout
        input_layout = QHBoxLayout()

        # Input Field Widgets
        self.input_label = QLabel('Enter value:')
        self.input_field = QLineEdit(self)

        # Combo Boxes for Unit Types and Units
        self.unit_type = QComboBox(self)
        self.unit_type.addItems(['Length', 'Temperature', 'Weight', 'Time', 'Speed'])
        self.unit_type.currentIndexChanged.connect(self.update_units)

        self.from_unit = QComboBox(self)
        self.to_unit = QComboBox(self)

        self.update_units()  # Initialize units based on the default selection

        # Convert Button
        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_units)

        # Input Field Layout Setup
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.unit_type)
        input_layout.addWidget(self.from_unit)
        input_layout.addWidget(self.to_unit)
        input_layout.addWidget(self.convert_button)

        # Result Layout
        result_layout = QHBoxLayout()
        self.result_label = QLabel('Result:')
        self.result_field = QLineEdit(self)
        self.result_field.setReadOnly(True)
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result_field)

        # Add all layouts to the main layout
        layout.addLayout(input_layout)
        layout.addLayout(result_layout)
        
        self.setLayout(layout)

        # Window settings
        self.setWindowTitle('Enhanced Unit Converter')
        self.setGeometry(100, 100, 800, 150)
        
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

    def update_units(self):
        """Update unit options based on selected unit type."""
        self.from_unit.clear()
        self.to_unit.clear()
        
        unit_type = self.unit_type.currentText()

        if unit_type == 'Length':
            units = ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Feet', 'Inches']
        elif unit_type == 'Temperature':
            units = ['Celsius', 'Fahrenheit', 'Kelvin']
        elif unit_type == 'Weight':
            units = ['Kilograms', 'Grams', 'Pounds', 'Ounces']
        elif unit_type == 'Time':
            units = ['Seconds', 'Minutes', 'Hours', 'Days']
        elif unit_type == 'Speed':
            units = ['Meters per second', 'Kilometers per hour', 'Miles per hour']
        
        self.from_unit.addItems(units)
        self.to_unit.addItems(units)

    def convert_units(self):
        """Convert units based on user input."""
        try:
            value = float(self.input_field.text())
            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()

            if from_unit == to_unit:
                result = value
            else:
                result = self.perform_conversion(value, from_unit, to_unit)

            self.result_field.setText(f"{result:.2f}")

        except ValueError:
            self.result_field.setText("Invalid input")

    def perform_conversion(self, value, from_unit, to_unit):
        """Perform unit conversion based on selected units."""
        # Conversion factors for length
        length_factors = {
            'Meters': 1,
            'Kilometers': 0.001,
            'Centimeters': 100,
            'Millimeters': 1000,
            'Feet': 3.28084,
            'Inches': 39.3701
        }

        # Conversion functions for temperature
        def celsius_to_fahrenheit(c):
            return (c * 9/5) + 32

        def fahrenheit_to_celsius(f):
            return (f - 32) * 5/9

        def celsius_to_kelvin(c):
            return c + 273.15

        def kelvin_to_celsius(k):
            return k - 273.15

        # Conversion factors for weight
        weight_factors = {
            'Kilograms': 1,
            'Grams': 1000,
            'Pounds': 2.20462,
            'Ounces': 35.274
        }

        # Conversion factors for time
        time_factors = {
            'Seconds': 1,
            'Minutes': 1/60,
            'Hours': 1/3600,
            'Days': 1/86400
        }

        # Conversion factors for speed
        speed_factors = {
            'Meters per second': 1,
            'Kilometers per hour': 3.6,
            'Miles per hour': 2.23694
        }

        if from_unit in length_factors and to_unit in length_factors:
            return value * (length_factors[to_unit] / length_factors[from_unit])
        elif from_unit in weight_factors and to_unit in weight_factors:
            return value * (weight_factors[to_unit] / weight_factors[from_unit])
        elif from_unit in time_factors and to_unit in time_factors:
            return value * (time_factors[to_unit] / time_factors[from_unit])
        elif from_unit in speed_factors and to_unit in speed_factors:
            return value * (speed_factors[to_unit] / speed_factors[from_unit])
        elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return celsius_to_fahrenheit(value)
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return fahrenheit_to_celsius(value)
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return celsius_to_kelvin(value)
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return kelvin_to_celsius(value)
        else:
            raise ValueError("Conversion not supported")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec_())
