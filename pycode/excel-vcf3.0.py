import tkinter
import pandas as pd
import os
import time
from tkinter import *
from tkinter import filedialog


def run(filedir):
    data = pd.read_excel(filedir)
    rows = data.shape[0]
    txtName = r'phonenumbers.txt'
    f = open(txtName, 'x', encoding='utf-8')
    for i in range(1, rows):
        name = str(data.iloc[i, 0])
        phone = str(data.iloc[i, 1])
        home = str(data.iloc[i, 2])
        note = str(data.iloc[i, 3])
        if len(phone) == 11:
            new_context = "BEGIN:VCARD\n" \
                          + "VERSION:3.0\n" \
                          + "N;CHARSET=gb2312:" + str(name) + '\n' \
                          + "TEL;TYPE=CELL:" + str(phone) + '\n' \
                          + "ADR;HOME;CHARSET=gb2312:" + str(home) + "\n" \
                          + "NOTE;CHARSET=gb2312:" + str(note) + "\n" \
                          + "END:VCARD\n"
            f.write(new_context)
    f.close()
    os.rename(r'phonenumbers.txt', 'contact3.0.vcf')


filename = tkinter.filedialog.askopenfilename()
run(filename)
