def sumaconcatena(a,b):
    if(type(a) == str or type(b) == str):
        return str(a) + str(b)
    else:
        return int(a) + int(b)

print(sumaconcatena(1,2))
print(sumaconcatena("1",2))
print(sumaconcatena("1","a"))