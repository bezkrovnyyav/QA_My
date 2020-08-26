# Create the array
string = ""
arr = []
len_of_arr = 0
while True:
  string = input() # Enter elements of the array
  if not string:
    break
  len_of_arr += 1  
  arr.append(string)
def rev_mass(arr):
# reversing the array
  i = 0
  while i < len_of_arr / 2:
    t = arr[i]
    arr[i] = arr[-i - 1]
    arr[-i - 1] = t
    i = i + 1
  return (arr)
 # displaying the reversed array
print(rev_mass(arr)) 