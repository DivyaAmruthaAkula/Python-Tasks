# write a function to test if array contains a specific value.
arr = list(map(int, input().split()))
target = int(input())
found = False
for num in arr:
    if num == target:
        found = True
        break
print(found)