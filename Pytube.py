from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

def click_download():
    if getURL.get() == "":
        messagebox.showinfo("ERROR", "ENTER URL ")
        return
    elif getLoc.get() == "":
        messagebox.showinfo("ERROR", "ENTER LOCATION ")
        return

    select = listbox.curselection()
    quality = videos[select[0]]
    location = getLoc.get()
    quality.download(location)
    messagebox.showinfo("Download Successful", yt.title + " has been downloaded successfully!")


def confirm_URL():
    # Get URL of the Video
    url = getURL.get()
    print(url)

    # Create Object to hold the URL
    global yt
    yt = YouTube(url)
    print(yt.title)

    # Get the Quality of the Videos and store in the 'videos' variable
    global videos
    videos = yt.streams.filter(progressive=True)

    # Get Quality and display as list in the Listbox
    count = 1
    for v in videos:
        listbox.insert(END, str(count) + ". " + str(v) + "\n\n")
        count += 1


def browse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)


def clear_all():
    getURL.set("")
    getLoc.set("")
    listbox.delete(0, END)


# Create Root Object
root = Tk()

# Set Title
root.title("PyTube")

# Set size of window
root.geometry("855x500")
# backgroundcolor
root.configure(bg="#B2BEB5")

# Make the Window not Resizeable
root.resizable(False, False)

# Set Labels
headLabel = Label(root, bg="#B2BEB5", fg="#8C0000", text="PyTube", font=("Rockwell", 30)).grid(row=0, column=1, padx=10,
                                                                                               pady=10)
urlLabel = Label(root, bg="#B2BEB5", text="URL:", font=("Verdana", 13)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel = Label(root, bg="#B2BEB5", text="SELECT QUALITY", font=("Verdana", 13)).grid(row=2, column=0, padx=10,
                                                                                           pady=10)
locLabel = Label(root, bg="#B2BEB5", text="LOCATION", font=("Verdana", 13)).grid(row=3, column=0, padx=10, pady=10)

# Get Input
getURL = StringVar()
getLoc = StringVar()

# Set Entry
urlEntry = Entry(root, font=("Century Gothic", 12), bg='#D9C6A5', textvariable=getURL, width=50, bd=3, relief=SUNKEN,
                 borderwidth=1).grid(row=1, column=1, padx=10, pady=10)
browseEntry = Entry(root, font=("Century Gothic", 12), bg='#D9C6A5', textvariable=getLoc, width=50, bd=3, relief=SUNKEN,
                    borderwidth=1).grid(row=3, column=1, padx=10, pady=10)

# Box for video Quality selection
listbox = Listbox(root, font=("Century Gothic", 11), bg='#D9C6A5', width=56, height=12, bd=3, relief=RAISED,
                  borderwidth=1)
listbox.grid(row=2, column=1, padx=10, pady=10)

# Buttons
confirmButton = Button(root, text="CONFIRM URL", bg='#FFCCCB', activebackground='#FFCCCB', font=("Century Gothic", 10),
                       width=15, relief=RAISED, borderwidth=1, command=confirm_URL).grid(row=1, column=2, padx=10,
                                                                                         pady=10)
browseButton = Button(root, text="BROWSE", bg='#FFCCCB', activebackground='#B4E197', font=("Century Gothic", 10),
                      width=15, relief=RAISED, borderwidth=1, command=browse).grid(row=3, column=2, padx=10, pady=10)
downloadButton = Button(root, text="DOWNLOAD", bg='#FFCCCB', activebackground='#FFCCCB', font=("Century Gothic", 10),
                        width=15, relief=RAISED, borderwidth=1, command=click_download).grid(row=4, column=1, padx=10,
                                                                                             pady=10)
clearallButton = Button(root, text="CLEAR ALL", bg='#FFCCCB', activebackground='#B4E197', font=("Century Gothic", 10),
                        width=15, relief=RAISED, borderwidth=1, command=clear_all).grid(row=4, column=2, padx=10,
                                                                                        pady=10)

# Set an infinite loop so window stays in view
root.mainloop()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
