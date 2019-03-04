'''
Read the dictionary of names and birthday dates from external file
Prints out information how many people were born according to month.
'''

import os
import json
from collections import Counter

# reads birthday json from external file
file_name = "28_Birthday-dictioneries.json"
if os.path.exists(file_name):
	with open(file_name, 'r') as file:
		bdays = dict(json.load(file))

# changes numeric symbol of a month to a name
months = [i[3:5]for i in bdays.values()]
month_name = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'Jun','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
months=[month_name[i] for i in months]

# counts and prints how many people were born each month
month_stat = Counter(months)
for m in month_stat.keys():
	print(f"{month_stat[m]} people were born in {m}")