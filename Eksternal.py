st.markdown(
    """
    <div style="background-color: #68041c; padding: 10px; border-radius: 5px; text-align: center;">
        <h3 style="color: white; margin: 0;">Leadtime-Eksternal</h3>
    </div>
    """,
    unsafe_allow_html=True
)
st.write('')

kat_eksternal = st.selectbox("KATEGORI BACKDATE:", ['PO(Datang)-PR(Create)','PO(Datang)-PO(Create)','PO(Datang)-RI(Create)'], index=0, on_change=reset_button_state)

if kat_eksternal =='PO(Datang)-PR(Create)':
    st.markdown('### PO(Datang)-PR(Create)')
    st.write('PIC Responsible: Logistic')
    st.write('Kategori Item: Eksternal Logistic')
    col = st.columns([1,2,1,1])
    
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
    with col[3]:
        st.dataframe(df_eksternal[(df_eksternal['Bulan PO']==bulan) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute','PO(Datang)-PR(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PR(Create) Group',values='Nomor PO').reset_index()
        )
    
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

if kat_eksternal =='PO(Datang)-PO(Create)':
    st.markdown('### Kategori PO(Datang)-PO(Create)')
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

if kat_eksternal =='PO(Datang)-RI(Create)':
    st.markdown('### Kategori PO(Datang)-RI(Create)')
    st.write('PIC Responsible: Resto')
    st.write('Kategori Item: Eksternal Logistic')
    col = st.columns([1,2,1])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan)
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan)
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
        
    st.write('Kategori Item: Eksternal Resto')
    col = st.columns([1,2,1])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) 
                 & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan)
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan)
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    
    st.write('PIC Responsible: WH/CK')
    st.write('Kategori Item: Internal Logistic')
    col = st.columns([1,2,1])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal['Bulan PO']==bulan) 
                 & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal['Bulan PO']==bulan)
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal['Bulan PO']==bulan)
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
