import csv

with open('名句精华piped.txt', 'r') as file:
    # load to variable
    lines = file.readlines()

category = ''
rows = []
print(lines)
processing = False
row_string = ''
for row in lines:
    if row == '\n':
        processing = False
        if not row_string:
            continue
        current_row = [
            category,
            *row_string.strip().split('|'),
        ]
        rows.append(current_row)
        row_string = ''
        continue
    if row.startswith('名句精华'):
        # get what is inside the ()
        category = row.split('（')[1].split('）')[0]
    else:
        processing = True
        row_string += row
if row_string:
    current_row = [
        category,
        *row_string.strip().split('|'),
    ]
    rows.append(current_row)
print(rows)

# write to csv
with open('名句精华.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# count number of rows by first column using raw Python
count = {}
for row in rows:
    if row[0] not in count:
        count[row[0]] = 0
    count[row[0]] += 1
print(count)
print(sum(count.values()))
    
# remove midstring newlines in the last item of each row and make this the new rows
# new_rows = []
# for row in rows:
#     new_row = row[:-1]
#     new_row.append(row[-1].replace('\n', ''))
#     new_rows.append(new_row)


# write to csv
# with open('名句精华.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(new_rows)