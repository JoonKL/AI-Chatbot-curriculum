# ### 1 ~30 변수와 데이터 타입
# #1
# print('Hello World')
# #2
# print("Mary's cosmetics")
# #3
# print('신씨가 소리질렀다. "도둑이야"')
# #4
# print("""C:\\Windows""")
# #5
# print("안녕하세요.\n 만나서\t\t반갑습니다.")
# #\n줄바꾸기 \t들여쓰기
# #6
# print("오늘은","일요일")
# # #7
# print('naver;'+'kakao;'+'sk;'+'samsung;')
# print('naver','kakao','sk','samsung', sep=';')
# #8
# print("""naver/kakao/sk/samsung""")
# #9
# print("first",end=' ');print("second")
# #10
# string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
# print(len(string))
# #11
# a="3";b="4"
# print(a+b)
# #34(문자열)
# #12
# s="hello";t="python"
# print(s+"! "+t)
# #13
# print("Hi" * 3)
# #Hi 가 연달아 세번 출력 예상.
# #14
# print('-'* 80)
# #15
# t1 = 'python'
# t2 = 'java'
# print((t1+t2)*4);
# #16
# print(20000*10)
# #17
# 2 + 2 * 3
# #8
# #18
# a=128
# print(type(a))
# a="132"
# print(type(a))
# #""로 써있기떄문에 문자열
# #19
# num_str ='720'
# num=int(num_str)
# print(type(num))
# #20
# num=100
# num_s =str(num)
# print(type(num_s))
#
# #21
# lang = 'python'
# print(lang[0],lang[2])
# #22
# license_plate = "24가 2210"
# print(license_plate[4:])
# #23
# string="홀짝홀짝홀짝"
# print(string[0::2])
# #24
# string="PYTHON"
# print(string[::-1])
# #25
# phone_number = "010-1111-2222"
# phone_number = phone_number.replace('-', ' ')
# print(phone_number)
# #27
# url= "http://sharebook.kr"
# print(url[-2:])
# #28
# # 리스트가 아니기때문에 오류가 난다.
# # lang = 'python'
# # lang[0] = 'P'
# # print(lang)
# #29
# string='abcdef2a354a32a'
# print(string.replace('a', 'A'))
# #30
# string = 'abcd'
# string = string.replace('b', 'B')
# print(string)
# #b가 B로 변경된다.
# ### 1 ~30 변수와 데이터 타입
# #41
# movie_rank = ['닥터스트레인지', '스플릿','럭키']
# print(movie_rank)
# #42
# movie_rank.append('배트맨')
# print(movie_rank)
# #43
# movie_rank.insert(1,'슈퍼맨')
# print(movie_rank)
# #44
# movie_rank.remove('럭키')
# print(movie_rank)
# #45
# del movie_rank[2:]
# print(movie_rank)
# #46
# lang1 = ["C","C++","JAVA"]
# lang2 = ["Python","Go","C#"]
# langs = lang1 + lang2
# # print(lang)
# #47
# nums = [1,2,3,4,5,6,7]
# print(max(nums))
# print(min(nums))
# #48
# nums = [1,2,3,4,5]
# print(sum(nums))
# #49
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))
# #50
# nums = [1,2,3,4,5]
# print(sum(nums)/len(nums))
# #51
# price = ['20180728',100,130,140,150,160,170]
# print(price[1:])
# #52
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums[0::2])
# #53
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums[1::2])
# #54
# nums = [1,2,3,4,5]
# print(nums[::-1])
# #55
# interest = ['삼성전자','LG전자','Naver']
# print(interest[0],interest[2])
# #56
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))
# #57
# print('/'.join(interest))
# #58
# print('\n'.join(interest))
# #59
# string = "삼성전자/LG전자/Naver"
# interest = [string[0:4], string[5:9], string[10:15]]
# print(interest)
# #60
# string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
# interest = string.split('/')
# print(interest)
# #61
# interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
# interest_1 = interest_0
# interest_1[0] = 'Naver'
# print(interest_0)
# #삼성전자가 Naver로 변경될 것
# #62
# interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
# interest_1 = interest_0[:2]
# interest_1[0] = 'Naver'
# print(interest_0)
# #그냥 interest_0 함수가 출력
# #63
# my_variable=()
# #64
# #튜플은 값을 변경불가능하다.
# #65
# num_65=(1,)
# #66
# t = 1,2,3,4
# print(type(t))
# #67
# t = ('a','b','c')
# #튜플은 값을 변경할 수가 없기때문에 리스트로변경 후 변경하던가 새로선언하던가해야한다.
# #68
# interest = ('삼성전자','lg전자','SK Hynix')
# interest2 = list(interest)
# print(interest2)
# #69
# interest3 = ['삼성전자,','LG전자','SK Hynix']
# interest4 = tuple(interest3)
# #70
# my_tuple = (1,2,3)
# a,b,c=my_tuple
# print(a+b+c)
#
# #71
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_scores,a,b=scores
# print(valid_scores)
# *valid_scores2,_,_=scores
# print(valid_scores2)
# #72
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b,*valid_scores3=scores
# print(valid_scores3)
# _,_,*valid_scores4=scores
# print(valid_scores4)
# #73
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _,*valid_scores5,_=scores
# #74
# temp ={}
# print(type(temp))
# #75
# icecream = {'메로나':1000,'폴라포':1200,'빵빠레':1800}
# print(icecream)
# #76
# icecream['죠스바']=1200
# icecream['월드콘']=1500
# print(icecream)
# #77
# print('메로나 가격:',icecream['메로나'])
# #78
# icecream['메로나']=1300
# print(icecream)
# #79
# del icecream['메로나']
# print(icecream)
# #80
# #누가바 라는 값이 딕셔너리에 존재하지않는다.
# #81
# inventory={}
# inventory={'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}
# print(inventory)
# #82
# print(inventory['메로나'][0],'원')
# #83
# print(inventory['메로나'][1],'개')
# #84
# inventory['월드콘']=[500,7]
# print(inventory)
# #85
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(list(icecream.keys()))
# #86
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(list(icecream.values()))
# #87
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(sum(icecream.values()))
# #88
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)
# #89
# keys= ('apple','peach','pear')
# vals = (300, 250, 400)
# dict1=dict(zip(keys,vals))
# print(dict1)
# #90
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))
# print(close_table)
# #91
# #파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# #bool데이터타
# #92
# print(3 == 5)
# #False 가 출력될듯
# #93
# print(3<5)
# #True 가 출력될듯
# #94
# x=4
# print(1<x<5)
# #True가 출력될듯
# #95
# print((3==3) and (4!=3))
# #True가 출력될듯
# #96
# #=>가 아니라 >=로 입력해야한다
# #97
# if 4<3:
#     print("Hello World")
# #False이기때문에 출력이 안됨
# #98
# if 4<3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
# #4가3보다 작지않으므로 Hi there이 출력된다.
# #99
# if True:
#     print("1")
#     print("2")
# else:
#     print("3")
# print("4")
# #True 이므로 1과 2가 출력되고 이후 조건문 밖인 4가 출력된다.
# #100
# if True:
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else:
#     print("4")
# print("5")
# #True이므로 3이 출력되고 조건문 밖인 5가 출력된다.
#101
a = input()
print(a*2)
#102
print("숫자를 입력하세요:")
b=int(input())
print(b+10)
#103
c = int(input())
if c % 2 == 0:
    print("짝수")
else:
    print("홀수")
#104
x = int(input("입력값:"))
if x+20 > 255:
    x = 255
else:
    x =x+20
print("출력값:",x)
#min함수를 이용하기
y= int(input("입력값:"))
print("출력값:",min(y+20,255))
#105
x = int(input("입력값:"))
if x-20>0:
    x = x-20
else:
    x =0
print(x)
x = int(input("입력:"))
print("출력:",max(x-20, 0))
#106
time = input("현재시간:")
if time[3:]=="00" :
    print("정각")
else:
    print("정각이 아님")
#107
fruit=["사과","포도","홍시"]
f=input("좋아하는과일은?")
if f in fruit:
    print("포함")
else:
    print("포함하지않음")
#108
warn_investmen_list =["Microsoft","Google","Naver","Kakao","Samsung","LG"]
w =input("투자경고종목 확인")
if w in warn_investmen_list:
    print("투자경고종목입니다")
else:
    print("투자경고종목이 아닙니다")
#109
fruit={"봄":"딸기","여름":"토마토","가을":"사과"}
a=input("좋아하는계절은:")
if a in fruit.keys():
    print("정답입니다")
else:
    print("오답입니다")
#110
fruit={"봄":"딸기","여름":"토마토","가을":"사과"}
b=input("좋아하는과일은?")
if b in fruit.values():
    print("정답입니다")
else:
    print("오답입니다.")
#111
a=input()
if a.islower():
    a = a.upper()
else:
    a = a.lower()
print(a)
#112
score = int(input("점수입력:"))
if score>80:
    print("성적은 A")
elif score>60:
    print("성적은 B")
elif score>40:
    print("성적은 C")
elif score>20:
    print("성적은 D")
else:
    print("성적은 E")
#113
money = input("돈입력").split()
a = money[0]
b = money[1]
if b == "달러":
    c = 1167
elif b =="엔":
    c=1.096
elif b == "유로" :
    c = 1268
else:
    c = 171
print(c*int(a),"원")
#114
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = max(num1, num2,num3)
print(num4)
#115
phone = input()
if phone[:3] =="011":
    print("skt")
elif phone[:3] =="016":
    print("kt")
elif phone[:3]=="019":
    print("lgt")
else:
    print("알수없음")
#116
num = input()
if num[2] == "012":
    print("강북구")
elif num[2]=="345":
    print("도봉구")
else:
    print("노원구")
#117
a = input()
if a[7] == "1":
    print("남자")
elif a[7]=="3":
    print("남자")
else:
    print("여자")
#118
num = input()
if int(num[8:9]) <=8:
    print("서울")
else:
    print("부산")
#119
#120
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
volatility = int(btc['max_price']) - int(btc['min_price'])
if int(btc['opening_price']) + volatility > int(btc['max_price']) :
    print("상승장")
else :
    print("하락장")
#121
for 변수 in ["가", "나", "다", "라"]:
    print(변수)
#네번
#122
for 변수 in ["사과", "귤", "수박"]:
    print(변수)
#사과 귤 수박이 나온다
#123
#사과 귤 수박이 차례로 나오고 중간에 --가 출력된다(for문)
#124
#사과 귤 수박이 차례로 출력되고 마지막줄에 --가 출력된다
#125
menu = ["김밥","라면","튀김"]
for i in menu:
    print("오늘의 메뉴:"+i)
#126
porfolio = ["sk하이닉스","삼성전자","LG전자"]
for i in porfolio:
    print(i+ ' 보유중')
#127
pets = ['dog','cat','parrot','squirrel','goldfish']
for i in pets:
    print(i,len(pets))
#128
prices = [100,200,300]
for i in prices:
    print(i+10)
#129
prices = ["129,300","1,000","2,300"]
for i in prices:
   a=i.replace(',','')
   print(int(a))
#130
menu = ["면라","밥김","김튀"]
for i in menu:
    print(i[::-1])
#131
my_list = ["가","나","다","라"]
for i in my_list[1:]:
    print(i)
#132
my_list =[1,2,3,4,5,6]
for i in my_list[0::2]:
    print(i)
#133
my_list=[1,2,3,4,5,6]
for i in my_list[1::2]:
    print(i)
#134
my_list=["가","나","다","라"]
for i in my_list[::-1]:
    print(i)
#135
my_list =[3,-20,-3,44]
for i in my_list:
    if i<0:
        print(i)
#136
my_list=[3,100,23,44]
for i in my_list:
    if i %3 ==0:
        print(i)
#137
my_list=["i","study","python","language","!"]
for i in my_list:
    if len(i) >3:
        print(i)
#138
my_list = [3,1,7,10,5,6]
for i in my_list:
    if i>5 and i<10:
        print(i)
#139
my_list=[13,21,12,14,30,18]
for i in my_list:
    if i>10 and i<20 and i%3==0:
        print(i)
#140
my_list = [3,1,7,12,5,16]
for i in my_list:
    if i % 3 ==0 or i % 4 ==0:
        print(i)
#141
my_list = ["A","b","c","D"]
for i in my_list:
    if i.isupper():
        print(i)
#142
my_list = ["A","b","c","D"]
for i in my_list:
    if i.islower():
        print(i)
#143
#upper(), lower() isupper(), islower() !
my_list =["A","b","c","D"]
for i in my_list:
    if i.isupper():
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')
#144
file_list = ['hello.py','ex01.py','ch02.py','intro.hwp']
for i in file_list:
    a=i.split('.')
    print(a[0])
#145
filenames =['intra.h','intra.c','define.h','run.py']
for i in filenames:
    if i.split('.')[1]== "h":
        print(i)
#146
filnames = ['intra.h','intra.c','define.h','run.py']
for i in filenames:
    if i.endswith(("h","c")):
        print(i)
#endswith!!! 튜플로 여러개의 확장자 전달가능
#147
my_list =[3,-20,-3,44]
newlist =[]
for i in my_list:
  if i >0:
    newlist.append(i)
    print(i)
#148
my_list=["A","b","c","D"]
upper_list=[]
for i in my_list:
    if i.isupper():
        upper_list.append(i)
#149
my_list = [3,4,4,5,6,6]
sole_list=[]
for i in my_list:
    if i not in sole_list:
        sole_list.append(i)
print(sole_list)
#150
my_list=[3,4,5]
a = 0
for i in my_list:
    a += i
print(a)
#162
class Human:
    def Human(self):
        return "응애응애"
areum = Human()
areum.Human