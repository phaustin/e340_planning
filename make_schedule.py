# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% trusted=true
# !ls

# %% trusted=true
import pandas as pd
import json
with open('template_schedule.py','r') as infile:
    the_lines=infile.readlines()
weeklist=[]
columns = ["count","day","date","topic","pre-quiz","assignment","instructor"]
for the_line in the_lines:
    a_field = the_line.split('|')
    trim_field = []
    for test_field in a_field:
        test = test_field.strip()
        if len(test) == 0:
            test = ' '
        trim_field.append(test)
#    print(len(a_field))
    new_dict=dict(zip(columns,trim_field))
    weeklist.append(new_dict)
#print(weeklist)

the_table = pd.DataFrame.from_records(weeklist)
print(len(the_table))
with open('schedule.json','w') as out:
    json.dump(weeklist,out,indent=4)
the_table


# %% trusted=true
def fmt(the_date):
    return the_date.strftime("%d-%b")

import datetime
first_tuesday = datetime.datetime(2020, 1, 12)
last_day = datetime.datetime(2020, 4, 14)
week = datetime.timedelta(days=7)
day = datetime.timedelta(days=1)
all_days = list()
all_lecs = list()
curr_tues = first_tuesday
week_count=1
lecture=0
while curr_tues < last_day:
    curr_thurs = curr_tues + 2 * day
    lecture+=1
    lecA = f"{lecture}({week_count})"
    lecture += 1
    lecB = f"{lecture}({week_count})"
    if curr_tues != datetime.datetime(2020, 2, 16):
        all_days.extend([fmt(curr_tues), fmt(curr_thurs)])
        all_lecs.extend([lecA,lecB])
    curr_tues = curr_tues + week
    week_count+=1
print(len(all_days))
lec_list=all_days[0]
print(list(zip(all_days,all_lecs)))



# %% trusted=true
daycount=0
for count, row in the_table.iterrows():
    print(count,row)
    the_table.loc[count,'date'] = all_days[daycount]
    the_table.loc[count,'count'] = daycount
    the_table.loc[count,'day'] = all_lecs[daycount]
    daycount+=1
the_table

# %% trusted=false
columns = the_table.columns
new_table=the_table[columns[1:]]
new_table.head()
new_table.to_csv('e340_2020t2.csv',index=False)

# %% trusted=false
new_table.head()

# %% trusted=false
