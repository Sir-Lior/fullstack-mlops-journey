user={
    "name":input("Enter Your Name:"),
    "age":int(input("Enter Your Age:")),
    "is_learning":True,
    "city":"nairobi"
}
if user["age"]<18:
    print(f"{user["name"]}, You are a minor. ")
elif 18<=user["age"]<=25:
    print(f"{user["name"]}, You are between 18 and 25.")
else:
    print(f"{user["name"]},You are over 25 years old.")
    