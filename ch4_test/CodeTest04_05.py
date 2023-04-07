str = input("문자열 입력 : ")
if str.isalpha() :
    print("글자입니다")
elif str.isdigit() :
    print("숫자입니다")
elif str.isalnum() :
    print("글자+숫자입니다")
else :
    print("모르겠습니다")

