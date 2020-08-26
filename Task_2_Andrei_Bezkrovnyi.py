# Create the array
string = ""
arr = []
while True:
  string = input() # Enter elements of the array
  if not string:
    break
  arr.append(string)
def rev_mass(arr):
# reversing the array
  i = 0
  while i < len(arr) / 2:
    t = arr[i]
    arr[i] = arr[-i - 1]
    arr[-i - 1] = t
    i = i + 1
  return (arr)
 # displaying the reversed array
print(rev_mass(arr)) 