import csv

DATADIR = r"C:\Users\tihan\OneDrive\Desktop\ATU\WSAA-coursework\labs\lab01-Datarepresentation\\"
FILENAME = "data.csv"

#with open(DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #for line in reader:
        #print(line)
        
        # Data type: list of strings
        
#with open (DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #linecount = 0
    #for line in reader:
        #if not linecount: # first row ie header row
            #print (f"{line}\n-------------------")
        #else: # all subsequent rows
            #print (line)
        #linecount += 1
        
#with open (DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #linecount = 0
    #total = 0
    #for line in reader:
        #if not linecount: # first row ie header row
            #pass
        #else: # all subsequent rows
            #total += int(line[1]) # why 1
            # because it refers to the second column of the csv file which contains the age.
        #linecount += 1
   # print (f"average is {total/(linecount-1)}") # why -1 ?
    # because the linecount includes the header row, so we subtract 1 to get the correct number of data rows for calculating the average.

#with open (DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    #linecount = 0
    #total = 0
    #for line in reader:
        #if not linecount: # first row ie header row
            #pass
        #else: # all subsequent rows
            #total += line[1] # why 1
            # because it refers to the second column of the csv file which contains the age.
        #linecount += 1
    #print (f"average is {total/(linecount-1)}") # why -1 ?
    # because the linecount includes the header row, so we subtract 1 to get the correct number of data rows for calculating the average.

  
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        # print (line)
        count +=1
    print (f"average is {total/(count)}") # why is there no -1 this time?
   
