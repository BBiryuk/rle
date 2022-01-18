import itertools
import re


def encode(str):
    result = ""
    for key, freq in itertools.groupby(str):
        result += f"{len(list(freq))}" + key
    return result


def decode(str):
    result = ""
    lst = re.findall(r"(\d+.)", str)
    for i in lst:
        result += int(i[:-1]) * i[-1]
    return result


def main():
    str = input("> ")
    print(f"Исходные данные: {str}")

    result1 = encode(str)
    print(f"Кодирование: {result1}")

    result2 = decode(result1)
    print(f"Декодирование: {result2}")


if __name__ == "__main__":
    main()
