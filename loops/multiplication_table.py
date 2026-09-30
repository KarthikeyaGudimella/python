n = int(input("Enter number of tables: "))

for i in range(1, n + 1):
    print("\nTable of", i)

    for j in range(1, 11):
        result = i * j
        print(i, "x", j, "=", result)