a = int(input("$ :"))
b = int(input("SENT :"))
n = int(input("SONI: "))

c = n * ((a * 100) + b)
print("$: ",  c // 100)
print("SENT: ",  c % 100)
 
