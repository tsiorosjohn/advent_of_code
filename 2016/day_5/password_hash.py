import hashlib

if __name__ == "__main__":
    door_id = 'cxdnnyjw'
    # door_id = 'abc'

    password = ''
    count = 0
    for i in range(8):

        while True:
            count += 1
            temp_md5 = hashlib.md5((door_id + str(count)).encode('utf-8')).hexdigest()
            if temp_md5.startswith('00000'):
                print(count, temp_md5)
                password += temp_md5[5]
                break
    print(f"{password = }")
