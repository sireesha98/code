lower1 = 100
upper = 2000
for num in range(lower1, upper + 1):
   order = len(str(num))
sum =0
temp = num
while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
if num == sum:
       print(num)
