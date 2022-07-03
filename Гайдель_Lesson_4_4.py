m = [1,5,3,3,3,1,1,5]
m1 = []
for i in m:
    if m.count(i) > 2:
        if m1.count(i) == 0 :
         m1.append(i)
print (m1)