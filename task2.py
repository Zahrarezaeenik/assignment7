def counter_word(str):
    if(str==""):
        return 0
    counter=1
    for ch in str:
        if ch == " ":
            counter+=1
    return counter

count=counter_word("python is a powerful programming language")
print(count)