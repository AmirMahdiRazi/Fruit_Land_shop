#Write and Read
import csv
import os
from persiantools.jdatetime import JalaliDateTime
import asyncio
from Text import *

Find = False
name_File = ''
ID = 0

time =JalaliDateTime.now().strftime("%x => %Y %B %A %X")
name_File=str(time).split(' ')
name_File=name_File[0].replace('/','-')

def write_file(Order,Cost):
    time =JalaliDateTime.now().strftime("%x => %Y %B %A %X")
    global ID
    ID = '{:d}'.format(int(ID) + 1).zfill(10)
    
    if os.path.exists(f'dataset/{name_File}.txt'):
        # Write On File
        with open(f'dataset/{name_File}.txt','a',encoding='utf-8',newline='') as fwriter:
            all_keys=["ID","Order","Cost","Time"]
            
            writer = csv.DictWriter(fwriter,quotechar='"',quoting=csv.QUOTE_MINIMAL,fieldnames=all_keys)
            
            writer.writerow({"ID": ID, "Order": Order, "Cost": Cost, "Time": time})
           

          
# work on file(Find ID and if File Exists Check Has Key (:if do not key Create Key and All Row Shit Down) if file doesnot exists \
# Create File and got Key and in then find ID)
async def wof():
    global ID
    
    if os.path.exists(f'dataset/{name_File}.txt'):

        if int(ID) == 0:
            with open(f'dataset/{name_File}.txt', 'r', encoding='utf-8') as f:
                txt = f.readlines()
                if (len(txt) != 0):
                    # If file exists and dont have Key Create Key in file
                    keys=txt[0].split(",")
                    if not (keys[0] == "ID" and keys[1] == "Order" and keys[2] == "Cost" and keys[3] == "Time\n"):
                        with open(f'dataset/{name_File}.txt','w',encoding='utf-8',newline='') as fwriter:
                            all_keys=["ID,","Order,","Cost,","Time"]
                            fwriter.writelines(all_keys)
                            fwriter.writelines(txt)
                else:
                    # If file exists and dont have any row just Create Key in file 
                    with open(f'dataset/{name_File}.txt','w',encoding='utf-8',newline='') as fwriter:
                        all_keys=["ID,","Order,","Cost,","Time"]
                        fwriter.writelines(all_keys)
                        return
                if (txt[-1].split(",")[0].isnumeric()):
                    #Find ID
                    last_line = txt[-1].split(",")
                    ID = '{:d}'.format(int(last_line[0])).zfill(10)
    #if File dont exists
    else:
        with open(f'dataset/{name_File}.txt','w',encoding='utf-8',newline='') as fwriter:
            all_keys=["ID","Order","Cost","Time"]
            writer = csv.DictWriter(fwriter,quotechar='"',quoting=csv.QUOTE_MINIMAL,fieldnames=all_keys)
            writer.writeheader()
if not Find:
    asyncio.run(wof())
    Find = True

# def read_file():
#     with open(f'dataset/{name_File}.txt','r',encoding='utf-8') as reader:
#                 text=reader.read()
#                 _T = arabic_reshaper.reshape(text)
#                 t = bidi.algorithm.get_display(_T)  
#                 print(t)
#                 if  t == Header:
#                     print("ok")

def read_file(args):
    if (args == "today" or len(args) == 8) :
        file=name_File
    
        if os.path.exists(f'dataset/{file}.txt'):
            with open(f'dataset/{file}.txt','r',encoding='utf-8') as reader:
                text=reader.readlines()
                return text

        else :
            return False
    else:
        text=[]
        out = []
        count = 0
        for i in range(1,32):
            d = f'{i}'.zfill(2)
            file = f'{args}-{d}'
            if os.path.exists(f'dataset/{file}.txt'):
                with open(f'dataset/{file}.txt','r',encoding='utf-8') as reader:
                    text=reader.readlines()
                    if count >= 1 :
                        text.pop(0)
                    count += 1
                    out.append(text)
        if(len(out) > 0):
            return out
        else:
            return False


# print(read_file())
# write_file(Txt("آب کرفس(1) آب سیب (2)"),6000)
