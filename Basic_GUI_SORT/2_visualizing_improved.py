from tkinter import *
from tkinter import ttk
import random

from BBubble_sort import Bubble_sort
from SSelection_sort import Selection_sort
from MMerge_sort import Merge_sort
from QQuick_sort import Quick_sort
from QQuick_xsort_3_way import QQuick_sort_3way

root=Tk()
root.title('SORTING')
root.maxsize(999, 777)
root.config(bg='black')

# selection of the algo from the options
selected_alg=StringVar()

# DECLARE THE DATA TO BE GLOBAL
data=[]



# the list data taking fn
# color_array for which element are being manipulated
def draw_data(data,color_array):
    # for delete
    canvas.delete('all')

    canvas_height=666
    canvas_width=777
    bar_width=canvas_width/(len(data))# as for the different data set
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

        canvas.create_rectangle(x0,y0,x1,y1,fill=color_array[i])
        # violet is been replaced by the color_array function
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))

    root.update_idletasks()

# define generator
def Generator():
    global data
    # print('Alg selected: ' + selected_alg.get())#we get the selected algo
    # data=[1,2,3,7,2,5,4,5,9,7]

    min_value=int(mini_entry.get())
    max_value=int(maxi_entry.get())
    size=int(size_entry.get())
    
    
    
    data=[random.randrange(min_value,max_value) for x in range(size)]

    draw_data(data,['#B71C1C' for x in range(len(data))])

def Start_Algo():
    global data
    speed = speed_scale.get()
    speed = 100 - speed
    speed=speed/1000
    # speed_scale.set(speed)
    # print(data)
    if selected_alg.get()=='BUBBLE_SORT':
        Bubble_sort(data,draw_data,speed)
    # here speed_scale is for the manually speed

    elif selected_alg.get()=='SELECTION_SORT':
        Selection_sort(data,draw_data,speed)
    
    elif selected_alg.get()=='Merge_Sort':
        Merge_sort(data,0,len(data),draw_data,speed)

    elif selected_alg.get()=='QUICK_SORT':
        Quick_sort(data,0,len(data)-1,draw_data,speed)
    
    elif selected_alg.get()=='QUICK_SORT_3WAY':
        QQuick_sort_3way(data,0,len(data)-1,draw_data,speed)

    draw_data(data,['#6633FF' for x in range(len(data))])# 00FF33




# frame
upper_frame = Frame(root, width=777, height=333,bg='grey')
upper_frame.grid(row=0,column=0)

# canvas
canvas = Canvas(root,width=777, height=666,bg='#000000')
canvas.grid(row=1,column=0,padx=7,pady=3)



# user interface area
# row 0
label=Label(upper_frame,text='SELECT ALGORITHM: ',bg='grey',width=27)
label.grid(row=0,column=0,padx=3,pady=5,sticky=W,ipadx=0)# stick in the west

# algorithm menu
algo_menu=ttk.Combobox(upper_frame,textvariable=selected_alg,values=['Merge_Sort','QUICK_SORT','BUBBLE_SORT','SELECTION_SORT','QUICK_SORT_3WAY'],width=30)
algo_menu.grid(row=0,column=1,padx=7,pady=5,ipadx=3,ipady=5)# here selected_alg will be the 
# selected one from the options

# for making the default
algo_menu.current(0)


# speed manager   
speed_scale=Scale(upper_frame,from_=1, to=100,length=200,digits=3,resolution=1,orient=HORIZONTAL,label='SPEED' )
speed_scale.grid(row=0,column=2,padx=7,pady=5)

start_algo=Button(upper_frame,text='Start',command=Start_Algo,bg='red')
start_algo.grid(row=0,column=3,padx=7,pady=5)


# because want to create the slider

# now for the size and the various thing min,max
size_entry=Scale(upper_frame,from_=25,to=90,resolution=1,length=200,orient=HORIZONTAL,label='size')
size_entry.grid(row=1,column=0,padx=7,pady=5,ipadx=3)

# for the min also
mini_entry=Scale(upper_frame,from_=1,to=10,resolution=1,length=200,orient=HORIZONTAL,label='MINIMUM VALUE')
mini_entry.grid(row=1,column=1,padx=7,pady=5,ipadx=3)

# for the max
maxi_entry=Scale(upper_frame,from_=10,to=100,resolution=1,length=200,orient=HORIZONTAL,label='MAXIMUM VALUE')
maxi_entry.grid(row=1,column=2,padx=7,pady=5,ipadx=3)


#generate button at the last
button = Button(upper_frame,text='GENERATE',command=Generator,bg='red')
button.grid(row=1,column=3,padx=7,pady=5,ipadx=3)

root.mainloop()
