import string
with open("first.txt", "r") as f:
    txt = f.read()

character = string.ascii_lowercase + " "
# count = [0] * len(character)
# print(count)
# for c in txt:
#     for i in range(len(character)):
#         if c == character[i]:
#             count[i] += 1
#             break
#
# for i in range(len(character)):
#     if count[i] == 0:
#         continue
#     print(character[i], " : ", count[i])
track = {}
for c in txt:
    if c in track:
        track[c] += 1
    else:
        track[c] = 1

track["space"] = track.pop(" ")
print(track)
