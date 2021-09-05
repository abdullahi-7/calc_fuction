import time
# abdullahi,10,kenya


add = "A"
subtract = "S"
multiply = "X"
divide = "D"

def cal(nX, op, nY):
    if op == add:
        answer = nX + nY
        print(answer)
    elif op == subtract:
        answer = nX - nY
        print(answer)
    elif op == multiply:
        answer = nX * nY
        print(answer)
    elif op == divide:
        answer = nX / nY
           print(answer)
    else:
        print("use the intruction above!!!!")



var = int(input("write the first number: "))
vari =input("which letter? ")
variable = int(input("write the second number: "))

cal(var, vari, variable)

time.sleep(5)