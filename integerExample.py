Print = ""
uv=1
num = int(input("Enter a number:"))
while num > 10:
    digit = num % 10
    num = int((num - digit) / 10)
    Print = " " + str(digit * uv) + Print
    uv = uv * 10
print(str(num * uv) + Print)
