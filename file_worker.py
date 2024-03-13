def write_to_file(file_name, text):
  try:
    file = open(f"{file_name}.txt", "a")
    file.write(text)
    file.close
  except Exception as e:
    print('oops file not found', e)

  

def read_from_file(file_name):
  try:
    file = open(f"{file_name}.txt", 'r')
    print(file.read())
    file.close
  except Exception as e:
    print('oops file not found', e)
  
def file_manager():
  while True:
    action = input("What do you want to do (write, read, exit)?: ")
    if action == 'exit' : break
    if action == 'write': 
      file_name = input('file name?: ')
      text = input('What need to be added?: ')
      write_to_file(file_name, text)
    if action == 'read': 
      file_name = input('file name?: ')
      read_from_file(file_name)
      
file_manager()