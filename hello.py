print('Hello world!')
name=input('Name: ')
# print('Hello '+name)

# String formatting with string literals
print(f"My name is {name}")

# if else statement
if name!="":
    print(f"You are welcome {name}")
else:
    print(f"You typed nothing")

age=int(input('Age: '))
if age<18:
    print(f"{name}, you're a minor")
elif age>18:
    print(f"{name}, your are an adult")
elif age==18:
    print(f"{name}, you're exactly 18 years")
else:
    print(f"You typed nothing")
