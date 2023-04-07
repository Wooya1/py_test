## 변수 선언 부분 ##
#77777 -> 50000, 10000, 5000, 1000 단위로 나누기.
# money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
money, c50000, c10000, c5000, c1000 = 0, 0, 0, 0, 0

## 메인 코드 부분 ##
# money=int(input("교환할 돈은 얼마 ? "))
money=int(input("교환할 돈은 얼마 ? "))
# c500 = money // 500
# money %= 500
c50000 = money // 50000
money %= 50000
# c100 = money // 100
# money %= 100
c10000 = money // 10000
money %= 10000
# c50 = money // 50
# money %= 50
c5000 = money // 5000
money %= 5000
# c10 = money // 10
# money %= 10
c1000 = money // 1000
money %= 1000

# print("\n 500원짜리 ==> %d개" % c500)
# print(" 100원짜리   ==> %d개 " % c100)
# print(" 50원짜리 ==> %d개 " % c50)
# print(" 10원짜리   ==> %d개 " % c10)
# print(" 바꾸지 못한 잔돈 ==> %d원" % money)

print("\n 50000원짜리 ==> %d개" % c50000)
print(" 100000원짜리   ==> %d개 " % c10000)
print(" 5000원짜리 ==> %d개 " % c5000)
print(" 1000원짜리   ==> %d개 " % c1000)
print(" 바꾸지 못한 잔돈 ==> %d원" % money)
