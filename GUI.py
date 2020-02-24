### WILL NOT WORK WITHOUT A SETUP POSTGRESQL DATABASE

from tkinter import *
import Backend
import sys

def view_command():
    lb_Books.delete(0,END)
    n=0
    for r in Backend.View():
        n+=1
        title = r[0]
        author = r[1]
        year = r[2]
        isbn = round(r[3])
        lb_Books.insert(END, f"{n}. {title}, {author}, {year}, {isbn}")

def search_command():
    entries = read_entries()
    t = entries[0]
    a = entries[1]
    y = entries[2]
    i = entries[3]
    lb_Books.delete(0,END)
    n=0
    for r in Backend.Search(t,a,y,i):
        n+=1
        title = r[0]
        author = r[1]
        year = r[2]
        isbn = r[3]
        lb_Books.insert(END, f"{n}. {title}, {author}, {year}, {isbn}")

def read_entries():
    title_entry = ""
    author_entry = "Fuckyourself"
    year_entry = 0
    isbn_entry = 0
    if title_text.get() != "": 
        try: 
            title_entry = str(title_text.get())
        except:
            title_entry = ""
    if author_text.get() != "": 
        try: 
            author_entry = str(author_text.get())
        except:
            author_entry = ""
    if year_text.get() != "": 
        try: 
            year_entry = int(year_text.get())
        except:
            year_entry = 0
    if isbn_text.get() != "": 
        try: 
            isbn_entry = int(isbn_text.get())
        except:
            isbn_entry = 0
    return title_entry, author_entry, year_entry, isbn_entry

def add_command():
    entries = read_entries()
    t = entries[0]
    a = entries[1]
    y = entries[2]
    i = entries[3]
    Backend.Insert(t,a,y,i)
    view_command()

def update_command():
    entries = read_entries()
    t = entries[0]
    a = entries[1]
    y = entries[2]
    i = entries[3]
    Backend.Update(title=t,author=a,year=y,isbn=i)
    view_command()

def delete_command():
    entries = read_entries()
    t = entries[0]
    Backend.Delete(t)
    view_command()

def lb_Books_selection_change(event):
    w = event.widget
    try:
        index = int(w.curselection()[0])
        value = w.get(index)
        value = value[3:].split(", ")
        
        #Change Entry Boxes
        eb_Title.delete(0,END)
        eb_Title.insert(0,value[0])

        eb_Author.delete(0,END)
        eb_Author.insert(0,value[1])
        
        eb_Year.delete(0,END)
        eb_Year.insert(0,value[2])
        
        eb_ISBN.delete(0,END)
        eb_ISBN.insert(0,value[3])
    except IndexError:
        pass

window = Tk()

#Define Labels
la_Title = Label(window, text="Title", width=10)
la_Title.grid(row=0, column=0)

la_Author = Label(window, text="Author", width=10)
la_Author.grid(row=0, column=2)

la_Year = Label(window, text="Year", width=10)
la_Year.grid(row=1, column=0)

la_ISBN = Label(window, text="ISBN", width=10)
la_ISBN.grid(row=1, column=2)

#Define EntryBoxes
title_text=StringVar()
eb_Title=Entry(window, textvariable=title_text, width=25)
eb_Title.grid(row=0, column=1)

author_text=StringVar()
eb_Author=Entry(window, textvariable=author_text, width=25)
eb_Author.grid(row=0, column=3)

year_text=StringVar()
eb_Year=Entry(window, textvariable=year_text, width=25)
eb_Year.grid(row=1, column=1)

isbn_text=StringVar()
eb_ISBN=Entry(window, text=isbn_text, width=25)
eb_ISBN.grid(row=1, column=3)

#Define Listbox
lb_Books = Listbox(window, height=6, width=40)
lb_Books.grid(row=2, columnspan=2, rowspan=6)
lb_Books.bind('<<ListboxSelect>>', lb_Books_selection_change)

scroll_Books=Scrollbar(window)
scroll_Books.grid(row=4, rowspan=2,column=2)

lb_Books.configure(yscrollcommand=scroll_Books.set)
scroll_Books.configure(command=lb_Books.yview)

#Define Buttons
btn_View = Button(window, text="View All", width=15, command=view_command)
btn_View.grid(row = 2, column = 3)

btn_Search = Button(window, text="Search Entry", width=15, command=search_command)
btn_Search.grid(row = 3, column = 3)

btn_Add = Button(window, text="Add Entry", width=15, command=add_command)
btn_Add.grid(row = 4, column = 3)

btn_Update = Button(window, text="Update Selected", width=15, command=update_command)
btn_Update.grid(row = 5, column = 3)

btn_Delete = Button(window, text="Delete Selected", width=15, command=delete_command)
btn_Delete.grid(row = 6, column = 3)

btn_Close = Button(window, text="Close", width=15, command=window.destroy)
btn_Close.grid(row = 7, column = 3)

view_command()
window.mainloop()

