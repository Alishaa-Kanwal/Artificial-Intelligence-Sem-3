def bubble_sort(string):
    num= len(string)
    for i in range(num):
        for j in range(0,num-i-1):
            if string[j] > string[j+1]:
                string[j], string[j + 1]= string[j+1],string[j]
def sort(Input):
    words=Input.split()
    bubble_sort(words)
    sorted=' '.join(words)
    return sorted

Input=input("Enter the String: ")
get= sort(Input)
print(get)