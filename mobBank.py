balance=0
def menu():
  print('''  1. to deposit
  2. to withdraw
  3. to transfer
  4. to check balance
  0. to exit''')
def password():
  for i in range(1,4):
    global pw
    pw=int(input('enter password: '))
    if pw==2020:
      print('Welcome to Mobile banking service\n')
      break
    else:
      print('you enter wrong password you remain ',3-i,'trial')
  else:
    print('your acount blocked')
    exit()

def choice():
  global need
  need=int(input('enter you want to do--> '))

def deposit(d):
  global balance
  balance +=d
  print(f'you deposited {amount} Birr and yuor balance is {balance} Birr')

def withdraw(w):
  global balance
  if balance<w:
    print('insufficient balance')
  else:
    balance-=w
    print(f'you withdraw {amount} Birr and yuor balance is {balance} Birr')

def transfer(t):
  global balance
  acount=int(input('enter reciver acount--> '))
  if balance<t:
    print('insufficient balance')
  else:
    balance-=t
    print(f'you transfered {amount} Birr to {acount} and yuor balance is {balance} Birr')

password()
if pw==2020:
  menu()
while True and pw==2020:
  choice()
  if need==0:
    print('you exit')
    break
  if need==1:
    amount=float(input('enter amount you deposit'))
    deposit(amount)
  elif need==2:
    amount=float(input('enter amount yo withdraw--> '))
    withdraw(amount)
  elif need==3:
    amount=float(input('enter amount yo transfer--> '))
    transfer(amount)
  elif need==4:
    print(f'your balace is {balance}  Birr \n Thankyou chooice us!!!')
  else:
    print('you entered error')