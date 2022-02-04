import csv, sys 

def main():

    # requires 3 arguments and throws an error 
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        exit(1)

    # reads a csv file from the databases directory into memory
    if sys.argv[1].endswith(".csv"):
        with open(f"databases/{sys.argv[1]}", 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            # reminder that a list in python is an iterable array
            # database contains one of the database entered by the user 
            database = list(reader) 
    else:
        print("Usage: '.csv'")
        exit(1)

    # reads a text file from sequences directory into memory

    if sys.argv[2].endswith(".txt"):
        with open(f"sequences/{sys.argv[2]}", 'r') as DNA:
            DNA = DNA.read()


    else:
        print("Usage: '.txt'")
        exit(1)


    STR = reader.fieldnames[1:len(reader.fieldnames)] # the top line of the csv sans 'name' field
    
    # print(database[1]) # selects the second name in the database and prints it
    # print(database[0:1])
    # print(DNA)
    # print(STR)
    

    ## TO DO ##
    # Find the longest consecutive repeats of STR in DNA
    consecutive_str_count = 0
    max_consecutive_str = 0
    for i in DNA:
        print(i)
    

    


main()
