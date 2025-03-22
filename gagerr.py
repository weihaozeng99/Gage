import streamlit as st
import pandas as pd
import re
from openpyxl import load_workbook

def get_row_num(cell):
    return int(re.search(r'\d+', cell).group())

def point_distance(point1, point2):
    return get_row_num(point2) - get_row_num(point1) + 1

#TODO: Need to confrim the data cell base
data_cell_base = 'A18'
template_data_offset = 3

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
        wb_data = load_workbook('data.cvs')
        ws_data = wb_data.active
        st.success('Data uploaded successfully')
        # Fill into template
        with st.form(key='data_form'):
            st.write('Input First Points Location')
            point_loc = st.text_area('First Points Location: A18')

            data_offset = st.text_area('Distance to Absoulte Value: 3')

            points_offset = st.text_area('Distance to Next Point: 9')
                        
            submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.write('Filling Data into Template')
            # Get First Points
            first_point = point_loc
            offset = int(data_offset)
            points_offset = int(points_offset)
            # Fill data into template
            point = ws_data[first_point]
            
            template_wb = load_workbook('template.xlsx')
            # TODO: Fill up one sheet first then move to the next sheet
            # TODO: Match the point in template

            while point is not None:
                data_base_point = template_ws[data_cell_base]   

                # TODO: Fill the data into the template, 9 points in a row
                for i in range(10):
                    for j in range(9):
                        # TODO: Use the offset to fill the data
                        if(j > 5):
                            #TODO:
                            offset_cell = data_base_point.offset(row=i, column=j+template_data_offset * 2)
                        elif (j > 2):
                            #TODO:
                            offset_cell = data_base_point.offset(row=i, column=j+template_data_offset)
                        else:
                            offset_cell = data_base_point.offset(row=i, column=j)

                # TODO: Record the row number

            wb.save('filled_template.xlsx')
            st.write('Data filled successfully')

    except Exception as e:
        st.error(e)
        st.stop()

