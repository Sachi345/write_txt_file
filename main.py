import csv

# write the txt or csv file
header = ['cus_no', 'fname', 'sname']
data = [
    ['1', 'thilina', 'blyz'],
    ['1', 'thilina', 'blyz'],
    ['2', 'che', 'hewa']
]

with open('output_1.txt', 'w', newline='') as file1:
    writer = csv.writer(file1, delimiter='\t')
    writer.writerow(header)
    writer.writerows(data)