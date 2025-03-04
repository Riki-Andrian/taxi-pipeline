import pandas as pd
import re


class Transformer:
    @staticmethod
    def calculate_trip_duration(df, start_col, end_col):
        print('Menambahkan kolom trip durasi')
        df = df.copy()
        df[end_col] = pd.to_datetime(df[end_col])
        df[start_col] = pd.to_datetime(df[start_col])
        df['trip_duration'] = (df[end_col] - df[start_col]).astype(str).str.split().str[-1]
        df[start_col] = df[start_col].dt.strftime('%Y-%m-%d %H:%M:%S')
        df[end_col] = df[end_col].dt.strftime('%Y-%m-%d %H:%M:%S')
        print('Kolom trip durasi berhasil ditambahkan\n')
        return df

    @staticmethod
    def to_snake_case(name):
        name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)  
        name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)  
        name = re.sub(r'[\s\W]+', '_', name)
        return name.lower().strip('_')

    @staticmethod
    def map_payment_types(df, df_mapping, key_col, value_col):
        print('Merubah semua nilai payment_type menjadi label')
        df = df.copy()
        payment_mapping = dict(zip(df_mapping[key_col], df_mapping[value_col]))
        df['payment_type'] = df['payment_type'].map(payment_mapping)
        print('Semua nilai payment_type berhasil menjadi label\n')
        return df

    @staticmethod
    def convert_distance_to_km(df, distance_col):
        print('Merubah satuan trip_distance menjadi km')
        df = df.copy()
        df[distance_col] = (df[distance_col] * 1.60934).round(2)
        print('Satuan trip_distance berhasil dirubah menjadi km\n')
        return df


class Loader:
    @staticmethod
    def load_data(df):
        save_format = input("Pilih format penyimpanan (csv/excel): ").strip().lower()
        if save_format == "csv":
            df.to_csv("./result/result_data.csv", index=False)
            print("Data berhasil disimpan sebagai CSV.")
        elif save_format == "excel":
            df.to_excel("./result/result_data.xlsx", index=False)
            print("Data berhasil disimpan sebagai Excel.")
        else:
            print("Format tidak dikenali. Silakan pilih antara 'csv' atau 'excel'.")