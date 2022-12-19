def swap_case(s):
    lists = [i for i in s]
    for i in range(len(s)):
        if lists[i] == " ":
            pass
        if lists[i].isalpha() and lists[i].isupper():
            lists[i] = lists[i].lower()
        elif lists[i].isalpha() and lists[i].islower():
            lists[i] = lists[i].upper()
        else:
            pass
            
    return "".join(lists)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
