from tkinter import filedialog as fd
from scan import read_qr_code


def scan():
    file = fd.askopenfilename()
    data = read_qr_code(file)
    return data
