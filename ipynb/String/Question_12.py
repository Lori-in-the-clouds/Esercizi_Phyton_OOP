def concat_ing(string : str):
    if len(string) < 3:
        return string
    if string[-3:] == "ing":
      return string+"ly"
    else:
      return string+"ing"

print(concat_ing("barting"))
print(concat_ing("cc"))
print(concat_ing("hello"))