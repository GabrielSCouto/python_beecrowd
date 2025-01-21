#BHASKARA FORMULA 1036 - SUBMISSION #43143075

def main():
    a, b, c = input().split()

    a = float(a)
    b = float(b)
    c = float(c)

    delta = b**2  -4 * a * c

    if a == 0 or delta < 0:
        print("Impossivel calcular")
    else:    
        root1 = (- b + delta**0.5) / (2 * a)
        root2 = (- b - delta**0.5) / (2 * a)
        print (f'R1 = {root1:.5f}')
        print (f'R2 = {root2:.5f}')
main()