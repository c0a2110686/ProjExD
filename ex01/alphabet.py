import random
import time

repeat = 5
sub = 10
miss = 2

def main(): #メイン関数
    start_time = time.perf_counter()
    for _ in range(repeat):
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1:
            break
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"所要時間{elapsed_time}秒かかりました")
            
def shutudai(): #出題関数
    alphabets = [chr(c+65) for c in range(26)]
    sub_lst = random.sample(alphabets, repeat)
    print(f"対象文字 : {sub_lst}")

    miss_lst = random.sample(sub_lst, miss)
    print(f"欠損文字:{miss_lst}")

    dis_lst = [c for c in sub_lst if c not in miss_lst]
    print(f"表示文字:{dis_lst}")

    return miss_lst

def kaitou(seikai): #解答関数
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != miss:
        print("不正解です")
        return 0

    else:
        print("正解です.それでは具体的に欠損文字を1つずつ入力してください")
        for i in range(miss):
            c = input(f"{i+1}つ目の文字を入力してください:")
            if c not in seikai:
                print("不正解です. またチャレンジしてください")
                return 0
            seikai.remove(c)
        print("正解です.")

if __name__ == "__main__":
    main()

    



