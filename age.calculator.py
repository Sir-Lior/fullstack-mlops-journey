print("===Age Calculator===")

current_year=2026
name=input("What is your name:")
birth_year=int(input("What year were you born:"))
age=current_year-birth_year

if age<0:
    print(f"{name},You are from the future😂 and if so ,please be kind to send some score prediction.")
elif age==0:
    print(f"{name},You were born today.")
elif age <13:
    print(f"{name},You are {age} years old and you are very young.")
elif age<20:
    print(f"{name},You are {age} years old and still a teenager.")
elif age<65:
    print(f"{name},You are {age} years old and an adult.")
else:
    print(f"{name}, You are {age} years old and a senior citizen.")

print(f"\nThanks for using the Age Calculator,{name}.")
