
Trgn_assignment3

Usage:
1)	Extract phone number from text file, 2) Lookup gene name (replace Ensembl with HUGO name) 3) Develop a histogram from data set.

Description:
1) Run the program as follows: type git clone https://github.com/alzubeid/trgn_assignment3.git 2) Run in the terminal; install all files in the same folder.  3) Will need to search the gene_name in Homo_sapiens.  This file to be accessed as wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz.  The file need to be unzipped with gunzip Homo_sapiens.GRCh37.75.gtf. 4) Will create a dictionary that matches the Ensemble names with the HUGO names.  5) The column number need to be -f.

Known Issues:
for the ensg2hugo.py: error obtained when attempting to use the unziped file (using gunzip).  This in turn is not allowing the dictionary to utilize the information to run the second part (matching the Ensemble name with the HUGO name.

![image](https://user-images.githubusercontent.com/112045479/191456791-cfeedef1-5c8f-417c-be56-feea6cd59fee.png)
