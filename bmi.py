def bml_caluclator(weight,height):
    return weight/(height ** 2)
def bml_category(bml):
    if bml < 18.5:
        return 'under weight'
    elif 18.5 <= bml <= 29.9:
        return 'normal weight'
    else:
        return 'obese weight'
def solti_input():
    try:
        weight = float(input("enter your weight in kg :"))
        height = float(input("Enter your height in meters"))
        return weight, height
    except ValueError:
        print('Entry mistake please add correct number ')
        return solti_input()
    