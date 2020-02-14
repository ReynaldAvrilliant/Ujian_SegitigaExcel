import xlrd
import xlsxwriter
import xlwt 
from xlwt import Workbook 


book = xlsxwriter.Workbook("segitigaexcel.xlsx")
sheet = book.add_worksheet("sheet1")

def segitigakata(y):
    z = ''
    x = 0
    kata = y.replace(' ', '')
    # Pola Segitiga
    pola = list(map(lambda row: row * (row + 1)/2, range(len(kata))))
    pola = list(map(int, pola))

    # Bentuk segitiga kata
    if len(kata) not in pola:
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
    else:
        for i in range(pola.index(len(kata))):
            for j in range(pola[i], pola[i + 1]):
                z += f"{kata[j]} "
                x += 1
            z += '\n'
        x = 0
    

    return z

row = 0
sheet.write(1,0,segitigakata("purwadhika"))
book.close()