import sys

def print_input():
    print('Cache Simulator CS 3853 Spring 2020 - Group #01\n\n')
    print('Trace File: %s\n\n' % (file_name))
    print('***** Cache Input Parameters *****\n\n')
    print('%-25s %s KB' % ('Cache Size:', cache_size))
    print('%-25s %s bytes' % ('Block Size:', block_size))
    print('%-25s %s' % ('Associativity:', associativity))
    print('%-25s %s' % ('Replacement Polity:', replacement))

def set_vars():
    global file_name
    global cache_size
    global block_size
    global associativity
    global replacement

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
    print_input()

if __name__ == '__main__':
    main()
