from tkinter import *
import xlsxwriter

window = Tk()
photo = PhotoImage(file = 'GIF2/picture06.gif')
h = photo.height()
w = photo.width()

photoR = [[0 for _ in range(h)] for _ in range(w)]
photoG = [[0 for _ in range(h)] for _ in range(w)]
photoB = [[0 for _ in range(h)] for _ in range(w)]

for i in range(w):
    for k in range(h):
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

workbook = xlsxwriter.Workbook('Excel/picture06_art.xlsx')

# RGB 값을 저장할 워크시트 생성
rgbWorksheet = workbook.add_worksheet('photoRGB')
rgbWorksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    rgbWorksheet.set_row(i, 9.5)  # 약 0.35

# Red 값을 저장할 워크시트 생성
redWorksheet = workbook.add_worksheet('Red')
redWorksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    redWorksheet.set_row(i, 9.5)  # 약 0.35

# Green 값을 저장할 워크시트 생성
greenWorksheet = workbook.add_worksheet('Green')
greenWorksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    greenWorksheet.set_row(i, 9.5)  # 약 0.35

# Blue 값을 저장할 워크시트 생성
blueWorksheet = workbook.add_worksheet('Blue')
blueWorksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    blueWorksheet.set_row(i, 9.5)  # 약 0.35

for i in range(w):
    for k in range(h):
        hexR = hex(photoR[i][k])
        hexG = hex(photoG[i][k])
        hexB = hex(photoB[i][k])
        hexStr = '#'
        if len(hexR[2:]) < 2:
            hexStr += '0' + hexR[2:]
        else:
            hexStr += hexR[2:]
        if len(hexG[2:]) < 2:
            hexStr += '0' + hexG[2:]
        else:
            hexStr += hexG[2:]
        if len(hexB[2:]) < 2:
            hexStr += '0' + hexB[2:]
        else:
            hexStr += hexB[2:]

        # RGB 값을 저장하는 워크시트에 데이터 저장
        cell_format = workbook.add_format()
        cell_format.set_bg_color(hexStr)
        rgbWorksheet.write(k, i, '', cell_format)

        # Red 값을 저장하는 워크시트에 데이터 저장
        redWorksheet.write(k, i, photoR[i][k])

        # Green 값을 저장하는 워크시트에 데이터 저장
        greenWorksheet.write(k, i, photoG[i][k])

        # Blue 값을 저장하는 워크시트에 데이터 저장
        blueWorksheet.write(k, i, photoB[i][k])



workbook.close()
print('Save. OK~')