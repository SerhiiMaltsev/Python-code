#Serhii Maltsev sm5zj


def binop(s):
    i = 0
    n1 = ''
    n2 = ''
    s = s.replace(" ", "")
    while (s[i] != "+") and (s[i] != "-") and (s[i] != "*") and (s[i] != "/"):
        n1 = n1 + s[i]
        i += 1
    s = s[i:len(s)]
    sign = s[0]
    s = s[1:len(s)]
    n2 = s
    if sign == "+":
        return int(n1)+int(n2)
    elif sign == "-":
        return int(n1)-int(n2)
    elif sign == "*":
        return int(n1)*int(n2)
    else:
        return int(n1)/int(n2)
