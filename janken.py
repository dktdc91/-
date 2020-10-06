# janken.py
# by Kevin dela Cruz for Persol Group

from random import randint

# 選ぶものリスト
choice = ["石", "紙", "ハサミ"]

# コンピューターの選んだもの
computer_choice = choice[randint(0,2)]

# メッセージの定義
computer_win = "負けた!!"
player_win = "勝った!!"

again = "Y"
while again == "Y":
    player_choice = input("石、紙、ハサミ：一つ選んでください。")
    computer_choice = choice[randint(0, 2)]
    if player_choice == computer_choice:
        print("同点だ！もう一回しよう")
    # 石
    elif player_choice == choice[0]:
        # 紙
        if computer_choice == choice[1]:
            print(computer_win + computer_choice + "が" + player_choice + "を覆う")
        # ハサミ
        else:
            print(player_win + player_choice + "が" + computer_choice + "を壊す")
    # 紙
    elif player_choice == choice[1]:
        # 石
        if computer_choice == choice[0]:
            print(player_win + computer_choice + "が" + player_choice + "を覆う")
        # ハサミ
        else:
            print(computer_win + player_choice + "が" + computer_choice + "を切る")
    # ハサミ
    elif player_choice == choice[2]:
        # 紙
        if computer_choice == choice[1]:
            print(player_win + computer_choice + "が" + player_choice + "を切る")
        # 石
        else:
            print(computer_win + player_choice + "が" + computer_choice + "を覆う")
    again = input("もう一回やる?(Y/N): ")
