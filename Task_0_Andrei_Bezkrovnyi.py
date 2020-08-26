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
  return [arr[i] for i in range(len_of_arr - 1, -1, -1)] # reversing the array
# displaying the reversed array
print(rev_mass(arr)) 
