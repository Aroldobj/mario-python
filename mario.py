from cs50 import get_int

while True:
    h = get_int("Qual a altura? ")
    if h < 1 or h > 8:
        print("Digite novamente entre 1 e 8")
    else:
        break
for i in range(1, h+1):
    print(" "*(h-i), end=" ")
    print("#"*i)