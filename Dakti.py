n = int(input())
words = []
for i in range(n):
   s = input()
   words.append(s)
   
for word in words:
    if word.find("1"):
        word.remove("1")
        words[0] = word
    elif word.find("2"):
        word.remove("2")
        words[1] = word
    elif word.find("3"):
        word.remove("3")
        words[2] = word