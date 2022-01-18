import itertools
import re


def encode(str):
    result = ""
    for key, freq in itertools.groupby(str):
        result += f"{len(list(freq))}" + key

    lst = re.findall(r"(\d+.)", result)
    lst.append("end")

    result = ""; count = 0; clipboard = ""

    for i in range(len(lst)-1):
        if lst[i][:-1] == "1":
            clipboard += lst[i][-1]
            count += 1
            if lst[i+1][:-1] != "1" or lst[i] == lst[-1]:
                result += f"-{count}" + clipboard
        else:
            result += lst[i]
            clipboard = ""
            count = 0
    return result


def decode(str):
    result = ""
    lst = re.findall(r"(-?\d+[^0123456789-]+)", str)
    for i in lst:
        if i[0] == "-":
            for j in i[1:]:
                if j.isalpha():
                    result += j
        else:
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
