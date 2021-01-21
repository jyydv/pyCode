# w: 쓰기
f = open("d:/work/p/20210111/pyWritten.txt", 'r')
line_num = 1
line_data = f.readline()
while line_data:
	# print('%d'%line_num,'%s'%line_data)
	print('num %d text %s' %(line_num, line_data))
	line_data = f.readline()
	line_num += 1
f.close()
