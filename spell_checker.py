from spellchecker import SpellChecker

# Initialize spell checker
spell = SpellChecker()

paragraph = "I am lerning Pythn. It's fun an powerful."

paragraph_no_dots = paragraph.replace(".", "")

words = paragraph_no_dots.split()

misspelled = spell.unknown(words)

print(paragraph)

for word in misspelled:
    print(f"{word} -> {spell.correction(word)}")

