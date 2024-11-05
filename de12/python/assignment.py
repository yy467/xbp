import random

migi=0
hidari=0
mylist=["migi","hidari"]
count=-1
#----------------------------------
#答えの方の右左
target=(random.choice(mylist))
#はずれかあたりか
while True:
    count += 1
    asw=input("migi or hidari")
    number=(random.choice(mylist))
    print(number,"が答えです")

    if number==asw:
        print("正解です！繰り返します")
    else:
        print("不正解です！終わります。")
        break
print("---------finish-------------")
print("あなたは",count,"回連続で正解できました！！")

