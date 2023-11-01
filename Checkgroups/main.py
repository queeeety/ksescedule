import streamlit as st
import checkgroups as cg
import pandas as pd # робота з таблицею excel
import datetime 
import findschedule as fs

#починаєм виводити в streamlit
st.title ("Пошук груп")
df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vT2aEeS8hEAxrMseZiHx56A80ypA9BKjXxSLStQ9T5KEh6CMhqLPswQ5pB-GpyblSvvM2U0sTMJpaCj/pub?output=xlsx", sheet_name='Students')
df = df.fillna(0)
values = df.values.tolist() # перетворює dataframe на list, values -- вся наша таблиця
values_surname = df.iloc[:, 0].values.tolist() # df.iloc шукає вибирає потрібні значення
values_name = df.iloc[:, 1].values.tolist()
column_names = df.columns.tolist()
#забирає від прізвищ пробіли
for i in range(len(values_surname)):
        values_surname[i] = values_surname[i].strip()

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

surname = st.selectbox("Введіть імʼя і прізвище", values_nameAndSurname, key = 'TheStudent', placeholder= "Choose an option")

if not surname in values_nameAndSurname:
        st.write("Неправильно введене імʼя")
elif surname != '' :
    index_student = find_surname(surname)
find_groups_names_array = (cg.find_groups(index_student,column_names,values,0))
find_groups_values_array = (cg.find_groups(index_student,column_names,values,1))
print(find_groups_values_array)

for i in range(len(find_groups_names_array)):
      st.write(f'{find_groups_names_array[i]}: {find_groups_values_array[i]}')

st.write("<hr>", unsafe_allow_html=True)

st.title ("Дата")
# Відображення вибору дати на веб-сторінці
start_date = st.date_input("Дата початку", datetime.date.today())
end_date = st.date_input("Дата кінця", datetime.date.today())
data_counter = (end_date - start_date).days
print(type(data_counter))

st.write(data_counter)

table_data = []

for i in range(data_counter+1):
    delta = datetime.timedelta(days = i)
    itterdate = start_date+delta
    print(start_date+delta)
    day_couples = fs.studentScheduleByDay(find_groups_values_array, itterdate)
    print (day_couples)
    table_data.append({'Дата': itterdate, '1 пара': day_couples[0], '2 пара': day_couples[1], '3 пара': day_couples[2], '4 пара': day_couples[3], '5 пара': day_couples[4], '6 пара': day_couples[5]})
st.table(pd.DataFrame(table_data, columns=['Дата', '1 пара', '2 пара', '3 пара', '4 пара', '5 пара', '6 пара']))