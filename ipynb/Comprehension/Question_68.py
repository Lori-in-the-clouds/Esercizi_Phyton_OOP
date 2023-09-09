sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(" ")
print(list((len(i) for i in words if i != "the")))