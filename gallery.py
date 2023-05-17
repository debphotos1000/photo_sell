import streamlit as st
from admin import view_data

def gallery():
    st.header('Gallery')
    col1,col2,col3 = st.columns(3)
    data = view_data()
    for i in range(0,len(data)):
        with col2:
            st.image(data[i][3],caption=f'Image id {data[i][0]}. Image price ${data[i][1]}. Image description : {data[i][2]}')