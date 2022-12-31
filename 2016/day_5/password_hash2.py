import hashlib

if __name__ == "__main__":
    door_id = 'cxdnnyjw'
    # door_id = 'abc'

    password_d = {}
    integer = 0
    while True:  # till 8 chars of pwd will be found
        while True:  # till an md5 with 5-0s will be found
            integer += 1
            temp_md5 = hashlib.md5((door_id + str(integer)).encode('utf-8')).hexdigest()
            if temp_md5.startswith('00000'):
                position = temp_md5[5]
                pwd_char = temp_md5[6]
                print(f"{integer = }, md5: {temp_md5} // 6th (position): {position}, 7th (pwd char): {pwd_char}")
                if position in '01234567':
                    if position not in password_d:
                        password_d[position] = pwd_char
                    print(f"temp {sorted(password_d.items()) = } ")
                    break
        if len(password_d) == 8:
            break
    print(f"Final dict - {sorted(password_d.items()) = }")
    password_chars = ''
    for char in sorted(password_d.items()):
        password_chars += char[1]
    print(f"Final pwd chars - {password_chars = }")

