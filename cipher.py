def num():
    alp = list(map(chr, range(97, 123)))
    alp.extend([",", ".", "!", "?"])

    def numcode():
        print(alp)
        string = input("Enter text to encode: ")
        num = int(input("Enter a passcode: "))
        numeric = list(map(int, range(num, num + 30)))
        print(numeric)
        output = ""
        for char in string:
            if char == " ":
                output += "* "
            else:
                output += str(numeric[alp.index(char)])
                output += " "
        print("Encoded message: " + output)

    def numdecode():
        output = input("Paste the encoded message:\n ")
        decode = output.split()
        de = int(input("Enter passcode for decrypting: "))
        text = ""
        numberlist = list(map(int, range(de, de + 30)))
        print(numberlist)
        for n in decode:
            if n == "*":
                text += " "
            else:
                text += alp[numberlist.index(int(n))]
        print("Decoded text: " + text)

    choice = int(input("Select an option\n1.Encode\n2.Decode\n"))
    if choice == 1:
        numcode()
    else:
        numdecode()


def morse():
    morse = {
        # Letters
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
        "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
        # Numbers
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        # Punctuation
        "&": ".-...", ",": "--..--", ".": ".-.-.-", "?": "..--..", " ": "  "}

    def morsecode():
        string = input("Enter string to encode: ")
        string = string.lower()
        output = ""
        for item in string:
            output += morse[item]
            output += " "
        print(output)

    def morsedecode():
        code = input("Paste the encoded text here: ")
        output = ""
        sp2 = code.split("  ")  # split between words
        for char in sp2:
            sp1 = char.split(" ")  # split between letters
            for item in sp1:
                for key, val in morse.items():
                    if (val == item):
                        output += key
            output += " "
        print(output)

    choice = int(input("1.Encode\n2.Decode\n"))
    if choice == 1:
        morsecode()
    else:
        morsedecode()


def letter():
    alp = list(map(chr, range(97, 123)))
    def lcode():
        string = input("Enter string to encode: ")
        string = string.lower()
        output = ""
        for char in string:
            if char == " ":
                output += "  "
            else:
                index = alp.index(char)
                output += alp[index - 1]
                if index == 25:
                    output += alp[0]
                else:
                    output +=alp[index+1]
        print(output)

    def ldecode():

        code = input("Paste the encoded text here: ")
        code=code.strip()
        output = ""
        for index in range(0, len(code), 2):
            if code[index] == " ":
                output += " "
            else:
                i = alp.index(code[index])

                if i==25:
                    output+=alp[0]
                else:
                    output+=alp[i+1]
        print(output)

    choice = int(input("1.Encode\n2.Decode\n"))
    if choice == 1:
        lcode()
    else:
        ldecode()


c = int(input("Select an option\n1.Number code\n2.Morse code\n3.Letter code\n"))
if (c == 1):
    num()
elif (c == 2):
    morse()
elif (c == 3):
    letter()
