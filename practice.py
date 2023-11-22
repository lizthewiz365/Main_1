d = {10: 55, 23: 66.7, 14: 87}

d.update({99: 55})

print(d)


print(38 in d)

if 38 in d:
    print(True)
else:
    print(False)

x = d[10]
print(x)

for key in d:
    if d[key] == 50:
        print("yes")
    else:
        print("no")

lst = [ ] 
for key in d:
    if d[key] == 55:
        lst += [key]
print( len(lst), " got 55%.")

counter = 0
for key in d:
    if d[key] == 55:
        counter += 1
print(counter, " got 55%.")

lst = [ ]
for key in d:
    if d[key] > 50:
        lst += [key]
print(lst)


lst = [ ]       
for key in d:
    lst += [key]
    for i in range(lst):
        if lst[i] ==
        
    
        
x = d[38]
print(x)

