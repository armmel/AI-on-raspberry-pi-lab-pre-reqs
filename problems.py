from bank_account import BankAccount

# n = int(input())

#1 Գրեք Python ծրագիր՝ ստուգելու համար՝ արդյոք տրված թիվը զույգ է, թե կենտ։
def even_odd(n):
  if n % 2 == 0:
    print("even")
  else:
    print("odd")
 
#2 Գրեք Python ծրագիր առաջին n բնական թվերի գումարը հաշվարկելու համար։
def sum(n):
  sum = 0
  for i in range(1,n+1):
    sum += i 
  print(sum)

#3 Գրեք Python ծրագիր՝ Ֆիբոնաչիի շարքը մինչև n թիվը տպելու համար։
def fibonacci(n):
  fib = [0,1]
  while fib[-1] + fib[-2] < n:
    next = fib[-1] + fib[-2]
    fib.append(next)
  for num in fib:
    print(num)
  
#4 Գրեք Python ծրագիր՝ ցուցակի ամենամեծ տարրը գտնելու համար:
def max_in_list(n):
  l=[1,5,7,26,38,62,3]
  #print(max(l)) բավականին լավ տարբերակ 
  max = l[0]
  for i in l:
    if max < i:
      max = i 
  print(max)

#5 Ստեղծեք Python դաս, որը կոչվում է BankAccount, որը ներկայացնում է բանկային հաշիվ:
# Create a bank account with an initial balance of $100 
account = BankAccount("123456789", 100.0) 
# Deposit $50 
account.deposit(50.0) 
# Withdraw $30 
account.withdraw(30.0) 
# Get the current balance 
balance = account.get_balance() 
print(f"Current balance: ${balance}")