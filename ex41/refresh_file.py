import pandas as pd

def atualizar_csv(origem_path, destino_path):
    df_origem = pd.read_csv(origem_path)
    try:
        df_destino = pd.read_csv(destino_path)
    except FileNotFoundError:
        df_destino = pd.DataFrame()  

    df_final = pd.concat([df_destino, df_origem]).drop_duplicates()
    
    if len(df_final) > len(df_destino):
        df_final.to_csv(destino_path, index=False)
        print("Novos dados foram adicionados ao CSV de destino.")
    else:
        print("Nenhum dado novo foi encontrado para adicionar.")

origem_path = r"C:\Users\Rafar\OneDrive\Área de Trabalho\file1.csv"
destino_path = r"C:\Users\Rafar\OneDrive\Área de Trabalho\file2.csv"

atualizar_csv(origem_path, destino_path)
