lst = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less, equal, more = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)
    return quick_sort(less) + equal + quick_sort(more)


print(quick_sort(lst))