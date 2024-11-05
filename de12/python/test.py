for i in range(3): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！
    name=input("名前を教えてください") #繰り返したいやつをまとめてtabする
    waist=float(input("腹囲は？")) #floatは小数点ありの数字
    age=int(input("年齢は？")) #intは整数

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=85 and age>=40:        #if文、for文は最後にコロン(:)をつけるだけでよい
        print(name,"さん、内臓脂肪蓄積注意です") #tabによってずらすことで動作をくくれる
    else:
        print(name,"さん、腹囲は問題ありません")

# 出力結果
# 0 人目
# 1 人目
# 2 人目
