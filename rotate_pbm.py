# This script is rotate the pbm image to either 90 or 180 degrees
# Author: bhanu.kiran117@gmail.com
# This script has function convert_pdbfile which accepts two parameters 1. pdb file 2. Angle to rorate
# This covert the pbm file and restore in rotated_Image_{angle}.pbm in same directory

import errno
import re
import sys

def covert_pbmfile(finame, angle):
    try:
        #trying to open a file in read mode
        fo = open(finame,"r")
        print("Image.pdm exists and opened")
        linesoffile = fo.readlines()
        # Validate pbm file 
        # check if the first line of the file is P1
        if linesoffile[0].rstrip() != "P1":
            print ("This is not a pbm file")
            sys.exit(1)
        # check if second line has comment
        if not re.match(r"^#",linesoffile[1].rstrip()):
            print ("This is not a pbm file")
            sys.exit(1)
        # Get the rows and columns from the thrid line
        rows_columns = linesoffile[2].rstrip().split()
        cols = int(rows_columns[0]) ; rows = int(rows_columns[1])

        if cols == rows:
            print ("Error: This is square image")
            sys.exit(1)
        print ( "Number of rows", rows, cols)
        array_data=[] 
        for row in range(rows):  # Added two
            pbm_index=row+3
            pbm_line = linesoffile[pbm_index].rstrip()
            #print (pbm_line)
            pbm_bad_char = False
            # Validate 1's and 0's and spaces in pbm bits
            char_position=0
            for character in pbm_line:
                if character != '0' and character != '1' and character != ' ':
                    print (character, "ERROR")
                    pbm_bad_char = True
                    break
            if pbm_bad_char == True:
                print("Bad characters in a pbm file")
                break    
            # Below command pbm_line.split() convert the line to list and list is adding to arry_data
            array_data.append([int(x) for x in pbm_line.split()])
        #print (array_data)
        #print("length of each element in arry_data", len(array_data[0]))
        #print("length of array_data", len(array_data))

        # Below code iterate number of columns, and convert the each to row to column
        rotated_array = []
        if angle == 90:
            for col_pos in range(cols):
                rotated_array_temp = []
                for element in range(rows-1, -1, -1):
                    #print(col_pos,y)
                    #print(array_data[y][col_pos]])
                    rotated_array_temp.append(array_data[element][col_pos])
                rotated_array.append(rotated_array_temp)
            cols,rows = rows, cols
            print (rotated_array)
        # Save the rorated bitmap arry to new file.

        
        if angle == 180:
            for y in range(rows-1, -1, -1):
                rotated_array_temp = []
                for x in range(cols-1, -1, -1):
                    rotated_array_temp.append(array_data[y][x])
                rotated_array.append(rotated_array_temp)

            print(rotated_array)

        if angle == 270:
            for x in range(cols-1, -1, -1):
                rotated_array_temp = []
                for y in range(rows):
                    rotated_array_temp.append(array_data[y][x])
                rotated_array.append(rotated_array_temp)
            cols,rows = rows, cols
            print(rotated_array)

        with open('rotated_Image_'+ str(angle) +'.pbm', 'w') as rotated_file:
                rotated_file.write(linesoffile[0])
                print (angle)
                rotated_file.write("#This is example of " + str(angle) + " degree rorated bitmap of letter 'J' ")
                rotated_file.write(f'{cols} {rows}\n')
                for row in rotated_array:
                    rotated_file.write(' '.join([str(x) for x in row]) + '\n')

    except FileNotFoundError:
        print("File does not exist")
    except Exception as e:
        print("Other error" + str(e))


covert_pbmfile("Image.pbm",90)
covert_pbmfile("Image.pbm",180)
covert_pbmfile("Image.pbm",270)


""" Example output

-rw-r--r-- 1 bhanuk          bhanuk                 187 Feb 25 14:17  rotated_Image_90.pbm
-rw-r--r-- 1 bhanuk          bhanuk                 188 Feb 25 14:17  rotated_Image_180.pbm
-rw-r--r-- 1 bhanuk          bhanuk                 188 Feb 25 14:17  rotated_Image_270.pbm

cat  rotated_Image_90.pbm rotated_Image_180.pbm rotated_Image_270.pbm
P1
#This is example of 90 degree rorated bitmap of letter 'J' 10 6
0 0 0 1 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
P1
#This is example of 180 degree rorated bitmap of letter 'J' 6 10
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 0
0 1 0 0 0 1
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
P1
#This is example of 270 degree rorated bitmap of letter 'J' 10 6
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 1 0 0 0

"""