from tkinter import *
from db import Database


db = Database("library_books.db")

class Root(Tk):

    def __init__(self):
        super().__init__()
        self.title("wellcome to the Rastava library")
        self.geometry('600x350')
        self.features()
        self.item_selection = 0 

    def features(self):
        self.Title = StringVar()
        label_T = Label(self, text = "Title")
        label_T.grid(row=0 , column=1)
        self.title_e = Entry(self , textvariable=self.Title)
        self.title_e.grid(row=0 , column=0)

        self.Author = StringVar()
        Author_l = Label(self , text="Author")
        Author_l.grid(row=1 , column=1)
        self.Author_e = Entry(self , textvariable=self.Author)
        self.Author_e.grid(row=1 , column=0)
       
       
        self.ISBN = StringVar()
        isbn_l = Label(self , text="ISBN")
        isbn_l.grid(row=2 , column=1)
        self.isbn_e = Entry(self , textvariable=self.ISBN)
        self.isbn_e.grid(row=2 , column=0)
       
        self.YEAR = StringVar()
        year_l = Label(self , text="Year")
        year_l.grid(row=3 , column=1)
        self.year_e = Entry(self , textvariable=self.YEAR)
        self.year_e.grid(row=3 , column=0)

        self.List_b = Listbox(self , height=8 , width=45)
        self.List_b.grid(row=0 , column=3 , rowspan=4 , columnspan=7 , padx=15 , pady=20)

        self.List_b.bind('<<ListboxSelect>>' , self.selecting)

        self.New = Button(self , text="New" , command=self.New_book)
        self.New.grid(row=8 , column=0 )
       
        self.Delete = Button(self , text="Delete" , command=self.Delete_book)
        self.Delete.grid(row=8 , column= 2)
       
        self.Edit = Button(self , text="Edit" , command=self.Edit_book)
        self.Edit.grid(row=8 , column=4 )
       
        self.serach = Button(self , text="Search" , command=self.search_book)
        self.serach.grid(row=8 , column=6 )

    def New_book(self):
        db.insert(self.Title.get() , self.Author.get() , self.YEAR.get() , self.ISBN.get())
        self.clear()
        self.Fetch()

    def selecting(self , event):
        widget = event.widget
        self.select_books=widget.get(ANCHOR)
        self.clear()
        self.title_e.insert(0 , self.select_books[1])
        self.Author_e.insert(0 , self.select_books[2])
        self.isbn_e.insert(0 , self.select_books[3])
        self.year_e.insert(0 , self.select_books[4])


    def Edit_book(self):
        db.update(self.select_books[0],self.Title.get() , self.Author.get() , self.YEAR.get() , self.ISBN.get())
        self.Fetch()

    def Delete_book(self):
        db.remove(self.select_books[0])
        self.clear()
        self.Fetch()

    def search_book(self):
        rows = db.search(self.Title.get() , self.Author.get() , self.YEAR.get() , self.ISBN.get())
        self.Fetch(rows)
    
    def clear(self):
        self.title_e.delete(0 , END)
        self.Author_e.delete(0 , END)
        self.year_e.delete(0 , END)
        self.isbn_e.delete(0 , END)

    def Fetch(self , rows=None):
        self.List_b.delete(0,END)
        if rows == None :
            rows = db.fetch()
        for row in rows:
            self.List_b.insert(END, row)


        


r = Root()
r.mainloop()


