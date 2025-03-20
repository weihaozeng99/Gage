import streamlit as st
import pandas as pd

st.title('GAGERR')

# Upload RFQ then create new template 
rfq = st.file_uploader("Upload RFQ")
if rfq is not None:
    try:
        df = pd.read_csv(rfq)
        st.success('RFQ uploaded successfully')
        # Input points and limits

        # Create new template

        

    except Exception as e:
        st.error(e)
        st.stop()


    with st.form(key='rfq_form'):
        st.write('Input Points and Limits')
        points_size = st.text_area('Size Points Location')

        points_form = st.text_area('Form Points')

        points_cruve = st.text_area('Cruve Points')
                    
        submit_button = st.form_submit_button(label='Submit')

    # Create new template
    if submit_button:
        st.write('Create New Template')


        st.write('Template created successfully')
        st.write('Upload Data')
  

# Upload Data then fill into template
data = st.file_uploader("Upload Data")
if data is not None:
    try:
        df = pd.read_csv(data)
        st.success('Data uploaded successfully')
        # Fill into template

    except Exception as e:
        st.error(e)
        st.stop()

