# Simulasi Trajektori Dinamika Kinetik Bioreaktor 🧬

Repositori ini berisi skrip Python untuk memodelkan dan mensimulasikan sistem jaringan alosterik pada bioreaktor berskala jaringan eksperimental dalam siklus fermentasi kontinu selama 48 jam.

Proyek ini memanfaatkan penyelesaian persamaan diferensial biasa (ODE) untuk melacak perubahan konsentrasi metabolit intermediet, akumulasi target biosintesis, dan produk sampingan (byproduct) secara real-time.

## 📌 Fitur Utama
* **Regulasi Alosterik Modifikasi**: Menggunakan modifikasi persamaan Michaelis-Menten yang terhambat oleh akumulasi produk (Inhibisi Alosterik).
* **Komputasi Numerik Tingkat Lanjut**: Mengintegrasikan sistem diferensial multi-kompartemen menggunakan fungsi `odeint` dari pustaka `SciPy`.
* **Visualisasi Kurva Temporal**: Menyajikan grafik trajektori interaktif untuk analisis tren akumulasi zat kimia dalam sitoplasma sel.

## 📊 Pemodelan Sistem
Sistem ini memodelkan perubahan tiga variabel utama seiring waktu ($t$):
1. **Pool Metabolit A ($A$)** - Intermediet Awal
2. **Pool Metabolit B ($B$)** - Toksik Peringatan
3. **Level Akumulasi Target Biosintesis ($P$)**

Fluks kinetika sintesis ($v_1$) dihambat secara alosterik oleh produk $P$ melalui faktor pengali konstanta inhibisi ($K_i$).

## 🚀 Cara Menjalankan Proyek

### 1. Prasyarat
Pastikan Anda sudah menginstal Python (versi 3.8 ke atas direkomendasikan) di perangkat Anda.

### 2. Kloning Repositori
Kloning proyek ini ke komputer lokal Anda menggunakan perintah:
```bash
git clone [https://github.com/USERNAME_ANDA/simulasi-kinetika-bioreaktor.git](https://github.com/USERNAME_ANDA/simulasi-kinetika-bioreaktor.git)
cd simulasi-kinetika-bioreaktor
