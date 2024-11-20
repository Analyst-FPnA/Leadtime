st.markdown(
    """
    <div style="background-color: #68041c; padding: 10px; border-radius: 5px; text-align: center;">
        <h3 style="color: white; margin: 0;">Leadtime-Eksternal</h3>
    </div>
    """,
    unsafe_allow_html=True
)
st.write('')
kat_eksternal = st.selectbox("KATEGORI BACKDATE:", ['PR(Create)-PO(Datang)','PO(Datang)-PO(Create)','PO(Datang)-RI(Create)'], index=0, on_change=reset_button_state)

if kat_eksternal =='PR(Create)-PO(Datang)':
    st.markdown('### PR(Create)-PO(Datang)')
    st.write('PIC Responsible: Logistic')
    st.write('Kategori Item: Eksternal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')
                 ].groupby(['Date PO'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'}).merge(df_eksternal[(df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')
                 ].groupby(['Date PO'])[['Nomor PO']].nunique().reset_index(), how='left')
        df_line['Nomor PO'] = (df_line['Nomor PO']/df_line['Total'])*100
        create_line_chart(df_line, x_column='Date PO', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute','PO(Datang)-PR(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PR(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
    
    st.write('Kategori Item: Internal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Internal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute','PO(Datang)-PR(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PR(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
        
    st.write('Kategori Item: Resto')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') 
                 ].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') ]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')].groupby(['Rute','PO(Datang)-PR(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PR(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)

if kat_eksternal =='PO(Datang)-PO(Create)':
    st.markdown('### Kategori PO(Datang)-PO(Create)')
    st.write('PIC Responsible: Procurement')
    st.write('Kategori Item: Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 ].groupby(['Kategori PO(Datang)-PO(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PO(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                ]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute','PO(Datang)-PO(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PO(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
        
    st.write('Kategori Item: Resto')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal['PIC Responsible']=='Resto') &
                 (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Kategori PO(Datang)-PO(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PO(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') 
                ]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute','PO(Datang)-PO(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PO(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ (df_eksternal['PIC Responsible']=='Resto') &
                 (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)

if kat_eksternal =='PO(Datang)-RI(Create)':
    st.markdown('### Kategori PO(Datang)-RI(Create)')
    st.write('PIC Responsible: Resto')
    st.write('Kategori Item: Eksternal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[ 
                 (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') &
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute','PO(Datang)-RI(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-RI(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ (df_eksternal['PIC Responsible']=='Logistic') &
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
        
    st.write('Kategori Item: Eksternal Resto')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[ 
                  (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[  
                 (df_eksternal['Kategori Item']=='Eksternal Resto')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute','PO(Datang)-RI(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-RI(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ 
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
    
    st.write('PIC Responsible: WH/CK')
    st.write('Kategori Item: Internal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[ 
                 (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[  
                 (df_eksternal['Kategori Item']=='Internal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute','PO(Datang)-RI(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-RI(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[ 
                 (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)

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

df_tanggal = pd.DataFrame(pd.date_range(start=pd.Timestamp(start_date), end=pd.Timestamp(end_date), freq='D'), columns=['Tanggal'])

if kat_eksternal =='PR(Create)-PO(Datang)':
    st.markdown('### PR(Create)-PO(Datang)')
    st.write('PIC Responsible: Logistic')
    st.write('Kategori Item: Eksternal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute','PO(Datang)-PR(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PR(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
    
    st.write('Kategori Item: Internal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Internal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute','PO(Datang)-PR(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PR(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
        
    st.write('Kategori Item: Resto')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 ].groupby(['Kategori PO(Datang)-PR(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PR(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') ]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PR(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')].groupby(['Rute','PO(Datang)-PR(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PR(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PR(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)

if kat_eksternal =='PO(Datang)-PO(Create)':
    st.markdown('### Kategori PO(Datang)-PO(Create)')
    st.write('PIC Responsible: Procurement')
    st.write('Kategori Item: Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 ].groupby(['Kategori PO(Datang)-PO(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PO(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                ]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute','PO(Datang)-PO(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PO(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
        
    st.write('Kategori Item: Resto')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Kategori PO(Datang)-PO(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-PO(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                ]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-PO(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute','PO(Datang)-PO(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-PO(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Resto') 
                 & (df_eksternal['Kategori PO(Datang)-PO(Create)']=='Backdate')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)

if kat_eksternal =='PO(Datang)-RI(Create)':
    st.markdown('### Kategori PO(Datang)-RI(Create)')
    st.write('PIC Responsible: Resto')
    st.write('Kategori Item: Eksternal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori Item']=='Eksternal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute','PO(Datang)-RI(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-RI(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) & (df_eksternal['PIC Responsible']=='Logistic') 
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
        
    st.write('Kategori Item: Eksternal Resto')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) 
                 & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))  
                 & (df_eksternal['Kategori Item']=='Eksternal Resto')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute','PO(Datang)-RI(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-RI(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) 
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Eksternal Resto')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
    
    st.write('PIC Responsible: WH/CK')
    st.write('Kategori Item: Internal Logistic')
    col = st.columns([1,2,1,2])
    
    with col[0]:
        df_pie = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) 
                 & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Kategori PO(Datang)-RI(Create)'])[['Nomor PO']].nunique().reset_index()
        create_pie_chart(df_pie, labels_column='Kategori PO(Datang)-RI(Create)', values_column='Nomor PO', title="OUTGOING BACKDATE")
    with col[1]:
        df_line = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')
                 ].groupby(['Tanggal PO'])[['Nomor PO']].nunique().reset_index()
        df_line = df_tanggal.merge(df_line,how='left',left_on='Tanggal',right_on='Tanggal PO').fillna(0)
        create_line_chart(df_line, x_column='Tanggal', y_column='Nomor PO', title="DAILY BACKDATE")
    with col[2]:
        df_bar = df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index()
        create_percentage_barchart(df_bar, 'Rute', 'Nomor PO')
    with col[3]:
        st.write('')
        col2 = st.columns(3)
        with col2[0]:
            st.metric(label="Total", value="{:,.0f}".format(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))  
                 & (df_eksternal['Kategori Item']=='Internal Logistic')]['Nomor PO'].nunique()), delta=None)
        with col2[1]:
            st.metric(label="On-Time", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='On-Time']['Nomor PO'].values[0]), delta=None)
        with col2[2]:
            st.metric(label="Backdate", value="{:,.0f}".format(df_pie[df_pie['Kategori PO(Datang)-RI(Create)']=='Backdate']['Nomor PO'].values[0]), delta=None)
        
        st.dataframe(df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date))
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute','PO(Datang)-RI(Create) Group'])[['Nomor PO']].nunique().reset_index().pivot(index='Rute',columns='PO(Datang)-RI(Create) Group',values='Nomor PO').reset_index().merge(
            df_eksternal[(df_eksternal["Tanggal PO"] >= pd.Timestamp(start_date)) & (df_eksternal["Tanggal PO"] <= pd.Timestamp(end_date)) 
                 & (df_eksternal['Kategori PO(Datang)-RI(Create)']=='Backdate') & (df_eksternal['Kategori Item']=='Internal Logistic')].groupby(['Rute'])[['Nomor PO']].nunique().reset_index().rename(columns={'Nomor PO':'Total'})
                 ),
                     hide_index=True)
