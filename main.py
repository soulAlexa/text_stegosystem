def bit_cod(ss):
    Out = ''
    ss += '\0'
    for i in ss:
        h = format(ord(i), 'b')
        while len(h) < 8:
            h = '0' + h
        Out += h + ' '
    return Out

def stego_cod(text, cod_text):
    bite_cod_text = bit_cod(cod_text)
    flag_1 = 0
    ret_text = ''
    for i, j in enumerate(text):
        if flag_1 > len(bite_cod_text) - 1:
            ret_text += j
            continue
        if bite_cod_text[flag_1] == ' ':
            flag_1 += 1
        if text[i] == ' ' and (text[i-1] == '.' or text[i-2] == '.'):
            continue
        if j == '.' and bite_cod_text[flag_1] == '0':
            ret_text += j
            flag_1 += 1
        elif j == '.' and bite_cod_text[flag_1] == '1':
            flag_1 += 1
            ret_text += j
            ret_text += ' '
        else:
            ret_text += j
    return ret_text


def stego_decod(text):
    binary_str = ''
    out_str = ''
    flag_1 = 0
    for i, j in enumerate(text):
        if j == '.' and text[i+1] != ' ':
            flag_1 += 1
            binary_str += '0'
        elif j == '.' and text[i+1] == ' ':
            flag_1 += 1
            binary_str += '1'
        if flag_1 == 8:
            c = chr(int(binary_str, 2))
            if c == '\0':
                break
            out_str += c
            binary_str = ''
            flag_1 = 0
    return out_str


if __name__ == '__main__':
    f = open('test_1.txt', 'r+')
    text = f.read()
    text2 = stego_cod(text, 'Hello DumpHous_man123')
    print(f'Исходный текст имеет длину {len(text)} символа \nТекст с секретом имеет длину {len(text2)} символа')
    f.close()
    f_1 = open('test_3.txt', 'w')
    f_1.write(text2)
    f_1.close()
    f_2 = open('test_2.txt', 'w')
    print(stego_decod(text2))
    f_2.write(stego_decod(text2))
    f_2.close()



