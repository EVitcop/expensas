# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:40:58 2020

@author: eduardo.vitcop
"""

from tkinter import *
     
def sortby(tree, col, descending):
       """sort tree contents when a column header is clicked on"""
       # grab values to sort
       data = [(tree.set(child, col), child) \
           for child in tree.get_children('')]
       # if the data to be sorted is numeric change to float
       #data =  change_numeric(data)
       # now sort the data in place
       data.sort(reverse=descending)
       for ix, item in enumerate(data):
           tree.move(item[1], '', ix)
       # switch the heading so it will sort in the opposite direction
       tree.heading(col, command=lambda col=col: sortby(tree, col, \
           int(not descending)))

header = ['car', 'repair']
data = [
   ('Hyundai', 'brakes') ,
   ('Honda', 'light') ,
   ('Lexus', 'battery') ,
   ('Benz', 'wiper') ,
   ('Ford', 'tire')]

root = Tk()
frame = ttk.Frame(root)
frame.pack()
table = ttk.Treeview(frame, columns=header, show="headings")
table.pack()

## table.tag_configure('items', foreground='blue')
## ttk.Style().configure("Treeview", background='red', foreground='yellow')
## ttk.Style().configure(".", font=('Helvetica', 8), foreground="white")

for col in header:
   table.heading(col, text=col.title(), 
                 command=lambda c=col: sortby(table, c, 0))
for item in data:
   table.insert('', 'end', values=item, tags=('items',))



root.mainloop()