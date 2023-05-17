import streamlit as st
from streamlit_lottie import st_lottie
import requests
from admin import view_data, get_puja_by_id
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
load = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_seidgi4z.json")
def buy_image():
    st.header('Buy image')
    col1,col2,col3 = st.columns(3)
    with col2:
        st_lottie(load)
    name = st.text_input("Your name")
    if not name:
        st.warning('Please type/write your name.')
        st.stop()
    email = st.text_input('Your email ex:- Example@gmail,com')
    if not email:
        st.warning('Please type/write your email.')
        st.stop()
    data = view_data()
    all_imag_id = [data[i][0] for i in range(0,len(data))]
    imag_id_select = st.selectbox('Choose an image ID', all_imag_id)
    re = get_puja_by_id(imag_id_select)
    for i in re:
        st.image(i[3])
        st.success(f'Price of image is ${i[1]}')
    

