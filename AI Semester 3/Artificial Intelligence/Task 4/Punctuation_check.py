def remove_punctuation(Input):
    final = ""
    for char in Input:
        if (char>= 'a' and char<= 'z') or (char>= 'A' and char<= 'Z') or (char>= '0' and char<= '9'):
            final += char
        elif char ==' ':
            final+= char
    return final
Input= input("Enter String To Remove Punctuation: ")
Get = remove_punctuation(Input)
print(Get) 