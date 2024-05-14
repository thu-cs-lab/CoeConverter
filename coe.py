def dump(mem, f, data_radix):
    word_count, word_length = mem.shape
    if data_radix == 'HEX':
        print('memory_initialization_radix=16;', file=f)
        print('memory_initialization_vector=', file=f)
        for i in range(word_count):
            for j in range(word_length):
                print(f'{mem[i][word_length-1-j]:02x}', end='', file=f)
            if i == word_count - 1:
                print(';', file=f)
            else:
                print(',', file=f)
    else:
        print('memory_initialization_radix=2;', file=f)
        for i in range(word_count):
            for j in range(word_length):
                print(f'{mem[i][word_length-1-j]:08b}', end='', file=f)
            if i == word_count - 1:
                print(';', file=f)
            else:
                print(',', file=f)