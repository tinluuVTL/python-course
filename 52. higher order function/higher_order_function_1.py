def divisor(x):
    def divident(y):
        return y / x
    return divident

divide_by_3 = divisor(3)
print(divide_by_3(18))