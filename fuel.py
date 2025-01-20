#FUEL (GASTO DE COMBUSTIVEL) - SUBMISSION #43125597

def main():

    time = int(input())
    avg_speed = int(input())

    fuel = (avg_speed * time) / 12

    print(f'{fuel:.3f}')
    
main()    