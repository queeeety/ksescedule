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
surname = st.selectbox("Прізвище", sur_list, key = 'surnameOfTheStudent')
names = []
for i in range(len(sur_list)):
    if surname == sur_list[i]:
        names.append(name_list[i])
if len(names) != 1:

    name = st.selectbox("Імʼя", names, key = 'nameOfTheStudent')




'''
import streamlit as st
import checkgroups as cg
import pandas as pd # робота з таблицею excel

#починаєм виводити в streamlit
st.title ("Пошук груп")
#surname = st.text_input("Прізвище: ")
df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vT2aEeS8hEAxrMseZiHx56A80ypA9BKjXxSLStQ9T5KEh6CMhqLPswQ5pB-GpyblSvvM2U0sTMJpaCj/pub?output=xlsx", sheet_name='Students')
df = df.fillna(0)
values = df.values.tolist() # перетворює dataframe на list, values -- вся наша таблиця
values_surname = df.iloc[:, 0].values.tolist() # df.iloc шукає вибирає потрібні значення
values_name = df.iloc[:, 1].values.tolist()
column_names = df.columns.tolist()
#забирає від прізвищ пробіли
for i in range(len(values_surname)):
        values_surname[i] = values_surname[i].strip()
#surname = st.selectbox("Прізвище: ", values_surname)

def find_surname(surname, name):
    i = 0
    while surname != values_surname[i] and name != values_name[i]:
        i+=1
    return (i)



name_list = values_name
surname = st.selectbox("Імʼя", values_surname, key = 'surnameOfTheStudent')
#surname = 'Кравченко'
names = []
"""
for i in range(len(values_surname)):
    if surname == values_surname[i]:
        names.append(name_list[i])
        if len(names) == 1:
             surname_index = i
if len(names) != 1:
    #name = input("Name: ")
    name = st.selectbox("Імʼя", names, key = 'nameOfTheStudent')
else:
     name = values_name[surname_index]
"""


if not surname in values_surname:
        st.write("Неправильно введене прізвище")
elif surname != '' and name != '':
    index_student = find_surname(surname, name)
find_groups_names_array = (cg.find_groups(index_student,column_names,values,0))
find_groups_values_array = (cg.find_groups(index_student,column_names,values,1))

for i in range(len(find_groups_names_array)):
      st.write(f'{find_groups_names_array[i]}: {find_groups_values_array[i]}')

'''