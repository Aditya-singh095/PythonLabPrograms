import string


def analyze_text(text):
    # Remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces and split into words
    words = text.split()

    # Total word count
    total_words = len(words)

    # Word frequency
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Find palindromes
    palindromes = []

    for word in words:
        if len(word) > 1 and word == word[::-1]:
            if word not in palindromes:
                palindromes.append(word)

    # Display report
    print("\n--- Text Analysis Report ---")
    print("Total words:", total_words)

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(word, ":", count)

    print("\nPalindromes:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindromes found.")


def main():
    print("Enter your text.")
    print("Type END on a new line to finish:\n")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    text = "\n".join(lines)

    analyze_text(text)


if __name__ == "__main__":
    main()
