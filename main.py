import sys

from get_data import get_data_homology,get_data_genome
from process_data import create_data_homology_ls
from req_data import download_data_h_post
from save_data import write_dict_json,write_file_multiple_json

arg=sys.argv
arg=arg[1:]

if len(arg)!=5:
    print("No. of arguments more or less. Please check")
    sys.exit(1)

a=[]
d={}
a_h=[]
d_h={}
ld=[]
ldg=[]
dir_g="data"

ld,ldg,a,d=get_data_genome(arg,dir_g,a,d,ld,ldg)
#print(a[0][0:10],"\n",d,"\n",ld[0][0:10],"\n")
dir_hom="data_homology"

a_h,d_h=get_data_homology(arg,dir_hom,a_h,d_h)
#print(a_h[0][0:10],"\n",d_h)

print("Data Read")

n=2 #no. of numbers neighbors

lsy,lcmap=create_data_homology_ls(a_h,d_h,n,a,d,ld,ldg)

print(len(lsy))

print("Neighbor Genes Found")

"""
print(lsy,"\n",lcmap)
lt=ldg[0]
for x in lsy:

    xr=lsy[x]['f']
    xl=lsy[x]['b']
    for g in range(len(xl)-1,-1,-1):
        print(a[0].iloc[lt[xl[g]],[3,4]])
    print("------------------\n",a[0].iloc[lt[x],[3,4]],"\n-------------------")
    for g in xr:
        print(a[0].iloc[lt[g],[3,4]])"""

seq_j,gmapseq=download_data_h_post(lsy)

print(len(seq_j),"\t",type(seq_j),"\t",len(gmapseq))

save_data_dir="processed"

write_dict_json("lcmap",save_data_dir,lcmap)
write_dict_json("gmapseq",save_data_dir,gmapseq)
write_file_multiple_json("neighbor_genes",save_data_dir,lsy)
write_file_multiple_json("gene_seq",save_data_dir,seq_j)
