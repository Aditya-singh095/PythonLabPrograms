from collections import Counter


def clean_text(text):
    """Remove spaces/punctuation and convert to lowercase."""
    return "".join(
        char.lower()
        for char in text
        if char.isalnum()
    )


def are_anagrams(text1, text2):
    """Check whether two texts are anagrams."""
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    # Sorting-based comparison
    return sorted(text1) == sorted(text2)


def are_anagrams_count(text1, text2):
    """Check anagrams using dictionary counting."""
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    return Counter(text1) == Counter(text2)


def build_pattern_key(text):
    """Create an immutable tuple key for fast lookup."""
    cleaned = clean_text(text)

    # Sorted tuple can be used as a dictionary key
    return tuple(sorted(cleaned))


def find_anagrams(words, target):
    """Find all words/phrases that are anagrams of target."""
    target_key = build_pattern_key(target)

    return [
        word for word in words
        if build_pattern_key(word) == target_key
    ]


# -------------------------
# Examples
# -------------------------

print("Anagram Check:")
print(are_anagrams("listen", "silent"))

print("\nPhrase Anagram Check:")
print(are_anagrams("The Eyes", "They See"))

print("\nCounter Method:")
print(are_anagrams_count("Dormitory", "Dirty Room"))


words = [
    "listen",
    "silent",
    "enlist",
    "hello",
    "inlets",
    "world"
]

print("\nMatching Anagrams:")
print(find_anagrams(words, "listen"))


# -------------------------
# Dictionary Pattern Lookup
# -------------------------

groups = {}

for word in words:
    key = build_pattern_key(word)

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print("\nAnagram Groups:")

for key, group in groups.items():
    if len(group) > 1:
        print(group)
