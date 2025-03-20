import streamlit as st
import pandas as pd
import re
from openpyxl import load_workbook

def get_row_num(cell):
    return int(re.search(r'\d+', cell).group())

def point_distance(point1, point2):
    return get_row_num(point2) - get_row_num(point1) + 1
st.title('GAGERR')

# Upload RFQ then create new template 
rfq = st.file_uploader("Upload RFQ")
if rfq is not None:
    try:
        df = pd.read_excel(rfq)
        st.success('RFQ uploaded successfully')
        # Input points and limits


        

    except Exception as e:
        st.error(e)
        st.stop()


    with st.form(key='rfq_form'):
        st.write('Input Operator names')
        operator_names = st.text_area('Operator Names: A, B, C')
        st.write('Input Points and Limits')
        points_size = st.text_area('Size Points Location: A18-A30')

        points_form = st.text_area('Form Points Location: A18-A30')

        points_cruve = st.text_area('Cruve Points Location: A18-A30')
                    
        submit_button = st.form_submit_button(label='Submit')

    # Create new template
    if submit_button:
        st.write('Create New Template')

        # Get Size Points
        size_points = points_size.split('-')
        size_num = point_distance(size_points[0], size_points[1])
        size = []

        wb = load_workbook('rfq.xlsx')
        ws = wb.active
        template = load_workbook('template.xlsx')

        for size_point in ws[size_points[0]:size_points[1]]:
            for cell in size_point:
                size.append(cell.value)
                original_sheet = template.active
                new_sheet = template.copy_worksheet(original_sheet)
                new_sheet.title = cell.value
            # TODO: Fill the limits and names into the new sheet

        # Get Form Points
        form_points = points_form.split('-')
        form_num = point_distance(form_points[0], form_points[1])
        form = []

        for form_point in ws[form_points[0]:form_points[1]]:
            for cell in form_point:
                form.append(cell.value)
                original_sheet = template.active
                new_sheet = template.copy_worksheet(original_sheet)
                new_sheet.title = cell.value

        # Get Cruve Points
        cruve_points = points_cruve.split('-')
        cruve_num = point_distance(cruve_points[0], cruve_points[1])
        cruve = []

        for cruve_point in ws[cruve_points[0]:cruve_points[1]]:
            for cell in cruve_point:
                cruve.append(cell.value)
                original_sheet = template.active
                new_sheet = template.copy_worksheet(original_sheet)
                new_sheet.title = cell.value
        

        # for i in range(size_num):
        #     # Record each point and copy a new sheet 
        #     size.append(r)



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

