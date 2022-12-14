import streamlit
import pandas
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale,spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-range Eggs') 
streamlit.text('🥑🍞 Avacado Toast')                
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruit_to_show)
streamlit.header("Fruityvice Fruit Advice!")
# lets normalise the json imput
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display the table on the page.
streamlit.dataframe(fruityvice_normalized)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
