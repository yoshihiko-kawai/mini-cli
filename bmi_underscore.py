def main():
    height_cm = float(input("身長 : ")) * 0.01
    weight_kg = float(input("体重: "))
    #変数のインライン化
    bmi = round(weight_kg / (height_cm ** 2), 2)
    #出力
    print(bmi)

if __name__ == '__main__':
    main()