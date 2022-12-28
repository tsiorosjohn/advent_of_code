

if __name__ == "__main__":

    house = 0
    elf = 0
    presents = 0
    while True:  # house loop
        house += 1
        while True:  # elf loop
            elf += 1
            if elf % house == 0:
                print(f"modulo {elf % house}")
                presents += elf * 10
                print(f"{house = } / {elf = } / {presents = } ")
                break
        print(f"xxx{house = } / {elf = } / {presents = } ")
        if house > 5:
            break