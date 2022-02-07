import pdb
import tkinter
from tkinter import filedialog

def str_to_hex(str_to_chg):

    tmp_bytes = bytes(str_to_chg, encoding='utf-8')
    tmp_chars = []
    for each_byte in tmp_bytes:
        tmp_chars.append('=' + str(hex(int(each_byte))).replace('0x', '').upper())
    return ''.join(tmp_chars)


fp = filename = tkinter.filedialog.askopenfilename()
wfile = r'contact2.1.vcf'
wf = open(wfile, 'w', encoding='utf-8')
try:
    with open(fp, 'r', encoding='utf-8') as file:
        all_content = file.readlines()
        ignore_lines = 0
        # pdb.set_trace()
        for line in all_content:
            if line[0:2] == 'N;':
                names = line[17:]
                s = wf.write('N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;' + str_to_hex(names.replace('\n', '')) + ';;;\n')
            elif line[0:3] == 'FN;':
                names = line[18:]
                s = wf.write('FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' + str_to_hex(names.replace('\n', '')) + '\n')
            elif line.startswith('VERSION:'):
                s = wf.write('VERSION:2.1\n')
            elif line[0:9] == 'ADR;HOME;':
                homes = line[28:]
                s = wf.write('ADR;HOME;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;;' + str_to_hex(homes.replace('\n', '')) + ';;;;\n')
            elif line[0:5] == 'NOTE;':
                notes = line[20:]
                s = wf.write('NOTE;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' + str_to_hex(notes.replace('\n', '')) + '\n')
            else:
                s = wf.write(line)
                ignore_lines = ignore_lines + 1
except Exception as ext:
    print("err:", ext)

wf.close()

