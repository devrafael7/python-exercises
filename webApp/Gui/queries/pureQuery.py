import pandas as pd

file_path = r'C:\Users\Rafar\OneDrive\Área de Trabalho\my_file.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Converte para HTML (em formato de string)
html_table = df.to_html(index=False)  # index=False para não mostrar a coluna de índice

# Salva em um arquivo HTML
with open('pureQuery.html', 'w', encoding='utf-8') as f:
    f.write(html_table)
