n = int(input())
if n < 1:
  print("This number is not prime")
elif n == 1:
  print("This number is not prime")
else:
  for x in range(2, n):
    if n % x == 0:
        print('This number is not prime')
        break
    else:
      print('This number is prime')
      break

