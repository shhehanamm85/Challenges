#wap to check whether a no is armstrong or not?
num=int(input("Enter a no: "))
temp=num
sum=0
while num!=0:
    digit=num%10
    sum+=digit**3
    num=num//10    
if temp==sum:
    print( temp," is an amstrong number") 
else:
    print(temp,"is not an amstrong number")       