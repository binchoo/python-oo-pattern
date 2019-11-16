'''
객체 기능을 동적으로 확장하도록 하는
Decorator 패턴을 연습해 봅니다
'''

class Fighter :

        def attack(self) :
                print("전방 공격!")

class AdvancedFighter(Fighter) :
        '''
        메모리에 존재하는 Fighter를 그대로 사용하며
        확장된 기능을 구현하는
        Decorator 패턴입니다
        '''

        def __init__(self, fighter=None) :
                self.base = fighter

        def extends(self, fighter) :
                self.base = fighter

        def attack(self) :
                if self.base != None :
                        self.base.attack()

class SideAttackFighter(AdvancedFighter) :

        def attack(self) :
                super().attack()
                print("측면 공격!")

class RearAttackFighter(AdvancedFighter) :

        def attack(self) :
                super().attack()
                print("후방 공격!")

#main
def printline() :
        print("----------")

if __name__ == '__main__' :
        f = Fighter()
        f.attack()

        printline()
        f = SideAttackFighter(f)
        f.attack()

        printline()
        f = RearAttackFighter(f)
        f.attack()

        printline()
        f = f.base
        f.attack()

        printline()
        f = f.base
        f.attack()
