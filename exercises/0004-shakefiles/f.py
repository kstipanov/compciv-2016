import os
FNAME = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
TOTAL_LINES = 4766
STARTING_LINE_NUM = TOTAL_LINES - 5 

romeoandjulietfile = open(FNAME, 'r')
for line_num in range(TOTAL_LINES): 
    line = romeoandjulietfile.readline()
    if line_num >= STARTING_LINE_NUM:
        the_line = str(line_num + 1) + ": " + line.strip()
        print(the_line) 

romeoandjulietfile.close()

