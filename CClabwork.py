# 1.1
for i in range (3):
        print("Bisman Singh ")

# 2.1 
a,b,c=1,2,3
 
sum= a+ b+c
print(c)

# 2.2
a="Bisman"
b= "Singh"
print(a+b)


# 4.1
for i in range(1,11):
        print("7","*",i,"="," ",7*i)

print("               ")
for i in range(1,11):
        print("9","*",i,"="," ",9*i)


#4.3

n=(int)(input(" enter the n"))
s=0
for i in range(n):
        s+=i
print(s)       


#5.1
n1= (int)(input("enter the n1"))
n2= (int)(input("enter the n2"))
n3= (int)(input("enter the n3"))

print(max(n1,n2,n3))

#5.2
n=(int)(input("enter the number"))
sum=0
for i in range(1,n+1):
        if i%7==0 and i%9==0:
                sum+=i

 
print(sum)

#5.3

n= (int)(input("enter the n "))
sum=0
def isPrime(n):
        for i in range(2,n//2+1):
                if(n%i==0):
                    return False
                
        return True
        
for i in range(2,n+1):
        if(isPrime(i)):
               sum+=i
print(sum)               

# 6.1


def find_sum(n):
    sum=0
    for i in range(1,n+1):
              sum+=i
    return sum 

n= (int)(input("enter the number"))
print(find_sum(n))
