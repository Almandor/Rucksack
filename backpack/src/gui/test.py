from Tkinter import *
import ttk


def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda: \
               treeview_sort_column(tv, col, not reverse))


root = Tk()

tree = ttk.Treeview(root)

columns = ("one", "two")
tree["columns"] = columns
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="column A")
tree.heading("two", text="column B")

tree.insert("", 0, text="Line 1", values=("1A", "1b"))

id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A", "2B"))

##alternatively:
tree.insert("", 3, "dir3", text="Dir 3")
tree.insert("dir3", 3, text=" sub dir 3", values=("3A", " 3B"))

for col in columns:
    tree.heading(col, text=col, command=lambda: \
                     treeview_sort_column(tree, col, False))

tree.pack()
root.mainloop()