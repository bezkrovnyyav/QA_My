# Create the array
string = ""
arr = []
while True:
  string = input() # Enter elements of the array
  if not string:
    break
  arr.append(string)
def rev_mass(arr):
  return [arr[i] for i in range(len(arr)-1, -1, -1)] # reversing the array
# displaying the reversed array
print(rev_mass(arr)) 
