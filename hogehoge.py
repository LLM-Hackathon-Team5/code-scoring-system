class Calculator:
    """
    下記の問題を含む
    - subtract メソッドで return ステートメントが不足している。
    - 最後の行に未使用の変数 unused_var がある。
    - コメントが不足している。
    - エラーハンドリングが不足している（例: 引数が数値でない場合の処理）。
    """
    def __init__(self, x, y):
        self.x = x  # First number
        self.y = y  # Second number

    def add(self):
        result = self.x + self.y
        print(f"The sum is {result}")
        return result

    def subtract(self):
        # Missing return statement
        print(f"The difference is {self.x - self.y}")

    def multiply(self):
        result = self.x * self.y
        print(f"The product is {result}")
        return result


# Creating an object of the Calculator class
calc = Calculator(10, 5)

# Performing addition
calc.add()

# Performing subtraction
calc.subtract()

# Performing multiplication
calc.multiply()

# Unused variable
unused_var = 50
