n=int(input("Enter n:"))
m=int(input("Enter m:"))
for row in range(n+1):
    for col in range(m+1):
        if col==0 and row==0:
            print(" x ",end="\t")
        elif row==0:
            print(f" {col} ",end="\t")
        elif col==0:
            print(f" {row} ",end="\t")
        else:
            print(f" {row*col} ",end="\t")
    print()