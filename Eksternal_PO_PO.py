st.markdown('#### Kategori PO(Datang)-PO(Create)')
st.write('PIC Responsible: Procurement')
st.write('Kategori Item: Logistic')
col = st.columns([1,2,1])

with col[0]:
    df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             ].groupby(['Kategori PO(Datang)-PO(Create)'])[['Nomor PO']].nunique().reset_index()
    create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PO(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
with col[1]:
    df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')
             ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
    df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
    create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
with col[2]:
    df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
             & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')



st.write('Kategori Item: Resto')
col = st.columns([1,2,1])

with col[0]:
    df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Resto') 
             & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Kategori PO(Datang)-PO(Create)'])[['Nomor PO']].nunique().reset_index()
    create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PO(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
with col[1]:
    df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Resto') 
             & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')
             ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
    df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
    create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
with col[2]:
    df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Resto') 
             & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')

