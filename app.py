import streamlit as st
import numpy as np

# Fungsi untuk Trapezoidal Rule
def trapezoidal_rule(func, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = func(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral, x, y

# Meta Halaman
st.set_page_config(
    page_title="Trapezoidal Rule Dengan Streamlit", 
    page_icon=":bar_chart:",  
)

# Halaman utama aplikasi
st.write("Muh. Afiq Ma'mun | 22.11.5163")
st.title("Metode Numerik: Trapezoidal Rule")
st.write("Aplikasi ini digunakan untuk menghitung integral tentu dari sebuah fungsi menggunakan metode trapezoidal rule.")

# Input fungsi
func_input = st.text_input("Masukkan fungsi f(x):", value="np.sin(x)")

# Input batas integral dan jumlah partisi
col1, col2, col3 = st.columns(3)
a = col1.number_input("Batas bawah (a):", value=0.0, format="%.2f")
b = col2.number_input("Batas atas (b):", value=np.pi, format="%.2f")
n = col3.number_input("Jumlah partisi (n):", value=10, min_value=1, step=1, format="%d")

# Evaluasi fungsi input
try:
    func = lambda x: eval(func_input)
    y_test = func(np.array([a, b]))  # Test fungsi untuk memastikan validitas
except Exception as e:
    st.error(f"Error pada fungsi: {e}")
    st.stop()

# Hitung integral dengan Trapezoidal Rule
integral, x, y = trapezoidal_rule(func, a, b, n)

# Output hasil integral
st.write(f"Hasil integral: {integral:.4f}")

# Buat data untuk visualisasi
x_plot = np.linspace(a, b, 1000)
y_plot = func(x_plot)

# Data untuk plot garis fungsi
# st.line_chart({"x": x_plot, "f(x)": y_plot}, use_container_width=True)

# Data untuk plot area trapezoid
area_data = []
for i in range(n):
    area_data.append({"x": x[i], "y": y[i]})
    area_data.append({"x": x[i+1], "y": y[i+1]})
    area_data.append({"x": x[i+1], "y": 0})
    area_data.append({"x": x[i], "y": 0})
    area_data.append({"x": x[i], "y": y[i]})

# Ubah menjadi format DataFrame
import pandas as pd

area_df = pd.DataFrame(area_data)

# Plot area trapezoid
st.area_chart(area_df.set_index("x"), use_container_width=True)
