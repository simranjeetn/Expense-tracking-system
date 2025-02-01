import streamlit as st
from add_update import add_update_tab
from analytics_category import analytics_tab
from analytics_month import analytics_tab2



st.title('Expenses Tracking System')

tab1 , tab2 , tab3 = st.tabs(["Add / Update " , "Analytics By Category" , "Analytics By Month"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_tab2()