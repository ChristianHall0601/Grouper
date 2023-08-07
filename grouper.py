from tkinter import *
from tkinter.filedialog import *
import os

main_window = Tk()
main_window.geometry("800x500")
main_window.resizable(False, False)
main_window.title("Grouper")
main_window.configure(bg="#D7ECFF")

global fromDir
global imgDir
global vidDir
global musDir
global docDir

def getFromDir():
    global fromDir
    fromDir = askdirectory()
    showFromDir.config(text=str(fromDir))
def getImgDir():
    global imgDir
    imgDir = askdirectory()
    showImgDir.config(text=str(imgDir))
def skipImgDir():
    global imgDir
    imgDir = None
    showImgDir.config(text="Skipped")
def getVidDir():
    global vidDir
    vidDir = askdirectory()
    showVidDir.config(text=str(vidDir))
def skipVidDir():
    global vidDir
    vidDir = None
    showVidDir.config(text="Skipped")
def getMusDir():
    global musDir
    musDir = askdirectory()
    showMusDir.config(text=str(musDir))
def skipMusDir():
    global musDir
    musDir = None
    showMusDir.config(text="Skipped")
def getDocDir():
    global docDir
    docDir = askdirectory()
    showDocDir.config(text=str(docDir))
def skipDocDir():
    global docDir
    docDir = None
    showDocDir.config(text="Skipped")
def sortFiles():
    #os.listdir(fromDir) will list all files in a folder (this includes folders inside fromDir)
    unsorted = os.listdir(fromDir)
    for i in range(len(unsorted)):
        #use unsorted[i] when moving files around myFile will be altered
        myFile = unsorted[i].lower()
        if ((myFile.endswith(".png") or myFile.endswith(".jpg") or myFile.endswith(".jpeg") or myFile.endswith(".gif") or myFile.endswith(".tiff") or myFile.endswith(".raw")) and imgDir != None):
            try:
                os.rename(fromDir + "\\" + unsorted[i], imgDir + "\\" + unsorted[i])
            except:
                print("duplicate: " + unsorted[i])
        elif ((myFile.endswith(".mp4") or myFile.endswith(".mov") or myFile.endswith(".webm") or myFile.endswith(".mxf") or myFile.endswith(".avi") or myFile.endswith(".avchd")) and vidDir != None):
            try:
                os.rename(fromDir + "\\" + unsorted[i], vidDir + "\\" + unsorted[i])
            except:
                print("duplicate: " + unsorted[i])
        elif ((myFile.endswith(".mp3") or myFile.endswith(".wav") or myFile.endswith(".pcm") or myFile.endswith(".aiff") or myFile.endswith(".aac") or myFile.endswith(".ogg") or myFile.endswith(".wma") or myFile.endswith(".flac") or myFile.endswith(".alac") or myFile.endswith(".wma")) and musDir != None):
            try:
                os.rename(fromDir + "\\" + unsorted[i], musDir + "\\" + unsorted[i])
            except:
                print("duplicate: " + unsorted[i])
        elif ((myFile.endswith(".pdf") or myFile.endswith(".docx") or myFile.endswith(".zip") or myFile.endswith(".doc") or myFile.endswith(".html") or myFile.endswith(".htm") or myFile.endswith(".xls") or myFile.endswith(".xlsx") or myFile.endswith(".ods") or myFile.endswith(".ppt") or myFile.endswith(".pptx") or myFile.endswith(".txt") or myFile.endswith(".7z")  or myFile.endswith(".rar")) and docDir != None):
            try:
                os.rename(fromDir + "\\" + unsorted[i], docDir + "\\" + unsorted[i])
            except:
                print("duplicate: " + unsorted[i])
    finished_window = Tk()
    finished_window.geometry("400x200")
    finished_window.resizable(False, False)
    finished_window.title("Grouper")
    finished_window.configure(bg="#D7ECFF")

    #This label is associated with the finished window
    finishedLbl = Label(finished_window, text="The program is finished!\nAny duplicates are still in the sorted folder", font =("Times New Roman", 16), bg="#D7ECFF")
    finishedLbl.place(anchor=CENTER, relx = 0.5, rely = 0.5)
# path = askdirectory()

# Labels will display output to user
welcome = Label(main_window, text="GROUPER", font=("Times New Roman", 18), bg="#D7ECFF")
welcome.place(relx = 0.5, y = 20, anchor=CENTER)
description = Label(main_window, text="This application sorts many types of files so you don't have to", font=("Times New Roman", 12), bg = "#D7ECFF")
description.place(relx = 0.5, y = 40, anchor=CENTER)

# These labels are all associated with the from directory
fromDirLbl = Label(main_window, text="Choose a folder that you want sorted:", font=("Times New Roman", 16), bg="#D7ECFF")
fromDirLbl.place(x = 50, y = 100)
fromLbl = Label(main_window, text="From:", font=("Times New Roman", 8), bg="#D7ECFF")
fromLbl.place(x = 50, y = 130)
showFromDir = Label(main_window, text="", font=("Times New Roman", 8), bg="#D7ECFF")
showFromDir.place(x = 120, y = 130)

# These labels are all associated with the image directory
imgDirLbl = Label(main_window, text="Choose a folder to put the image files in:", font=("Times New Roman", 16), bg="#D7ECFF")
imgDirLbl.place(x = 50, y = 170)
imgLbl = Label(main_window, text="Images:", font=("Times New Roman", 8), bg="#D7ECFF")
imgLbl.place(x = 50, y = 200)
showImgDir = Label(main_window, text="", font=("Times New Roman", 8), bg="#D7ECFF")
showImgDir.place(x = 120, y = 200)

# These labels are all associated with the video directory
vidDirLbl = Label(main_window, text="Choose a folder to put the video files in:", font=("Times New Roman", 16), bg="#D7ECFF")
vidDirLbl.place(x = 50, y = 240)
vidLbl = Label(main_window, text="Videos:", font=("Times New Roman", 8), bg="#D7ECFF")
vidLbl.place(x = 50, y = 270)
showVidDir = Label(main_window, text="", font=("Times New Roman", 8), bg="#D7ECFF")
showVidDir.place(x = 120, y = 270)

# These labels are all associated with the music directory
musDirLbl = Label(main_window, text="Choose a folder to put the music files in:", font=("Times New Roman", 16), bg="#D7ECFF")
musDirLbl.place(x = 50, y = 310)
musLbl = Label(main_window, text="Music:", font=("Times New Roman", 8), bg="#D7ECFF")
musLbl.place(x = 50, y = 340)
showMusDir = Label(main_window, text="", font=("Times New Roman", 8), bg="#D7ECFF")
showMusDir.place(x = 120, y = 340)

# These labels are all associated with the document directory
docDirLbl = Label(main_window, text="Choose a folder to put the document files in:", font=("Times New Roman", 16), bg="#D7ECFF")
docDirLbl.place(x = 50, y = 380)
docLbl = Label(main_window, text="Documents:", font=("Times New Roman", 8), bg="#D7ECFF")
docLbl.place(x = 50, y = 410)
showDocDir = Label(main_window, text="", font=("Times New Roman", 8), bg="#D7ECFF")
showDocDir.place(x = 120, y = 410)

#Buttons

#These buttons are associated with the from directory
fromBtn = Button(main_window, text= "Choose folder", font=("Times New Roman", 12), bd = "5", command=getFromDir)
fromBtn.place(x = 450, y = 95)

#These buttons are associated with the img directory
imgBtn = Button(main_window, text= "Choose folder", font=("Times New Roman", 12), bd = "5", command=getImgDir)
imgBtn.place(x = 450, y = 165)
imgBtnSkip = Button(main_window, text= "Skip", font=("Times New Roman", 12), bd = "5", command=skipImgDir)
imgBtnSkip.place(x = 600, y = 165)

#These buttons are associated with the video directory
vidBtn = Button(main_window, text= "Choose folder", font=("Times New Roman", 12), bd = "5", command=getVidDir)
vidBtn.place(x = 450, y = 235)
vidBtnSkip = Button(main_window, text= "Skip", font=("Times New Roman", 12), bd = "5", command=skipVidDir)
vidBtnSkip.place(x = 600, y = 235)

#These buttons are associated with the music directory
musBtn = Button(main_window, text= "Choose folder", font=("Times New Roman", 12), bd = "5", command=getMusDir)
musBtn.place(x = 450, y = 305)
musBtnSkip = Button(main_window, text= "Skip", font=("Times New Roman", 12), bd = "5", command=skipMusDir)
musBtnSkip.place(x = 600, y = 305)

#These buttons are associated with the document directory
docBtn = Button(main_window, text= "Choose folder", font=("Times New Roman", 12), bd = "5", command=getDocDir)
docBtn.place(x = 450, y = 375)
docBtnSkip = Button(main_window, text= "Skip", font=("Times New Roman", 12), bd = "5", command=skipDocDir)
docBtnSkip.place(x = 600, y = 375)

#This button will begin the sorting functions
sortBtn = Button(main_window, text= "Sort", font=("Times New Roman", 12), bd = "5", command=sortFiles)
sortBtn.place(x = 700, y = 450)


main_window.mainloop()
