# Frame development

# imports 
import os
import tkinter as tk
import logging as lg
import merge as m


def merge_pdf():
    lg.info("Working inside merge functions")
    path = folder.get()
    try:    
        lg.info("Trying to list all files and folder in present directory")
        files = os.listdir(path)
    except Exception as e:
        lg.warning("sorry path is wrong %s",e)
        lg.error("the error for %s",path)
        top = tk.Toplevel()
        top.title("Error")
        tk.Label(top,text="Given path is wrong").pack()
        top.mainloop()
    else:
        lg.info("Working on pdf_files merger function")
        pdf_files=[]
        for file in files:
            if file.split('.')[-1]=='pdf':
                pdf_files.append(file)
        if len(pdf_files)==0:
            top = tk.Toplevel()
            top.title("Error")
            tk.Label(top,text="No Pdf found").pack()
        lg.info("importing merge.py")
        m.PDFmerge(pdf_files,"output.pdf",path)
        
            
    

def search():
    # files in path given
    lg.info("extracting data from input field")
    path = folder.get()
    try:    
        lg.info("Trying to list all files and folder in present directory")
        files = os.listdir(path)
    except Exception as e:
        lg.warning("sorry path is wrong %s",e)
        lg.error("the error fro %s",path)
        top = tk.Toplevel()
        top.title("Error")
        tk.Label(top,text="Given path is wrong").pack()
        top.mainloop()
    else:
        # list of files in present directory
        lg.info("list of files in present directory")
        scrollbar=tk.Scrollbar(main_screen)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        mylist = tk.Listbox(main_screen,yscrollcommand = scrollbar.set)


        for file in files:  
            mylist.insert(tk.END,file)
        mylist.pack(side =tk.BOTTOM,fill=tk.BOTH,expand=True)
        scrollbar.config(command=mylist.yview)
# MAin Screen 
lg.info("Main screen created")
main_screen = tk.Tk()
main_screen.title("PDF Merger")






# frame 1 for search and merge options
lg.info("frame 1 for input path ,search and merge options")
frame = tk.Frame(main_screen)
frame.pack()
tk.Label(frame,text="Path").grid(row=0,column=0)
folder = tk.Entry(frame)
folder.grid(row=0,column=1)
find = tk.Button(frame,text="search",command=search,activeforeground="White",activebackground="Black")
find.grid(row=0,column=2)
merge = tk.Button(frame,text="Merge",command=merge_pdf,activeforeground="White",activebackground="Black")
merge.grid(row=0,column=3)



# main screen looping 
lg.info(" main screen looping for presentation")
main_screen.mainloop()