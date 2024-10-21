#def calculate_bmi(height, weight):
#   print("Height = " + height)
#    print("Weight = " + weight)

#calculate_bmi(weight=57,height=1.73)
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    

#To calculate BMI
    bmi = (weight)/(height*height)
    print("the  bmi value is :",bmi)

    if bmi < 18.5:
        print("User is underweigh")
    elif bmi>=18.5 and bmi<=25.0:
        print("User is in Normal weight")
    else :
        print("User is overweight")
    
        

calculate_bmi(weight=57,height=1.73)
