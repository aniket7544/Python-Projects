def numVowels(str):
    c=0
    for i in str:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            c=c+1
    
    return c



str=input()

print(numVowels(str))
