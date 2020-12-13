with open("input.txt") as f:
    entries = [int(line.strip()) for line in f if line.strip()]

# finding a+b=2020 is equiv to finding a = 2020-b
def two_sum(arr, target):
    diffs = [target - el for el in arr]
    for el in arr:
        try:
            idx = diffs.index(el)
        except ValueError:
            continue
        return el*arr[idx]
    return None


#finding a+b+c=2020 is equiv to finding a+b=2020-c for some c
def three_sum(arr, target):
    for c in arr:
        t = two_sum(arr, target-c)
        if t != None:
            return c*t

print(two_sum(entries, 2020))
print(three_sum(entries, 2020))