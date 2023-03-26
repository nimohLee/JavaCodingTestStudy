envelope = 10000
envelope2 = 20000
envelope3 = "hi"
print(envelope)
print(envelope2)
print(envelope3)

# 형변환
print(int('2'))
print(float('1.5'))
print(int(float('1.7')))
print(str(2))
print(bool('hello')) #True
print(bool('   ')) #True
print(bool('')) #False
print(bool(1)) #True
print(bool(-2)) #True
print(bool(0)) #False
print(bool(None)) #False

#산술 연산자

#논리 연산자
print(2>1 and 1>5) #False
print(2>1 or 1>5) #True
# 멤버 연산자
  # in
print('c' in 'cat')
  # not in
print('z' not in 'cat')

# 주석
# 한줄 주석
''' 여러 줄 주석
  이것이 됩니다.
'''

# 인덱스와 슬라이싱
ex = 'python'
print(ex[0]) # p
print(ex[5]) # n
print(ex[0:2]) # py
print(ex[-1]) # n
print(ex[:]) # python
print(ex[3:]) # hon
print(ex[:4]) # pyth

# 문자열 처리
  # 문자열 더하기
snack = '꿀꽈배기'
two = '2개'
juseyo = snack + two
juseyo += '주세요'
print(juseyo)
  # 문자열 길이
print(len(juseyo))
  # 여러줄 문자
multi_line = '''꿀꽈배기는
너무
맛있어요
'''
print(multi_line)

# 메소드
  # 문자열 메소드
    # 모두 소문자로
letter = 'how are YOU?'
print(letter.lower())

    # 모두 대문자로
print(letter.upper())

    # 첫 글자만 대문자로
print(letter.capitalize())

    # 각 단어들의 첫 글자만 대문자로 
print(letter.title())

    # 대소문자 뒤바꾸기
print(letter.swapcase())

    # 문자열 나누기
print(letter.split())

    # 단어가 몇번 쓰였는지?
print(letter.count('how'))

    # 문자열이 해당 단어로 시작하는지?
print(letter.startswith('how')) # return Bool 

    # 문자열이 해당 단어로 끝나는지?
print(letter.endswith('?')) # return Bool

    # 앞 뒤로 불필요한 부분 제거
s = '...나도고등학교...'
b = '   나도고등학교   '
print(s.strip('.')) # 나도고등학교
print(b.strip(' ')) # 아무것도 넣지 않으면 공백제거 -> 나도고등학교

    # 문자 치환
s1 = '나도고등학교'
print(s1.replace('고등학교','고교')) # 나도고교

    # 특정 글자 찾기
print(s1.find('학교')) # 인덱스 기준 위치 찾아줌. 현재 예시에서는 4

    # 다른 문자들 사이에 가운데로
print(s1.center(10,'-')) # 10글자만큼 기존 문자열 앞 뒤로 '-'로 채움

# 문자열 포맷
python = '파이썬'
java = '자바'
  # 문자열 출력
print('지금 배우는 건'+python+'입니다. '+java+'가 아닙니다.')
print('지금 배우는 건',python,'입니다. ',java,'가 아닙니다.')
print('지금 배우는 건 {}입니다. {}가 아닙니다.'.format(python, java))
print('지금 배우는 건 {1}가 아닙니다. {0}입니다.'.format(python, java))
print(f'지금 배우는 건 {java}가 아닙니다. {python}입니다.')

# 따옴표 문제
#print(''속으로 생각했다'') -> 에러 발생
print("하지만 '속으로 생각했다..'")
'''print("하지만 '나만 당할 수 없지'라는 생에 " 엄청 !@#@!#"") -> 에러발생 문자열 따옴표안에 동일한 따옴표가 있으면 안됨'''

  # 탈출 문자
print('하지만 \'나만 당할 순 없지\'라는 생각에 \"엄청 쉽지\" 라고 했다.')
print('\\로 역슬래시') # \
print('꿀꽈배기는\n너무\n맛있다')

# 리스트1
my_list = ['오예스','몽쉘','초코파이']
my_list_dup = ['오예스','몽쉘','초코파이', '초코파이', '초코파이'] # 중복 허용
your_list = [1,2,3.14,True,False,'아무거나'] # 뭐든 지 가능
empty_list = [] # 빈 리스트 간으
print(my_list)
print(my_list_dup)
print(your_list)
print(empty_list)

# 리스트2
  # 인덱스
print(my_list[0]) # 순서가 존재하기 때문에 인덱스로 접근 가능
  # 슬라이스
print(my_list[0:2]) # ['오예스', '몽쉘']
  # in : 포함
print('몽쉘' in my_list) # True
  # len() : list 갯수
print(len(my_list)) # 3
  # 리스트 수정
my_list[1] = '몽쉘카카오' # 값 수정
print(my_list)
  # 제일 뒤에 값 추가
my_list.append('빅파이') # 값 추가
print(my_list)
  # 제일 뒤에 값 삭제
my_list.remove('오예스')
print(my_list)
  # 다른 리스트와 합치기
my_list.extend(your_list)
print(my_list)

# 튜플 : 수정 불가 (읽기 전용 리스트) -> 수정 메서드는 없고 나머지는 리스트와 메서드 동일.
튜플 = ('값1','값2')
 
my_tuple = ('오예스','몽쉘','초코파이') # 패킹
(pie1, pie2, pie3) = my_tuple # 언패킹
numbers = (1,2,3,4,5,6,7,8,9,10)
(one, two, *others) = numbers
(*others2, nine, ten) = numbers
print(others)
print(others2)

# 세트(set) : 집합 -> 순서X, 중복X
A = {'돈가스','보쌈','제육덮밥'}
B = {'짬뽕','초밥','제육덮밥'}
  # 교집합 
print(A.intersection(B))
  # 합집합
print(A.union(B))
  # 차집합
print(A.difference(B))
  # 값 추가
A.add("김밥")
  # 값 제거
A.remove("제육덮밥")
print(A)
  # 모든 값 삭제
A.clear()
print(A)
  # 자료형 삭제
del A

# 딕셔너리 (사전형) key : value
딕셔너리 = {'key1':'value1', 'key2':'value2'}
print(딕셔너리)
person = {'이름':'나귀욤','나이':7,'키':120,'몸무게':23}
  # key에 해당하는 value 확인
print(person['이름']) # 나귀욤
print(person['나이']) # 7
# print(person['별명']) -> 없는 키 값이므로 에러 발생
print(person.get('별명')) # 에러는 발생하지 않고 None이 반환됨
print(person.get('이름'))
print(person.get('나이'))
  # 새로운 데이터를 추가
person['최종학력'] = '유치원'
  # 이미 존재하는 key의 값 변경
person['키'] = 130
  # 이미 존재하는 여러 key의 값 변경
person.update({'키':140,'몸무게':30})
  # 특정 key:value를 삭제하려면?
person.pop('몸무게')
  # 어떤 key 들이 있는지?
print(person.keys())
  # 어떤 value 들이 있는지?
print(person.values())
  # 어떤 key:value 들이 있는지?
print(person.items())
print(person)
  # in : key가 딕셔너리에 포함하고 있는지
print('키' in person)
  # 모든 데이터 삭제
# person.clear()

# 자료형 변환
  # tuple을 수정하고 싶을 때 리스트로 변환
tup = ('오예스','몽쉘')
lit = list(tup)
lit.append('초코파이')
tup = tuple(lit)
print(tup)
  # 리스트의 중복을 제거하고 싶을 때
my_dic = dict.fromkeys(my_list_dup) # 딕셔너리는 key의 중복을 허용하지 않으며 순서가 있다.
print(my_dic)
my_list_dup = list(my_dic) # 딕셔너리를 리스트로 변환하는 경우 key를 모두 가져옴
print(my_list_dup)

# 조건문
today = '일요일'
if today == '일요일':
    print('게임 한판')
else: 
    print('바로 공부')

# 반복분
'''
  for 변수 in 반복 번위 또는 대상:
    반복 수행 문장
'''
for x in range(10): # range는 0~9까지 만들어줌
  print(f'팔 벌려 뛰기 {x}회')

# range()
# range(stop) : range(5) 0이상 5미만 -> 0,1,2,3,4
# range(start, stop) : range(1,5) 1이상 5미만 -> 1,2,3,4
# range(start, stop, step) : range(1,10,2) 1이상 10미만 2 만큼 증가-> 1,3,5,7,9

# 반복문 활용
# 반복 대상을 활용하여 반복 : 리스트, 튜플, 딕셔너리 (순서가 있음)
  # 리스트
for_list = [1,2,3]
for x in for_list:
  print(x)


  # 딕셔너리
    # 키만 반복
for k in person.keys():
  print(k)
    # 값만 반복
for v in person.values():
  print(v)
    # 키와 값 반복
for k,v in person.items():
  print(k,v)   

  # 문자열
fruit = 'apple'
for x in fruit:
  print(x)

# while : 조건이 참인 동안 계속 반복


# 리스트 컴프리헨션
# new_list = [변수 활용 for 변수 in 반복대상 if 조건]
com_list = [1,2,3,4,5]
new_list = [x for x in com_list if x>3]
new_list2 = [x+1 for x in com_list if x>3]
new_list3 = [x*3 for x in com_list if x>3]
new_list4 = [str(x)+'번째' for x in com_list if x>3]
print(new_list)
print(new_list2)
print(new_list3)
print(new_list4)

# 함수
  # def 함수명():
def show_price(customer):
  print(f'{customer} 고객님')
  print('감성 커트 가격은 15000원입니다.')
show_price("이호민")

  # 반환값
def get_price():
  return 15000
price = get_price()
print(f'커트 가격은 {price}원입니다')

def get_price2(is_vip):
  if is_vip == True:
    return 10000
  else:
    return 15000
price2 = get_price2(True)
print(price2)
  # 기본값
'''def 함수명(전달값=기본값):
  수행할 문장'''
def get_price_default(is_vip=False):
  if is_vip == True:
    return 10000
  else:
    return 15000

  # 키워드값
def get_price_keyword(is_vip=False,
                      is_birthday=False,
                      is_membership=False,
                      card=False,
                      review=False,
                      first_time=False
                      ):
  print('hi')
get_price_keyword(review=True, is_birthday=True)

  # 가변인자 : 가변인자는 마지막에 딱 한 번만
def visit(today, *customers):
  print(today)
  for customer in customers:
    print(customer)

# 사용자 입력 : 무조건 문자열이 들어옴
name = input('안녕하세요?')

# 파일 입출력
  # 쓰기 모드
f = open('list.txt','w',encoding='utf8')
f.write('김xx\n')
f.write('정xx\n')
f.write('허xx\n')
f.close()
  # 읽기 모드
r = open('list.txt','r',encoding='utf8')
contents = r.read()
print(contents)
r.close()

# 클래스
class Aclass:
  def __init__(self, name, price): # 생성자
    self.name = name
    self.price = price
  
  def set_travel_mode(self):
    print('여행 모드 ON')
  
  # self
  '''
  self 는 객체 자기 자신  
  '''
  
  # 상속
class BlackBox:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class TravleBlackBox(BlackBox): # 상속
  def set_travel_mode(self,min):
    print(str(min) + '분 동안 여행 모드 ON')      

# 예외처리
'''
try:
  수행 문장
except:
  에러 발생 시 수행 문장
else:
  정상 동작 시 수행 문장
finally:
  마지막으로 수행할 문장
'''