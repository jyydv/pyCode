# w: 쓰기
f = open("d:/work/p/20210111/pyWritten.txt", 'w')
students = ['김철수', '최영', '한석규', '김태희']
for student in students:
	msg = student
	f.write(msg+"\r")
f.close()