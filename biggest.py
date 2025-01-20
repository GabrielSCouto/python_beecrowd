#THE BIGGEST (O MAIOR) - SUBMISSION #43125477

def main():

    user_input = input()
    numbers = user_input.split()

    biggest_ab = (int(numbers[0]) + int(numbers[1]) + abs(int(numbers[0]) - int(numbers[1]))) / 2

    biggest = (biggest_ab + int(numbers[2]) + abs(biggest_ab - int(numbers[2]))) / 2

    print(f'{biggest:.0f} eh o maior')

main()