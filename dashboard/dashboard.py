import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import time

import streamlit as st

df_all = pd.read_csv("dashboard/df_all.csv")

with st.sidebar:
    st.title('Selamat Datang di Project Streamlit Pertama Apau 😄')

    st.image("dashboard/Logo Streamlit.jpg")

    st.markdown("Documentasi Coding")
    st.page_link("https://github.com/alpaai18", label="Github", icon="🖥️")


# plot number of daily orders (2021)
st.header('Dashboard Kualitas Udara (AQI) :sparkles:', divider='gray')
with st.expander("Gambaran Umum Dashboard"):
    st.write('''
        Dalam dashboard ini tersedia informasi dari
        kualitas udara pada beberapa stasiun. Data
        yang digunakan berasal dari link 
        
        https://github.com/marceloreis/HTI/tree/master
             
        Juga penulis menggunakan indikator AQI yang penulis
        temukan dari internet. Berikut penjelasan ukuran
        AQI yang digunakan.
    ''')
    st.image("https://plutusias.com/wp-content/uploads/2023/10/Screenshot-2023-10-25-103447.png")

    st.write('''
        Akan tetapi untuk mempermudah pemahaman para pembaca
        penulis menggunakan 2 kriteria besar yakni **Baik untuk rentang 0 - 100**
        dan kriteria **Buruk untuk rentang lebih dari 100**
    ''')

df_PM_2016 = df_all[df_all['year'] == 2016]

bar_tampil = ['Ao', 'Cha', 'Ding', 'Dong', 'Guan', 'Guc', 'Hua', 'Nong', 'Shu', 'Tia', 'Wan','Wansho']

bar_PM25 = np.arange(len(bar_tampil))
bar_PM10 = np.arange(len(bar_tampil)) + 0.2
jarak_bar = 0.2

st.subheader("Gambaran Kondisi Kualitas Udara Pada Tahun Terbaru", divider='gray')

tab1, tab2 = st.tabs(["Polutan Partikel", "Polutan Asap"])

with tab1:
    fig, ax = plt.subplots(figsize=(30,15))

    ax.bar(bar_PM25, df_PM_2016['PM2.5_AQI'], jarak_bar, label='PM2.5')
    ax.bar(bar_PM10, df_PM_2016['PM10_AQI'], jarak_bar, label='PM10')
    ax.set_xticks(bar_PM25, bar_tampil)
    ax.set_xlabel('Masing - Masing Stasiun', fontsize=35)
    ax.set_ylabel('AQI', fontsize=35)
    ax.set_title('Tahun 2016', fontsize=45)
    ax.axhline(y=100, linestyle='--', label="Batas Aman Max", color='g')
    ax.legend(fontsize=35)

    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(figsize=(30,15))

    ax.bar(bar_PM25, df_PM_2016['SO2_AQI'], jarak_bar, label='SO2')
    ax.bar(bar_PM10, df_PM_2016['NO2_AQI'], jarak_bar, label='NO2')
    ax.bar(bar_PM10 + 0.2, df_PM_2016['CO_AQI'], jarak_bar, label='CO')
    ax.bar(bar_PM10 + 0.4, df_PM_2016['O3_AQI'], jarak_bar, label='O3')
    ax.set_xticks(bar_PM25, bar_tampil)
    ax.set_xlabel('Masing - Masing Stasiun', fontsize=35)
    ax.set_ylabel('AQI', fontsize=35)
    ax.set_title('Tahun 2016', fontsize=45)
    ax.axhline(y=100, linestyle='--', label="Batas Aman Max", color='g')
    ax.legend(fontsize=35)

    st.pyplot(fig)

with st.expander("Penjelasan Barchart"):
    st.write('''
        Pada Tab1 dilakukan pengecekan **polutan Partikel PM2.5 dan PM10**
        dimana terlihat bahwa pada tahun data terbaru, **Setiap Stasiun**
        - Stasiun Aothizhongxin             - Stasiun Changping 
        - Stasiun Dingling                  - Stasiun Dongsi
        - Stasiun Guanyuan                  - Stasiun Gucheng
        - Stasiun Huairou                   - Stasiun Nongzhanguan
        - Stasiun Shunyi                    - Staisun Tiantan
        - Stasiun Wanliu                    - Stasiun Wanshouxigong

        memiliki permasalahan serius pada polutan PM2.5, dimana polutan ini
        sangat berbahaya bagi pengidap penyakit pernapasan.

        Selanjutnya pada Tab2 penulis merancang pengecekan berdasarkan polutan
        yang berbentuk asap. Kabar baiknya berdasarkan data yang tertampil, di
        Tahun 2016 **Semua Stasiun Tidak Memiliki Permasalahan Pada Polutan Asap** 
    ''')

st.subheader("Ada Permasalahan Pada Polutan PM2.5, Apa yang Harus dilakukan?", divider='gray')
st.markdown("Melakukan Proses Pengecekan *Heatmap* Untuk Mengetahui Hubungan Indicator Alam dengan Polutan")


viz_df_all_heatmap = df_all[['PM2.5','TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']]

sns.set_theme()

fig, ax = plt.subplots(figsize=(15, 6))
sns.heatmap(viz_df_all_heatmap.corr(), annot=True, fmt=".2f", linewidths=.5, square=True)

st.pyplot(fig)
with st.expander("Penjelasan Heatmap"):
    st.write('''
        Berdasarkan visualisasi *Heatmap* yang tertampil,
        diketahui bahwa PM2.5 memiliki korelasi kepada 
        - WSPM (Kecepatan Angin) dengan korelasi -0.36
        - PRES (Tekanan Udara) dengan korelasi 0.46
             
        Dimana untuk korelasi negatif, semakin tinggi kecepatan angin
        pada suatu wilayah akan berdampak pada pengurangan kadar PM2.5
             
        Sebaliknya untuk korelasi positif, semakin tinggi tekanan udara
        pada suatu wilayah maka akan berdampak makin tinggi kadar PM2.5 
    ''')

st.subheader("Konklusi", divider='gray')

kesimpulan = """
Menurut sedikit pengetahuan yang penulis dapatkan, pemerintah bisa untuk
lebih berfokus kepada **Penanganan PM2.5 dengan memanfaatkan Korelasi PRES
atau Tekanan Udara**.

Hal ini bisa dilakukan dengan beberapa cara seperti Menggalakkan:
- **Proses Penghijauan Lahan**
- Mengganti **Energi Tak Terbarukan menjadi Energi Ramah Lingkungan**
- Proses **Pengurangan Limbah**
- dan lain sebagainya

Selain itu untuk para penduduk yang ada di sekitar sana, penulis dapat memberikan saran untuk

- **Selalu menggunakan masker saat beraktivitas** 

juga untuk para penderita penyakit pernapasan untuk 

- **Selalu membawa obat untuk keadaan darurat**

Sehingga kita tetap bisa menjalani hari dengan tetap memperhatikan kesehatan pernapasan
serta meminimalisir hal-hal yang tidak diinginkan.
"""

penutup="""
Terimakasih Banyak Karena Sudah Berkenan Untuk Mengunjungi Dashbaord Streamlit Saya.

Saya harap walau sangat minimalis tapi dashboard ini bisa memberikan manfaat walau hanya sedikit.
Juga saya sangat mengharapkan feedback dari para pengakses sekalian dengan dapat mengirimkan masukan ke

Instagram Penulis : @\_alpaai\_
"""

def kesimpulan_akhir():
    for kata in kesimpulan.split(" "):
        yield kata + " "
        time.sleep(0.05)


if st.button("Kesimpulan Akhir"):
    st.write_stream(kesimpulan_akhir)

def kalimat_penutup():
    for kata in penutup.split(" "):
        yield kata + " "
        time.sleep(0.05)

if st.button("Kalimat Penutup"):
    st.write_stream(kalimat_penutup)
