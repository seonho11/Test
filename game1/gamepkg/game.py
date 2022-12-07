import random
class Game:
  right = ['1','2']
  
  goal_money = 15000
  count = 0 
  def __init__(self,name,m,a):
    #c:character, m:money, a:answer
    Game.count += 1
    self.name=name
    self.m=m
    self.f_money = m
    self.a=a

  @staticmethod     # 스태틱 매소드 를사용하여 홀과 짝이 아닌경우 다시 하도록 함 . 
  def is_valid2(a):
    if a not in Game.right:
      print('홀과 짝중 선택해주세요(홀 입력시 :1, 짝 입력시 :2)' )
      return False
    else: 
      return True

  def is_valid(c):
    k = ['lion','tiger']
    if c in k :
      print('정상적인 입력입니다')
    else :
      raise ValueError('입력을 확인하세요')


    
    
  def makeA(self):
    self.right=random.randint(0,1);
  def uanswer(self):
    inta= 0 if self.a=='1' else 1
    print('맞았습니다 ' if (self.right==inta) else '틀렸습니다.');
    print('정답은 홀 입니다.' if self.right==0 else '정답은 짝 입니다.')
    if self.right == inta:
      self.c= True 
    else :
      self.c = False
  def money_cal(self) : #4
    if self.c == True :
      self.m = self.m + self.m *1.5 

    else :
      self.m = self.m - self.m/2  
    print('당신의 현재돈은 {} 입니다'.format(self.m))
    return self.m

  def go_stop(self) : #5 # 초기에 설정한 돈보다 적어지면 게임이 스탑 
    
    
    if self.m < 900 :
      print('당신은 돈을 거의 잃었습니다. 게임을 종료합니다 \n 절망으로 치닫는 도박 중독의 위험, 지금 벗어나야 합니다. \n 도박문제 전화상담 1336 ')   
      return False 
    
    elif self.m >= 15000 :
      print('당신은 목표한 금액에 달성하였습니다. 게임이 종료됩니다. ')
      return False
      

    elif self.m > 0 : 
      k = input('게임을 계속하시겠습니까?(yes/그만하시려면 아무거나 눌러주십시오.)')
      if k== 'yes':
       return True
      else :
        print('게임을 종료합니다 \n 절망으로 치닫는 도박 중독의 위험, 지금 벗어나야 합니다. \n 도박문제 전화상담 1336 ')
        return False 

  @classmethod
  def inform(cls) : # 정보 
    print('게임 횟수:',cls.count)

  def inform2(self) : # 정보 
    print('이름 :',self.name,'\n현재 가진 돈 :',self.m)
          
