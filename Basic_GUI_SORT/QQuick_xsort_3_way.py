import time,random


def randomization(array,l,r):
    x=random.randrange(l,r+1)
    array[l],array[x]=array[x],array[l]

def QQuick_sort_3way(array,l,r,draw_data,time_delay):
    if l>= r:
        return

    randomization(array,l,r)
    m1,m2=Partition(array,l,r,draw_data,time_delay)

    QQuick_sort_3way(array,l,m1-1,draw_data,time_delay)
    QQuick_sort_3way(array,m2+1,r,draw_data,time_delay)

    draw_data(array,['green' if x>=l and x<=m1 else 'red' for x in range(len(array)) ])
    time.sleep(time_delay)

def Partition(array,l,r,draw_data,time_delay):
    i=j=l# here j for the index of the last equal 
    compare=array[l]

    for x in range(l+1,r+1):
        if array[x]<compare:
            j+=1
            array[j],array[x]=array[x],array[j]
            
            i+=1
            array[i],array[j]=array[j],array[i]

            draw_data(array,color(len(array),l,r,i,j,x))
            time.sleep(time_delay)
        elif array[x]==compare:
            j+=1
            array[j],array[x]=array[x],array[j]
            draw_data(array,color(len(array),l,r,i,j,x))
            time.sleep(time_delay)

    # swap
    array[l],array[i]=array[i],array[l]


    return i,j

def color(length,l,r,i,j,x):
    ret=[]
    for y in range(length):
        if y==j:
            ret.append('pink')
        elif y==i:
            ret.append('violet')
        elif y==x:
            ret.append('black')
        elif y>=l and y<=r:
            ret.append('green')
        else:
            ret.append('red')
    return ret