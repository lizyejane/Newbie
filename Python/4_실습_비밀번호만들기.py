'''
문제)
사이트별로 비밀번호를 생성하는 프로그램을 작성하세요.
http://naver.com
http://daum.net
http://google.com
http://youtube.com

조건)
http:// 부분은 제외한다.
처음 만나는 점(.)이후 부분도 제외한다.
남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e'의 개수 + '!'로 구성한다.
프로그램을 실행했을 때 실행결과는 다음과 같은 형태로 나와야한다.
    http://naver.com의 비밀번호는 nav51!입니다.
'''

url = "http://naver.com"
#url = "http://daum.net"
#url = "http://google.com"
#url = "http://youtube.com"

my_str = url.replace("http://", "")
#naver.com일 때 my_str.index(".")의 결과는 5
#따라서 다음 문장은 my_str = mystr[0:5]와 같음

my_str =my_str[:my_str.index(".")]   # 위에서 받은 my_str은 naver.com이고 naver.com 처음 ~ .이전까지인 naver 출력
print(my_str)                        # naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

'''
셀프체크)
영어 문장이 주어졌을 대 첫 번째 글자는 대문자로, 나머지 글자는 모두 소문자로 변환하는 프로그램을 작성하세요.

#주어진 문장 : 
# the early bird catches the worm.
# Actions speak louder than words.
# Practice makes perfact.'''

sentence = "the early bird catches the worm."
print(sentence[0].upper() + sentence[1:].lower())
