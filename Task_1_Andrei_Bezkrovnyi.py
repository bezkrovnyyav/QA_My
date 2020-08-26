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
  hi_index = len_of_arr - 1
  its = int(len_of_arr // 2)                
  for i in range(0, its):    
    temp = arr[hi_index]     
    arr[hi_index] = arr[i]
    arr[i] = temp
    hi_index -= 1            
  return(arr)
# displaying the reversed array
print(rev_mass(arr)) 