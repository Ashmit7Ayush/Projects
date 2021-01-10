import time

def Merge_sort(array,l,r,draw_data,time_delay):
    if l==r or l==r-1:
        return 

    m=(l+r)//2

    Merge_sort(array,l,m,draw_data,time_delay)
    Merge_sort(array,m,r,draw_data,time_delay)

    Merge(array,l,m,r,draw_data,time_delay)

    draw_data(array,['green' if x>=l and x<r else 'red' for x in range(len(array)) ])
    time.sleep(time_delay)
    # return merge

def Merge(array,l,m,r,draw_data,time_delay):
    index_l=l
    index_r=m

    ret_list=[]
    draw_data(array,color(len(array),l,m,r))
    time.sleep(time_delay)
    while index_l<m and index_r<r:
        ll=array[index_l]
        rr=array[index_r]

        if ll<=rr:
            ret_list.append(ll)
            index_l+=1

        else:
            ret_list.append(rr)
            index_r+=1

    if index_l<m:
        ret_list.extend(array[index_l:m])
    if index_r<r:
        ret_list.extend(array[index_r:r])

    array[l:r]=ret_list

def color(length,left,middle,right):
    ret=[]
    for x in range(length):
        if x >= left and x<middle:# from start left to end left
            ret.append('violet')
        elif x>=left and x<right:
            ret.append('black')
        else:
            ret.append('red')
    return ret