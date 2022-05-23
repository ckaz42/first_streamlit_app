import streamlit
streamlit.title('Ruthie\'s New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🧆 Omega 3, Gluten Free, Blueberry Falafal')
streamlit.text('🍏 Apple Ginger Rocket Smoothie')
streamlit.text('🍳 Hard-Boiled Free-Range Eggs and organic onions')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🥝🍑Make Your Own Fruit Smoothie🍌🍉')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawbrries'])

#display the table
streamlit.dataframe(my_fruit_list)
