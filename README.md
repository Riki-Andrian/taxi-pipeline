# CAPSTONE PROJECT MODULE 1

### Riki Andrian Nugraha
### JCDEON 003

Struktur Folder
```
 taxi_pipeline/
 │-- data/
 │   │-- csv/      # Folder untuk menyimpan data CSV
 │   │-- json/     # Folder untuk menyimpan data JSON
 │-- result/       # Folder untuk menyimpan hasil transform
 │-- src/          # Folder untuk source code
 │-- staging/      # Folder untuk penyimpanan hasil ekstrak

```

Taxi Pipeline adalah program untuk mengekstrak dan transform data taksi dalam berbagai format, seperti CSV dan JSON.

## Panduan Penggunaan
1. Persyaratan
- Python 3.7 atau lebih baru
- pandas
- openpyxl (untuk menyimpan data dalam format Excel)

<br>

2. Cara Menjalankan Program
  - Pastikan Python dan dependensi telah terinstal.
  - Jalankan program dengan perintah berikut:
```
python main.py
```
<br>
3. Proses Ekstraksi
Proses ekstraksi bertanggung jawab untuk membaca data dari berbagai sumber dan menyimpannya ke area staging.

Fitur:
  - Mendukung input dalam format JSON dan CSV.
  - Menggunakan Pandas untuk membaca dan mengelola data.
  - Menampilkan log informasi mengenai data yang diekstrak.
  - Menyimpan hasil ekstraksi ke area staging untuk proses lebih lanjut.

Contoh Implementasi:
```
import pandas as pd
import glob
import os

def extract_data(folder_path):
    try:
        csv_files = glob.glob(os.path.join(folder_path, "csv/*.csv"))
        json_files = glob.glob(os.path.join(folder_path, "json/*.json"))

        if not csv_files and not json_files:
            print("Tidak ada file CSV atau JSON yang ditemukan.")
            return None

        df_list = []

        for file in csv_files:
            print(f"[INFO] Membaca file CSV: {file}")
            df = pd.read_csv(file)
            df_list.append(df)

        for file in json_files:
            print(f"[INFO] Membaca file JSON: {file}")
            df = pd.read_json(file)
            df_list.append(df)

        df_combined = pd.concat(df_list, ignore_index=True)

        os.makedirs("staging", exist_ok=True)
        staging_csv = "staging/staged_data.csv"

        df_combined.to_csv(staging_csv, index=False)

        print(f"[INFO] Data berhasil disimpan di {staging_csv}")

        return df_combined
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None
```
<br>
4. Proses Transformasi
Pada tahap transformasi, data diproses untuk memastikan kualitas dan konsistensi. Beberapa transformasi utama yang dilakukan:

Fitur:
  - Menambahkan kolom trip_duration berdasarkan lpep_pickup_datetime dan lpep_dropoff_datetime.
  - Normalisasi nama kolom menjadi format snake_case.
  - Mengubah nilai payment_type menjadi label yang lebih mudah dibaca.
  - Konversi trip_distance dari mil ke kilometer.
  - Menampilkan log setiap proses transformasi.

Contoh Implementasi:
```
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
```
<br>
5. Proses Load
Proses load bertanggung jawab untuk menyimpan hasil akhir ke format yang diinginkan.

Fitur:
  - Menyimpan data ke dalam format CSV atau Excel.
  - Data yang disimpan merupakan gabungan dari semua sumber data.

Contoh Implementasi:
```
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
```

