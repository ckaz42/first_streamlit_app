import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('Ruthie\'s New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🧆 Omega 3, Gluten Free, Blueberry Falafal')
streamlit.text('🍏 Apple Ginger Rocket Smoothie')
streamlit.text('🍳 Hard-Boiled Free-Range Eggs and organic onions')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🥝🍑Make Your Own Fruit Smoothie🍌🍉')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response 
streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like to dilute?')
if not fruit_choice:
  streamlit.error("Please choose a fruze to get information.")
else:
  fruityvice_response = requests.get ("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
streamlit.stop() 

#streamlit.text(fruityvice_response.json())
#take the json version and normalize it
#output it to the screen as a table


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

add_my_fruit = streamlit.text_input('What fruit would you like to toot?')
streamlit.write('The user entered', add_my_fruit + '.')
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows= my_cur.fetchall()
#streamlit.text("Hello from the Snow:")
streamlit.header("The fruit load list conatins:")
streamlit.dataframe(my_data_rows)
