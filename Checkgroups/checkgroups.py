def find_groups (stud_index, column_names, values, typeofdata): # column_names - назви рядочків, aka групи і ПІБ, values - таблиця
    count_groups = len(column_names) - 2
    group_array = []
    group_name = []
    counter_skipped = 0
    for i in range(count_groups):
        group_name.append(column_names[i+2])
        group_array.append(values[stud_index][i+2])
        if  group_array[i - counter_skipped] == 0:
            group_name.pop()
            group_array.pop()
            counter_skipped += 1
    if typeofdata == 0:
        return(group_name)
    else:
        return(group_array)