import streamlit as st
import datetime
st.title ("Дата")
# Відображення вибору дати на веб-сторінці
selected_date = st.date_input("Виберіть дату", datetime.date.today())

# Виведення вибраної дати
st.write("Ви вибрали дату:", selected_date)
st.write("Тиждень:", selected_date.isoweekday())
st.write("Тип вибраної дати:", type(selected_date))
print (selected_date)