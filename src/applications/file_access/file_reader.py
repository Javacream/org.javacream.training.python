def read_demo():
    path = 'src/applications/file_access/simple.txt'
    with open(path, 'rt', encoding='utf-8') as file:
        content = file.read()
    rows = content.split('\n')    
    print(content)
    print('Hello')
def write_demo():
    path = 'src/applications/file_access/result.txt'
    with open(path, 'wt', encoding='utf-8') as file:
        file.write('dqfwghsdicsdabvf ä ül öö')

def main():
    read_demo()
    write_demo()
main()