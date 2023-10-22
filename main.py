import streamlit as st
import pandas as pd # робота з таблицею excel
#починаєм виводити в streamlit
st.title ("Умовний title")
surname = st.text_input("Surname: ")
def find_surname(surname):
    df = pd.read_excel("ITBA27_1term.xlsx")
    values = df.values.tolist() # перетворює dataframe на list
    values_surname = df.iloc[:, 0].values.tolist() # df.iloc шукає вибирає потрібні значення
    for i in range(len(values_surname)):
        values_surname[i] = values_surname[i].strip()
    i = 0
    if not surname in values_surname:
        st.write("Неправильно введене прізвище")
    else:
        while surname != values_surname[i]:
            i+=1
        vm_piba = values[i][5]
        print(vm_piba)
        st.write(f"Математична група (практика): {vm_piba}")

if surname !='':
    find_surname(surname)
