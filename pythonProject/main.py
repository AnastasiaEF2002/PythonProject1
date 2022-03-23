x=float(input())
y=float(input())
print(x*1/(x-y))
print(x%(x-y/2)*x/10)

txt=("1000-500/23")
print(txt,"=",eval(txt))
t=int(eval(txt))
while t>0:
    t=t-500/23
    print(t)

name=input("What is your name? ")
age=int(input("How old are you?"))
print("Welcome, ",name+"!")
print("You were born in ",2022-age)
