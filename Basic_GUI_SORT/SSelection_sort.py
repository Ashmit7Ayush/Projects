import time

# wee have to find minimum in each iteration
def Selection_sort(array,draw_data,time_delay):
    for x in range(len(array)):
        mini=x
        for y in range(mini+1,len(array)):
            if array[mini] > array[y]:
                mini=y
                draw_data(array,['green' if i==mini or i==x else 'red' for i in range(len(array))])
                time.sleep(time_delay)
        # swap
        array[x],array[mini]=array[mini],array[x]
        draw_data(array,['green' if i==mini or i==x else 'red' for i in range(len(array))])
    draw_data(array,['blue' for x in range(len(array))])