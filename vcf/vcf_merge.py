#!/usr/bin/env python
import sys
import os
import pandas as pd
from glob import glob
def vcf_merge(path,par1,par2,output):
  #     path="~/program/LAxMol_v1_SNP/v1/nnxnp_llxlm"
        os.system('cd %s'%(path))
        fil_st=glob("*.vcf")
        for file_n in fil_st:
                if par1 in file_n:
                        n_list=file_n.split('.')
                        col_n=n_list[0].rstrip()
                        P1=pd.read_table(file_n)
                elif par2 in file_n:
                        n_list=file_n.split('.')
                        col_n=n_list[0].rstrip()
                        P2=pd.read_table(file_n)
	try:
        	Par_mtr=pd.merge(P1,P2,on=['Locus','Position'],how='outer').fillna('././././').sort_values(by=['Locus','Position'])
	except:
        	Par_mtr=P1
        for file_n in fil_st:
        	if par1 not in file_n and par2 not in file_n:
                        n_list=file_n.split('.')
                        fcol_n=n_list[0]
                        F1=pd.read_table(file_n)
                        Par_mtr=pd.merge(Par_mtr,F1,on=['Locus','Position'],how='outer').fillna('././././').sort_values(by=['Locus','Position'])
        Par_mtr.to_csv(output,sep='\t',index=False)
if __name__ == '__main__':
	from optparse import OptionParser
	ms_usage='python %prog [-f] File_path [-P1] Parent1 [-P2] Parents [-o] output.file'
	descr='Use this script to merge the vcf genotype files which separate called in the process'
	optpar=OptionParser(usage=ms_usage,description=descr)
	optpar.add_option('-f', '--file_path',dest='path',
			  help='Input your absolute path where prepared vcf_file for merging')
	optpar.add_option('-p','--Parent1',dest='par1',
			  help='Input a key word include in your parent 1 vcf file name')
	optpar.add_option('-m','--Parent2',dest='par2',
			  help='Input a key word include in your parent 2 vcf file name, if you just have one parent, please input a key word not in all vcf files')
	optpar.add_option('-o','--output.file',dest='output',
			  help='preparing a filename to save your merged result')
	options,args=optpar.parse_args()
	path=options.path
	par1=options.par1
	par2=options.par2
	output=options.output
	vcf_merge(path,par1,par2,output)
