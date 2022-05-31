import csv
import pandas as pd
file_1 = 'dwarf_stars.csv'
file_2 = 'bright_stars.csv'
d1 = []
d2 = []
with open(file_1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d1.append(i)

with open(file_2, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]
p_d1 = d1[1:]
p_d2 = d2[1:]
h = h1+h2
p_d = []
for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)

with open("merged_data.csv", 'w', encoding='utf8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(p_d)
df = pd.read_csv('merged_data.csv')
df.tail(8)