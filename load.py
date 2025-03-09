import pandas as pd
from sklearn.datasets import load_iris
from datetime import datetime
from pathlib import Path

def load_and_prepare_iris_data():
    """Carga el conjunto de datos Iris y lo convierte en un DataFrame."""
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df.sample(frac=0.05)

def load_existing_data(file_path):
    """Carga un DataFrame existente desde un archivo CSV."""
    return pd.read_csv(file_path, sep=',', decimal='.', header=0, encoding='utf-8')

def save_data(df, file_path):
    """Guarda el DataFrame en un archivo CSV."""
    df.to_csv(file_path, encoding='utf-8-sig', index=False)

def main():
    # Imprime la fecha actual
    print(f'La fecha es: {datetime.now()}')

    # Carga y prepara el nuevo conjunto de datos Iris
    df_new = load_and_prepare_iris_data()
    print(f'shape new: {df_new.shape}')

    # Carga el DataFrame existente
    file_path = Path('df.csv')
    df_old = load_existing_data(file_path)
    print(f'shape old: {df_old.shape}')

    # Combina los DataFrames
    df = pd.concat([df_old, df_new], ignore_index=True)
    print(f'shape actual: {df.shape}')

    # Guarda el DataFrame combinado
    save_data(df, file_path)

    # Visualiza las primeras filas del DataFrame (opcional)
    # print('Aca se imprime el dataframe iris:')
    # print(df.head())

if __name__ == "__main__":
    main()