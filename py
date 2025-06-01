from scipy.stats import norm

# Berat X ~ N(500, 20)
# Panjang Y ~ N(100, 5)

# Peluang berat antara 490g dan 510g
p_berat = norm.cdf(510, loc=500, scale=20) - norm.cdf(490, loc=500, scale=20)

# Peluang panjang Lebih dari 102cm
p_panjang = 1 - norm.cdf(102, loc=100, scale=5)

# Peluang lolos inspeksi
p_lolos = p_berat * p_panjang

# Ekspektasi jumlah produk yang lolos dari 200 unit
ekspektasi_lolos = 200 * p_lolos

print("Peluang lolos inspeksi:", round(p_lolos, 4))
print("Ekspektasi produk lolos (200 unit):", round(ekspektasi_lolos, 2))
