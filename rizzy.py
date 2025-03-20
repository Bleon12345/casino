song = "The weather oustide is rizzy but the fire is so skibidii but since i've GYATT to go Ohio Ohio Ohio!"

still_water = []
words = song.split()

for word in words:
    for i in range(len(word)- 1):
        if word[i] == word[i+1]:
            still_water.append(word)
            break

print(still_water)

https://www.programiz.com/online-compiler/2uyvEyIPFH8rc
