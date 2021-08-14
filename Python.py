import csv

rows = []

with open("star_with_gravity.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

for index, star_data in enumerate(star_data_rows):
  final_star_data = []
  if star_data[2].lower() < 101:
      final_star_data.append(star_data)
  if star_data[5].lower() > 149 and star_data[5] < 351:
      final_star_data.append(star_data)

print(final_star_data)