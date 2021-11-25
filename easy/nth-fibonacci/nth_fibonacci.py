def getNthFib(n):
    # Write your code here.
    print(n)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return n + getNthFib(n-1)

if __name__ == "__main__":
    getNthFib(6)