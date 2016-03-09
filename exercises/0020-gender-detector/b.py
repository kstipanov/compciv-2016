from os.path import join
from os.path import basename

from glob import glob
DATA_DIR = 'tempdata'
alltxtfiles_path = join(DATA_DIR, '*.txt')
alltxtfiles_names = glob(alltxtfiles_path)

myfilenames = []
for fname in alltxtfiles_names:
  bname = basename(fname) 
  year = bname[3:7]
  if year >= "1950":
      myfilenames.append(fname)

gendict = {'M': 0, 'F': 0}

for fname in myfilenames:
    babyfile = open(fname, "r")
    for line in babyfile:
        name, gender, babies = line.split(',')
        gendict[gender] += int(babies)

print("F:", str(gendict['F']).rjust(6),
      "M:", str(gendict['M']).rjust(6))

f_to_m_ratio = round(100 * gendict['F'] / gendict['M'])
print("F/M baby ratio:", f_to_m_ratio)