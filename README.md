---

# 🧪 Dokumentasi Proyek Deploy Model Anomaly Detection dengan Docker

## 1. Overview

Proyek ini bertujuan membangun model Machine Learning untuk deteksi anomali, mengemasnya dalam container Docker, dan melakukan deployment pada Virtual Machine (VM) di server untuk digunakan sebagai API.

---

## 2. Langkah-Langkah yang Telah Dilakukan

### a. Pembuatan dan Pelatihan Model

* Membuat model deteksi anomali menggunakan dataset tertentu (detail model dan dataset bisa dijelaskan lebih lanjut jika ada).
* Melakukan pelatihan dan validasi model di JupyterLab.

### b. Membuat API untuk Model

* Membuat REST API menggunakan framework Python (misal Flask atau FastAPI) untuk menerima request dan memberikan prediksi anomali berdasarkan model yang sudah dibuat.
* Menyiapkan file `app.py` (atau file lain) untuk menjalankan server API.

### c. Membuat Dockerfile

* Membuat `Dockerfile` untuk mengemas aplikasi dan model ke dalam container Docker.
* Mengatur image base, install dependencies, copy source code, dan perintah menjalankan server menggunakan Gunicorn.

### d. Build Docker Image

* Menjalankan perintah:

  ```
  docker build -t anomaly-api .
  ```

  untuk membuat image Docker dari Dockerfile.

### e. Run Docker Container di VM

* Menjalankan container dengan mapping port 5000 (port API di container) ke port 8080 di host VM:

  ```
  docker run -d -p 8080:5000 --name anomaly-api-container anomaly-api
  ```
* Memastikan container berjalan dengan:

  ```
  docker ps
  ```
* Mengecek logs container dengan:

  ```
  docker logs anomaly-api-container
  ```
* Melakukan testing API lokal di VM menggunakan `curl` dengan perintah:

  ```
  curl http://localhost:8080
  ```

  dan mendapat respons `Anomaly Detection API is running!` seperti gambar dibawah ini.

  ![Screenshot 2025-05-15 140611](https://github.com/user-attachments/assets/7c651469-105c-4f86-aa2a-de0298a3c6c8)

* Melakukan tes endpoint "predict/"

  - Gunakan perintah curl berikut untuk menguji endpoint prediksi:

  ```
  curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '[{
    "Time": 100, "V1": 0.1, "V2": 0.2, "V3": 0.3, "V4": 0.4, "V5": 0.5,
    "V6": 0.6, "V7": 0.7, "V8": 0.8, "V9": 0.9, "V10": 1.0, "V11": 1.1,
    "V12": 1.2, "V13": 1.3, "V14": 1.4, "V15": 1.5, "V16": 1.6, "V17": 1.7,
    "V18": 1.8, "V19": 1.9, "V20": 2.0, "V21": 2.1, "V22": 2.2, "V23": 2.3,
    "V24": 2.4, "V25": 2.5, "V26": 2.6, "V27": 2.7, "V28": 2.8,
    "Amount": 1000
  }]'

  ```
  - Hasil

    ```
    {"prediction": [0]}
    ```

  ![Screenshot 2025-05-15 140611 - Copy](https://github.com/user-attachments/assets/ceb9755b-9623-42c7-8d90-54d1e0870a5d)

  Keterangan:

  Nilai 0 berarti data dianggap normal.
  
  Nilai 1 berarti data dianggap anomaly


### f. Testing Akses API dari Browser

* Port 8080 sudah di-mapping, sehingga API bisa diakses dari browser dengan alamat:

  ```
  http://<IP_VM>:8080
  ```

  (pastikan port 8080 di firewall VM sudah dibuka)

---

## 3. Kesimpulan

* Model anomaly detection berhasil dibuat dan dibungkus dalam Docker container.
* Docker container berhasil dijalankan di VM dan API sudah dapat diakses lokal maupun dari browser (jika port sudah dibuka).
* Deploy berjalan tanpa harus menggunakan Google Cloud Registry atau layanan cloud lain, cukup menggunakan VM yang sudah disediakan.

---
