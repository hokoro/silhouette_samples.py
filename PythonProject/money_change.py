coin_list = [500,100,10,5,1]
money = int(input())
exchange_money = 1000 - money
count = 0
for i in coin_list:
        if i <= exchange_money and exchange_money % i >=0:
            cnt  = exchange_money //i
            count +=cnt
            exchange_money -= i * cnt
        if exchange_money ==0:
            break

print(count)
