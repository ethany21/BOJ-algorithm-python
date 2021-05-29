n = int(input())

for i in range(n):
    if int((n-(2*i+1))/2) >= 0:
        print(" " * int((n-(2*i+1))/2)+"*" * (2*i+1)+" " * int((n-(2*i+1))/2))
    else:
        print(" "*int((2*i+2-n)/2)+"*"*(2*n - (2*i+1))+" "*int((2*i+2-n)/2))