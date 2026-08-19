print("PoetryBridge - Rhyme Test")

lines = []

print("Enter your poem.")
print("Type END when finished.")

while True:
    line = input("> ")

    if line == "END":
        break

    if line.strip():
        lines.append(line)

print()
print("Rhyme comparison:")

for i in range(len(lines) - 1):
    word1 = lines[i].split()[-1].lower()
    word2 = lines[i + 1].split()[-1].lower()

    ending1 = word1[-3:]
    ending2 = word2[-3:]

    print(word1, "->", ending1)
    print(word2, "->", ending2)

    if ending1 == ending2:
        print("These lines may rhyme.")
    else:
        print("These lines do not match.")

    print()
