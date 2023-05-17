import streamlit as st
from PIL import Image
from home import home
from streamlit_option_menu import option_menu
from admin import admin
from gallery import gallery
from buy_image import buy_image
logo = Image.open('Logo (1).png')
def config():
    st.set_page_config(
    page_title='Shutter Moments',
    page_icon= logo,
    layout="wide")
def hide_st():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
back = """
<style>
[class="main css-uf99v8 egzxvld5"] {
background-image: url("https://www.toptal.com/designers/subtlepatterns/uploads/double-bubble-outline.png");
background-repeat: repeat;
background-attachment: fixed;
}
"""
config()
hide_st()
def main():
    st.cache()
    st.markdown(back,True)
    selected = option_menu(
            menu_title=None,
            options=['Home', 'Gallery','Buy image','Admin Login'],
            icons=['house-door-fill','image','card-checklist','person-fill'],
            menu_icon='cast',
            default_index=0,
            orientation="horizontal",
            styles= {"nav-link": {"font-size": "18px", "text-align": "center", "margin":"0px", "--hover-color": "#64A3E8"}}
    )
    st.title("Shutter Moments")
    if selected == 'Home':
        home()
    if selected == 'Gallery':
        gallery()
    if selected == 'Buy image':
        buy_image()
    if selected == 'Admin Login':
        admin()



if __name__ == "__main__":
  main()