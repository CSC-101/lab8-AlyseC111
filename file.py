import sys
#our program should open the file and read each line until the entire contents have been read.
# Each line in the file is expected to consist of two float values (how can you split a line into
# these two separate values?). For each line, convert the float values and print their sum.
if __name__ == '__main__':
    print(sys.argv)

    try:
       with open(sys.argv[1], 'r') as infile:
           content = infile.readlines()
           for i in range(len(content)):
               content[i] = content[i].rstrip('\n')
               elem = content[i].split(' ')
               if len(elem) != 2:
                   print("Error - line did not contain 2 elements")
               else:
                    try:
                        elem[0] = float(elem[0])
                        elem[1] = float(elem[1])
                        print(elem[0] + elem[1])
                    except ValueError:
                        print("Error - line cannot be processed")
    except IOError as e:
        print("Cannot open file: ", e)


