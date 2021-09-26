import string
with open("file.txt", "r") as f:
    content = f.read()
text = ""
num = 0
character = string.ascii_lowercase + string.ascii_uppercase + " "
#Romove any unwanted character from the txt
for c in content:
    for i in range(len(character)):
        if c == character[i]:
            text += c
            break
print(text)
# for input1 in content:
#     if (num < len(content)):
#         if (input1 == ","):
#             num += 1
#             continue
#         elif (input1 == "."):
#             num += 1
#             continue
#         else:
#             text += input1
#             num += 1

txt = text.strip().split()
track = {}
for c in txt:
    if c in track:
        track[c] += 1
    else:
        track[c] = 1
print(f"Number of word {len(track)}")

print(track)
# print(text)