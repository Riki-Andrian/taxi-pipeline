import pandas as pd
import glob
import os

# def extract_data(folder_path):
#     try:
#         csv_files = glob.glob(os.path.join(folder_path, "csv/*.csv"))
#         json_files = glob.glob(os.path.join(folder_path, "json/*.json"))

#         if not csv_files and not json_files:
#             print("Tidak ada file CSV atau JSON yang ditemukan.")
#             return None

#         df_list = []

#         for file in csv_files:
#             print(f"[INFO] Membaca file CSV: {file}")
#             df = pd.read_csv(file)
#             df_list.append(df)

#         for file in json_files:
#             print(f"[INFO] Membaca file JSON: {file}")
#             df = pd.read_json(file)
#             df_list.append(df)

#         df_combined = pd.concat(df_list, ignore_index=True)

#         os.makedirs("staging", exist_ok=True)
#         staging_csv = "staging/staged_data.csv"

#         df_combined.to_csv(staging_csv, index=False)

#         print(f"[INFO] Data berhasil disimpan di {staging_csv}")

#         return df_combined
    
#     except Exception as e:
#         print(f"Terjadi kesalahan: {e}")
#         return None


class Extractor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def extract_data(self):
        try:
            csv_files = glob.glob(os.path.join(self.folder_path, "csv/*.csv"))
            json_files = glob.glob(os.path.join(self.folder_path, "json/*.json"))

            if not csv_files and not json_files:
                print("Tidak ada file CSV atau JSON yang ditemukan.")
                return None

            df_list = []
            for file in csv_files:
                print(f"[INFO] Membaca file CSV: {file}")
                df_list.append(pd.read_csv(file))
            
            for file in json_files:
                print(f"[INFO] Membaca file JSON: {file}")
                df_list.append(pd.read_json(file))
            
            df_combined = pd.concat(df_list, ignore_index=True)
            os.makedirs("staging", exist_ok=True)
            df_combined.to_csv("staging/staged_data.csv", index=False)
            print("[INFO] Data berhasil disimpan di staging/staged_data.csv")
            return df_combined
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            return None