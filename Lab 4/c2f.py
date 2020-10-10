#Serhii Maltsev sm5zj

#Following line asks user to input the temperature in celcius
tInCelsius = float(input("What is the temperature in Celsius? "))

#Next line converts the temperature from celsius to farenheits
tInFarenheits = round((9 * (tInCelsius+40))/5-40, 1)

#Next line prints out the results
print("It is " + str(tInFarenheits) +" degrees Fahrenheit")
