import random

def guess_the_number():
    try:
        n = int(input("最小値を入力してください: "))
        m = int(input("最大値を入力してください: "))

        if n > m:
            print("エラー: 最小値は最大値以下でなければなりません。")
            return

        secret_number = random.randint(n, m)
        max_attempts = 5

        print(f"{n} から {m} の数を当ててください（最大 {max_attempts} 回まで）")

        for attempt in range(1, max_attempts + 1):
            guess = int(input(f"{attempt} 回目の試行: "))

            if guess == secret_number:
                print(f"正解！{attempt} 回目で当たりました！")
                break
            elif guess < secret_number:
                print("もっと大きい数です。")
            else:
                print("もっと小さい数です。")
        else:
            print(f"残念！正解は {secret_number} でした。")

    except ValueError:
        print("数字を入力してください。")

# ゲームを開始
guess_the_number()

