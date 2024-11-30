# ****
# ****
# ****
# ****


def print_pattern1(rows):
    for i in range(rows):
        for j in range(rows):
            print("*", end="")
        print("\n")


def print_pattern2(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end="")
        print("\n")


def print_pattern3(rows):
    for i in range(rows):
        for j in range(i + 1):
            print(j + 1, end="")
        print("\n")


def print_pattern4(rows):
    for i in range(rows):
        for j in range(i + 1):
            print(i + 1, end="")
        print("\n")


def print_pattern5(rows):
    for i in range(rows):
        for j in range(rows, i, -1):
            print("* ", end="")
        print("\n")


def print_pattern6(rows):
    for i in range(rows):
        for j in range(rows - i):
            print(j + 1, end="")
        print("\n")


# def print_pattern7(rows):
#     for i in range(rows):

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

arr = [1, 0, 2, 3, 0, 4, 5, 0]


for i in range(len(arr) - 1, -1, -1):
    print(i)
    if arr[i] == 0:
        arr.pop()
        arr.insert(i, 0)
        print("0 index: ", i)
    print(arr)

print(arr)
