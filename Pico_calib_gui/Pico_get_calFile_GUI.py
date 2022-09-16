import tkinter as tk
from tkinter import *
from tkinter.filedialog import FileDialog
import serial
import serial.tools.list_ports
import parse_settings_status
import parse_caldates
import parse_calcoeffs
import parse_ID
import parse_ver
from datetime import datetime
import tkinter.ttk as ttk

root= Tk()
root.title('Create Pico-pH Calibration File')
root.geometry('1200x800')

def selected(event):
   #myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() != 'Pico-pH COM Port':
        print(clicked.get()+' Selected')
        global port
        port = clicked.get().split()[0]
        print(port)
    else: 
        print('COM not selected')

def getcalinfo():
    ser = serial.Serial(port=port,baudrate='19200',bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

    ser.write('#IDNR\r\n'.encode('Ascii')) # get unique ID
    global idnr
    idnr = ser.read(100).decode('Ascii')
    print(idnr)
    #response = ('#IDNR 2636648693379505685')
    idnr = parse_ID.parse(idnr)

    ser.write('#VERS\r\n'.encode('Ascii')) # get unique ID
    global ver
    ver = ser.read(100).decode('Ascii')
    print(ver)
    # response = ('#VERS 4 1 405 1071 2 271')
    ver = parse_ver.parse(ver)

    ser.write('RMR1 30 0 24\r\n'.encode('Ascii')) # get sensor settings
    global settings_status
    settings_status = ser.read(100).decode('Ascii')
    print(settings_status)
    #settings_status = ('RMR1 30 0 24 1178796032 3 6 756 576 222757027 0 0 1 0 8 0 0 0 0 1000 0 0 0 0 0 0 0 0')
    settings_status = parse_settings_status.parse(settings_status)

    ser.write('RMR1 31 0 7\r\n'.encode('Ascii')) # get calibration dates
    global caldates
    caldates = ser.read(100).decode('Ascii')
    print(caldates)
    #caldates = ('RMR1 31 0 7 1054220830 996220902 900001231 0 0 0 0')
    caldates = parse_caldates.parse(caldates)

    ser.write('RMR1 1 0 30\r\n'.encode('Ascii')) # get calibration coefficients
    global calcoeffs
    calcoeffs = ser.read(150).decode('Ascii')
    print(calcoeffs)
    #calcoeffs = ('RMR1 1 0 30 1722488 0 20000 7500 66777 14000 20000 7500 0 57800 33900 0 0 904900 -5670 8082 1034000 -1108 -803 0 -16280 970 126 622367 1416295 -5853 0 0 0 0')
    calcoeffs = parse_calcoeffs.parse(calcoeffs)

    global calstring 
    calstring = settings_status+idnr+','+ver+'\n'+caldates+calcoeffs
    print(calstring)

    disp.config(text=calstring)
    ser.close()
    global filelocation
    filelocation = fileloc.get()

def save_text():
    txtfile = open(filelocation,'a')
    txtfile.write(calstring)
    txtfile.close()
    savelabel = Label(root, text='Calibration file Saved!')
    savelabel.pack()

ports = serial.tools.list_ports.comports()
clicked = StringVar()
clicked.set('Select Pico-pH COM Port')
drop = OptionMenu(root, clicked, *ports, command=selected)
drop.pack(pady=20)

label = Label(root, text = 'Enter desired calibration file location:')
label.pack()

fileloc = Entry(root,width=70)
fileloc.insert(END,r'C:\Users\taylo\Desktop\Pico_SN_CalFile_20220902.txt')
fileloc.pack()
filelocation = fileloc.get()

getbutton = Button(root, text='Get cal info', command = getcalinfo)
getbutton.pack(pady=20)

disp = Label(root, text='Calibration info will appear here!', height=10,justify= LEFT)
disp.pack()

savebutton = Button(root, text='Save cal info to file', command = save_text)
savebutton.pack(pady=20)

root.mainloop()
