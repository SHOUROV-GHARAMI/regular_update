
def counting_characters(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        
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

filename = "input.txt" 
counting_characters(input.txt)