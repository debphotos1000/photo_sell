import streamlit as st
from PIL import Image
import sqlite3

# Define a function to create the table in the database
def create_table():
    conn = sqlite3.connect('product_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  price REAL,
                  description TEXT,
                  image BLOB)''')
    conn.commit()
    conn.close()

# Define a function to insert a new product into the database
def insert_product(price, description, image):
    conn = sqlite3.connect('product_database.db')
    c = conn.cursor()
    c.execute('''INSERT INTO products (price, description, image)
                 VALUES (?, ?, ?)''', (price, description, image))
    conn.commit()
    conn.close()

def view_data():
    conn = sqlite3.connect("product_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    data = c.fetchall()
    conn.close()
    return data
def get_puja_by_id(id):
    conn = sqlite3.connect("product_database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM products WHERE id="{}"'.format(id))
    data = c.fetchall()
    conn.close()
    return data

def create_table2():
    conn = sqlite3.connect('sell_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sells
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT,
                  image id TEXT)''')
    conn.commit()
    conn.close()
def insert_sell(name, email, image_id):
    conn = sqlite3.connect('sell_database.db')
    c = conn.cursor()
    c.execute('''INSERT INTO sells (name, email, image id)
                 VALUES (?, ?, ?)''', (name, email, image_id))
    conn.commit()
    conn.close()
def view_data2():
    conn = sqlite3.connect('sell_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sells")
    data = c.fetchall()
    conn.close()
    return data
# Create the table if it doesn't exist
create_table()
def admin():
    st.title("Admin Login")
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password',type='password')
    if st.sidebar.checkbox("Login"):
        if username == "deb" and password == "deb":
            st.success(f'Logined as {username}')
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
            # Add text input widgets for the price and description
            price = st.number_input("Price", min_value=0.0, step=0.01)
            description = st.text_input("Description")
            # If an image was uploaded, display it
            if uploaded_file is not None:
                st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

            if st.button("Submit"):
                if uploaded_file is not None:
                    insert_product(price, description, uploaded_file.read())
                    st.success("Product added to database.")
                else:
                    st.error("Error: Please upload an image.")
            
            
                