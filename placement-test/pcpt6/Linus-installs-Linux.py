def getAns(string):
    entries = string.split('/')
    stack = []
    for entry in entries:
        if entry == '..':
            if stack:
                stack.pop()            
        elif entry == '':
            continue
        elif entry == '.':
            continue
        else:
            stack.append(entry)
    answer = '/'.join(stack)
    
    return '/'+ answer
    
def main():
    t = int(input().strip())
    for _ in range(t):
        string = input().strip()
        print(getAns(string))
main()