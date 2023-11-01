import pandas as pd

# Load the data from Google Sheets
df_lectors = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vT2aEeS8hEAxrMseZiHx56A80ypA9BKjXxSLStQ9T5KEh6CMhqLPswQ5pB-GpyblSvvM2U0sTMJpaCj/pub?output=xlsx", sheet_name='Teachers')
df_lectors = df_lectors.fillna(0)

df_schedule = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vSS_9qQkbHFMPyWQaTsDLIK4X5Vzv7IsEXl_VrCMzn0gOFd8eOaVpuVPRIYfPzc2wjNYhnsNcc2yiYl/pub?output=xlsx", sheet_name='Schedule')
df_schedule = df_schedule.fillna(0)

# Convert DataFrames to lists
lectors = df_lectors.values.tolist()
sc_table = df_schedule.values.tolist()

group_of_student = ["КШЕ1", "ТЙ1 (Л)", "ЛА3 (Л)", "ТЙІТ2 (П)", "ЛАІТ2 (П)", "А (ІТ) 1", "ОП (П) 1"]

intable_groups = df_lectors.iloc[:, 1]
groups_naming = df_lectors.iloc[:, 0].values.tolist()
intable_groups = intable_groups.values.tolist()

schedule = [None] * 8

def findschedule(groups_student):
    onecouplegroups = df_schedule.iloc[1, 2:10].values.tolist()
    print(onecouplegroups)
    
    for i in range(8):
        for f in range(len(groups_naming)):
            if groups_student[i] == groups_naming[f]:
                tempgroup = intable_groups[f]
                if tempgroup in groups_naming:
                    schedule[i] = onecouplegroups[i]
    
    print(schedule)
    return schedule

print(findschedule(group_of_student))
