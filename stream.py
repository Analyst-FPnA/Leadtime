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
    <div style="background-color: #68041c; padding: 10px; border-radius: 5px; text-align: center;">
        <h2 style="color: white; margin: 0;">Dashboard-Leadtime</h2>
    </div>
    """,
    unsafe_allow_html=True
)
st.write(' ')

data = {
    "Tanggal": pd.date_range(start="2024-01-01", end="2024-12-31", freq="D"),
    "Penjualan": range(1, 367)
}
df = pd.DataFrame(data)


# Widget untuk memilih rentang tanggal
start_date, end_date = st.date_input(
    "RANGE DATE ",
    [df["Tanggal"].min(), df["Tanggal"].max()],  # Default nilai awal
    min_value=df["Tanggal"].min(),
    max_value=df["Tanggal"].max()
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


def create_pie_chart(df, labels_column, values_column, title="Pie Chart", key=None):
    color_mapping = {
        'On-Time': px.colors.sequential.RdBu[1],  
        'Backdate': px.colors.sequential.RdBu[0] 
    }
    fig = px.pie(
        df, 
        names=labels_column, 
        values=values_column, 
        title='',
        hole=0.3,
        color=labels_column,
        color_discrete_map=color_mapping  # Skema warna yang lebih estetis
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
        
df_tanggal = pd.DataFrame(pd.date_range(start=pd.Timestamp(start_date), end=pd.Timestamp(end_date), freq='D'), columns=['Tanggal'])
df_internal['Rute Global'] = pd.Categorical(df_internal['Rute Global'],['WH/DC to WH/DC','WH/DC to Resto','Resto to WH/DC','Resto to Resto'])
df_eksternal['Tanggal PO'] = pd.to_datetime(df_eksternal['Tanggal PO'])
df_internal['Tanggal IT Kirim'] = pd.to_datetime(df_internal['Tanggal IT Kirim'])
df_internal['Tanggal IT Terima'] = pd.to_datetime(df_internal['Tanggal IT Terima'])



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
