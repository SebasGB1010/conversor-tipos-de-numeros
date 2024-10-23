import tkinter as tk
from tkinter import ttk

def convert():
    input_type = input_type_var.get()
    output_type = output_type_var.get()
    input_value = input_entry.get()

    if input_type == "Binário":
        decimal_value, input_steps = binary_to_decimal(input_value)
    elif input_type == "Decimal":
        decimal_value = int(input_value)
        input_steps = [f"Entrada Decimal: {input_value}"]
    elif input_type == "Octal":
        decimal_value, input_steps = octal_to_decimal(input_value)
    elif input_type == "Hexadecimal":
        decimal_value, input_steps = hexadecimal_to_decimal(input_value)
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Tipo de entrada no válido")
        return

    if output_type == "Binário":
        result, output_steps = decimal_to_binary(decimal_value)
    elif output_type == "Decimal":
        result = str(decimal_value)
        output_steps = []
    elif output_type == "Octal":
        result, output_steps = decimal_to_octal(decimal_value)
    elif output_type == "Hexadecimal":
        result, output_steps = decimal_to_hexadecimal(decimal_value)
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Tipo de salida no válido")
        return

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Resultado: {result}\n\nPassos:\n" + "\n".join(input_steps + output_steps))

def copy_steps():
    steps = result_text.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(steps)
    root.update()  # Necesario para que el portapapeles se actualice
    print("Pasos copiados al portapapeles")

# Configuración de la raíz
root = tk.Tk()
root.title("Conversor de Números")
root.state('zoomed')  # Abrir en pantalla completa

# Estilo
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background='#f0f0f0', font=('Arial', 16))
style.configure('TButton', background='#4CAF50', foreground='white', font=('Arial', 16))
style.configure('TEntry', font=('Arial', 16))
style.configure('TCombobox', font=('Arial', 16))

# Layout
main_frame = ttk.Frame(root, padding="20 20 20 20", style='TFrame')
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variables
input_type_var = tk.StringVar()
output_type_var = tk.StringVar()
input_entry = tk.StringVar()
result_var = tk.StringVar()

# Widgets
# Sección de entrada a la izquierda
input_frame = ttk.Frame(main_frame, padding="20 20 20 20", style='TFrame')
input_frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))
input_frame.columnconfigure(0, weight=1)
input_frame.rowconfigure(0, weight=1)

ttk.Label(input_frame, text="Tipo de Entrada:").grid(column=0, row=0, sticky=tk.W, pady=10)
input_type_menu = ttk.Combobox(input_frame, textvariable=input_type_var, values=["Binário", "Decimal", "Octal", "Hexadecimal"])
input_type_menu.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=10)

ttk.Label(input_frame, text="Número:").grid(column=0, row=1, sticky=tk.W, pady=10)
input_entry_widget = ttk.Entry(input_frame, textvariable=input_entry)
input_entry_widget.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=10)

ttk.Label(input_frame, text="Tipo de Saída:").grid(column=0, row=2, sticky=tk.W, pady=10)
output_type_menu = ttk.Combobox(input_frame, textvariable=output_type_var, values=["Binário", "Decimal", "Octal", "Hexadecimal"])
output_type_menu.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=10)

convert_button = ttk.Button(input_frame, text="Converter", command=convert)
convert_button.grid(column=1, row=3, sticky=tk.W, pady=20)

copy_button = ttk.Button(input_frame, text="Copiar Passos", command=copy_steps)
copy_button.grid(column=1, row=4, sticky=tk.W, pady=20)

# Sección de resultado a la derecha
result_frame = ttk.Frame(main_frame, padding="20 20 20 20", style='TFrame')
result_frame.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))
result_frame.columnconfigure(0, weight=1)
result_frame.rowconfigure(0, weight=1)

result_text = tk.Text(result_frame, wrap="word", font=('Arial', 16), bg='#f0f0f0', relief='flat')
result_text.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))
result_text['yscrollcommand'] = scrollbar.set

# Padding
for child in main_frame.winfo_children():
    child.grid_configure(padx=20, pady=10)

# Funciones de conversión
def binary_to_decimal(binary_str):
    decimal = 0
    steps = []
    for i, digit in enumerate(reversed(binary_str)):
        value = int(digit) * (2 ** i)
        decimal += value
        steps.append(f"{digit} * 2^{i} = {value}")
    steps.append(f"Resultado final: {decimal}")
    return decimal, steps

def decimal_to_binary(decimal_int):
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

def decimal_to_octal(decimal_int):
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

def decimal_to_hexadecimal(decimal_int):
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

def octal_to_decimal(octal_str):
    decimal = 0
    steps = []
    for i, digit in enumerate(reversed(octal_str)):
        value = int(digit) * (8 ** i)
        decimal += value
        steps.append(f"{digit} * 8^{i} = {value}")
    steps.append(f"Resultado final: {decimal}")
    return decimal, steps

def hexadecimal_to_decimal(hex_str):
    decimal = 0
    steps = []
    for i, digit in enumerate(reversed(hex_str)):
        value = int(digit, 16) * (16 ** i)
        decimal += value
        steps.append(f"{digit} * 16^{i} = {value}")
    steps.append(f"Resultado final: {decimal}")
    return decimal, steps

root.mainloop()