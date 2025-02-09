
arr = []

for i in range(int(input())):
    line = list(map(str, input().split(" ")))
    command = line[0]
    if command == "insert":
        arr.insert(int(line[1]), int(line[2]))
    elif command == "print":
        print(arr)
    elif command == "remove":
        arr.remove(int(line[1]))
    elif command == "append":
        arr.append(int(line[1]))
    elif command == "sort":
        arr.sort()
    elif command == "pop":
        arr.pop()
    elif command == "reverse":
        arr.reverse()
    