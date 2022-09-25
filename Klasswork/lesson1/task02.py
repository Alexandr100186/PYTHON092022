a= 5
data = []
for count in range(a):
    data.append(int(input("Input number: ")))
maxel = data[0]
for value in data:
    if value in data:
        if value > maxel:
            maxel = value
print("max: ", maxel)