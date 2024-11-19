import streamlit as st
import requests
import zipfile
import io
import pandas as pd
import os
import gdown
import tempfile
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objs as go
import streamlit as st

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .nav-link {
        background-color: #FF4B4B !important; /* Warna background tombol */
        color: white !important; /* Warna teks */
        border-radius: 5px; /* Membuat sudut tombol melengkung */
        padding: 10px; /* Memberikan jarak dalam tombol */
        margin: 5px; /* Jarak antar tombol */
    }
    .nav-link:hover {
        background-color: #68041c !important; /* Warna saat tombol di-hover */
    }
    .nav-link.active {
        background-color: #FF0000 !important; /* Warna tombol aktif */
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style="background-color: #68041c; padding: 10px; border-radius: 5px; text-align: center;">
        <h2 style="color: white; margin: 0;">Dashboard-Leadtime</h2>
    </div>
    """,
    unsafe_allow_html=True
)
def download_file_from_github(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# Fungsi untuk mereset state button
def reset_button_state():
    st.session_state.button_clicked = False

def download_file_from_google_drive(file_id, dest_path):
    if not os.path.exists(dest_path):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, dest_path, quiet=False)

file_id = '1lHbP84SQEuehk1JMgidMT4gMXE2waa_f'
dest_path = f'downloaded_file.zip'
download_file_from_google_drive(file_id, dest_path)
        
if 'df_internal' not in locals():
  with zipfile.ZipFile(f'downloaded_file.zip', 'r') as z:
    with z.open('Leadtime_internal.csv') as f:
        df_internal = pd.read_csv(f)
    with z.open('Leadtime_eksternal.csv') as f:
        df_eksternal = pd.read_csv(f)


def create_pie_chart(df, labels_column, values_column, title="Pie Chart"):

    # Membuat grafik pie menggunakan Plotly
    fig = px.pie(
        df, 
        names=labels_column, 
        values=values_column, 
        title='',
        hole=0.3,  # Membuat grafik menjadi doughnut
        color_discrete_sequence=px.colors.sequential.RdBu  # Skema warna yang lebih estetis
    )
    
    # Kustomisasi tampilan
    fig.update_traces(
        textinfo='percent+label',  # Menampilkan label dan persentase
        textfont_size=12,  # Ukuran teks yang lebih besar
        pull=[0.1 if value == df[values_column].max() else 0 for value in df[values_column]]  # Memperbesar bagian terbesar
    )

    fig.update_layout(
        showlegend=True,  # Menampilkan legenda
        legend=dict(
            orientation="h",  # Menampilkan legenda secara horizontal
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        )
    )
    fig.update_layout(width=350, height=350)
    # Menampilkan grafik di Streamlit
    st.plotly_chart(fig)

def create_line_chart(df, x_column, y_column, title="Line Chart"):
    """
    Membuat grafik garis (line chart) dengan Plotly dan menampilkannya di Streamlit.
    
    Parameters:
    - df: DataFrame yang berisi data untuk grafik
    - x_column: Nama kolom yang ingin digunakan sebagai sumbu X
    - y_column: Nama kolom yang ingin digunakan sebagai sumbu Y
    - title: Judul grafik (default: "Line Chart")
    """
    # Membuat line chart menggunakan Plotly
    fig = px.line(df, x=x_column, y=y_column)
    color = px.colors.sequential.RdBu[0]
    # Kustomisasi tampilan
    fig.update_traces(
        line=dict(color=color, width=2.5),  # Warna garis biru dengan ketebalan 2.5
        mode='lines+markers'  # Menampilkan garis dan titik data
    )
    
    fig.update_layout(
        xaxis_title=x_column,
        yaxis_title=y_column
    )
    fig.update_layout(width=500, height=350)
    # Menampilkan grafik di Streamlit
    st.plotly_chart(fig)

def create_percentage_barchart(df, x_col, y_col):
    # Menghitung persentase berdasarkan y_col
    df['Percentage'] = (df[y_col] / df[y_col].sum()) * 100

    # Membuat bar chart menggunakan Plotly
    fig = px.bar(
        df,
        x=x_col,
        y='Percentage',
        labels={x_col: 'Kategori', 'Percentage': '%'},
        color_discrete_sequence=px.colors.sequential.RdBu,
        hover_data={y_col: True, 'Percentage': ':.2f%'}  # Menampilkan angka kuantitas dan persentase pada hover
    )
    
    # Menambahkan nilai persentase pada setiap bar
    fig.update_traces(
        texttemplate='%{y:.2f}%', 
        textposition='inside', 
        insidetextanchor='middle'
    )
    
    # Mengatur layout grafik
    fig.update_layout(
        width=350, 
        height=350
    )
    
    # Menampilkan grafik di Streamlit
    st.plotly_chart(fig)

list_bulan = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
        
bulan = st.selectbox("MONTH:", list_bulan, index=9, on_change=reset_button_state)
df_tanggal = pd.DataFrame(pd.date_range(start=f'{2024}-{int(pd.to_datetime(f'{bulan}-2024',format='%B-%Y').strftime('%m')):02d}-01', end=f'{2024}-{int(pd.to_datetime(f'{bulan}-2024',format='%B-%Y').strftime('%m')):02d}-28', freq='D'), columns=['Tanggal'])
bulan = bulan[:3]+'-24'
df_internal['Rute Global'] = pd.Categorical(df_internal['Rute Global'],['WH/DC to WH/DC','WH/DC to Resto','Resto to WH/DC','Resto to Resto'])
df_eksternal['Tanggal PO'] = pd.to_datetime(df_eksternal['Tanggal PO'])

import requests
from streamlit_option_menu import option_menu


# Membuat navigasi bar
option = option_menu(
    menu_title=None,  # required
    options=["Leadtime-Internal", "Leadtime-Eksternal"],  # required  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

# Fungsi untuk menjalankan file python yang diunduh
def run_stream_script(url):
    # Mengunduh file dari GitHub
    response = requests.get(url)
    if response.status_code == 200:
        # Menjalankan file yang diunduh
        exec(response.text, globals())
    else:
        st.error(f"Failed to download file: {response.status_code}")

# Arahkan ke aplikasi berdasarkan pilihan pengguna
if option == 'Leadtime-Internal':
    stream1_url = 'https://raw.githubusercontent.com/Analyst-FPnA/Leadtime/main/Internal.py'
    run_stream_script(stream1_url)
  
elif option == 'Leadtime-Eksternal':
    stream2_url = 'https://raw.githubusercontent.com/Analyst-FPnA/Leadtime/main/Eksternal.py'
    run_stream_script(stream2_url)
