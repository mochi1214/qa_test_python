from itertools import count


class MyClass:
    def __init__(self):
        pass

    # 第一題
    def correct_scores(self, wrong_scores):

        fixed_scores = []
        for score in wrong_scores:
            fixed_score = int(str(score)[::-1])
            fixed_scores.append(fixed_score)

        return fixed_scores

    # 第二題
    def count_letters(self, text):
        text = text.upper()
        count = {}

        for i in text:
            if i.isalnum():
                count[i] = count.get(i, 0) + 1

        sorted_count = sorted(count.items())

        formatted_list = []

        print("第二題輸出:")
        for key, value in sorted_count:
            formatted_string = f"{key} {value}"
            formatted_list.append(formatted_string)
            print(formatted_string)

    # 第三題
    def count_order(self, n):
        while True:
            if n.isdigit():
                input_number = int(n)
                if 0 <= input_number <= 100:
                    break
                else:
                    print("請輸入 0 - 100 的數值")
            else:
                print("請輸入有效的數字")

            n = input("請重新輸入人數：")

        people = list(range(1, input_number + 1))
        index = 0

        # 當餘數為 0 時，圈圈要從index 0 重新計算
        while len(people) > 1:
            index = (index + 2) % len(people)
            people.pop(index)

        return people[0]



