def remove_punctuation(Input):
    final = ""
    for char in Input:
        if (char>= 'a' and char<= 'z')or(char>= 'A' and char<= 'Z')or(char>= '0' and char<= '9'):
            final= final + char
        elif char ==' ':
            final= final + char
    return final
String= input("Enter String To Remove Punctuation: ")
Get = remove_punctuation(String)
print(Get) 