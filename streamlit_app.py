import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

   
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Adding a pick list here so they  can pick the fruit to include
fruits_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page

streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruitvice Fruit Advice !')
fruit_choice = streamlit.text_input('what fruit would you like information about?', 'kiwi')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

#don't run anything past here while we troubleshoot
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('what fruit would you like to add?', 'jackfruit')

streamlit.write('thanks for adding ' , add_my_fruit)

my_cur.execute("insert into FRUIT_LOAD_LIST VALUES ('from streamlit')")



