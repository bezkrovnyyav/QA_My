# Create the array
string = ""
arr = []
while True:
  string = input() # Enter elements of the array
  if not string:
    break
  arr.append(string)
def rev_mass(arr):
  result = list(reversed(arr)) # reversing the array
  return result
# displaying the reversed array
print(rev_mass(arr)) 
