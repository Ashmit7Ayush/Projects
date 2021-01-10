import time

def Quick_sort(array,l,r,draw_data,time_delay):
    if l>=r:
        return
    
    m=Partition(array,l,r,draw_data,time_delay)
    Quick_sort(array,l,m-1,draw_data,time_delay)
    Quick_sort(array,m+1,r,draw_data,time_delay)

    draw_data(array,['green' if x>=l and x<=r else 'red' for x in range(len(array))])
    time.sleep(time_delay)
def Partition(array,l,r,draw_data,time_delay):

    i=j=l
    compare=array[l]

    for x in range(l+1,r+1):
        if array[x]<=compare:
            i+=1
            # swap
            array[x],array[i]=array[i],array[x]

            draw_data(array,color(len(array),l,r,i,x))
            time.sleep(time_delay)

    # swap
    array[i],array[l]=array[l],array[i]
    return i

def color(length,l,r,i,x):
    ret=[]
    for y in range(length):
        if y ==i and y==x:
            ret.append('black')
        elif y>=l and y<=r:
            ret.append('violet')
        else:
            ret.append('red')
    return ret
        