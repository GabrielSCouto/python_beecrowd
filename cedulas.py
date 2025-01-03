#CÉDULAS / MONEY BILLS - SUBMISSION #42995156

amount = int(input())
print(amount)
def bill_calc(amount):
    bill_list = [100,50,20,10,5,2,1]
    for i in range(len(bill_list)):
        print(f'{amount // bill_list[i]} nota(s) de R$ {bill_list[i]},00')
        while amount // bill_list[i] > 0:
            amount -= bill_list[i]         
bill_calc(amount)

