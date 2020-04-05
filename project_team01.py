import sys

file_name = ''
cache_size = 0
block_size = 0
associativity = 0
replacement = ''

def set_vars():
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '-f':
            file_name = sys.argv[i+1]
        elif sys.argv[i] == '-s':
            cache_size = int(sys.argv[i+1])
        elif sys.argv[i] == '-b':
            block_size = int(sys.argv[i+1])
        elif sys.argv[i] == '-a':
            associativity = int(sys.argv[i+1])
        elif sys.argv[i] == '-r':
            replacement = sys.argv[i+1]
        else:
            print('invalid command ', sys.argv[i])

def main():
    set_vars()

if __name__ == '__main__':
    main()
