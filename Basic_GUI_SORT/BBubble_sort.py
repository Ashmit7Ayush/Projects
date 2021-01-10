import time


def Bubble_sort(array, draw_data,time_delay):
    mark=False
    l=len(array)
    for x in range(l):
        for y in range(0,l-x-1):
            if array[y]>array[y+1]:
                array[y],array[y+1]=array[y+1],array[y]
                mark=True

                # for funality
                draw_data(array,['green' if i==y or i==y+1 else 'red' for i in range(len(array)) ])
                time.sleep(time_delay)
        if not mark:
            break
    draw_data(array,['blue' for x in range(len(array))])
    
