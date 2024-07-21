def Caesarcode(cleartext='2 21WF Z1V'):
    order = 0
    i = 1
    list = []
    bool1 = bool2 = 0
    for x in cleartext:
        if x.isdigit():
            count = 10
            bool1 = 1
        if x.isalpha():
            count = 26
            bool2 = 1
    if bool1 and bool2:
        count = 130
    # print (count)
    while i < count:
        str = ''
        j = 0
        while j <= len(cleartext) - 1:
            if (cleartext[j] >= 'a' and cleartext[j] <= 'z'): order = 97  # a-z:97-122
            if (cleartext[j] >= 'A' and cleartext[j] <= 'Z'): order = 65  # A-Z:65-90
            if (cleartext[j] >= '0' and cleartext[j] <= '9'): order = 48  # 0-9:48-57
            if order in [65, 97]:
                letter = ord(cleartext[j]) - order  # ord()字符转换为ASCII码
                letter = (letter + i) % 26
                str = str + chr(order + letter)  # chr()ASCII码转换为字符
            elif order == 48:
                letter = ord(cleartext[j]) - order
                letter = (letter + i) % 10
                str = str + chr(order + letter)
            else:
                str = str + cleartext[j]
            j += 1
            order = 0
        i += 1
        list.append(str)
    return list


def main():
    # cleartext = str(input("明文:"))
    cleartext = '2 21WF Z1V'  # 0 09UD XNT
    ciphertext = Caesarcode(cleartext)
    for x in ciphertext:
        print(x)


if __name__ == "__main__":
    main()
