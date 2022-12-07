import gamepkg.game

while True:
  try:
    ans = input('로봇이 아니라면 lion,tiger 중 하나를 입력하시오.')
    gamepkg.game.Game.is_valid(ans)
    break
  except Exception as e:
    print('error:',e)

name= input('이름을 입력하시오.')
print(' [게임 규칙] \n -홀과 짝을 고르는 게임입니다. \n -시작하는 돈은 1000원과 2000원 사이로 입력하십시오. \n 15000원을 채우면 게임은 종료됩니다.')
while True:
  c= input('게임을 시작할 금액을 입력하시오 ')
  if c.isdigit() ==True:
    if 1000<=int(c) <=2000:
      break
  else: 
    continue
c= int(c)
count = 0

while True:
  
  count += 1 
  choose= input('홀과 짝중 하나를선택하시오 게임이 시작됩니다.(홀 입력시 :1 입력, 짝 입력시 :2 를 입력해주세요)')

  instanceg=gamepkg.game.Game(name,c,choose)
  
  while instanceg.is_valid2(choose)== False:
      choose= input('홀과 짝중 하나를선택하시오 게임이 시작됩니다')
  instanceg.inform()
  instanceg.inform2()

  instanceg.makeA()
  instanceg.uanswer()
  c = instanceg.money_cal()
  print('당신의 돈은 {}입니다 '.format(c))
  
  if instanceg.go_stop() == False :
    break
  else :
    continue
