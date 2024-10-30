# Conversor de Números

Esta aplicação permite converter números entre diferentes sistemas numéricos (Binário, Decimal, Octal e Hexadecimal), bem como somar e multiplicar números binários.

## Funcionalidades

- Conversão entre Binário, Decimal, Octal e Hexadecimal.
- Soma de números binários.
- Multiplicação de números binários.
- Interface gráfica moderna.
- Resultados e passos da conversão exibidos na interface.
- Possibilidade de copiar os passos da conversão para a área de transferência.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/conversor-de-numeros.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd conversor-de-numeros
    ```
3. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute a aplicação:
    ```sh
    python conversor.py
    ```
2. A aplicação abrir-se-á em ecrã completo.
3. Selecione o tipo de entrada e saída, introduza o número e clique em "Converter".
4. Os resultados e os passos da conversão serão mostrados na interface.
5. Pode copiar os passos da conversão para a área de transferência clicando em "Copiar Passos".

## Contribuições

As contribuições são bem-vindas. Por favor, abra um issue ou um pull request para discutir qualquer alteração que deseje realizar.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

## Atualizações Recentes

### Reorganização da Interface

- Os elementos de entrada estão agora centrados na interface.
- Adicionada uma barra de rolagem ao widget de texto para permitir o deslocamento quando o conteúdo é muito grande.
- Melhorias no estilo da interface utilizando QSS para um tema moderno e escuro.
- As conversões serão feitas em real time