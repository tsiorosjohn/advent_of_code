

with open("input.txt") as reader:
    all_calories = reader.readlines()

elves = []
elf_nr = 0
temp_cal = 0

for i, cal in enumerate(all_calories):
    if cal != '\n':
        temp_cal += int(cal.strip())
        # print(f"{elves[elf_nr] = }")
        print(f"{temp_cal = }")

    else:
        elves.append([temp_cal])
        elf_nr += 1
        temp_cal = 0
        print(f"{elf_nr = }")

print(elves)

print(max(elves))

