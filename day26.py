# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

#탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드/시즈모드 있음
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage): #attack이라는 함수 만들고, 이름/공격위치/데미지를 받겠다
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 이렇게 수작업으로 유닛을 추가할 수 있지만, 게임하다보면 유닛이 수십 수백개가 된다.
# 이런 경우에 class(붕어빵기계)를 사용해야함
# 재료만 넣으면 붕어빵을 무한정 만들 수 있는 틀. class도 그 틀이라고 보면 된다.
# 서로 연관이 있는 변수와 함수의 집합, 정도로 이해하면 된다. 

class Unit: #class를 만들고, 이름을 붙이고 콜론으로 마무리
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        #이제 unit이라는 하나의 class가 만들어진 것이다.

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35) #Unit이라는 class이기 때문에 대소문자 확실히
# 이렇게 하면 수작업이 덜어진다.