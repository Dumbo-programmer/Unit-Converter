import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
                             QComboBox, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox)
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
        self.unit_type.addItems(['Length', 'Temperature', 'Weight', 'Time', 'Speed', 
                                 'Data Storage', 'Area', 'Volume', 'Energy', 'Currency'])
        self.unit_type.currentIndexChanged.connect(self.update_units)

        self.from_unit = QComboBox(self)
        self.to_unit = QComboBox(self)

        self.update_units()  # Initialize units based on the default selection

        # Convert Button
        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_units)

        # Favorite Checkbox
        self.favorite_checkbox = QCheckBox("Add to Favorites")

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

        # Favorites Layout
        favorites_layout = QVBoxLayout()
        self.favorites_label = QLabel('Favorites:')
        self.favorites_box = QComboBox(self)
        self.favorites_box.currentIndexChanged.connect(self.load_favorite)
        favorites_layout.addWidget(self.favorites_label)
        favorites_layout.addWidget(self.favorites_box)

        # Add all layouts to the main layout
        layout.addLayout(input_layout)
        layout.addLayout(result_layout)
        layout.addWidget(self.favorite_checkbox)
        layout.addLayout(favorites_layout)
        
        self.setLayout(layout)

        # Window settings
        self.setWindowTitle('Advanced Unit Converter')
        self.setGeometry(100, 100, 900, 200)
        
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

        # Initialize favorites list
        self.favorites = []

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
        elif unit_type == 'Data Storage':
            units = ['Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes']
        elif unit_type == 'Area':
            units = ['Square meters', 'Square kilometers', 'Square feet', 'Square inches']
        elif unit_type == 'Volume':
            units = ['Liters', 'Milliliters', 'Cubic meters', 'Cubic inches']
        elif unit_type == 'Energy':
            units = ['Joules', 'Calories', 'Kilowatt-hours']
        elif unit_type == 'Currency':
            units = ['USD', 'EUR', 'JPY', 'GBP']  # Static for now; can be dynamic with an API

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

            # Save to favorites if checkbox is checked
            if self.favorite_checkbox.isChecked():
                self.save_favorite(value, from_unit, to_unit, result)
                self.favorite_checkbox.setChecked(False)  # Reset checkbox

        except ValueError:
            self.result_field.setText("Invalid input")

    def perform_conversion(self, value, from_unit, to_unit):
        """Perform unit conversion based on selected units."""
        # Conversion factors and logic for various types go here...
        # For now, let's use the earlier logic and expand as needed.
        # This section can be expanded with new conversion logic.

        return value  # Placeholder: replace with actual conversion logic

    def save_favorite(self, value, from_unit, to_unit, result):
        """Save the conversion to favorites."""
        favorite_text = f"{value} {from_unit} to {to_unit} = {result:.2f}"
        self.favorites.append(favorite_text)
        self.favorites_box.addItem(favorite_text)

    def load_favorite(self):
        """Load a favorite conversion into the input fields."""
        favorite = self.favorites_box.currentText()
        if favorite:
            parts = favorite.split()
            self.input_field.setText(parts[0])
            self.from_unit.setCurrentText(parts[1])
            self.to_unit.setCurrentText(parts[3])
            self.result_field.setText(parts[5])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec_())
