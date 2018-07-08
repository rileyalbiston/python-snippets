import csv

# Method 1 way of opening and reading the csv using csv.DictReader
with open('files/mpg.csv') as csv_file:
    mpg = list(csv.DictReader(csv_file))   
print(mpg[:2], '\n')

# Method 2 way of opening and reading the csv using csv.DictReader
file = open('files/mpg.csv')
file_content = list(csv.DictReader(file))
print(file_content[:2], '\n')

# Show the number of rows in the csv, minus the heading row
print(len(file_content), '\n')

# Show the column headers
print(file_content[0].keys(), '\n')

# Find the average mpg
print(sum(float(d['mpg']) for d in file_content) / len(file_content), '\n')

# Find the average weight of vehicles
print(sum(float(d['weight']) for d in file_content) / len(file_content), '\n')

# Using set to return all the unique number of cylinders of the cars
cylinders = set(d['cylinders'] for d in file_content)
print(cylinders, '\n')

# find the average mpg grouped by the number of cylinders
mpg_by_cylinders = []
for c in cylinders: # iterate over all the cylinder levels
    sum_mpg = 0
    cylinders_type_count = 0
    for d in file_content: # iterate over all dictionaries
        if d['cylinders'] == c: # if the cylinder level type matches,
            sum_mpg += float(d['mpg']) # add the mpg
            cylinders_type_count += 1 # increment the count
    mpg_by_cylinders.append((c, sum_mpg / cylinders_type_count)) # append the tuple ('cylinder', 'avg mpg')


mpg_by_cylinders.sort(key=lambda x: x[0])
print(mpg_by_cylinders, '\n')

# Using set to return all the unique year numbers of the cars
vehicle_year = set(d['model_year'] for d in file_content) # what are the year models in the data set
print(vehicle_year, '\n')


# find the average mpg grouped by the year
mpg_by_year = []
for y in vehicle_year: # iterate over all the vehicle years
    sum_mpg = 0
    vehicle_years_count = 0
    for d in file_content: # iterate over all dictionaries
        if d['model_year'] == y: # if the year model type matches,
            sum_mpg += float(d['mpg']) # add the mpg
            vehicle_years_count += 1 # increment the count
    mpg_by_year.append((y, sum_mpg / vehicle_years_count)) # append the tuple ('model_year', 'avg mpg')

    
mpg_by_year.sort(key=lambda x: x[1])
print(mpg_by_year, '\n')