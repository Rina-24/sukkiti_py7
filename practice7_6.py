from random import randint

print("数当てゲームを始めます。3桁の数を当ててください！")

# 正解の数の作成（not inで重複しないようにする）
answer = []
for n in range(3):
    answer_num = randint(0, 9)
    while answer_num in answer:  # 既存の数と重複する場合は再生成
        answer_num = randint(0, 9)
    answer.append(answer_num)

print(answer) # デバック用の答え

is_continue = True
while is_continue == True:
        
    prediction =[]
    for n in range(len(answer)):
        prediction_num = int(input(f"{n+1}桁目の予想を入力。(0～9)>>"))
        prediction.append(prediction_num)
    print(prediction)

    hit = 0
    blow = 0

    for index in range(len(answer)):
        if prediction[index] == answer[index]: 
            hit +=1
        else:
            for index2 in range(len(answer)):
                if prediction[index] == answer[index2]:
                    blow += 1
                    break

    # 結果発表
    print(f"{hit}ヒット、{blow}ボール！")
    if hit == 3:
        print("正解です！！")
        is_continue = False
    else:
        if int(input("続けますか？1：続ける 2：終了")) == 2:
            print(f"正解は{answer}でした")
            is_continue = False

