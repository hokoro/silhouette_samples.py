#동전의 거스름돈을 입력 받고
#해당 화폐로 거슬러줄수 있는 동전의 개수 세기

n = int(input()) #거슬러 주는 돈 입력 받기
count = 0

array = [500,100,50,10] #동전의 개수를 몇개로 설정 할지 저장

for coin in array:   #시간 복잡도 O(k) : 화폐의 종류만큼 반복이 수행된다
    count += n // coin
    n %= coin

print(count) #동전의 총 종류에만 영향을 받는다

