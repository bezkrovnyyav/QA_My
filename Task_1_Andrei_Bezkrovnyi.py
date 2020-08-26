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
  size = len(arr)             
  hi_index = size - 1
  its = int(size//2)                
  for i in range(0, its):    
    temp = arr[hi_index]     
    arr[hi_index] = arr[i]
    arr[i] = temp
    hi_index -= 1            
  return(arr)
# displaying the reversed array
print(rev_mass(arr)) 