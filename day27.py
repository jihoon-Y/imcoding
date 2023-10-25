# init함수

class Unit: #class를 만들고, 이름을 붙이고 콜론으로 마무리
    def __init__(self, name, hp, damage):
        #객체가 생성될 때는 기본적으로 __init__함수에 정의된 개수와 동일하게 설정해야한다. self는 빼고.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        #이제 unit이라는 하나의 class가 만들어진 것이다.

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35) #Unit이라는 class이기 때문에 대소문자 확실히
#marine3 = Unit("마린") #이런건 안된다
#marine3 = Unit("마린",40) #이런건 안된다

# __init__은 파이썬에서 쓰이는 생성자 이다. 객체가 만들어질 때 자동으로 호출되는 부분이다
#객체=class로부터 만들어지는 녀석들, marine과 tank는 Unit class의 instance(객체)이다.