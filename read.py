import pandas as pd

def read_csv_file(file_path):

    data = pd.read_csv(file_path, sep=';')
    return data

file_path = 'username.csv'
df = read_csv_file(file_path)
print(df.head())
