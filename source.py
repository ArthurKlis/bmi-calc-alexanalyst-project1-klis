name=input("Enter your name: ")
weight=int(input("Enter your weight in pounds: "))
height=int(input("Enter your height in inches: "))
bmi_calculated_value=(weight*703)/(height*height)
if bmi_calculated_value>0:
    if(bmi_calculated_value<18.5):
        print(name+", you are underweight")
    elif (bmi_calculated_value<=24.9):
        print(name+", you are normal weight")
    elif (bmi_calculated_value<=29.9):
        print(name+", you are overweight.")
    elif (bmi_calculated_value<=34.9):
        print(name+", you are obese")
    elif (bmi_calculated_value<=39.9):
        print(name+", you are severely obese")
    elif (bmi_calculated_value>=40):
        print(name+", you are morbidly obese")
    else:
        print("Enter valid inputs")
