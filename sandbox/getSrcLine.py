"""
sourceScarapping 이후에 특정 단어 검색시 미리 만들어 놓은 index 추출 파일에 기반해서
검색된 ilne 을 입력시 해당내용을 포함하는 파일을 반환 (단순 숫자 비교만 하면 될듯)

필요 로직 D:/tmp/scrap/scrap.ALL_Controller.index.groovy 등의 인덱스 파일 read
값 입력 대기후 이력된 number 값을 해당 파일의 라인 접두어 부분의 number 와 비교
입력된 값보다 큰 값이 나올때 까지 탐색하여 큰값이 나오면 비교한 값의 이전값이 반환되도록
이전라인의 내용을 버퍼에 저장한후,  해당 내용을 반환
"""

# w: 쓰기
f = open("d:/work/p/20210111/pyWritten.txt", 'w')
students = ['김철수', '최영', '한석규', '김태희']
for student in students:
	msg = student
	f.write(msg+"\n")
f.close()

