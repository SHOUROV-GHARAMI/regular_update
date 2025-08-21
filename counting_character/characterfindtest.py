
def counting_characters(text):
    counts = {}
    for ch in text:
        if('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            lower_ch = ch.lower()
            if lower_ch not in counts:
                counts[lower_ch] = 1
            else:
                counts[lower_ch] += 1


    for ch in sorted(counts.keys()):
        print(f"'{ch}' appears {counts[ch]} times")

text = 'For other languages or extensions, search for similar \"codelens" or "debug" related settings to disable the specific feature. '
counting_characters(text)