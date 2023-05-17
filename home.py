import streamlit as st
from PIL import Image
import io
from streamlit_extras.add_vertical_space import add_vertical_space
from admin import view_data

def home():
    st.header("Home")
    col1, col2  = st.columns(2)
    with col1:
        ima = Image.open('deb.jpeg')
        st.image(ima)
    with col2:
       st.subheader("Summary")
       add_vertical_space()
       st.write("My strong interest in the art of capturing moments and expressing emotions through images indicates that I view photography as a form of artistic expression. I see the potential for images to convey powerful messages, tell stories, and capture memories that last a lifetime. This passion likely stems from my appreciation for the visual arts, as well as my desire to communicate and connect with others through my photographs.")
       add_vertical_space()
       st.write("As someone who enjoys exploring different techniques and experimenting with various camera settings, I approach photography as a creative process that requires both technical skill and artistic vision. I am constantly trying out new equipment, playing with lighting and composition, and learning new software tools to enhance and refine my work.")
       add_vertical_space()
       st.write("My drive to constantly learn and improve my skills suggests that I am committed to growing as a photographer. Whether through formal training, workshops, or self-study, I recognize that there is always more to learn and new challenges to take on. This mindset of continuous improvement helps me stay motivated and engaged with my photography, even when I encounter obstacles or setbacks.")
       add_vertical_space() 
       st.write("Finally, my joy in sharing my work with others demonstrates a desire to connect with and inspire others through my photography. I share my photos on social media, exhibit my work in galleries, or collaborate with others on projects. This desire to share my passion with others also leads me to seek out feedback and constructive criticism from other photographers, which can help me improve and grow even further.")
       add_vertical_space() 
       st.write("Overall, my passion for photography is a significant part of my life, and it brings me a great deal of fulfillment and joy. My dedication to improving my skills and sharing my work with others is a testament to the power of photography as a form of creative expression and communication.")
    st.subheader("here are some images")
    data = view_data()
    for i in range(0,len(data)):
        st.image(data[i][3])
        

