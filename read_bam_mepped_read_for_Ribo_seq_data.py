import pysam
import os
import sys



bamfile = ['Jan_accepted_hits.bam']


for bam in bamfile:
	#print(bam)
	counter=0
	read_count = open(bam+'.tab','w')
	samfile = pysam.AlignmentFile(bam, "rb")
	cds_file= open('selected_CDS_info.tab','r')
	for line in cds_file:
		print(line)
		line = line.split('\t')
		#print(len(line))
		steps = (len(line)-5)/2
		print(steps)
		loop_step = int(steps)
		start_position = 5
		end_position = 6
		chr = line[1]
		if chr == 'chrmt':
			continue
		read_count.write(line[0]+'\t'+line[3]+'\t')
		b = 0
		for loops in range(loop_step):
			#print('loop')
			start =int(line[start_position])
			#print('start',start)
			stop = int(line[end_position])
			#print('stop',stop)
			n = 0
			counter+=1
			while start <= stop:
				start1 = start-1
				#print(start)
				#print(start1)
				n = 0
				#a = 0
				for read in samfile.fetch(chr, start1, int(start)):
					#print(read)
					#print(read.reference_start)
					if str(start1) == str(read.reference_start):
						#print(read)
						n+=1
						#print(dt)
					#print(fddf)
					#n+=1
				#print(n)
				#print(a)
				#print(df)
				if steps == b:
					if start == stop:
						read_count.write(str(n)+'\n')
					else:
						read_count.write(str(n)+',')
				else:
					read_count.write(str(n)+',')
				start+=1
			start_position+=2
			end_position+=2
			b+=1
			sys.stdout.write("Line of cds file currently being parsed: {0}.\t\r".format(counter))
			sys.stdout.flush()
		read_count.write('\n')
		

	cds_file.close()
	samfile.close()
	read_count.close()
	#print(fxb)