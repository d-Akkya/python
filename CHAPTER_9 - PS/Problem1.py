f = open("F:/python/CHAPTER_9 - PS/poem.txt")
content = f.read()
if("Twinkle" in content):
    print("File contains the twinkle word")

else:
    print("File doesn't contain any twinkle word")

print(content)

f.close()
