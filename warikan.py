def main():

    amount = int(input("金額は？ >"))
    number_of_people = int(input("人数は？ >"))

    payment = amount // number_of_people
    remainder = amount % number_of_people

    print("金額:" + str(amount) + "人数:" + str(number_of_people) + "一人当たり:" + str(payment) + "円" "端数:" + str(remainder))
    #出力　f-stringという機能（f記法）python3.6~
    print(f"一人当たり{payment}円です。端数は{remainder}円です。")
if __name__ == '__main__':
    main()