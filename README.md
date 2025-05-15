---

# Dokumentasi Proyek Deploy Model Anomaly Detection dengan Docker

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

* Melakukan tes endpoint "predict/" seperti gambar dibawah ini

  ![Screenshot 2025-05-15 140611 - Copy](https://github.com/user-attachments/assets/ceb9755b-9623-42c7-8d90-54d1e0870a5d)


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
