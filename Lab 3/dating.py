#Serhii Maltsev sm5zj

#Next line asks user to input age

age =int(input("How old are you? "))

#Next two lines calculate the yungest and oldest person you can date

ageLow = int((age/2)+7)
ageTop = int((age*2)-13)

#Next line prints out the result of the program

print("You can date people between "+str(ageLow)+" and "+str(ageTop)+" years old")
