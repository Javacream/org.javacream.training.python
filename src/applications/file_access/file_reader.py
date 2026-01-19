def read_demo():
    path = 'src/applications/file_access/simple.txt'
    file = open(path, 'rt', encoding='utf-8')
    content = file.read()
    file.close()
    print(content)

def write_demo():
    path = 'src/applications/file_access/result.txt'
    file = open(path, 'wt', encoding='utf-8')
    file.write('dqfwghsdicsdabvf ä ül öö')
    file.close()
def main():
    read_demo()
    write_demo()
main()