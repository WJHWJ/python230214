# DemoList.py
colors = ["red","green","blue"]
print(colors)

colors.append("white")
print(colors)
colors.append("black")
print(colors)
colors.insert(1, "yellow")
print(colors)
colors += ["red"]
print(colors)
print(colors.index("red"))
print(colors.count("red"))

colors += "red"
print(colors)
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)
colors.remove("red")
print(colors)
colors.extend(["red","pink","white"])
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

