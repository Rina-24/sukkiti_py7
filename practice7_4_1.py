
num = []
print("3つの数字を入力してください。")
num1 = int(input("1つ目の数字を入力してください。"))
num2 = int(input("2つ目の数字を入力してください。"))
num3 = int(input("3つ目の数字を入力してください。"))
num.append(num1)
num.append(num2)
num.append(num3)

def maxNum(value):
    value= max(value)
    print(value)
    return value

maxNum(num)
