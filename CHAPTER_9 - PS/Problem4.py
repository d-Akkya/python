word = "Donkey"

with open("F:/python/CHAPTER_9 - PS/file.txt", "r") as f:
    content = f.read()

newContent = content.replace(word, "######")

with open("F:/python/CHAPTER_9 - PS/file.txt", "w") as f:
    f.write(newContent)