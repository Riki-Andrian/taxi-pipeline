import os
# import pandas as pd
# from transform import calculate_trip_duration, map_payment_types, convert_distance_to_km, to_snake_case, load_data
# from ekstrak import extract_data

from ekstrak import Extractor
from transform import Transformer, Loader
import pandas as pd

# def check_staging_file():
#     staging_file = "./staging/staged_data.csv"
#     return os.path.exists(staging_file)

# def load_staging_data():
#     staging_file = "./staging/staged_data.csv"
#     if check_staging_file():
#         print("Menggunakan data dari staging/staged_data.csv")
#         return pd.read_csv(staging_file)
#     else:
#         print("Data belum tersedia. Silakan ekstrak terlebih dahulu.")
#         return None

# def main():
#     df = None
#     df1 = pd.read_csv('./data/payment_type.csv')
    
#     while True:
#         print("\nMenu Transformasi Data:")
#         print("1. Ekstrak Data")
#         print("2. Transform Data")
#         print("3. Load Data")
#         print("4. Tampilkan Data (Head)")
#         print("5. Keluar")
        
#         choice = input("Pilih opsi (1-5): ")
        
#         if choice == "1":
#             if check_staging_file():
#                 use_existing = input("File staged_data.csv sudah ada. Gunakan data ini? (y/n): ").strip().lower()
#                 if use_existing == 'y':
#                     df = load_staging_data()
#                 else:
#                     folder_path = "./data/"
#                     df = extract_data(folder_path)
#             else:
#                 folder_path = "./data/"
#                 df = extract_data(folder_path)
        
#         elif choice == "2":
#             if df is None:
#                 df = load_staging_data()
#                 if df is None:
#                     continue

#             df = calculate_trip_duration(df, 'lpep_pickup_datetime', 'lpep_dropoff_datetime')

#             print("Merubah semua nama kolom menjadi snake_case.")
#             df.columns = [to_snake_case(col) for col in df.columns]
#             print("Semua nama kolom berhasil dirubah menjadi snake_case.\n")

#             df = map_payment_types(df, df1, 'payment_type', 'description')
#             df = convert_distance_to_km(df, 'trip_distance')
        
#         elif choice == "3":
#             load_data(df)
        
#         elif choice == "4":
#             if df is None:
#                 df = load_staging_data()
#                 if df is None:
#                     continue
#             print(df.head())
#             print(df.info())
#         elif choice == "5":
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid atau data belum tersedia, silakan coba lagi.")
    
# if __name__ == "__main__":
#     main()

def check_staging_file():
    staging_file = "./staging/staged_data.csv"
    return os.path.exists(staging_file)

def load_staging_data():
    staging_file = "./staging/staged_data.csv"
    if check_staging_file():
        print("Menggunakan data dari staging/staged_data.csv")
        return pd.read_csv(staging_file)
    else:
        print("Data belum tersedia. Silakan ekstrak terlebih dahulu.")
        return None

class MainApp:
    def __init__(self):
        self.df = None
        self.extractor = Extractor("./data/")
        self.transformer = Transformer()
        self.loader = Loader()
        self.df_payment = pd.read_csv('./data/payment_type.csv')

    def run(self):
        while True:
            print("\nMenu Transformasi Data:")
            print("1. Ekstrak Data")
            print("2. Transform Data")
            print("3. Load Data")
            print("4. Tampilkan Data (Head)")
            print("5. Keluar")
            choice = input("Pilih opsi (1-5): ")
            
            if choice == "1":
                if check_staging_file():
                    use_existing = input("File staged_data.csv sudah ada. Gunakan data ini? (y/n): ").strip().lower()
                    if use_existing == 'y':
                        self.df = load_staging_data()
                    else:
                        self.df = self.extractor.extract_data()
                else:
                    self.df = self.extractor.extract_data()
            elif choice == "2":
                if self.df is None:
                    self.df = load_staging_data()
                    if self.df is None:
                        continue
                self.df = self.transformer.calculate_trip_duration(self.df, 'lpep_pickup_datetime', 'lpep_dropoff_datetime')
                self.df.columns = [self.transformer.to_snake_case(col) for col in self.df.columns]
                self.df = self.transformer.map_payment_types(self.df, self.df_payment, 'payment_type', 'description')
                self.df = self.transformer.convert_distance_to_km(self.df, 'trip_distance')
            elif choice == "3":
                if self.df is not None:
                    self.loader.load_data(self.df)
                else:
                    print("Tidak ada data untuk disimpan.")
            elif choice == "4":
                if self.df is not None:
                    print(self.df.head())
                    print(self.df.info())
                else:
                    print("Tidak ada data untuk ditampilkan.")
            elif choice == "5":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    app = MainApp()
    app.run()
