
def roman_int(s):

    roman_no = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
    s=input("Enter your no:")
    n=len(s)
    total=0
    for i in range(n):
        cv=roman_no[s[i]]
        if i< len(s)-1 and  cv < roman_no[s[i+1]]:
            total-=cv
        else:
            total+=cv  
    return total
p=0
print(roman_int(p))