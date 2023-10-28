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

def find_surname(surname):
    i = 0
    while surname != values_nameAndSurname[i]:
        i+=1
    return (i)

comnames = []
def combine (sur, nam):
    for i in range (len(sur)):
        comnames.append(sur[i] + ' ' + nam[i])
    return comnames


values_nameAndSurname = combine(values_surname, values_name)
surname = st.selectbox("Імʼя", values_nameAndSurname, key = 'nameOfTheStudent')

if not surname in values_nameAndSurname:
        st.write("Неправильно введене імʼя")
elif surname != '':
    index_student = find_surname(surname)
find_groups_names_array = (cg.find_groups(index_student,column_names,values,0))
find_groups_values_array = (cg.find_groups(index_student,column_names,values,1))

for i in range(len(find_groups_names_array)):
      st.write(f'{find_groups_names_array[i]}: {find_groups_values_array[i]}')