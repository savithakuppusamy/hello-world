num=int(input('Enter the integer:'))
r=0
rs=0
while(num>0):
    r=num%10
    rs=rs*10+r
    num=num/10
print("Reverse of entered number is:",rs)
    

