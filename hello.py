m= int(input("Enter amount:"))
s= int(input("Enter stepup percent:"))
t= int(input("Enter number of years:"))
r = int(input("Enter expected rate of return:"))

numberofmonths= t*12
a= r/12
rate=a/100
invested=0 
outcome=0

for i in range(1,numberofmonths+1):
  invested =invested+m
  b=1+rate
  outcome= (outcome+m)*b

  if i % 12 == 0:
    c=s/100
    d=1+c
    m = m*d

  gain = outcome-invested  

print("Invested:",int(invested))

print("Profit amount:",int(gain))

print("Final amount:",int(outcome))
