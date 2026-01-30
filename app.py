import streamlit as st
st.title('IST488Labs')
tab1 = st.Page('HW/hw-1.py', title = 'Homework 1')
tab2 = st.Page('HW/hw-2.py', title = 'Homework 2')

pg = st.navigation([tab1, tab2])
st.set_page_config(page_title = 'IST488 Homework',
                    initial_sidebar_state = 'expanded')

pg.run()