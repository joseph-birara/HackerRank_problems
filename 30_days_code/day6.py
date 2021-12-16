# Task
# Given a string,S , of length N that is indexed from  0 to N-1,
#  print its even-indexed and odd-indexed characters as 2 space-separated 
# strings on a single line (see the Sample below for more detail).

# Note:  is considered to be an even index.# Enter your code here. Read input from STDIN. Print output t
def string_separator():
    str=input()
    str1=''
    str2=''
    for item in str:
        if str.index(item)%2==0:
            str1=str1+item
        else:
            str2=str2+item
    print(str1+" "+str2)
    print('josepj')
