# trgn_assignment3

 Run the program as follows:
Type: git clone https://github.com/alzubeid/trgn_assignment3.git
2) Run in the terminal; install all files in the same folder

3) We will need to search gene_name in Homo_sapiens.GRCh37.75.gtf.  This file to be accessed as follows:
type: wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
then unzip the file with gunzip Homo_sapiens.GRCh37.75.gtf.gz
4) Will create a dictionary that matches the ENSEMBL names with the HUGO names.
5) The column number need to be -f

##Usage
-Requires use of:
fileinput
nupy
pandas
matplotlib

##Known Issues
For the ensg2hugo.py: error obtained when attempting to use the unziped file (using gunzip).  This in turn is not alloweing the dictionary to utilize the information to run the second part (matching the Ensemble name with HUGO name.
Furthermore, a unit test is not performed yet.
