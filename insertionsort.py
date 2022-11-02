#insertion sort örneği
s = [22,27,16,2,18,6];

ek = s[0]
print(s)
print("-"*50)

for i in range(len(s)):
    ek = s[i]
    for j in range(i,len(s)):
        if(ek>s[j]):
            ek = s[j]
    s.remove(ek)
    s.insert(i, ek)
    print(s)

print("-"*50)    
print(s)