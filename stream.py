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

def download_file_from_github(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

st.title('Dashboard - Leadtime')

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
    
    # Membuat bar chart menggunakan Plotly
    fig = px.bar(df, 
                 x=x_col, 
                 y=y_col, 
                 labels={x_col: 'Department', y_col: 'Total Trx'},
                 color_discrete_sequence=px.colors.sequential.RdBu)
    
    # Menambahkan nilai persentase pada setiap bar
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='inside', insidetextanchor='middle')
    fig.update_layout(width=350, height=350)
    # Menampilkan grafik
    st.plotly_chart(fig)

list_bulan = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
        
bulan = st.selectbox("MONTH:", list_bulan, index=9, on_change=reset_button_state)
pic = st.selectbox("PIC RESPONSIBLE:", ['All','WH/DC','Resto'], index=0, on_change=reset_button_state)
bulan = bulan[:3]+'-24'
df_internal['Rute Global'] = pd.Categorical(df_internal['Rute Global'],['WH/DC to WH/DC','WH/DC to Resto','Resto to WH/DC','Resto to Resto'])


col = st.columns([1,2,1,2])
with col[0]:
    df_pie = df_internal[(df_internal['Bulan Kirim']==bulan) & (df_internal['Kirim #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))].groupby(['Kategori Leadtime SJ'])[['Nomor IT Kirim']].nunique().reset_index()
    
    create_pie_chart(df_pie, labels_column='Kategori Leadtime SJ', values_column='Nomor IT Kirim', title="OUTGOING BACKDATE")
with col[1]:
    df_line = df_internal[(df_internal['Bulan Kirim']==bulan) & (df_internal['Kirim #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
                 & (df_internal['Kategori Leadtime SJ']=='Backdate')].groupby(['Tanggal IT Kirim'])[['Nomor IT Kirim']].nunique().reset_index()
    
    create_line_chart(df_line, x_column='Tanggal IT Kirim', y_column='Nomor IT Kirim', title="DAILY BACKDATE")
with col[2]:
    df_bar = df_internal[(df_internal['Bulan Kirim']==bulan) & (df_internal['Kirim #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
             & (df_internal['Kategori Leadtime SJ']=='Backdate')].groupby(['Terima #2'])[['Nomor IT Kirim']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Terima #2', 'Nomor IT Kirim')
with col[3]:
    col2 = st.columns(2)
    with col2[0]:
        st.metric(label="Total", value="{:,.0f}".format(df_internal[(df_internal['Bulan Terima']==bulan) & (df_internal['Terima #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))]['Nomor IT Terima'].nunique()), delta=None)
    with col2[1]:
        st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori Leadtime SJ']=='On-Time']['Nomor IT Kirim'].values), delta=None)
    with col2[1]:
        st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori Leadtime SJ']=='Backdate']['Nomor IT Kirim'].values), delta=None)
        
    st.dataframe(df_internal[(df_internal['Bulan Kirim']==bulan) & (df_internal['Kirim #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
             & (df_internal['Kategori Leadtime SJ']=='Backdate')].groupby(['Leadtime SJ Group','Rute Global'])[['Nomor IT Kirim']].nunique().reset_index().pivot(index='Rute Global',columns='Leadtime SJ Group',values='Nomor IT Kirim').reset_index(),
                 hide_index=True
    )


col = st.columns([1,2,1,2])
with col[0]:
    df_pie = df_internal[(df_internal['Bulan Terima']==bulan) & (df_internal['Terima #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))].groupby(['Kategori Leadtime RI'])[['Nomor IT Terima']].nunique().reset_index()
    
    create_pie_chart(df_pie, labels_column='Kategori Leadtime RI', values_column='Nomor IT Terima', title="OUTGOING BACKDATE")
with col[1]:
    df_line = df_internal[(df_internal['Bulan Terima']==bulan) & (df_internal['Terima #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
                 & (df_internal['Kategori Leadtime RI']=='Backdate')].groupby(['Tanggal IT Terima'])[['Nomor IT Terima']].nunique().reset_index()
    
    create_line_chart(df_line, x_column='Tanggal IT Terima', y_column='Nomor IT Terima', title="DAILY BACKDATE")
with col[2]:
    df_bar = df_internal[(df_internal['Bulan Terima']==bulan) & (df_internal['Terima #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
             & (df_internal['Kategori Leadtime RI']=='Backdate')].groupby(['Kirim #2'])[['Nomor IT Terima']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Kirim #2', 'Nomor IT Terima')
with col[3]:
    st.dataframe(df_internal[(df_internal['Bulan Terima']==bulan) & (df_internal['Terima #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
             & (df_internal['Kategori Leadtime RI']=='Backdate')].groupby(['Leadtime RI Group','Rute Global'])[['Nomor IT Terima']].nunique().reset_index().pivot(index='Rute Global',columns='Leadtime RI Group',values='Nomor IT Terima').reset_index(),
                 hide_index=True
    )


