def binary_code(s: str, k: int):
    if len(s) < 2 ** k + k - 1:
        return False
    codes = [False for _ in range(2 ** k)]
    for i in range(len(s) - k + 1):
        codes[int('0b' + s[i:i+k], 2)] = True
    return all(codes)

if __name__ == '__main__':
    print(binary_code('00110110', 2))
    print(binary_code('01100', 2))
    print(binary_code('0110', 1))