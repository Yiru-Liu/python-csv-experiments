import csv

# with open('quotesum.csv', newline='') as r, open('out.csv', 'w', newline='') as w:
#     reader = csv.reader(r)
#     for row in reader:
#         print(row[19] + '\t' + row[21] + '\t' + row[22])
#         w.write('"' + row[19] + '","' + row[21] + '","' + row[22] + '"\n')
#     w.close()

with open('test dummy.csv', newline='') as r, open('removed.csv', 'w', newline='') as w:
    reader = csv.reader(r)
    for row in reader:
        print(row)
        if all('' == s or s.isspace() for s in row):
            print('true')
        else:
            print('false')
    w.close()