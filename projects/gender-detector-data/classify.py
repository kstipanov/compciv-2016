from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'data'

WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled_carnegie_collection.csv')
CLASSIFIED_HEADERS = ['title', 'creation_date', 'date_acquired', 'cited_name', 'party_type',  'ratio', 'gender', 'usable_name']
CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified_carnegie_collection.csv')



with open(WRANGLED_DATA_FILENAME, 'r') as f:
	datarows = list(DictReader(f))



wf = open(CLASSIFIED_DATA_FILENAME, 'w')
cwf = DictWriter(wf, fieldnames=CLASSIFIED_HEADERS)
cwf.writeheader()


def extract_usable_name(name_string):
	name_list = name_string.split(', ')
	almost_first_name = name_list[-1]
	first_name_list = almost_first_name.split(' ')
	first_name = first_name_list[-1]
	return first_name_list[0]

linecount = 0
for row in datarows:
	linecount += 1
	the_name = row['cited_name']
	usable_name = extract_usable_name(the_name)
	print(linecount, " -- Extracted", usable_name, "from", the_name)


	genderdict = detect_gender(usable_name)
	# now write the row...
	row['gender'] = genderdict['gender']
	row['ratio'] = genderdict['ratio']
	row['usable_name'] = usable_name
	cwf.writerow(row)
