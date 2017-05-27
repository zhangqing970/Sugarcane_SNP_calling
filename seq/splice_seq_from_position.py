#!/usr/bin/env python
def splic_seq_2(fa,r_id_,g_id_,position_1,position_2,strand):
    import sys
    import Anti_
#   sequence_file= open(options.fasta_seq)
    sequence_file=open(fa)
    seq_line= sequence_file.readline()
#   for seq_line in sequence_file: 
    if r_id_ in seq_line:
        splice_seq_name =seq_line.rstrip()+'\t'+g_id_+'\t'+position_1+'\t'+position_2+'\t'+strand 
        print splice_seq_name 
        seq_line= sequence_file.readline()
        tgt_line=''
	if strand=='+':
        	while seq_line:
            		if '>' not in seq_line:
                		tgt_line += seq_line.rstrip()
                		seq_line= sequence_file.readline()
            		else:
                		break
        	print tgt_line[int(position_1):int(position_2)]
	elif strand=='-':
		while seq_line:
			if '>'not in seq_line:
				anti_sline=Anti_.aq_antisense_strand(seq_line)
				tgt_line += anti_sline.rstrip()
				seq_line= sequence_file.readline()
			else:
				break
		tgt_line=tgt_line[::-1]
		print tgt_line[int(position_1):int(position_2)]
				
    else:
    	seq_line= sequence_file.readline()
    	while seq_line:
        	if '>' not in seq_line:
                		seq_line= sequence_file.readline()
            	else:
                	break
	
def splice_seq_1(gtf,id,fa):
    import sys
    gtf_content = open(gtf)
    ge_id=open(id) 
    for line in gtf_content:
        for g_id_ in ge_id:
            if g_id_.rstrip() in line:
                line_list = line.split('\t')
#		print line_list[0].rstrip(),line_list[3].rstrip(),line_list[4].rstrip()
                splic_seq_2(fa,line_list[0].rstrip(),g_id_.rstrip(),line_list[3].rstrip(),line_list[4].rstrip(),line_list[6].rstrip())
	ge_id.seek(0)
if __name__=='__main__':
    from optparse import OptionParser
    ms_usage='usage:%prog [-g] gtf.file [-i] gene-id.file [-f] fasta.file'
    descr='''use this script to according to  the gene-id to find the 
corresponding sequences from fasta.file base on the position and 
antisense/positive-strand descripted in gtf.file.'''
    optpar=OptionParser(usage=ms_usage,description=descr)
    optpar.add_option('-g','--gtf.file',dest='gtf_file',
                      help='input the anotition-file(filename.gtf).')
    optpar.add_option('-i','--gene-id.file',dest='Gene_id',
                      help='input the gene-id file contain the gene id which you want to extract.')
    optpar.add_option('-f','--genome.fa',dest='fasta_seq',
                      help='input the genome-fasta that comtained the whole sequences')
    options,args=optpar.parse_args()
    gtf=options.gtf_file
    id=options.Gene_id
    fa=options.fasta_seq
    splice_seq_1(gtf,id,fa) 
