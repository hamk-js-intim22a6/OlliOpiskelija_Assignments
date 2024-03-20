import csv

# Task 1: Generate csv file called eu_countries.csv
# Populate it with data: country name, population, land area
eu_countries_data = [
    ['Country Name', 'Population', 'Land Area (km²)'],
    ['Germany', '83190556', '357022'],
    ['France', '67391582', '551695'],
    ['Italy', '59554023', '301340'],
    ['Spain', '47351567', '505990'],
    ['Poland', '37950802', '312696']
]
# Write the data to the csv file
with open('eu_countries.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(eu_countries_data)

# Task 2: Read the csv file
with open('eu_countries.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        