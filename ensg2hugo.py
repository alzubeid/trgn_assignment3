%%file ensg2hugo.py
import sys
import fileinput
import re


#creating a dictionary

my_dict_file= sys.argv[1]
Lookup_gene={}
for each_line_of_text in fileinput.input("trgn_assignment3/Homo_sapiens.GRCh37.75.gtf"):
    gene_id = re.findall(r'gene_id "(ENSG\d*?)"', each_line_of_text, re.I)
    #print(gene_id)
    gene_name = re.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)
    #print(gene_name)
    if gene_id:
        if gene_name:
            Lookup_gene[gene_id[0]] = gene_name[0]
            #print(gene_id[0] + " : " + gene_name[0])
   

#Column option setup:
    if len(sys.argv) > 2:
        if sys.argv[1][:2]  == '-f':
        columnnumber = int(sys.argv[1][2]) - 1
        dataframe = sys.argv[2]
       
    else: 
        columnnumber = 0 #this is the first column (1-1=0)
        dataframe = sys.argv[1]
  
sample = open('final_expression_analysis', 'w')
input_file_to_change=sys.argv[2]
print('"","gene_id","gene_name","gene_type","logFC","AveExpr","t","P.Value","adj.P.Val"', file = sample)
for each_line_of_text in fileinput.input(input_file_to_change): 
    replacecolumn_array = re.replace(
