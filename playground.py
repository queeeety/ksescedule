import streamlit as st
import main 
#with st.form(key='Name'):
#    c1, c2 = st.columns(2)
#    with c1:
#        surname = st.selectbox("Прізвище", ["s", "s", "s"])
#    with c2:
#       name = st.selectbox("Імʼя", ["s", "s", "s"])
#    submitButton = st.form_submit_button(label = 'Показати')
sur_list = main.values_surname
name_list = main.values_name
surname = st.selectbox("Прізвище", sur_list)
names = []
for i in range(len(sur_list)):
    if surname == sur_list[i]:
        names.append(name_list[i])
if len(names) == 1:
    name = st.selectbox("Імʼя", [names])
