def analyze_poem(lines):
    result = {}

    # Number of lines
    result["line_count"] = len(lines)

    # Number of words
    total_words = 0

    for line in lines:
        total_words += len(line.split())

    result["word_count"] = total_words

    # Longest line
    if lines:
        result["longest_line"] = max(lines, key=len)
    else:
        result["longest_line"] = ""

    # Common words that usually aren't useful for poetry analysis
    common_words = {
        "the", "a", "an", "and", "or", "but",
        "is", "are", "was", "were", "be", "been",
        "to", "of", "in", "on", "at", "for",
        "with", "from", "by", "as", "it",
        "he", "she", "they", "we", "you", "i",
        "this", "that", "these", "those"
    }

    # Clean and collect meaningful words
    words = []

    for line in lines:
        cleaned_line = line.lower()
        words.extend(cleaned_line.split())

    # Count meaningful words
    word_counts = {}

    for word in words:
        word = word.strip(".,!?;:\"'()")

        if word and word not in common_words:
            word_counts[word] = word_counts.get(word, 0) + 1

    result["word_counts"] = word_counts

    # Find repeated meaningful words
    repeated_words = {}

    for word, count in word_counts.items():
        if count > 1:
            repeated_words[word] = count

    result["repeated_words"] = repeated_words

    return result