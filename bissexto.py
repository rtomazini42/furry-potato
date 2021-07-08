def ehbissexto(n):
    if(n%4 == 0):
        if(n%100 == 0):
            if(n%400 == 0):
                return True
            else:
                return False
        return True
    else:
        return False


print(ehbissexto(200))
print(ehbissexto(2000))