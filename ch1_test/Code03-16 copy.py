# i, k = 0, 0

# for i in range(2, 10, 1) :
#      print("## %d단 ##" %(i))
#      for k in range(1, 10, 1) :
#           print("%d X %d = %2d" %(i, k, i * k))
#      print("")	

# while True :
#     print("미안")


hap = 0
for i in range(3333, 10000) :
     if i % 1234 == 0 :
          continue
     hap += i
     if hap > 100000 :
          hap -= i
          break

print("합계", hap)


total = 0
for num in range(3333, 10000):
    if num % 1234 == 0:  # 1234의 배수인 경우
        continue  # 아래의 코드를 실행하지 않고 다음 숫자로 건너뜁니다.
    total += num
    if total > 100000:  # 합계가 100000을 넘긴 경우
        total -= num  # 마지막에 더한 숫자를 다시 빼주고
        break  # 반복문을 종료합니다.

print("합계:", total)