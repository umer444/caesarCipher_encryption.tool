message = '`7Xc7kc\h7JJIHK'
key = 23
mode = "decrypt"
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
t = ""
s = t
message = message.upper()

for words in message:
    if words in LETTERS:
        num = LETTERS.find(words)
        if mode == "encrypt":
            num = num + key

        elif mode == "decrypt":
            num = num - key
            s = t + LETTERS[num]

        if num >= len(LETTERS):
            num = num-len(LETTERS)
        elif num <= 0:
            num = num+len(LETTERS)

        s = t + LETTERS[num]
    else:
        translated = translated + words

    print(s)
