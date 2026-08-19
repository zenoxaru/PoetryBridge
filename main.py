from analyzer import analyze_poem
import pronouncing

print("================================")
print("        POETRYBRIDGE")
print("================================")
print("Enter your poem one line at a time.")
print("When you are finished, type END.")

lines = []

while True:
    line = input("> ")

    if line == "END":
        break

    if line.strip():
        lines.append(line)

print()
print("========== ANALYSIS ==========")

# Count lines
print("Number of lines:", len(lines))

# Count words
total_words = 0

for line in lines:
    total_words += len(line.split())

print("Number of words:", total_words)

# Find longest line
if lines:
    longest_line = max(lines, key=len)
    print("Longest line:", longest_line)

# Clean and collect words
words = []

for line in lines:
    cleaned_line = line.lower()
    words.extend(cleaned_line.split())

# Count words
word_counts = {}

for word in words:
    word = word.strip(".,!?;:\"'()")

    if word:
        word_counts[word] = word_counts.get(word, 0) + 1

# Word frequency
print()
print("Word frequency:")

for word, count in word_counts.items():
    print(word, ":", count)

# Repeated words
print()
print("Repeated words:")

found_repeated = False

for word, count in word_counts.items():
    if count > 1:
        print(word, ":", count)
        found_repeated = True

if not found_repeated:
    print("No repeated words found.")

# Rhyme scheme
print()
print("Rhyme scheme:")

rhyme_parts = []

for line in lines:
    words_in_line = line.split()

    if not words_in_line:
        rhyme_parts.append(None)
        continue

    word = words_in_line[-1].lower()
    phones = pronouncing.phones_for_word(word)

    if phones:
        rhyme = pronouncing.rhyming_part(phones[0])
        rhyme_parts.append(rhyme)
    else:
        rhyme_parts.append(None)

labels = []
rhyme_labels = {}
next_label = "A"

for rhyme in rhyme_parts:
    if rhyme is None:
        labels.append("?")
        continue

    if rhyme not in rhyme_labels:
        rhyme_labels[rhyme] = next_label
        next_label = chr(ord(next_label) + 1)

    labels.append(rhyme_labels[rhyme])

print(" ".join(labels))

print()
print("========== END ==========")
