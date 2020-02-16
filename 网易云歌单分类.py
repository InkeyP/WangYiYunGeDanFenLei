#coding=utf-8
lista = input("First list：")
liste = input("Last list：")

#listname = input("list name:")

from shutil import copyfile
from sys import exit
import os
import os.path

#lista = r"D:\Onedive\OneDrive - KABCY\Documents\编程\Python\网易云歌单分类\网易云歌单分类\Music"
#liste = r"D:\Onedive\OneDrive - KABCY\Documents\编程\Python\网易云歌单分类\网易云歌单分类\中文"

isExists=os.path.exists(liste)
if not isExists:
        os.makedirs(liste) 

def GetFileNameAndExt(filename):
    (filepath,tempfilename) = os.path.split(filename)
    (shotname,extension) = os.path.splitext(tempfilename)
    return shotname,extension

fn = liste + ".txt"

with open(fn, "r", encoding='UTF-8') as f:
    for line in f.readlines():
        line1 = line.split("-")
        name = line1[0]
        singer = line1[1]

        img = os.listdir(lista)
        
        for filename in img:
            filenm = GetFileNameAndExt(filename)
            name1 = filenm[0]
            name_a = name1.strip()
            name_b = name.strip()
            singer_b = singer.strip()
            #if name_b in name_a and singer_b in name_a:
            if name_b in name_a:
                first = lista + "\\" + filename
                second = liste + "\\" + filename
                try:
                    copyfile(first, second)
                    print("copy", name_a, "Yes")
                except:
                    print("No such a song!")