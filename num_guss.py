#number gussing game
import random
num=random.randint(1,100)
trial=0
while True:
  guss=int(input('gusss the number b/n 1-100-->'))
  trial+=1
  if guss==num:
    print(f' congratulation you won {num}, by {trial} trial')
    break
  elif guss>num:
    print(f'errror, guss below {guss}')
  else:
    print(f'error, guss above {guss}')