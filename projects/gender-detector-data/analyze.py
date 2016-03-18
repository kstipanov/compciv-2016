from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'data'

CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified_carnegie_collection.csv')
LOWER_YEAR = 1980
LOWER_LOWER_YEAR = 1960
UPPER_YEAR = 1995
UPPER_UPPER_YEAR = 2015

all_rows = list(DictReader(open(CLASSIFIED_DATA_FILENAME)))

male_count = 0
female_count = 0
for row in all_rows:
	if row['gender'] == "M":
		male_count += 1
	if row['gender'] == "F":
		female_count += 1
line_count = female_count + male_count

print("In total:")
print("      Carnegie's collection holds ", round((female_count / line_count) * 100), " percent female artists.")


females_before_lower_year = 0
males_before_lower_year = 0
females_after_upper_year = 0
males_after_upper_year = 0
for row in all_rows:
	if row['date_acquired']:
		if (int(row['date_acquired']) > UPPER_YEAR) and (int(row['date_acquired']) < UPPER_UPPER_YEAR):
			if row['gender'] == 'F':
				females_after_upper_year += 1
			elif row['gender'] == 'M':
				males_after_upper_year += 1
		elif int(row['date_acquired']) < LOWER_YEAR and (int(row['date_acquired']) < LOWER_LOWER_YEAR):
			if row['gender'] == 'F':
				females_before_lower_year += 1
			elif row['gender'] == 'M':
				males_before_lower_year += 1

total_after_upper_year = males_after_upper_year + females_after_upper_year
total_before_lower_year = males_before_lower_year + females_before_lower_year

print("Carnegie Museum of Art's new collections between the years ", LOWER_LOWER_YEAR, " and ", LOWER_YEAR, ":")
print("      Included:", round((females_before_lower_year / total_before_lower_year) * 100), " percent female artists.")
print("Carnegie Museum of Art's new collections between the years ", UPPER_YEAR, " and ", UPPER_UPPER_YEAR, ":")
print("      Included:", round((females_after_upper_year / total_after_upper_year) * 100), " percent female artists.")

