marks = {
    "Akkya": 89,
    "Parshya": 100,
    "Rohya": 75,
    0: "Akkya"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Akkya": 92, "Prajakta": 98})
# print(marks)

print(marks.get("Akkya2"))  #Prints None
print(marks["Akkya2"])  #Returns an Error