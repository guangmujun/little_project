import random

class Computer():
    def __init__(self):
        a = random.randint(0,2)
        nameList = ['刘备','关羽','张飞']
        self.name = nameList[a]
        self.score = 0
    
    def showQuan(self):
        a = random.randint(0,2)
        quans = ['石头','剪刀','布']
        print('电脑：',self.name,'出了',quans[a])
        return int(a)

class Person():
    def __init__(self):
        pname = input('选择角色：[0：孙悟空 1：猪八戒 2：沙僧]\n')
        names = ['孙悟空','猪八戒','沙僧']
        self.name = names[int(pname)]
        self.score = 0

    def showQuan(self):
        q = input('请您出拳：[0：石头 1：剪刀 2：布]\n')
        qs = ['石头','剪刀','布']
        print('玩家：',self.name,'出了',qs[int(q)])
        return int(q)

class Game():
    def __init__(self):
        self.count = 0
        self.countw = 0
        self.countp = 0
        self.countc = 0
        self.c = Computer()
        self.p = Person()
        self.begin()

    def begin(self):
        answer = input('是否继续：[Y/N]\n')
        while answer=='Y' or answer=='y':
            a = self.p.showQuan()
            b = self.c.showQuan()

            if (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
                self.p.score += 5
                self.countw += 1
                print('恭喜您赢了！')
            elif a is b:
                self.countp += 1
                print('平局')
            else:
                self.c.score += 5
                self.countc += 1
                print('电脑赢了！')
            self.count += 1
            answer = input('是否继续：[Y/N]\n')
        self.showMessage()

    def showMessage(self):
        print(self.p.name,' VS ',self.c.name)
        print('比赛总次数：',self.count)
        print('玩家：',self.p.name,'赢的次数：',self.countw)
        print('平局的次数：',self.countp)
        print('电脑：',self.c.name,'赢的次数：',self.countc)
        if self.c.score > self.p.score:
            print(self.c.name,'赢了！')
        elif self.c.score == self.p.score:
            print('平局！')
        else:
            print(self.p.name,'赢了！')

if __name__ == '__main__':
    game = Game()


