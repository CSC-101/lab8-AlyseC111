import sys

if __name__ == '__main__':
    print(sys.argv)

    try:
       with open('sys.argv', 'r') as infile:
           content = infile.readlines()
           for i in range(len(content)):
               elem = content[i].split(' ')
               sum = 0
               if len(elem) == 2 and elem[0] == float and elem[1] == float:
                   for j in elem:
                       sum += j
               else:
                   print("Error; line cannot be processed")
               print(sum)
    except IOError as e:
        print("Cannot open file: ", e)
    except ValueError as e:
        print("No File Provided: ", e)


