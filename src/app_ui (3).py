import streamlit as st

import app_db

st.title('STREAMLIT DATABASE UI')

option = st.sidebar.selectbox('Select Your Option: ',
                    ('SELECT ALL RECORDS',
                     'SELECT RECORD BY ID',
                     'INSERT RECORD',
                     'DELETE RECORD BY ID',
                     'UPDATE RECORD BY ID'))

if option == 'SELECT ALL RECORDS':
    if st.button('SHOW DATA'):
        result = app_db.select_all_records()
        st.write(result)
elif option == 'SELECT RECORD BY ID':
    pass
elif option == 'INSERT RECORD':
    pass
elif option == 'UPDATE RECORD BY ID':
    pass
elif option == 'DELETE RECORD BY ID':
    pass