def dump(mem, f, packed=False, data_radix='HEX'):
    word_count, word_length = mem.shape
    if data_radix == 'HEX':
        print('memory_initialization_radix=16;', file=f)
        print('memory_initialization_vector=', file=f)
        for i in range(word_count):
            if packed:
                for j in range(word_length):
                    print(f'{mem[i][word_length-1-j]:02x}', end='', file=f)
            else:
                for j in range((word_length + 7) // 8):
                    word = 0
                    for k in range(8):
                        if j * 8 + k < word_length:
                            word |= mem[i][word_length - 1 - j * 8 - k] << (7 - k)
                    print(f'{word:02x}', end='', file=f)
            if i == word_count - 1:
                print(';', file=f)
            else:
                print(',', file=f)
    else:
        print('memory_initialization_radix=2;', file=f)
        for i in range(word_count):
            for j in range(word_length):
                if packed:
                    print(f'{mem[i][word_length-1-j]:08b}', end='', file=f)
                else:
                    print(f'{mem[i][word_length-1-j]}', end='', file=f)
            if i == word_count - 1:
                print(';', file=f)
            else:
                print(',', file=f)