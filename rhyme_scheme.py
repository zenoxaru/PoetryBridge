import pronouncing


def detect_rhyme_scheme(lines):
    rhyme_parts = []

    for line in lines:
        words = line.split()

        if not words:
            rhyme_parts.append(None)
            continue

        word = words[-1].lower()
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

    return " ".join(labels)