#!/usr/bin/env python
import sys
def aq_antisense_strand(line):
	'''convert the nuclear strand to antisense strand'''
	list_anti=[]
	for i in line:
		if i =='A':
			list_anti.append('T')
		elif i=='T':
			list_anti.append('A')
		elif i =='G':
			list_anti.append('C')
		elif i =='C':
			list_anti.append('G')
		elif i =='N':
			list_anti.append('N')
	return ''.join(list_anti)

def fasta_to_dict(genome_fa):
	fasta_seq=open(genome_fa)
	fasta_line=fasta_seq.readline()
	fasta_dict={}
	while fasta_line:
		if '>' in fasta_line:
			key = fasta_line.rstrip()
			fasta_line=fasta_seq.readline()
			value_seq=''
			while fasta_line:
				if '>' not in fasta_line:
					value_seq += fasta_line.rstrip()
					fasta_line=fasta_seq.readline()
           	 		else:
		 	 		fasta_dict[key]=value_seq	
               		 		break
		else:
            		fasta_line=fasta_seq.readline()
    	return fasta_dict

def splice_specific_site_seq(seq,start,end):
	seq_fa=seq[start:end+1]
	return seq_fa
def get_info_gff(gff,genome_fa,out_file):
	file1=open(gff,'r')
	file2=open(out_file,'w')
	for gf_line in file1:
		if 'gene	' in gf_line:
			gf_line_list=gf_line.split('\t')
			scaf_id='>'+gf_line_list[0].rstrip()
			start=int(gf_line_list[3].rstrip())
			end=int(gf_line_list[4].rstrip())
			strand=gf_line_list[6].rstrip()
			gf_line_list2=gf_line_list[8].split(';')
			gene_id='>'+gf_line_list2[0].rstrip()[3:]
			fa_dict=fasta_to_dict(genome_fa)
			seq_fa=fa_dict[scaf_id]
			gene_seq=splice_specific_site_seq(seq_fa,start,end)
			if strand=='+':
				file2.write(gene_id+'\n')
				file2.write(gene_seq+'\n')
			elif strand=='-':
				file2.write(gene_id+'\n')
				neg_stand_seq=aq_antisense_strand(gene_seq)
				file2.write(neg_stand_seq+'\n')
	file2.close()
if __name__ == '__main__':
	from optparse import OptionParser
	ms_usage='usage:%prog [-g] gff.file [-f] fasta.file [-o] out.fa'
    	descr='''use this script to according to  the gene-id to find the corresponding sequences from fasta.file base on the position and antisense/positive-strand descripted in gtf.file.'''
    	optpar=OptionParser(usage=ms_usage,description=descr)
    	optpar.add_option('-g','--gff.file',dest='gff_file',
                      help='input the anotition-file(filename.gff).')
    	optpar.add_option('-f','--genome.fa',dest='fasta_seq',
                      help='input the genome-fasta that comtained the whole sequences')
	optpar.add_option('-o','--out.fa',dest='out_fa',
			  help='please define a filename to place your result seq')
    	options,args=optpar.parse_args()
	out_file=options.out_fa
    	gff=options.gff_file
    	genome_fa=options.fasta_seq
	get_info_gff(gff,genome_fa,out_file)
					
				
