import streamlit as st
import numpy as np
import pandas as pd # робота з таблицею excel
#починаєм виводити в streamlit
st.title ("Пошук груп")
#surname = st.text_input("Прізвище: ")
df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vT2aEeS8hEAxrMseZiHx56A80ypA9BKjXxSLStQ9T5KEh6CMhqLPswQ5pB-GpyblSvvM2U0sTMJpaCj/pub?output=xlsx")
df = df.fillna(0)
values = df.values.tolist() # перетворює dataframe на list, values -- вся наша таблиця
values_surname = df.iloc[:, 0].values.tolist() # df.iloc шукає вибирає потрібні значення
#забирає від прізвищ пробіли
for i in range(len(values_surname)):
        values_surname[i] = values_surname[i].strip()
surname = st.selectbox("Прізвище: ", values_surname)
column_names = df.columns.tolist()
group_array = []
group_name = []

#Функція нижче буде виводити назву групи і саму групу людини
def find_groups (stud_index):
    count_groups = len(column_names) - 2
    for i in range(count_groups):
        group_name.append(column_names[i+2])
        group_array.append(values[stud_index][i+2])
        if group_name[i] != 'Вступ до математики':
            if group_array[i] != 0: 
                st.write (f"{group_name[i]}: {group_array[i]}")
                print(f"{group_name[i]}: {group_array[i]}")
    print(group_array)
                
def find_surname(surname):
    i = 0
    while surname != values_surname[i]:
        i+=1
    return (i)


if not surname in values_surname:
        st.write("Неправильно введене прізвище")
elif surname != '':
    index_student = find_surname(surname)
    find_groups(index_student)
