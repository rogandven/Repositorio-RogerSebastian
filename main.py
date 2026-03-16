matrix = []
array = None

if __name__ == "__main__":
    print("hello world")
    for i in range(0, 100):
        array = []
        for j in range(0, 100):
            array.append(j)
            print("[" + str(j) + "]", end="")
        matrix.append(array)
        print()