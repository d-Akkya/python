words = ["Donkey", "bad", "ganda"]

with open("F:/python/CHAPTER_9 - PS/file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("F:/python/CHAPTER_9 - PS/file.txt", "w") as f:
    f.write(content)