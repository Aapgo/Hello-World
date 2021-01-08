Withdraw= 0
Diposite= 0
option= 0
Balance= 2000
import sys
print('Welcome to RBC ATM what would you like to do today')
while True:
  print('1.Withdraw')
  print('2.Diposit')
  print('3.Balance')
  print('4.Quit')
  option=int (input('Select one of the above: '))
  if(option==1):
    Withdraw=int (input('please enter your withdral amount'))
    if(Withdraw>Balance):
      print('You cannot Withdraw more then your own Balance')
    else:
      Balance=Balance-Withdraw 
    print(Balance) 
  elif(option==2): 
    Diposite=int(input('How much would you like to Diposit?'))
    if(Diposite>100000):
      print('you cannot Diposit more than $100,000')
    Balance=Balance+Diposite
    print(Balance)
  elif(option==3):
    print('Your Balance is ' + str(Balance))
  elif(option==4):
    sys.exit('Thank you for coming to our ATM')
  