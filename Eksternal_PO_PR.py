st.markdown('#### PO(Datang)-PR(Create)')
st.write('PIC Responsible: Logistic')
st.write('Kategori Item: Eksternal Logistic')
col = st.columns([1,2,1])

with col[0]:
    df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
    create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
with col[1]:
    df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')
             ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
    df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
    create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
with col[2]:
    df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    

st.write('Kategori Item: Internal Logistic')
col = st.columns([1,2,1])

with col[0]:
    df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
    create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
with col[1]:
    df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')
             ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
    df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
    create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
with col[2]:
    df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')

st.write('Kategori Item: Resto')
col = st.columns([1,2,1])

with col[0]:
    df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Resto') 
             ].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
    create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
with col[1]:
    df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Resto') 
             & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')
             ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
    df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
    create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
with col[2]:
    df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Resto') 
             & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')

