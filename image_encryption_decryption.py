#use tkinter to create the gui
from tkinter import *
#HELP US TO OPENT THE FILE SELECTION OPTION
from tkinter import filedialog

#create the window sizes
root = Tk()
root.geometry("200x160")

#encrypt image function
def encrypt_image():
    file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg'),('png file','*.png')])
    if file1 is not None:
        print(file1) 
        file_name=file1.name
        #extract the key which is entered by the user
        key=entry1.get(1.0,END)
        print(file_name,key)
        #extract the data from that specific file
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image= bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)    
        fi1.close()


#button that will open the file dialog box
b1=Button(root,text="encrypt",command=encrypt_image)
b1.place(x=70,y=10)

#entry widget or the text box widget to input the password
entry1=Text(root,height=1,width=10)
entry1.place(x=50,y=50)

root.mainloop() 