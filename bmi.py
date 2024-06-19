def calculation(weight,height):
    bmi=weight/height**2
    return bmi
def comment(bmi,name):
    if bmi <18.5:
        return f"{name} you are Underweight"
    elif 18.5<=bmi<24.9:
        return f"{name} you are normal"
    elif 25<=bmi<29.9:
        return f"{name} you are overweight"
    else:
        return "obesity"
def main():
    try:
        name=input("enter your name")
        weight =int(input("enter your weight in kg"))
        height =int(input("enter your height in m"))

        if height<=0 or weight<=0:
            raise ValueError("entered value of height or weight is wrong ,please recheck it.")
        Calculation=calculation(weight, height)
        print(f"your bmi is {Calculation}")
        Comments=comment(Calculation,name)
        print(Comments)
    except ValueError as e:
        print(f"invalid input{e}")

main()


