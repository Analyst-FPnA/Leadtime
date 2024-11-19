st.markdown('### Leadtime-Internal')
pic = st.selectbox("PIC RESPONSIBLE:", ['All','WH/DC','Resto'], index=0, on_change=reset_button_state)

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
             & (df_internal['Kategori Leadtime SJ']=='Backdate')].groupby(['Kirim #2'])[['Nomor IT Kirim']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Kirim #2', 'Nomor IT Kirim')
with col[3]:
    st.write('')
    col2 = st.columns(3)
    with col2[0]:
        st.metric(label="Total", value="{:,.0f}".format(df_internal[(df_internal['Bulan Kirim']==bulan) & (df_internal['Kirim #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))]['Nomor IT Kirim'].nunique()), delta=None)
    with col2[1]:
        st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori Leadtime SJ']=='On-Time']['Nomor IT Kirim'].values[0]), delta=None)
    with col2[2]:
        st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori Leadtime SJ']=='Backdate']['Nomor IT Kirim'].values[0]), delta=None)
    
    df_tabel = df_internal[(df_internal['Bulan Kirim']==bulan) & (df_internal['Kirim #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
             & (df_internal['Kategori Leadtime SJ']=='Backdate')].groupby(['Leadtime SJ Group','Rute Global'])[['Nomor IT Kirim']].nunique().reset_index().pivot(index='Rute Global',columns='Leadtime SJ Group',values='Nomor IT Kirim').reset_index()
    if pic =='Resto':
        st.dataframe(df_tabel.loc[df_tabel['Rute Global'].isin(['Resto to WH/DC','Resto to Resto'])],hide_index=True)
    else:
        st.dataframe(df_tabel.loc[df_tabel['Rute Global'].isin(['WH/DC to WH/DC','WH/DC to Resto'])],hide_index=True)

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
             & (df_internal['Kategori Leadtime RI']=='Backdate')].groupby(['Terima #2'])[['Nomor IT Terima']].nunique().reset_index()
    create_percentage_barchart(df_bar, 'Terima #2', 'Nomor IT Terima')
with col[3]:
    st.write('')
    col2 = st.columns(3)
    with col2[0]:
        st.metric(label="Total", value="{:,.0f}".format(df_internal[(df_internal['Bulan Terima']==bulan) & (df_internal['Terima #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))]['Nomor IT Terima'].nunique()), delta=None)
    with col2[1]:
        st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori Leadtime RI']=='On-Time']['Nomor IT Terima'].values[0]), delta=None)
    with col2[2]:
        st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori Leadtime RI']=='Backdate']['Nomor IT Terima'].values[0]), delta=None)

    df_tabel = df_internal[(df_internal['Bulan Terima']==bulan) & (df_internal['Terima #2'].isin(['Resto','WH/DC'] if pic=='All' else [pic]))
             & (df_internal['Kategori Leadtime RI']=='Backdate')].groupby(['Leadtime RI Group','Rute Global'])[['Nomor IT Terima']].nunique().reset_index().pivot(index='Rute Global',columns='Leadtime RI Group',values='Nomor IT Terima').reset_index()
    if pic=='Resto':
        st.dataframe(df_tabel.loc[df_tabel['Rute Global'].isin(['WH/DC to Resto','Resto to Resto'])],hide_index=True)
    else:
        st.dataframe(df_tabel.loc[df_tabel['Rute Global'].isin(['Resto to WH/DC','WH/DC to WH/DC'])],hide_index=True)
