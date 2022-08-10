from random import randint

arr = []
for i in range(10):
    arr.append(randint(1, 99))
print(arr)

i = 0

while i < 10 - 1:
    m = i
    j = i + 1

    while j < 10:
        if arr[j] < arr[m]:
            m = j
        j += 1

    arr[i], arr[m] = arr[m], arr[i]

    i += 1

print(arr)
