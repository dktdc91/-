# password_generator.py
# by Kevin dela Cruz

import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = string.punctuation

def get_password_length():
    length = input("パスワードの長さを入力してください: ")
    return int(length)

def password_generator(length=8):
    # 静的ストリングから英数字を作成
    generate = f'{LETTERS}{NUMBERS}{SYMBOLS}'

    # ストリングからリストに変換して、文字をシャッフルする
    generate_list = list(generate)
    random.shuffle(generate_list)

    # パスワードを作成して、ストリングで戻る
    password = random.choices(generate_list, k=length)
    password = ''.join(password)
    return password


# 実行
password_length = get_password_length()
password = password_generator(password_length)

print("パスワード: " + password)
