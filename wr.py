#Write and Read
import csv
import os
from persiantools.jdatetime import JalaliDateTime
import asyncio
from Text import *

Find = False

ID = 0

def write_file(Order,Cost):
    time =JalaliDateTime.now().strftime("%x => %Y %B %A %X")
    print(Order)
    
    global ID
    ID = '{:d}'.format(int(ID) + 1).zfill(10)
    if os.path.exists("Myfile.txt"):
    
        # Write On File
        with open('..//Myfile.txt','a',encoding='utf-8',newline='') as fwriter:
            all_keys=["ID","Order","Cost",'Time']
            
            writer = csv.DictWriter(fwriter,quotechar='"',quoting=csv.QUOTE_MINIMAL,fieldnames=all_keys)
            
            writer.writerow({"ID": ID, "Order": Order, "Cost": Cost, "Time": time})
            
            
# work on file(Find ID and if File Exists Check Has Key (:if do not key Create Key and All Row Shit Down) if file doesnot exists \
# Create File and got Key and in then find ID)
async def wof():
    global ID
    if os.path.exists("../Myfile.txt"):

        if int(ID) == 0:
            with open('../Myfile.txt', 'r', encoding='utf-8') as f:
                txt = f.readlines()
                if (len(txt) != 0):
                    # If file exists and dont have Key Create Key in file
                    keys=txt[0].split(",")
                    if not (keys[0] == "ID" and keys[1] == "Order" and keys[2] == "Cost" and keys[3] == "Time\n"):
                        with open('../Myfile.txt','w',encoding='utf-8',newline='') as fwriter:
                            all_keys=["ID,","Order,","Cost,",'Time\n']
                            fwriter.writelines(all_keys)
                            fwriter.writelines(txt)
                else:
                    # If file exists and dont have any row just Create Key in file 
                    with open('../Myfile.txt','w',encoding='utf-8',newline='') as fwriter:
                        all_keys=["ID,","Order,","Cost,",'Time\n']
                        fwriter.writelines(all_keys)
                        return
                if (txt[-1].split(",")[0].isnumeric()):
                    #Find ID
                    last_line = txt[-1].split(",")
                    ID = '{:d}'.format(int(last_line[0])).zfill(10)
    #if File dont exists
    else:
        with open('../Myfile.txt','w',encoding='utf-8',newline='') as fwriter:
            all_keys=["ID","Order","Cost",'Time']
            writer = csv.DictWriter(fwriter,quotechar='"',quoting=csv.QUOTE_MINIMAL,fieldnames=all_keys)
            writer.writeheader()
if not Find:
    asyncio.run(wof())
    Find = True

# def read_file():
#     with open('Myfile.txt','r',encoding='utf-8') as reader:
#                 text=reader.read()
#                 _T = arabic_reshaper.reshape(text)
#                 t = bidi.algorithm.get_display(_T)  
#                 print(t)
#                 if  t == Header:
#                     print("ok")

def read_file():
    with open('../Myfile.txt','r',encoding='utf-8') as reader:
        text=reader.readlines()
        return text
# print(read_file())
# write_file(Txt("آب کرفس(1) آب سیب (2)"),6000)
