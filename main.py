# Importing the necessary libraries
import streamlit as st
import langchain_helper

# Providing the title of the webpage
st.title("Restaurant Name Generator")

# Creating a sidebar to pick one cuisine
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Mexican", "Italian", "Portuguese", "Spanish"))

if cuisine:
    response = langchain_helper.restaurant_name_and_items(cuisine)
    
    # Displaying the restaurant name
    st.header(response['restaurant_name'].strip())
    
    # Displaying the menu items
    menu_items = response['menu_items'].strip().split(",")
    
    st.write("--Menu Items--")
    
    for items in menu_items:
        st.write(f"- {items}")
