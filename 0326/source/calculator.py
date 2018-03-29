def number():
        y = int(input("請輸入數字1:"));x = input("請輸入符號");z = int(input("請輸入數字2:"))
        if x == "+":
            return("結果:",y+z)
        elif x == "-":
            return("結果:",y-z)
        elif x == "*":
            return("結果:",y*z)
        elif x == "%":
            return("結果:",y%z)
        else:
            return("輸入錯誤")