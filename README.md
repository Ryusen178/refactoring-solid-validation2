# Refactoring Struktur Kode Menggunakan Prinsip SOLID

## 📌 Deskripsi Proyek

Repository ini berisi implementasi **refactoring sistem validasi registrasi mahasiswa** dengan menerapkan prinsip **SOLID** pada Pemrograman Berorientasi Objek (PBO). Proyek ini bertujuan untuk memperbaiki struktur kode yang sebelumnya tidak terstruktur dengan baik, sulit dikembangkan, dan melanggar prinsip desain berorientasi objek.

Proyek ini dikerjakan untuk memenuhi **Tugas Praktikum PBO – Refactoring Struktur Kode Menggunakan Prinsip SOLID**.

---

## 🎯 Tujuan

* Memahami dan menerapkan prinsip **SOLID**
* Menghilangkan *code smell* akibat penggunaan `if/else` berlebihan
* Meningkatkan **maintainability** dan **scalability** kode
* Menerapkan dokumentasi kode menggunakan **Google Style Docstring**
* Menggunakan **logging** sebagai pengganti `print()`
* Mengelola proyek menggunakan **Git & GitHub**

---

## 🧩 Prinsip SOLID yang Diterapkan

### 1️⃣ Single Responsibility Principle (SRP)

Setiap class memiliki satu tanggung jawab. Aturan validasi dipisahkan ke dalam class masing-masing.

### 2️⃣ Open/Closed Principle (OCP)

Sistem dapat dikembangkan dengan menambahkan aturan validasi baru tanpa mengubah kode yang sudah ada.

### 3️⃣ Dependency Inversion Principle (DIP)

Class utama bergantung pada **abstraksi (interface)**, bukan pada implementasi konkret.

---

## 📁 Struktur Folder

```
refactoring-solid-validation/
│
├── before/
│   └── validator_manager.py
│
├── after/
│   ├── validation_rule.py
│   ├── registration_validator.py
│   ├── ipk_validator.py
│   ├── sks_validator.py
│   ├── semester_validator.py
│   └── prasyarat_validator.py
│
└── README.md
```

---

## 🔍 Analisis Kode Sebelum Refactoring (before)

Kode sebelum refactoring memiliki beberapa permasalahan:

* Satu class menangani seluruh logika validasi
* Sulit dikembangkan jika ada aturan baru
* Ketergantungan langsung pada implementasi
* Tidak menggunakan logging
* Tidak memiliki dokumentasi kode

---

## ✅ Implementasi Setelah Refactoring (after)

### ✔ Pemisahan Class Validasi

Setiap aturan validasi dibuat dalam class terpisah:

* `IPKValidator`
* `SKSValidator`
* `SemesterValidator`
* `PrasyaratValidator`

### ✔ Interface Abstraksi

Semua validator mengimplementasikan interface:

* `IValidationRule`

### ✔ Central Validator

* `RegistrationValidator` bertugas menjalankan seluruh aturan validasi

---

## 📝 Dokumentasi (Docstring)

Seluruh class dan method telah dilengkapi **Google Style Docstring** untuk memudahkan pemahaman kode dan kolaborasi.

Contoh:

```python
class IValidationRule:
    """
    Interface untuk semua aturan validasi registrasi mahasiswa.
    """
```

---

## 📊 Logging

Program menggunakan modul `logging`:

* `INFO` → proses validasi berhasil
* `WARNING` → validasi gagal

Keuntungan logging:

* Mudah melakukan debugging
* Tidak mencampur output dengan log sistem
* Lebih profesional dibanding `print()`

---

## ▶️ Cara Menjalankan Program

### 1. Pastikan Python Terinstall

```bash
python --version
```

### 2. Clone Repository

```bash
git clone https://github.com/Ryusen178/refactoring-solid-validation2.git
```

### 3. Masuk ke Folder Proyek

```bash
cd refactoring-solid-validation2
```

### 4. Jalankan Program

```bash
python after/registration_validator.py
```

---

## 🗂 Version Control (Git)

Repository ini menggunakan Git dengan beberapa commit terpisah:

* Initial commit (struktur awal)
* Penambahan refactoring SOLID
* Penambahan `.gitignore`
* Penambahan docstring dan logging

---

## 📌 Kesimpulan

Dengan menerapkan prinsip SOLID, kode menjadi:

* Lebih terstruktur
* Mudah dikembangkan
* Mudah dipelihara
* Lebih profesional

Refactoring ini membuktikan bahwa desain kode yang baik sangat penting dalam pengembangan perangkat lunak jangka panjang.

---

## 👨‍🎓 Author

Nama: Saifullah Yusuf
Mata Kuliah: Praktikum Pemrograman Berorientasi Objek
