num_sum = 0

for i in range(1,1000000):
    if (str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1]):
        num_sum += i

print(num_sum)
