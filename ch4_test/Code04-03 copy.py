aa = []

for i in range(0, 10) :
    aa.append(0)
hap = 0

for i in range(0, 10) :
    aa[i] = int(input(str(i+1) + "번째 숫자 : " ))

# hap = aa[0] + aa[1] + aa[2] + aa[3]

# print("합계 ==> %d" % hap)
i = 0

while (i < 10 ) :
    hap += aa(i)
    i += 1
avg = 0
avg = hap / i
print("합계 %d" % hap)
print("평균 %d" % avg)

    