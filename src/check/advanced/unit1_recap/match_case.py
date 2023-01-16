# https://learnpython.com/blog/python-match-case-statement/

def file_handler_v2(command):
     match command.split():
         case ['show']:
             print('List all files and directories: ')
             # code to list files
         case ['remove' | 'delete', *files] if '--ask' in files:
             del_files = [f for f in files if len(f.split('.'))>1]
             print('Please confirm: Removing files: {}'.format(del_files))
             # code to accept user input, then remove files
         case ['remove' | 'delete', *files]:
             print('Removing files: {}'.format(files))
             # code to remove files
         case _:
             print('Command not recognized')

file_handler_v2('remove --ask file1.txt file2.jpg file3.pdf')
file_handler_v2('delete file1.txt file2.jpg file3.pdf')