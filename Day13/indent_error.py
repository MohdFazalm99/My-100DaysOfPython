#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
# Here is the error we indent the b_list inside the for loop otherwise it will only give us one output that is 26 .
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])