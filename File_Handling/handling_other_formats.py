# work with binary files: use the mode 'b'
# open a binary file in read mode
#Most of the files that we see in our computer system are called binary files.

# Example:
# Document files: .pdf, .doc, .xls etc.
# Image files: .png, .jpg, .gif, .bmp etc.
# Video files: .mp4, .3gp, .mkv, .avi etc.
# Audio files: .mp3, .wav, .mka, .aac etc.
# Database files: .mdb, .accde, .frm, .sqlite etc.
# Archive files: .zip, .rar, .iso, .7z etc.
# Executable files: .exe, .dll, .class etc.


with open('file_handling_basics.py', 'rb') as f:
    lines = f.readlines()

for line in lines:
    print(line, end='')



# With CSV files

import csv 

# Reading from CSV files (as lists)
with open('demo_csv.csv') as file:
    # print(f.read())
    # skip initialspace True means that 
    # if any space b/w the comma and value are removed
    reader = csv.reader(file, skipinitialspace=True)
    print(reader)
    for row in reader:
        # Every row is a list
        print(row)

# Reading from CSV files (as dicts)
with open('demo_csv.csv') as file:
    # print(f.read())
    # skip initialspace True means that 
    # if any space b/w the comma and value are removed
    reader = csv.DictReader(file, skipinitialspace=True)
    print(reader)
    for row in reader:
        # Every row is a list
        print(row)



# Writing to CSV files
with open('marks.csv','w', newline='') as fw:
    writer =  csv.writer(fw)
    writer.writerow(["roll_no","marks"])
    writer.writerow([1,100])
    writer.writerow([2,200])
    writer.writerow([3,300])


