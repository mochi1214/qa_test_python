from python.my_class import MyClass

if __name__ == "__main__":
    my_instance = MyClass()

    # 第一題：輸入
    wrong_scores = [35, 46, 57, 91, 29]

    fixed_scores = my_instance.correct_scores(wrong_scores)
    print("第一題輸出：", fixed_scores)

    # 第二題：輸入
    letter = "Hello welcome to Cathay 60th year anniversary"
    count_letter = my_instance.count_letters(letter)

    # 第三題：輸入
    user_input = input("請輸入人數：")
    winner = my_instance.count_order(user_input)
    print(winner)




