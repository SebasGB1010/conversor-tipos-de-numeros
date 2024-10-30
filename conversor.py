import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Números")
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.conversion_tab = QWidget()
        self.sum_tab = QWidget()
        self.multiply_tab = QWidget()

        self.tabs.addTab(self.conversion_tab, "Conversão")
        self.tabs.addTab(self.sum_tab, "Soma de Binários")
        self.tabs.addTab(self.multiply_tab, "Multiplicação de Binários")

        self.init_conversion_tab()
        self.init_sum_tab()
        self.init_multiply_tab()

        self.apply_styles()

    def init_conversion_tab(self):
        layout = QVBoxLayout()

        # Layout para tipo de entrada
        input_type_layout = QHBoxLayout()
        input_type_layout.addWidget(QLabel("Tipo de Entrada:"))
        self.input_type_combo = QComboBox()
        self.input_type_combo.addItems(["Binário", "Decimal", "Octal", "Hexadecimal"])
        self.input_type_combo.setMaximumWidth(200)
        input_type_layout.addWidget(self.input_type_combo)
        input_type_layout.addStretch()
        layout.addLayout(input_type_layout)

        # Layout para número de entrada
        input_number_layout = QHBoxLayout()
        input_number_layout.addWidget(QLabel("Número:"))
        self.input_entry = QLineEdit()
        self.input_entry.setMaximumWidth(200)
        input_number_layout.addWidget(self.input_entry)
        input_number_layout.addStretch()
        layout.addLayout(input_number_layout)

        # Layout para tipo de saída
        output_type_layout = QHBoxLayout()
        output_type_layout.addWidget(QLabel("Tipo de Saída:"))
        self.output_type_combo = QComboBox()
        self.output_type_combo.addItems(["Binário", "Decimal", "Octal", "Hexadecimal"])
        self.output_type_combo.setMaximumWidth(200)
        output_type_layout.addWidget(self.output_type_combo)
        output_type_layout.addStretch()
        layout.addLayout(output_type_layout)

        # Botão de conversão
        self.convert_button = QPushButton("Converter")
        self.convert_button.setMinimumSize(200, 50)
        self.convert_button.clicked.connect(self.convert)
        layout.addWidget(self.convert_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Texto de resultado
        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.conversion_tab.setLayout(layout)

    def init_sum_tab(self):
        layout = QVBoxLayout()

        # Layout para número 1
        input_sum1_layout = QHBoxLayout()
        input_sum1_layout.addWidget(QLabel("Número 1:"))
        self.input_entry_sum1 = QLineEdit()
        self.input_entry_sum1.setMaximumWidth(200)
        input_sum1_layout.addWidget(self.input_entry_sum1)
        input_sum1_layout.addStretch()
        layout.addLayout(input_sum1_layout)

        # Layout para número 2
        input_sum2_layout = QHBoxLayout()
        input_sum2_layout.addWidget(QLabel("Número 2:"))
        self.input_entry_sum2 = QLineEdit()
        self.input_entry_sum2.setMaximumWidth(200)
        input_sum2_layout.addWidget(self.input_entry_sum2)
        input_sum2_layout.addStretch()
        layout.addLayout(input_sum2_layout)

        # Botão de soma
        self.sum_button = QPushButton("Somar")
        self.sum_button.setMinimumSize(200, 50)
        self.sum_button.clicked.connect(self.sum_binary)
        layout.addWidget(self.sum_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Texto de resultado
        self.result_text_sum = QTextEdit()
        layout.addWidget(self.result_text_sum)

        self.sum_tab.setLayout(layout)

    def init_multiply_tab(self):
        layout = QVBoxLayout()

        # Layout para número 1
        input_multiply1_layout = QHBoxLayout()
        input_multiply1_layout.addWidget(QLabel("Número 1:"))
        self.input_entry_multiply1 = QLineEdit()
        self.input_entry_multiply1.setMaximumWidth(200)
        input_multiply1_layout.addWidget(self.input_entry_multiply1)
        input_multiply1_layout.addStretch()
        layout.addLayout(input_multiply1_layout)

        # Layout para número 2
        input_multiply2_layout = QHBoxLayout()
        input_multiply2_layout.addWidget(QLabel("Número 2:"))
        self.input_entry_multiply2 = QLineEdit()
        self.input_entry_multiply2.setMaximumWidth(200)
        input_multiply2_layout.addWidget(self.input_entry_multiply2)
        input_multiply2_layout.addStretch()
        layout.addLayout(input_multiply2_layout)

        # Botão de multiplicação
        self.multiply_button = QPushButton("Multiplicar")
        self.multiply_button.setMinimumSize(200, 50)
        self.multiply_button.clicked.connect(self.multiply_binary)
        layout.addWidget(self.multiply_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Texto de resultado
        self.result_text_multiply = QTextEdit()
        layout.addWidget(self.result_text_multiply)

        self.multiply_tab.setLayout(layout)

    def convert(self):
        input_type = self.input_type_combo.currentText()
        output_type = self.output_type_combo.currentText()
        input_value = self.input_entry.text()

        if input_type == "Binário":
            decimal_value, input_steps = self.binary_to_decimal(input_value)
        elif input_type == "Decimal":
            decimal_value = int(input_value)
            input_steps = [f"Entrada Decimal: {input_value}"]
        elif input_type == "Octal":
            decimal_value, input_steps = self.octal_to_decimal(input_value)
        elif input_type == "Hexadecimal":
            decimal_value, input_steps = self.hexadecimal_to_decimal(input_value)
        else:
            self.result_text.setText("Tipo de entrada não válido")
            return

        if output_type == "Binário":
            result, output_steps = self.decimal_to_binary(decimal_value)
        elif output_type == "Decimal":
            result = str(decimal_value)
            output_steps = []
        elif output_type == "Octal":
            result, output_steps = self.decimal_to_octal(decimal_value)
        elif output_type == "Hexadecimal":
            result, output_steps = self.decimal_to_hexadecimal(decimal_value)
        else:
            self.result_text.setText("Tipo de saída não válido")
            return

        self.result_text.setText(f"Resultado: {result}\n\nPassos:\n" + "\n".join(input_steps + output_steps))

    def sum_binary(self):
        bin1 = self.input_entry_sum1.text()
        bin2 = self.input_entry_sum2.text()
        decimal1 = int(bin1, 2)
        decimal2 = int(bin2, 2)
        sum_result = decimal1 + decimal2
        binary_result = bin(sum_result)[2:]
        self.result_text_sum.setText(f"Soma: {binary_result}")

    def multiply_binary(self):
        bin1 = self.input_entry_multiply1.text()
        bin2 = self.input_entry_multiply2.text()
        decimal1 = int(bin1, 2)
        decimal2 = int(bin2, 2)
        multiply_result = decimal1 * decimal2
        binary_result = bin(multiply_result)[2:]
        self.result_text_multiply.setText(f"Multiplicação: {binary_result}")

    def binary_to_decimal(self, binary_str):
        decimal = 0
        steps = []
        for i, digit in enumerate(reversed(binary_str)):
            value = int(digit) * (2 ** i)
            decimal += value
            steps.append(f"{digit} * 2^{i} = {value}")
        steps.append(f"Resultado final: {decimal}")
        return decimal, steps

    def decimal_to_binary(self, decimal_int):
        binary = ""
        steps = []
        n = int(decimal_int)
        while n > 0:
            remainder = n % 2
            binary = str(remainder) + binary
            steps.append(f"{n} / 2 = {n // 2}, Resto = {remainder}")
            n = n // 2
        steps.append(f"Resultado final: {binary}")
        return binary, steps

    def decimal_to_octal(self, decimal_int):
        octal = ""
        steps = []
        n = int(decimal_int)
        while n > 0:
            remainder = n % 8
            octal = str(remainder) + octal
            steps.append(f"{n} / 8 = {n // 8}, Resto = {remainder}")
            n = n // 8
        steps.append(f"Resultado final: {octal}")
        return octal, steps

    def decimal_to_hexadecimal(self, decimal_int):
        hexadecimal = ""
        steps = []
        n = int(decimal_int)
        while n > 0:
            remainder = n % 16
            hex_digit = hex(remainder)[2:].upper()
            hexadecimal = hex_digit + hexadecimal
            steps.append(f"{n} / 16 = {n // 16}, Resto = {remainder} ({hex_digit})")
            n = n // 16
        steps.append(f"Resultado final: {hexadecimal}")
        return hexadecimal, steps

    def octal_to_decimal(self, octal_str):
        decimal = 0
        steps = []
        for i, digit in enumerate(reversed(octal_str)):
            value = int(digit) * (8 ** i)
            decimal += value
            steps.append(f"{digit} * 8^{i} = {value}")
        steps.append(f"Resultado final: {decimal}")
        return decimal, steps

    def hexadecimal_to_decimal(self, hex_str):
        decimal = 0
        steps = []
        for i, digit in enumerate(reversed(hex_str)):
            value = int(digit, 16) * (16 ** i)
            decimal += value
            steps.append(f"{digit} * 16^{i} = {value}")
        steps.append(f"Resultado final: {decimal}")
        return decimal, steps

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #0078d7;
            }
            QPushButton {
                font-size: 14px;
                padding: 10px;
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
            QPushButton:pressed {
                background-color: #003f8a;
            }
            QTextEdit {
                font-size: 14px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QComboBox {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QComboBox:focus {
                border: 1px solid #0078d7;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())