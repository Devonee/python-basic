# -*- coding: utf-8 -*-
# title: class_SimpleChat.py
# author(s): Devonee (Hyemi Jo)
# date created: 2019-08-11
# description: creating a simple QnA sequence in Korean

import random

class Person:
    """대화 참여자를 나이와 예의바름(싸가지)으로 표현하는 클래스."""
    def __init__(self, age, manner):
        self.age = age
        self.manner = manner

class SimpleChat(Person):
    """Person의 인스턴스인 p1과 p2에 대해,
    p1이 p2에게 질문하고, p2가 p1에게 답변하는 예문으로 이루어진
    간단한 대화문을 반환하는 클래스.
    예문은 나이, 물리적 거리, 대화 참여자의 예의바름에 따라 달라질 수 있으며, 
    기본 꼴은 다음과 같다.
    "이/그/저것은 뭔가?" --> "이/그/저것은 사과다."
    """
    def __init__(self, p1, p2, d_pp, d_p1, d_p2): 
        self.p1 = p1 #대화 참여자 1
        self.p2 = p2 #대화 참여자 2
        self.d_pp = d_pp #p1과 p2 사이의 거리. 가깝0/멂1
        self.d_p1 = d_p1 #p1과 사과 사이의 거리. 가깝0/멂1
        self.d_p2 = d_p2 #p2와 사과 사이의 거리. 가깝0/멂1
        self.age_diff = self.p1.age - self.p2.age #p1과 p2의 나이 차이
    
    def demonstrative(self, p):
        """대화 참여자를 인수로 받고,
        (p1 혹은 p2)와 사과 사이의 거리에 따라 지시사(문자열)를 반환하는 함수.
        거리가 0이면 가깝고 1이면 멀다.
        """
        if (p == self.p1): #p1 기준
            if (self.d_p1 == 0): #자기에게 가깝
                return "이"
            elif (self.d_p2 == 0): #자기에게 멀고 상대에게 가깝
                return "그"
            else: #자기, 상대 모두 멂
                return "저"
        else: #p2 기준
            if (self.d_p2 == 0):
                return "이"
            elif (self.d_p1 == 0):
                return "그"
            else:
                return "저"
    
    def what(self):
        """p1가 p2에게 하는 질문의 일부(문자열)를 반환하는 함수
        p1의 예의바름, p1과 p2의 나이에 따라 내용 달라진다."""
        if (self.p1.manner): #p1이 예의바른 경우
            if (self.age_diff >= 0): #p1이 연상/동갑
                return "뭔가요?"
            else: #p2가 연상
                return "무엇입니까?"
        else: #p1이 무례한 경우
            if (self.age_diff >= 0): #p1이 연상/동갑
                return "뭐냐?" #"뭐냐?", "뭐야?", "뭔가?", "뭐지?"
            else: #p2가 연상
                return "뭐요?"

    def apple(self): #p2 -> p1에게 답변.
        """p2가 p1에게 하는 답변의 일부(문자열)를 반환하는 함수.
        p2의 예의바름, p1과 p2의 나이에 따라 내용 달라진다."""
        if (self.p2.manner): #p2가 예의바른 경우
            if (self.age_diff <= 0): #p2가 연상/동갑
                return "사과예요."
            else: #p1가 연상
                return "사과입니다."
        else: #p2가 무례한 경우
            if (self.age_diff <= 0): #p2가 연상/동갑
                return "사과잖아."
            else: #p1가 연상
                return "사과요."
    
    def rude(self):
        """p1과 p2가 모두 무례할 경우에만 무례한 말(문자열)을 반환하는 함수
        """
        if (self.p1.manner == 0) and (self.p2.manner == 0):
            rudewords = ["그걸 왜 나한테 묻는지, 원.", "묻긴 뭘 물어.", "거 보면 모르나?", 
            "눈깔이 제 구실을 못하는구만.", "귀찮게 정말.", "초면에 예의 없긴.", "말뽄새 하고는."]
            return random.choice(rudewords) + " "
        else:
            return ""

    def question(self):
        """p1이 p2에게 하는 질문(문자열)을 반환하는 함수.
        [지시사]게 [무엇인가?] 꼴.
        """
        q = f"{self.demonstrative(self.p1)}게 {self.what()}"
        return q
    
    def answer(self):
        """p2가 p1에게 하는 답변(문자열)을 반환하는 함수.
        [지시사]건 [사과다.] 꼴로, 해당 꼴 앞뒤에 [무례한 말] 올 수도 있음.
        """
        a1 = f"{self.rude()}{self.demonstrative(self.p2)}건 {self.apple()}"
        a2 = f"{self.demonstrative(self.p2)}건 {self.apple()} {self.rude()}"
        answers = [a1, a2]
        return random.choice(answers)
        
    def conv(self):
        """p1의 질문과 p2의 대답(문자열)을 한꺼번에 반환하는 함수.
        """
        return (self.question()+'\n'+self.answer())


#전치사 테스트
a = Person(20,0)
b = Person(25,0)
#def __init__(self, p1, p2, d_pp, d_p1, d_p2)
chats = [SimpleChat(a, b, 0, 0, 0), SimpleChat(a, b, 0, 0, 1), SimpleChat(a, b, 0, 1, 0), SimpleChat(a, b, 0, 1, 1), 
         SimpleChat(a, b, 1, 0, 0), SimpleChat(a, b, 1, 0, 1), SimpleChat(a, b, 1, 1, 0), SimpleChat(a, b, 1, 1, 1)]

print("======demonstrative======")
for chat in chats:
    print(chat.conv())
    print()

#말투 테스트
#1. manner x
chats = [SimpleChat(a, a, 0, 0, 0), SimpleChat(a, b, 0, 0, 0), SimpleChat(b, a, 0, 0, 0)]

print("======rude-동갑, p1연상, p2연상======")
for chat in chats:
    print(chat.conv())
    print()

#2. manner o
a = Person(20,1)
b = Person(25,2)

chats = [SimpleChat(a, a, 0, 0, 0), SimpleChat(a, b, 0, 0, 0), SimpleChat(b, a, 0, 0, 0)]

print("======polite-동갑, p1연상, p2연상======")
for chat in chats:
    print(chat.conv())
    print()
