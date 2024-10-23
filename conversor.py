import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica
from tkinter import ttk  # Importa o módulo ttk para usar widgets com estilo

# Função para converter os números
def convert():
    input_type = input_type_var.get()  # Obtém o tipo de entrada selecionado
    output_type = output_type_var.get()  # Obtém o tipo de saída selecionado
    input_value = input_entry.get()  # Obtém o valor de entrada

    # Verifica o tipo de entrada e converte para decimal
    if input_type == "Binário":
        decimal_value, input_steps = binary_to_decimal(input_value)  # Converte binário para decimal
    elif input_type == "Decimal":
        decimal_value = int(input_value)  # Converte a entrada para inteiro
        input_steps = [f"Entrada Decimal: {input_value}"]  # Regista o passo da conversão
    elif input_type == "Octal":
        decimal_value, input_steps = octal_to_decimal(input_value)  # Converte octal para decimal
    elif input_type == "Hexadecimal":
        decimal_value, input_steps = hexadecimal_to_decimal(input_value)  # Converte hexadecimal para decimal
    else:
        result_text.delete(1.0, tk.END)  # Limpa o texto do resultado
        result_text.insert(tk.END, "Tipo de entrada não válido")  # Exibe mensagem de erro
        return  # Sai da função

    # Converte de decimal para o tipo de saída desejado
    if output_type == "Binário":
        result, output_steps = decimal_to_binary(decimal_value)  # Converte decimal para binário
    elif output_type == "Decimal":
        result = str(decimal_value)  # Converte o valor decimal para string
        output_steps = []  # Não há passos adicionais para decimal
    elif output_type == "Octal":
        result, output_steps = decimal_to_octal(decimal_value)  # Converte decimal para octal
    elif output_type == "Hexadecimal":
        result, output_steps = decimal_to_hexadecimal(decimal_value)  # Converte decimal para hexadecimal
    else:
        result_text.delete(1.0, tk.END)  # Limpa o texto do resultado
        result_text.insert(tk.END, "Tipo de saída não válido")  # Exibe mensagem de erro
        return  # Sai da função

    # Exibe o resultado e os passos da conversão
    result_text.delete(1.0, tk.END)  # Limpa o texto do resultado
    result_text.insert(tk.END, f"Resultado: {result}\n\nPassos:\n" + "\n".join(input_steps + output_steps))  # Insere o resultado e os passos

# Função para copiar os passos da conversão para a área de transferência
def copy_steps():
    steps = result_text.get(1.0, tk.END)  # Obtém o texto dos passos
    root.clipboard_clear()  # Limpa a área de transferência
    root.clipboard_append(steps)  # Adiciona os passos à área de transferência
    root.update()  # Necessário para que a área de transferência seja atualizada
    print("Passos copiados para a área de transferência")  # Exibe mensagem no console

# Configuração da janela principal
root = tk.Tk()  # Cria a janela principal
root.title("Conversor de Números")  # Define o título da janela
root.state('zoomed')  # Abrir em ecrã completo

# Estilo
style = ttk.Style()  # Cria um objeto de estilo
style.theme_use('clam')  # Define o tema 'clam'
style.configure('TLabel', background='#f0f0f0', font=('Arial', 16))  # Configura o estilo das etiquetas
style.configure('TButton', background='#4CAF50', foreground='white', font=('Arial', 16))  # Configura o estilo dos botões
style.configure('TEntry', font=('Arial', 16))  # Configura o estilo das entradas de texto
style.configure('TCombobox', font=('Arial', 16))  # Configura o estilo das caixas de combinação

# Layout
main_frame = ttk.Frame(root, padding="20 20 20 20", style='TFrame')  # Cria o frame principal
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # Posiciona o frame principal
root.columnconfigure(0, weight=1)  # Configura a coluna para expandir
root.rowconfigure(0, weight=1)  # Configura a linha para expandir

# Variáveis
input_type_var = tk.StringVar()  # Cria uma variável de string para o tipo de entrada
output_type_var = tk.StringVar()  # Cria uma variável de string para o tipo de saída
input_entry = tk.StringVar()  # Cria uma variável de string para a entrada de texto
result_var = tk.StringVar()  # Cria uma variável de string para o resultado

# Widgets
# Seção de entrada à esquerda
input_frame = ttk.Frame(main_frame, padding="20 20 20 20", style='TFrame')  # Cria o frame de entrada
input_frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))  # Posiciona o frame de entrada
input_frame.columnconfigure(0, weight=1)  # Configura a coluna para expandir
input_frame.rowconfigure(0, weight=1)  # Configura a linha para expandir

ttk.Label(input_frame, text="Tipo de Entrada:").grid(column=0, row=0, sticky=tk.W, pady=10)  # Cria e posiciona a etiqueta do tipo de entrada
input_type_menu = ttk.Combobox(input_frame, textvariable=input_type_var, values=["Binário", "Decimal", "Octal", "Hexadecimal"])  # Cria a caixa de combinação para o tipo de entrada
input_type_menu.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=10)  # Posiciona a caixa de combinação

ttk.Label(input_frame, text="Número:").grid(column=0, row=1, sticky=tk.W, pady=10)  # Cria e posiciona a etiqueta do número
input_entry_widget = ttk.Entry(input_frame, textvariable=input_entry)  # Cria a entrada de texto para o número
input_entry_widget.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=10)  # Posiciona a entrada de texto

ttk.Label(input_frame, text="Tipo de Saída:").grid(column=0, row=2, sticky=tk.W, pady=10)  # Cria e posiciona a etiqueta do tipo de saída
output_type_menu = ttk.Combobox(input_frame, textvariable=output_type_var, values=["Binário", "Decimal", "Octal", "Hexadecimal"])  # Cria a caixa de combinação para o tipo de saída
output_type_menu.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=10)  # Posiciona a caixa de combinação

convert_button = ttk.Button(input_frame, text="Converter", command=convert)  # Cria o botão de conversão
convert_button.grid(column=1, row=3, sticky=tk.W, pady=20)  # Posiciona o botão de conversão

copy_button = ttk.Button(input_frame, text="Copiar Passos", command=copy_steps)  # Cria o botão para copiar os passos
copy_button.grid(column=1, row=4, sticky=tk.W, pady=20)  # Posiciona o botão para copiar os passos

# Seção de resultado à direita
result_frame = ttk.Frame(main_frame, padding="20 20 20 20", style='TFrame')  # Cria o frame de resultado
result_frame.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))  # Posiciona o frame de resultado
result_frame.columnconfigure(0, weight=1)  # Configura a coluna para expandir
result_frame.rowconfigure(0, weight=1)  # Configura a linha para expandir

result_text = tk.Text(result_frame, wrap="word", font=('Arial', 16), bg='#f0f0f0', relief='flat')  # Cria o widget de texto para o resultado
result_text.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # Posiciona o widget de texto

scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)  # Cria a barra de rolagem vertical
scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))  # Posiciona a barra de rolagem
result_text['yscrollcommand'] = scrollbar.set  # Configura a barra de rolagem para o widget de texto

# Padding
for child in main_frame.winfo_children():
    child.grid_configure(padx=20, pady=10)  # Adiciona padding aos widgets

# Funções de conversão
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

root.mainloop()  # Inicia o loop principal da aplicação