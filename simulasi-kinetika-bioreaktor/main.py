import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 1. Definisi Parameter Kinetik Skala Jaringan Eksperimental
V1_max = 5.0   # Plafon kecepatan sintesis lintasan komitmen V1
Km1 = 2.0      # Setengah-afinitas saturasi katalitik (Konstanta Michaelis)
Ki = 3.0       # Afinitas pengikatan represi alosterik (Konstanta Inhibisi)
X = 10.0       # Level ketersediaan pasokan substrat bioreaktor (konstan)
k2 = 1.0       # Proporsi kecepatan massa spesifik kompartemen A -> B
k3 = 0.8       # Proporsi kecepatan massa spesifik fungsional B -> P
k4 = 0.3       # Proporsi pendarahan pelarian enzimatik A -> Byproduct

def model_sistem_jaringan_alosterik(y, t):
    # Mengekstraksi vektor status spasial sesaat per kompartemen
    A, B, P = y
    
    # Kalkulasi Regulasi Hambatan Michaelis-Menten Modifikasi secara Real-time
    multiplier_inhibitor = 1.0 + (P / Ki)
    v1_kinetika_termodulasi = (V1_max * X) / ((Km1 + X) * multiplier_inhibitor)
    
    # Pengenaan Perhitungan Persamaan Murni Difusi Orde-Satu
    v2_fluks_aktif = k2 * A
    v3_fluks_konversi = k3 * B
    v4_buangan_parasit = k4 * A
    
    # Penerjemahan Sistem Diferensial (dx/dt) dari Evaluasi Matriks Stoikiometri Baseline
    dA_dt = v1_kinetika_termodulasi - v2_fluks_aktif - v4_buangan_parasit
    dB_dt = v2_fluks_aktif - v3_fluks_konversi
    dP_dt = v3_fluks_konversi
    
    return [dA_dt, dB_dt, dP_dt]

# 2. Pendefinisian Kondisi Awal (Initial Value Boundaries)
vektor_konsentrasi_inisial = [0.0, 0.0, 0.0]  # Keadaan awal tangki steril

# 3. Diskreti Vektor Grid Parameter Ruang Waktu (Siklus 48 Jam)
interval_jam_bioreaktor = np.linspace(0, 48, 1000)

# 4. Inisiasi Penyelesaian Integrasi Komputasi Lanjut via ODE Solver
arsip_simulasi = odeint(model_sistem_jaringan_alosterik, vektor_konsentrasi_inisial, interval_jam_bioreaktor)

# Pemisahan Matriks Hasil Integrasi Multi-kolom menjadi Kurva Temporal Individual
trajektori_A = arsip_simulasi[:, 0]
trajektori_B = arsip_simulasi[:, 1]
trajektori_P = arsip_simulasi[:, 2]

# 5. Konstruksi Presentasi Visual Kurva
plt.figure(figsize=(11, 7))
plt.plot(interval_jam_bioreaktor, trajektori_A, label='Pool Metabolit A (Intermediet Awal)', color='blue', linewidth=2.5)
plt.plot(interval_jam_bioreaktor, trajektori_B, label='Pool Metabolit B (Toksik Peringatan)', color='red', linestyle='--', linewidth=2.5)
plt.plot(interval_jam_bioreaktor, trajektori_P, label='Level Akumulasi Target Biosintesis (P)', color='green', linewidth=3)

plt.title("Analisis Trajektori Dinamika Kinetik Modifikasi Genetik Bioreaktor (Siklus 48 Jam)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Rentang Waktu Fermentasi Kontinu (Jam)", fontsize=12)
plt.ylabel("Tingkat Konsentrasi Internal Sitoplasma Sel (mmol/L)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.75)
plt.legend(loc='best', fontsize=11)
plt.tight_layout()
plt.show()