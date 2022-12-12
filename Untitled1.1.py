#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end="    ")
    print()


# In[3]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==0:
            if i%3==0
            :
                print("*",end=" ")
        else:
             print("$",end=" ")
    print()
    


# In[29]:


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            print("*",end=" ")
        else:
             print("$",end="")
    print()
    


# In[38]:


print( "*")
print(  "*")
print(   "*")
print(    "*")
print(     "*")
print(      "*")


# # reverse patern

# In[3]:


n=int(input())
for i in range (1,n+1):
    for j in range(n-i):
        print("",end=" ")
    for j in range(i):
        print("*",end="")
    print()


# In[17]:


n=int(input())
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
    print()
        


# In[2]:


n=int(input())                #for              #
for i in range(n):  #spaces
    for j in range(n-i-1):       #only
        print(end=" ")
    for j in range(0,i+1):      #for 
        print("*",end=" ")      #printing    #if we put space the 
    print()                    #stars          pattern will be changed


# In[1]:


n=int(input())
h=n//2+1
for i in range(1,h+1):
    s=h-i
    for j in range(1,s+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("* ",end="")
    print()
k=1
for j in range(h+1,n+1):
    for l in range(1,k+1):
        print(" ",end="")
    k=k+1
    for m in range(1,n-(j-1)+1,1):
        print("* ",end="")
    print()
    
        


# In[2]:


str=input()
l=len(str)#len() it is used to check the length of str
for i in range(l):
    for j in range (i+1):
        print(str[j],end=" ")
    print()


# In[31]:


n=int(input())                        
for i in range(1,n+1):               
    for j in range(0,n-i+1):       
        print(end=" ")
    for j in range(i,0,-1): 
        print(j,end="") 
    for j in range(2,i+1):
        print(j,end="")
    print()                  


# In[14]:


n=input()
l=len(n)
i=0
for i in range(l):
    if j=n[i]:
        if j in("a",):
            k=k+1
            if ((i+1)%2==0):
                print(i+1," ",a[i])
                print("total: ",k)
    


# In[12]:


n=input()
a=input()
c=input()
l=len(n)
for i in range (l):
    if n[i]==a:
        n[i]=c
print(n)


# #     function
# # -->  function are group of statments for specific taskes
# #  --> and use for code reusability|

# In[25]:


a="pushpinder"                   #1     
def abc():                       #3
    a="chitkara"                 #4
    print("hello",a)             #5  
abc()  #function calling         #2


# # return

# In[23]:


def abc(a,b):     #()under these barrakets it is called as parameter
    return a+b
print(abc(20,30))   #()under these barrakets it is called as argument


# # types of arguments
# 1.default
# 2.keyword
# 3.postional
# 4.variable length

# In[17]:


#1. default arguments
#like:
n=int(input())
def abc(n):             #()under these brracets it is called as parameter
    if n==94:
        print("vaues are correct:",n//2)
    else:
        print("invalid")
    #abc(n)                     ()under these barrakets it is called as argument\
  
abc(n)


# In[13]:



#2.keyword arguments
d=int(input())
c=int(input())
def abc(d,c):
    return d/c
abc(c=20,d=30)     #value which is assign in functional calling is called keyword  
print(abc(d,c))


# In[6]:


#3. postional arguments
a=2
b=30
def abc(a,b):
    return a*b
abc(a=3,b=4)            #postional is just suffling the values
print(abc(a,b))

 


# In[8]:


#4.variable length:
#1.
def record(**marks):
    for i in marks:
        subject=i
        subject_marks=marks[i]
        print(subject, subject_marks)
record(a=int(input()),b=int(input()))
print(len())


# In[10]:


a=74
def abc():
    print("______________________________________________")
for i in range(10):
    print("hello")
    print(a)
    abc()
    abc()
#               #calling the fuction again and again
abc()

    


# In[23]:


def triangle(b,h):
    return(.5*b*h)
def circles(r):
    return(3.14*r*r)
print("for area of traingle insert 1")
print(" for area of cirlce insert 2")
a=int(input())
if a==1:
    b=int(input())
    h=int(input())
    print(triangle(b,h))
if a==2:
    r=int(input())
    print(circles(r))
else:
    print("invalid input")
    


# In[8]:


def temp(i,e,s):
    for f in range(i,e,s):
        c=(f-32)*(5/9)
        print(f," ",c)
for j in range(4):
    a=int(input())
    b=int(input())
    c=int(input())
temp(a,b,c)


# In[8]:


num = int(input())
temp = num
rev = 0
while temp > 0:
    remainder = temp % 10
    rev = (rev* 10) + remainder
    temp = temp // 10
if num == rev:
  print('yes')
else:
  print("no")


# In[13]:


n=int(input())
for i in range (1,n+1):
    for j in range(i):
        print("*",end=" ")
    print() 


# In[5]:


#recursive function
#repeating a function till base condition is meet
# steps to deffine
#1.define base condtion
#2.define base function
#3.making the function call inside the function
#4.printing
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input())
print(fact(x))


# In[6]:


def print_table(num): 
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 
n = int(input())
print_table(n)


# In[ ]:


i=1
while i<5:
    if i==3:
            continue
    print(i,end=" ")
    i = i + 1


# In[3]:


i=1
while i<3:
    j=0
    while j<5:
        j = j +1
        if j==3:
            continue
        print(j,end=" ")
    i = i +1


# In[2]:


#lambda functions: anontmous function
a=lambda x,y:x*5*y
b=int(input())
c=int(input())

print(a(c,b))


# In[1]:


def abc(m):
    return lambda x:x*m
a=abc(2)
print(a(5))


# In[ ]:


while True:
    output=""
    num=int(input())
    if num ==1:
        exit()       
    for i in range (1,num+1):
        output +="{}".format(i)
        if i !=num:
            output +="+"
    output +="={}".format(sum(range(num+1)))
    print (output)


# In[ ]:


2^64


# In[ ]:


n=int(input())                
for i in range(n): 
    for j in range(n-i-1):     
        print(end=" ")
    for j in range(0,i+1):      
        print("*",end=" ")      
    print()                    


# In[8]:


a = 5,6,7
print(a[2:])


# In[1]:





# In[1]:



a = 1,2
c={}
b = (4,5)
d = (a,b)
print(d[1])


# In[1]:


x=54.21
print("%5.2f"%x)


# In[5]:


5^74


# In[1]:


n=int(input())
if n==1:
    print("monday")
elif n==2:
    print("tuesday")
elif n==3:
    print("wednesday")
elif n==4:
    print("thursday")
elif n==5:
    print("friday")
elif n==6:
    print("saturday")
elif n==7:
    print("sunday")
else:
    
    print("invalid input")


# In[7]:


n=input("Enter the munbers")
num=n.split(",")
print(num)


# In[3]:


n=int(input("enter the number"))
for i in range(1,n+1):
    print(i)
    if i==5:
        break


# In[4]:


n=int(input("enter the number"))
for i in range(1,n+1):
    print(i)
    if i==5:
        continue


# # array and list

# In[12]:


a=arr.array("i",[1,2,30])
print("the older created  array is:" ,end=" ")


# In[5]:


a=arr.array("i",[1,2,3,4,5,6])
print("array is :",end="" )
for i in range(0,7):
    print(a[i],end="")


# In[49]:


x=lambda x,y:x*y
print(x(84,54))


# In[56]:


power=lambda x,y:x**y
print(power(5,2))


# In[12]:


li=list(input().split())
print(type(li))

print(li)


# In[8]:


li=list(map(int,input().split()))
print(li)
print(type(li))


# In[20]:


a=[8, 4, 54,95 ,84]
a.remove(8)
a[0]=84
print(a)


# In[27]:


a=[84,945,75,74]
a.append(94)
print(a)


# In[31]:


a=[84,945,75,74]
a.copy()
print(a)


# In[35]:


a=[84,945,75,74]
a.clear()
print(a)


# In[43]:


a=[84,945,75,74]
a.count(65)
print(a)                     #


# In[48]:


a=[84,945,75,74]
a.extend(input().split())
print(a)


# In[54]:


a=[84,945,75,74]
a.index(74)
print(a)


# In[59]:


a=[84,945,75,74]
a.insert(3,94)
print(a)


# In[61]:


a=[84,945,75,74]
a.remove(84)
print(a)


# In[63]:


a=[84,945,75,74]
a.reverse()
print(a)


# In[65]:


a=[84,945,75,74]
a.sort()
print(a)


# In[7]:


a=[74,84,8,9,4]
print(a[2:])


# In[16]:


n=int(input())
k=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==k:
            print("1",end=" ")
            k=k-1
        elif j<k:
            print("0",end=" ")
        else :
            print("2",end=" ")
    print()


# In[4]:


m=[]
n1=int(input())
n2=int(input())
k=int(input())
for i in range(1,k+1):
    temp=m[i][n1]
    m[i][n1]=m[i][n2]
    m[i][n2]=temp


# In[2]:


b,n,m = map(int,input().split())
k  = list(map(int,input().split()))
d  = list(map(int,input().split()))
print(max([x+y for x in k for y in d if x+y<=b]or[-1]))


# In[1]:


n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="      ")
        j+=1
    print()


# In[1]:


get_ipython().set_next_input('What will be the output of following code');get_ipython().run_line_magic('pinfo', 'code')
def sum_multiply(a,b,*more):
    sum_value = a+b
    m_value = a*b
    for i in more:
        sum_value += i
        m_value*=i
    return sum_value,m_value
s_m = sum_multiply(2,3,4)
print(s_m)


# In[21]:


list = [2, 4, 6, 8, 10]
length = len(list)
for i in range(length):
    print(list[i])


# In[23]:


print("enter the table you want to print")
i=int(input())
print('enter the number ,till you want to print ')
a=int(input())
for i in range(1,a+1):
    print(i,"x",a,"=",i*a)


# In[25]:


n=int(input("enter the number"))
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp==rev:
    print("Transction proceed")
else:
    print("Transction declined")


# In[23]:


n=int(input())
if n<=100:
    a=n*0
    print("Amount to pay:",a)
elif n<200:
    a=(n-100)*5
    print("Amount to pay:",a)
elif n>=200:
    a=(100*5)+(n-200)*10
    print("Amount to pay:",a)


# In[16]:


a=input()[0]
n=int(input())
if a=='m':
    if n>10000:
        m=((n/100)*10)+n
    else:
        m=((n/100)*12.5)+n
elif a=='f':
    if n>10000:
        m=((n/100)*15)+n
    else:
        m=((n/100)*17.5)+n
print(int(m))


# In[18]:


n=int(input('Enter the size of list \n'))
a=[]
for i in range(n):
    print('Enter Element',i+1,end=': ')
    a.append(int(input()))
for i in range(1,n):
    a[i]*=a[i-1]
print(a)


# In[1]:


n=int(input())
d=[]
for i in range(n):
    a=int(input())
    b=int(input())
    c=int(input())
    x=(b/c)
    if int(x)<x:
        x=int(x)+1
    d.append(int(x)*a)
print(d)


# In[3]:


li =['abcd', 'def']
li.insert(4,5)
print(li)


# In[6]:


li = ['abcd',5,'def',5]
li.remove(5)
print(li)


# In[ ]:


n = int(input())
li = []
for i in range(n):
    li.append(input())
print(li)


# In[ ]:


def change(li):
    li[1] = li[1] + 2
li = [1,2,3,4,5]
change(li)
print(li)


# In[2]:


s="abcd"
s[0]='c'
print(s) 


# In[1]:


s = "abcdef"
print (s[4:2:-1])


# In[4]:


atuple=100,200,300,400,500
atuple[1]=800
print(atuple)


# In[5]:


student={
    "name":"emma",
    "class":9,
    "marks": 75
}
m=student['marks'])


# In[10]:


l=[none]*10
print(len(l))


# In[11]:


my_list=["hello","python"]
print("-".join(my_list))


# In[14]:


print(bool(0),bool(3.14159),bool(-3),bool(1.0+1j))


# In[23]:


str1="hello"
c=0
for x in str1:
    if(x!="l"):
        c=c+1
    else:
        pass
print(c)


# In[24]:


str1="welcome"
print(str1[:6]+"efg")


# In[26]:


def fun1(num):
    return num+25
fun1(5)
print(num)


# In[28]:


str1="stack of books"
print(len(str1))


# In[31]:


x="abcd"
for i in range(len(x)):
    print(i)


# In[33]:


xs=[1,1]
for k in range(1,7):
    xs.append(xs[k]=xs[k-1])


# In[35]:


b=0
for i in range(0,10,2):
    b+=a+1


# In[1]:


list1=[3,4,8,7]
list1.pop(1)


# In[3]:


def greetingstoPerson(*name):
    print("hello",name)
greetingstoPerson("george","brown")


# In[5]:


34+"3"


# In[17]:


def foo():
    try:
        return 1
    except:
        return 3
    finally:
        return 2
k=foo()
print(k)


# In[19]:


a=input()
b=a*a
print(b)


# In[1]:


1/3.0


# In[4]:


a,b=10,5
if a+b:
    print("true")
else:
    print("false")
a=50


# In[6]:


x=0
while (x<100):
    x+=2
print(x)


# In[8]:


j=i=1
i-=j+j*5
print(i)


# In[10]:


print("hello"+1+2+3)


# In[1]:


if 1:
    print("1is hu")
else:
    print("//")


# In[32]:


seclist=[
    21
    ,984,
    [4,7,8],4,
    {"de":84,"ed":58},
    48,44
]
h=84,74
print(seclist[2][2])
print(type(h))


# In[1]:


tw=[[1,2,3],
    [4,5,6],
    [7,8,9],
    [10]]
for row in tw:
    for col in row: 
        print(col,end)
    


# In[1]:


dict1={i:f"item {i+10}" for i in range(11) }
dict2={value:key for key ,value in dict1.items()}
print(dict1,
"\n",dict2)


# In[ ]:


Dict=dict([(2,94),(7,84)])
print(Dict[2
          ])
print(
    type(Dict)
     )
print("\n".Dict[7])


# In[17]:


Employee = { "Name":"John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print("Name : %s" %Employee["Name"])  


# In[24]:


{"Name":"John","Age":29,"salary":25000,"Company":"GOOGLE"}  
print(type(d))  
print("printing d data .... ")  
print("Name : %s" %d["Name"]) 


# In[38]:


d={"1":"ef","2":"ef"}
d.get("1")
print(d)
d.update({"1":48})
d.get("1")
print(d)


# In[62]:


d={}
d[0]="bg"
d[1]="WG"
d.get(0)


# In[63]:


Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100,201,31]:"Department ID"}    


# In[69]:


t=7,8.4,"tuples","hvt"
print(t[1])
ti=4,
print(type(ti))


# In[1]:


t={7,8,"4":4}
print(t["4"])


# In[29]:


tuple_= set([28,43,54,45,65,34,23,354])
print(type(tuple_))
print(tuple_)


# In[3]:


from turtle import*
speed(50)
color('cyan')
bgcolor('black')
b=200
while b>0:
    left(b)
    forward(b*3)
    b=b-1
    

