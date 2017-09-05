def FourDigitCombinations():
    numbers = []
    for code in range(10000):
        code = str(code).zfill(4)
        print code,
        numbers.append(code)
if __name__ == "__main__":
            FourDigitCombinations()
