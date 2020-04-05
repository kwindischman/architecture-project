import sys

def print_args():
    print('Cache Simulator CS 3853 Spring 2020 - Group #01')
    print('\nTrace File: %s' % (file_name))
    print('\n***** Cache Input Parameters *****')
    print('\n%-30s %d KB' % ('Cache Size:', cache_size))
    print('%-30s %d bytes' % ('Block Size:', block_size))
    print('%-30s %d' % ('Associativity:', associativity))
    print('%-30s %s' % ('Replacement Polity:', replacement))

def print_calculated_values():
    print('\n***** Cache Calculated Values *****')
    print('%-30s %d' % ('Total # Blocks:', (cache_size / block_size)))
    print('%-30s %d bits' % ('Tag Size:', -1))
    print('%-30s %d bits' % ('Index Size:', -1))
    print('%-30s %d' % ('Total # Rows:', -1))
    print('%-30s %d bytes'% ('Overhead Size:', -1))
    print('%-30s %0.2f KB (%d bytes)' % ('Implementation Memory Size:', -1.0, -1))
    print('%-30s $%0.2f' % ('Cost:', -1.0))

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
    print_args()
    print_calculated_values()

if __name__ == '__main__':
    main()
