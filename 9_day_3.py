def is_pangram(text, alphabet):
    text = text.replace(" ", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text_set = set(text.lower())
    alpha = set(alphabet)
    if len(text_set.symmetric_difference(alpha)) == 0:
        res = True
    else:
        res = False
    return res

text_en = "The five boxing wizards jump quickly"
a_en = 'abcdefghijklmnopqrstuvwxyz'
print(text_en, " --- text is a pangram? ", is_pangram(text_en, a_en))


text_lv = "Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!"
a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(text_lv, " --- text is a pangram? ", is_pangram(text_lv, a_lv))

text_not = "Šis nav pangrams"
print(text_not, " --- text is a pangram? ", is_pangram(text_not, a_lv))
