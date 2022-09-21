#creating a folder 'extract_phonenum.py'
import os

path = "trgn_assignment3/extract_phonenum.py"

if not os.path.exists(path):
    os.makedirs(path)
#else: 
    print ("folder already exists") 
    
# creating a textfile named 'textfile.txt' that contains my phone number.     
f = open ('trgn_assignment3/extract_phonenum.py/mytextfile.txt', 'r+')

print (f.name)

#creating a pattern to read the telephone number in the file (mytextfile)
pattern = re.compile (r'[(][\d]{2}[)][\d]{3}-[\d]{3}-[\d]{4}')
mytextfile = re.findall(pattern, text)
mytextfile
