print("\n\t\t              BMI CALCULATOR")

weight=int(input("Enter  your  weight in  pounds :"))
height=int(input("Enter  your height  in  inches :"))
BMI=(weight * 703)/(height * height)
print(BMI)


print("BMI           Classification    Health risk")
print("under18.5     Underweight       Minimal ")
print("18.5-24.9     normalweight      Minimal ")
print("25-29.9       overweight        increased ")
print("30-34.9       obese             high ")
print("35-39.9       severlyobese      very high ")
print("40 and over   morbidlyobese     Extremly high ")


if BMI>0:
    
    if BMI < 18.5:
        print("Underweight")
    elif BMI > 18.5 and BMI <25:
        print("normalweight")
    elif BMI >25 and BMI <30:
        print("overweight")
    elif BMI >30 and BMI<35:
        print("obese")
    elif BMI >35 and BMI <40:
        print ("several  obese")
    else:
        print("morbidlyobese")
else:
    print("invalid")
    
        