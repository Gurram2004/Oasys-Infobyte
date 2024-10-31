hei=float(input('enter the height in meters: '))
wei=float(input('enter the weight in kilograms: '))
bmi=wei/(hei*hei)
c=None
print("-"*50)
if(bmi<18.5):
    print('your in underweight')
    c="underweight"
elif(18.5<=bmi and bmi<=24.9):
    print('your in normal weight')
    c="normal"
elif(25<=bmi and bmi<=29.9):
    print('your in overweight')
    c="overweight"
elif(30<=bmi and bmi<=34.9):
    print('your in class-1 obesity')
    c="class-1 obesity"
elif(35<=bmi and bmi<=39.9):
    print('your in class-2 obesity')
    c="class-2 obesity"
elif(bmi>=40):
    print('your in class-3 obesity')
    c="class-3 obesity"
print("-"*50)
