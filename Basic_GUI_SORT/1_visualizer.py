from tkinter import *
from tkinter import ttk
import random


root=Tk()
root.title('SORTING')
root.maxsize(999, 777)
root.config(bg='black')

# selection of the algo from the options
selected_alg=StringVar()


# the list data taking fn
def draw_data(data):
    # for delete
    canvas.delete('all')

    canvas_height=666
    canvas_width=777
    bar_width=canvas_width/(len(data)+1)# as for the different data set
    offset=21
    spacing=7# bt/n the bars

    #normalizing the data
    normalize_data=[i/max(data) for i in data]

    for i,height in enumerate(normalize_data):
        # top left
        x0 = i * bar_width + offset + spacing
        y0 = canvas_height - height*600

        # bottom right
        x1 =  (i + 1) * bar_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill='violet')
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))



# define generator
def Generator():
    print('Alg selected: ' + selected_alg.get())#we get the selected algo
    # data=[1,2,3,7,2,5,4,5,9,7]
    try:
        min_value=int(mini_entry.get())
    except:
        min_value=0    
    try:
        max_value=int(maxi_entry.get())
    except:
        max_value=50
    try:
        size=int(size_entry.get())
    except:
        size=33
    
    if min_value<0:
        min_value=0
    if max_value>(10**9):
        max_value=(10**9)
    if size>100:
        size=100
    if min_value>max_value:
        min_value,max_value=max_value,min_value
    data=[random.randrange(min_value,max_value+1) for x in range(size)]

    draw_data(data)


# frame
upper_frame = Frame(root, width=777, height=333,bg='grey')
upper_frame.grid(row=0,column=0,padx=7,pady=3)

# canvas
canvas = Canvas(root,width=777, height=666,bg='skyblue')
canvas.grid(row=1,column=0,padx=7,pady=3)



# user interface area
# row 0
label=Label(upper_frame,text='ALGORITHM: ',bg='grey')
label.grid(row=0,column=0,padx=7,pady=5,sticky=W,ipadx=3)# stick in the west

# algorithm menu
algo_menu=ttk.Combobox(upper_frame,textvariable=selected_alg,values=['Merge_Sort','QUICK_SORT'])
algo_menu.grid(row=0,column=1,padx=7,pady=5,ipadx=3)# here selected_alg will be the 
# selected one from the options

# for making the default
algo_menu.current(0)
#generate button
button = Button(upper_frame,text='GENERATE',command=Generator,bg='red')
button.grid(row=0,column=2,padx=7,pady=5,ipadx=3)

# now for the size and the various thing min,max
size=Label(upper_frame,text='SIZE',bg='grey')
size.grid(row=1,column=0,padx=7,pady=5,ipadx=3,sticky=W)
# now the entr for the size
size_entry=Entry(upper_frame)
size_entry.grid(row=1,column=1,padx=7,pady=5,ipadx=3,sticky=W)

# for the min also
mini=Label(upper_frame,text='MIN',bg='grey')
mini.grid(row=1,column=2,padx=7,pady=5,ipadx=3,sticky=W)
mini_entry=Entry(upper_frame)
mini_entry.grid(row=1,column=3,padx=7,pady=5,ipadx=3,sticky=W)

# for the max
maxi=Label(upper_frame,text='MAX',bg='grey')
maxi.grid(row=1,column=4,padx=7,pady=5,ipadx=3,sticky=W)
maxi_entry=Entry(upper_frame)
maxi_entry.grid(row=1,column=5,padx=7,pady=5,ipadx=3,sticky=W)

root.mainloop()