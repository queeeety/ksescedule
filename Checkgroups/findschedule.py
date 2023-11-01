import datetime

def studentScheduleByDay(group_of_student, date):
    import pandas as pd
    df_lectors = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vT2aEeS8hEAxrMseZiHx56A80ypA9BKjXxSLStQ9T5KEh6CMhqLPswQ5pB-GpyblSvvM2U0sTMJpaCj/pub?output=xlsx", sheet_name='Teachers')
    df_lectors = df_lectors.fillna(0)
    lectors = df_lectors.values.tolist()

    weeks = (date - datetime.date(2023,9,4)).days //7
    print (weeks)
    sheetname = f"Тиждень " + str(weeks+1)
    print (sheetname)
    df_scedule = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vSS_9qQkbHFMPyWQaTsDLIK4X5Vzv7IsEXl_VrCMzn0gOFd8eOaVpuVPRIYfPzc2wjNYhnsNcc2yiYl/pub?output=xlsx", sheet_name=sheetname)
    df_scedule = df_scedule.fillna(0)
    sc_table = df_scedule.values.tolist()


    day_of_the_week = date.isoweekday()
    intable_groups = df_lectors.iloc[:, 1]
    groups_naming = df_lectors.iloc[:, 0]
    groups_naming = groups_naming.values.tolist()
    intable_groups = intable_groups.values.tolist()
    tempgroup = ' '
    schedule = []
    for w in range (6):
        line_groups_per_couple = df_scedule.iloc[w+1, -6 + 8*day_of_the_week: 2 + 8*day_of_the_week]
        line_groups_per_couple = line_groups_per_couple.values.tolist()
        print (line_groups_per_couple)
        ifadded = False
        for i in range(8):
            onecouple = line_groups_per_couple[i]
            if onecouple != 0:
                try:
                    index = intable_groups.index(onecouple)
                except ValueError as e:
                    pass

                if groups_naming[index] in group_of_student:
                    tempgroup = groups_naming[index]
                    schedule.append (tempgroup)
                    ifadded = True
        if not ifadded:
            schedule.append (' ')
        
    print (schedule)
    return schedule

date = datetime.date(2023,11,1)
group_of_student = ["КШЕ1", "ТЙ1 (Л)", "ЛА3 (Л)", "ТЙІТ2 (П)", "ЛАІТ2 (П)", "А (ІТ) 1",	"ОП (П) 1"]
print(studentScheduleByDay(group_of_student,date))