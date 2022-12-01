with open("data.txt") as Data:
    Elf = []
    Calories = 0
    for line in Data:
        if str(line) == "\n":
            Elf.append(Calories)
            Calories = 0
        else:
            Calories += int(line.replace("\n", ""))
        
print(max(Elf))
# Part 2
Elf.pop(Elf.index(max(Elf)))
print(max(Elf))
Elf.pop(Elf.index(max(Elf)))
print(max(Elf))
Elf.pop(Elf.index(max(Elf)))
