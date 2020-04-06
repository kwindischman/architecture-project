import sys
import math


def print_args():
    RR = 'Round Robin'
    RND = 'Random'
    LRU = 'Least Recently Used'

    print('Cache Simulator - CS 3853 - Team 01')
    print('\nTrace File: %s' % file_name)
    print('\n***** Cache Input Parameters *****')
    print('\n%-30s %d KB' % ('Cache Size:', cache_size))
    print('%-30s %d bytes' % ('Block Size:', block_size))
    print('%-30s %d' % ('Associativity:', associativity))

    if replacement.upper() == 'RR':
        print('%-30s %s' % ('Replacement Policy:', RR))
    elif replacement.upper() == 'RND':
        print('%-30s %s' % ('Replacement Policy:', RND))
    elif replacement.upper() == 'LRU':
        print('%-30s %s' % ('Replacement Policy:', LRU))
    else:
        print('bad input for replacement policy')
        sys.exit(-1)


def print_calculated_values():
    print('\n***** Cache Calculated Values *****')
    print('%-30s %d' % ('Total # Blocks:', total_blocks))
    print('%-30s %d bits' % ('Tag Size:', tag_size))
    print('%-30s %d bits' % ('Index Size:', index_size))
    print('%-30s %d' % ('Total # Rows:', total_rows))
    #print('%-30s %d bytes' % ('Overhead Size:', overhead_size))
    #print('%-30s %0.2f KB (%d bytes)' % ('Implementation Memory Size:', -1.0, -1))
    #print('%-30s $%0.2f' % ('Cost:', cost))


def calculate_values():
    global total_blocks
    global tag_size
    global index_size
    global total_rows
    #global overhead_size
    #global implementation_mem_size
    #global cost

    total_blocks = (cache_size * 1024) / block_size
    total_rows = (cache_size * 1024) / (block_size * associativity)
    index_size = math.log(total_rows, 2)
    tag_size = 32 - math.log(block_size, 2) - index_size
    #overhead_size =
    #implementation_mem_size =
    #cost =

def set_vars():
    global file_name
    global cache_size
    global block_size
    global associativity
    global replacement

    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '-f':
            file_name = sys.argv[i + 1]
        elif sys.argv[i] == '-s':
            cache_size = int(sys.argv[i + 1])
        elif sys.argv[i] == '-b':
            block_size = int(sys.argv[i + 1])
        elif sys.argv[i] == '-a':
            associativity = int(sys.argv[i + 1])
        elif sys.argv[i] == '-r':
            replacement = sys.argv[i + 1]
        else:
            print('invalid command ', sys.argv[i])
            sys.exit(-1)


def main():
    set_vars()
    print_args()
    calculate_values()
    print_calculated_values()


if __name__ == '__main__':
    main()
