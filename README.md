Goal: Help you understand the internal operations of CPU caches.
Group: Brent, Kai, Kareem

Due Dates: 
Milestone #1 - Input parameters and parsing the trace file. DUE: Thu Apr 6th, 11:59pm
Milestone #2 - The Cache Simulator Program. DUE: Mon Apr 27th, 11:59pm 
Milestone #3 - Analysis. DUE: May 7th, 2020, 7:30pm

Programming Language: Python

You are required to simulate a Level 1 cache for a 32-bit CPU. Assume a 32-bit data bus.

The cache must be command line configurable to be direct-mapped, 2-way, 4-way, 8-way, or 16-way set associative and implement both round-robit and random replacement policies for performance comparisons. (You may implement LRU in lieu of either of the others)

This project requires coding, testing, documenting results and writing the final results.

Your simulator will have the following input parameters:

1. -f [ name of text file with the trace ]
2. -s [ 1 KB to 8 MB ]
3. -b [ 4 bytes to 64 btes ]
4. -a [ 1, 2, 4, 8, 16 ]
5. -r [ RR or RND or LRU for bonus points ]
Sample command lines: Sim.exe -f trace1.txt -s 1024 -b 16 -a 2 -r RR

That would read the trace file named "trace1.txt", configure a total cache size of 1 MB with a block size of 16 bytes/block. It would be a 2-way set associative and use the replacement policy of Round Robin. We will assume a write-through policy. COST: $0.05/KB

Your simulator should output the simulation results to the screen (stdout). 
The output should have a short header formatted as follows: 

Cache Simulator CS 3853 Spring 2020 - Group #01 
Cmd Line: Sim.exe -f trace1.txt -s 1024 -b 16 -a 2 -r RR 
Trace File: Sim.exe 
Cache Size: 1024 KB 
Block Size: 16 bytes 
Associativity: 2-way 
R-Policy: RR
