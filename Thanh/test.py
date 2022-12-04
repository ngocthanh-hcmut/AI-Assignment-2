array = [0]

i = 0
while i < len(array):
    print(i)
    array.append(len(array))
    if i == 10: 
        break
    i += 1

print(array)