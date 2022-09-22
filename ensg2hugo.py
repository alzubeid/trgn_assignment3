%%file ensg2hugo.py
import sys
import fileinput
import re
import numpy as np 
import pandas as pd

#creating a dictionary
Lookup_gene={}

my_dict_file= sys.argv[1]
Lookup_gene={}
for each_line_of_text in fileinput.input("trgn_assignment3/Homo_sapiens.GRCh37.75.gtf"):
    gene=re.findall(r'^.*?\t.*?\t(gene)t', each_line_of_text, re.I)
    gene_ID=re.findall(r'gene_id "(ENSG\d*?)"', each_line_of_text, re.I)
    gene_name=r.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)
    homo_sapiens_split= re.split('\t', each_line_of_text)
    if gene:
        if gene_name:
            Lookup_gene[gene_id[0]] = gene_name[0]
 

    if sys.argv[1][:2]  == '-f':
        columnnumber = sys.arg[1][2]
        dataframe = sys.argv[2]
        column = int(columnnumber) - 1
    else: 
        column = 1
        data = sys.arv[1]
  
#Using Pandas
df = pd.DataFrame(raw_data, r)
df['gene_id'].replace(['gene_name'], inplace=True)
df

#Data_replaced = data.rename(columns = {'gene_id' : 'gene_name'}
 #                      print (Data_replaced)
