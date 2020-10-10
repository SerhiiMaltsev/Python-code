#Serhii Maltsev sm5zj

def st_jeor (mass, height, age, sex):
    if sex == "male":
        s = +5
    else:
        s = -161

    p = 10.0*mass+6.25*height-5.0*age+s
    return p
