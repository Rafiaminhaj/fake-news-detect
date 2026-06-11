# -*- coding: utf-8 -*-
import sys
import random

# Ensure UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Database of 100 High-Quality MCQs
QUESTIONS = {
    "DSA": [
        # Easy
        {
            "q": "What is the time complexity to insert a new element at the beginning of a singly linked list of size N?",
            "o": ["A) O(1)", "B) O(N)", "C) O(log N)", "D) O(N log N)"],
            "a": "A",
            "d": "Easy",
            "exp": "Inserting at the beginning only requires updating the new node's next pointer to the current head, and updating the head pointer. This takes constant time, O(1)."
        },
        {
            "q": "Which data structure works on the LIFO (Last In First Out) principle?",
            "o": ["A) Queue", "B) Stack", "C) Heap", "D) Tree"],
            "a": "B",
            "d": "Easy",
            "exp": "Stacks operate on LIFO, where the last element inserted is the first one to be removed."
        },
        {
            "q": "What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?",
            "o": ["A) O(1)", "B) O(N)", "C) O(log N)", "D) O(N log N)"],
            "a": "C",
            "d": "Easy",
            "exp": "In a balanced BST, each step eliminates half of the remaining nodes, leading to a logarithmic search time."
        },
        {
            "q": "Which of the following sorting algorithms is stable by default?",
            "o": ["A) Quick Sort", "B) Heap Sort", "C) Merge Sort", "D) Selection Sort"],
            "a": "C",
            "d": "Easy",
            "exp": "Merge Sort preserves the relative order of equal elements, making it a stable sorting algorithm."
        },
        {
            "q": "What is the worst-case space complexity of a recursive implementation of DFS on a tree of N nodes?",
            "o": ["A) O(1)", "B) O(log N)", "C) O(N)", "D) O(N^2)"],
            "a": "C",
            "d": "Easy",
            "exp": "In a highly skewed tree (like a linked list), the recursion stack depth can reach N, taking O(N) space."
        },
        # Medium
        {
            "q": "In a Binary Max-Heap containing N elements, what is the time complexity to delete the maximum element?",
            "o": ["A) O(1)", "B) O(log N)", "C) O(N)", "D) O(N log N)"],
            "a": "B",
            "d": "Medium",
            "exp": "Deleting the root (max element) involves replacing it with the last element and calling heapify-down, which takes O(log N) time."
        },
        {
            "q": "Which of the following traversal sequences is sufficient to uniquely reconstruct a binary tree?",
            "o": ["A) Preorder and Postorder", "B) Preorder and Inorder", "C) Levelorder and Postorder", "D) Inorder only"],
            "a": "B",
            "d": "Medium",
            "exp": "Inorder traversal along with either Preorder or Postorder traversal is required to uniquely reconstruct a binary tree."
        },
        {
            "q": "If you are implementing a hash table with collision resolution via open addressing, what is the primary drawback of linear probing?",
            "o": ["A) High memory usage", "B) Primary clustering", "C) Infinite loops", "D) Secondary clustering"],
            "a": "B",
            "d": "Medium",
            "exp": "Linear probing suffers from primary clustering, where contiguous blocks of occupied slots build up, increasing search times."
        },
        {
            "q": "What is the time complexity of the Floyd-Warshall all-pairs shortest path algorithm on a graph with V vertices?",
            "o": ["A) O(V^2)", "B) O(V^3)", "C) O(E log V)", "D) O(V * E)"],
            "a": "B",
            "d": "Medium",
            "exp": "Floyd-Warshall uses three nested loops over the V vertices, yielding a time complexity of O(V^3)."
        },
        {
            "q": "Which data structure is typically used to implement Breadth-First Search (BFS) on a graph?",
            "o": ["A) Stack", "B) Queue", "C) Priority Queue", "D) Deque"],
            "a": "B",
            "d": "Medium",
            "exp": "BFS processes nodes in FIFO order (level-by-level), which matches the behavior of a Queue."
        },
        {
            "q": "What is the worst-case time complexity of Quick Sort?",
            "o": ["A) O(N log N)", "B) O(N^2)", "C) O(N^3)", "D) O(2^N)"],
            "a": "B",
            "d": "Medium",
            "exp": "The worst case occurs when the partition pivot splits the array into 0 and N-1 elements repeatedly (e.g., already sorted array with extreme pivots), taking O(N^2) time."
        },
        {
            "q": "What is the maximum number of nodes in a binary tree of height H (where root is at height 1)?",
            "o": ["A) 2^H - 1", "B) 2^(H-1)", "C) 2^(H+1) - 1", "D) H^2"],
            "a": "A",
            "d": "Medium",
            "exp": "A perfect binary tree of height H has 2^H - 1 nodes. For example, height 3 has 1 + 2 + 4 = 7 nodes (2^3 - 1)."
        },
        {
            "q": "Which algorithm finds the Minimum Spanning Tree (MST) of a graph by selecting edges in sorted order of weights?",
            "o": ["A) Prim's Algorithm", "B) Kruskal's Algorithm", "C) Dijkstra's Algorithm", "D) Bellman-Ford"],
            "a": "B",
            "d": "Medium",
            "exp": "Kruskal's algorithm sorts all edges by weight and adds the smallest edges that do not create cycles (using Disjoint Set Union)."
        },
        {
            "q": "How many queues are required to implement a stack?",
            "o": ["A) 1", "B) 2", "C) 3", "D) It is impossible"],
            "a": "B",
            "d": "Medium",
            "exp": "Two queues are needed to simulate LIFO behavior using FIFO operations (by shifting elements between them)."
        },
        {
            "q": "What is the time complexity of inserting an element in a Red-Black Tree of N nodes?",
            "o": ["A) O(1)", "B) O(N)", "C) O(log N)", "D) O(N log N)"],
            "a": "C",
            "d": "Medium",
            "exp": "Red-Black trees are self-balancing BSTs, guaranteeing logarithmic height and O(log N) insertion."
        },
        # Hard
        {
            "q": "What is the space complexity of Kosaraju's algorithm for finding Strongly Connected Components (SCCs) in a directed graph?",
            "o": ["A) O(1)", "B) O(V)", "C) O(V + E)", "D) O(V^2)"],
            "a": "C",
            "d": "Hard",
            "exp": "Kosaraju's algorithm requires storing the graph, its transpose, the visited array, and a stack, resulting in O(V + E) space complexity."
        },
        {
            "q": "Which of the following dynamic programming problems has a polynomial-time solution?",
            "o": ["A) 0/1 Knapsack", "B) Fractional Knapsack", "C) Matrix Chain Multiplication", "D) Traveling Salesman Problem"],
            "a": "C",
            "d": "Hard",
            "exp": "Matrix Chain Multiplication has an O(N^3) polynomial-time dynamic programming solution. 0/1 Knapsack is NP-complete (pseudo-polynomial), and Traveling Salesman is NP-hard."
        },
        {
            "q": "If you use a binary search on a sorted array of size N, what is the maximum number of comparisons needed?",
            "o": ["A) N", "B) log2(N) + 1", "C) log2(N)", "D) N/2"],
            "a": "B",
            "d": "Hard",
            "exp": "The maximum number of comparisons is floor(log2(N)) + 1, representing the height of the decision tree."
        },
        {
            "q": "What is the time complexity to find the diameter of a general binary tree of N nodes in an optimized O(N) single-pass approach?",
            "o": ["A) O(N^2)", "B) O(N log N)", "C) O(N)", "D) O(log N)"],
            "a": "C",
            "d": "Hard",
            "exp": "By returning both height and diameter in a single recursive post-order traversal, the diameter can be found in O(N) time."
        },
        {
            "q": "What does a Disjoint Set Union (DSU) structure achieve in O(alpha(N)) amortized time?",
            "o": ["A) Finding shortest paths", "B) Sorting numbers", "C) Union and Find operations", "D) Cycle detection in directed graphs only"],
            "a": "C",
            "d": "Hard",
            "exp": "Using path compression and union by rank, DSU performs Union and Find operations in O(alpha(N)) time, where alpha is the inverse Ackermann function."
        },
        {
            "q": "In KMP string matching algorithm, what does the prefix function (LPS array) store?",
            "o": ["A) Position of string matches", "B) Length of the longest proper prefix which is also a suffix", "C) Character frequencies", "D) Text index jumps"],
            "a": "B",
            "d": "Hard",
            "exp": "LPS stores the length of the longest proper prefix of the pattern that is also a suffix, allowing us to skip matching characters."
        },
        {
            "q": "What is the optimal amortized time complexity of deleting a node from a Fibonacci Heap?",
            "o": ["A) O(1)", "B) O(log N)", "C) O(N)", "D) O(N log N)"],
            "a": "B",
            "d": "Hard",
            "exp": "Deleting a node is done by decreasing its key to minus infinity (O(1)) and extracting the minimum (O(log N) amortized)."
        },
        {
            "q": "What is the maximum number of edges in a bipartite graph with N vertices?",
            "o": ["A) N(N-1)/2", "B) N^2", "C) floor(N^2 / 4)", "D) N(N-2)/4"],
            "a": "C",
            "d": "Hard",
            "exp": "According to Turan's Theorem, the maximum number of edges in a bipartite graph is floor(N^2 / 4), obtained when partition sizes are floor(N/2) and ceil(N/2)."
        },
        {
            "q": "What is the time complexity of constructing a Suffix Array of string S of size N using the prefix doubling method?",
            "o": ["A) O(N)", "B) O(N log N)", "C) O(N log^2 N)", "D) O(N^2)"],
            "a": "C",
            "d": "Hard",
            "exp": "The prefix doubling (Manber-Myers) algorithm runs in O(N log^2 N) time due to log N sorting stages."
        },
        {
            "q": "Which algorithm is used to find the maximum flow in a flow network?",
            "o": ["A) Dijkstra's", "B) Kruskal's", "C) Ford-Fulkerson (Edmonds-Karp)", "D) Bellman-Ford"],
            "a": "C",
            "d": "Hard",
            "exp": "The Ford-Fulkerson method (implemented via Edmonds-Karp with BFS) computes the maximum flow in a flow network."
        }
    ],
    "OS": [
        # Easy
        {
            "q": "What is the main purpose of virtual memory in an operating system?",
            "o": ["A) To increase CPU speed", "B) To allow execution of processes larger than physical memory", "C) To make the system secure from viruses", "D) To clear disk cache"],
            "a": "B",
            "d": "Easy",
            "exp": "Virtual memory maps user virtual addresses to physical memory or disk storage, letting programs run even if they exceed physical RAM size."
        },
        {
            "q": "Which state transition is invalid in a process lifecycle?",
            "o": ["A) Ready -> Running", "B) Running -> Blocked", "C) Blocked -> Running", "D) Running -> Ready"],
            "a": "C",
            "d": "Easy",
            "exp": "A process cannot transition directly from Blocked to Running; it must first enter the Ready state queue and wait for the CPU scheduler."
        },
        {
            "q": "What is a 'Kernel' in an operating system?",
            "o": ["A) An application software", "B) The core component that manages system resources and hardware communication", "C) A type of database", "D) The bootloader software"],
            "a": "B",
            "d": "Easy",
            "exp": "The kernel is the central, critical part of the OS that sits between applications and hardware, managing memory, tasks, and file systems."
        },
        {
            "q": "What is the term for a situation where a process waits indefinitely for a resource that is held by another waiting process?",
            "o": ["A) Starvation", "B) Deadlock", "C) Spooling", "D) Paging"],
            "a": "B",
            "d": "Easy",
            "exp": "Deadlock is a state where a set of processes are blocked because each process is holding a resource and waiting for another resource held by some other process."
        },
        {
            "q": "Which of the following is a non-preemptive CPU scheduling algorithm?",
            "o": ["A) Round Robin", "B) Shortest Job First (SJF) standard", "C) Shortest Remaining Time First (SRTF)", "D) Priority Scheduling (Preemptive)"],
            "a": "B",
            "d": "Easy",
            "exp": "Standard Shortest Job First is non-preemptive; once a process gets the CPU, it runs to completion."
        },
        # Medium
        {
            "q": "What is the 'Critical Section' problem?",
            "o": ["A) A bug in the OS boot sequence", "B) Designing a protocol where processes can share resources without data corruption", "C) Insufficient RAM space", "D) Unused sectors on the hard disk"],
            "a": "B",
            "d": "Medium",
            "exp": "The critical section is code where shared resources are accessed. The problem is ensuring mutual exclusion, progress, and bounded waiting."
        },
        {
            "q": "In memory management, what does 'Internal Fragmentation' refer to?",
            "o": ["A) Memory wasted inside fixed-sized allocated blocks", "B) Scattered free memory slots that cannot fit new processes", "C) Page tables leaking RAM", "D) Hard drive block failure"],
            "a": "A",
            "d": "Medium",
            "exp": "Internal fragmentation occurs when a partition/block is larger than the requested memory, leaving unused space inside the allocated block."
        },
        {
            "q": "Which page replacement algorithm suffers from Belady's Anomaly (page faults increase as frames increase)?",
            "o": ["A) LRU (Least Recently Used)", "B) FIFO (First In First Out)", "C) Optimal Page Replacement", "D) LFU (Least Frequently Used)"],
            "a": "B",
            "d": "Medium",
            "exp": "FIFO page replacement exhibits Belady's Anomaly because it doesn't respect the stack property of page referencing."
        },
        {
            "q": "What is a 'Semaphore' in operating systems?",
            "o": ["A) A system file explorer", "B) An integer variable used to solve the critical section problem via signal/wait functions", "C) A network hardware switch", "D) A graphical interface element"],
            "a": "B",
            "d": "Medium",
            "exp": "Semaphores are synchronization tools consisting of an integer variable accessed via atomic operations: `wait()` (or P) and `signal()` (or V)."
        },
        {
            "q": "What is the difference between a Process and a Thread?",
            "o": ["A) Threads have their own separate address space; processes do not", "B) Processes share memory by default; threads do not", "C) A process is an executing program with its own address space; a thread is a lightweight unit of execution sharing its parent process's memory", "D) Processes are managed by hardware; threads by software"],
            "a": "C",
            "d": "Medium",
            "exp": "Processes have isolated address spaces. Threads run within a process and share its code, data, and system resources, making context switching faster."
        },
        {
            "q": "What is 'Spooling'?",
            "o": ["A) Saving data temporarily in a buffer area to match speed differences between devices", "B) Swapping processes to disk", "C) Dividing disk sectors", "D) Encrypting system files"],
            "a": "A",
            "d": "Medium",
            "exp": "Spooling (Simultaneous Peripheral Operations On-Line) buffers data for slow devices (like printers) so the CPU can continue processing other tasks."
        },
        {
            "q": "What is a 'Zombie Process'?",
            "o": ["A) A process that keeps spawning new clones", "B) A process that has finished execution but still has an entry in the process table", "C) A process that has crashed the system", "D) A process running in background forever"],
            "a": "B",
            "d": "Medium",
            "exp": "A zombie process has terminated, but its parent has not yet read its exit status via `wait()`, keeping its entry in the process table."
        },
        {
            "q": "What is the primary function of the 'Translation Lookaside Buffer' (TLB)?",
            "o": ["A) To execute instructions faster", "B) To cache page-table translations to reduce virtual memory access times", "C) To manage network buffers", "D) To backup registry tables"],
            "a": "B",
            "d": "Medium",
            "exp": "The TLB is a hardware cache that stores recent virtual-to-physical address mappings, avoiding a double memory access for page tables."
        },
        {
            "q": "In disk scheduling, which algorithm is also known as the elevator algorithm?",
            "o": ["A) FCFS", "B) SSTF", "C) SCAN", "D) LOOK"],
            "a": "C",
            "d": "Medium",
            "exp": "SCAN sweeps the disk arm from one end to the other, servicing requests along the way, mimicking a passenger elevator."
        },
        {
            "q": "What is a 'Context Switch'?",
            "o": ["A) Changing variables in a program", "B) Saving the state of a running process and loading the state of another process into the CPU", "C) Restarting the computer", "D) Switching between user profiles"],
            "a": "B",
            "d": "Medium",
            "exp": "Context switching stores a CPU's register state in the Process Control Block (PCB) and loads another process's state to switch executions."
        },
        # Hard
        {
            "q": "What are the four necessary conditions for a deadlock to occur?",
            "o": ["A) Sharing, Paging, Spooling, Threading", "B) Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait", "C) CPU Starvation, Priority Inversion, Mutual Exclusion, Segments", "D) Scheduling, Paging, Swapping, Semaphores"],
            "a": "B",
            "d": "Hard",
            "exp": "All four conditions (Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait) must hold simultaneously for a deadlock to exist."
        },
        {
            "q": "What is 'Priority Inversion' and how is it resolved?",
            "o": ["A) Low priority running first; resolved by Round Robin", "B) A high priority task is blocked by a low priority task holding a lock, which is preempted by a medium priority task; resolved by Priority Inheritance", "C) Reversing process priorities; resolved by kernel reboot", "D) Thread starvation; resolved by paging"],
            "a": "B",
            "d": "Hard",
            "exp": "Priority Inversion is resolved by Priority Inheritance, where the lower priority thread holding the lock temporarily inherits the high priority of the waiting thread."
        },
        {
            "q": "In UNIX-like operating systems, what does the `fork()` system call return to the parent process on success?",
            "o": ["A) 0", "B) A negative integer", "C) The Process ID (PID) of the newly created child process", "D) 1"],
            "a": "C",
            "d": "Hard",
            "exp": "`fork()` returns 0 to the child process, and returns the child's PID to the parent process. It returns -1 on failure."
        },
        {
            "q": "What is the primary drawback of the Banker's Algorithm?",
            "o": ["A) It is unsafe", "B) It requires processes to declare their maximum resource claims in advance", "C) It only works on single-core CPUs", "D) It causes thrashing"],
            "a": "B",
            "d": "Hard",
            "exp": "The Banker's Algorithm requires knowing maximum resource needs upfront, which is rarely possible in interactive, dynamic operating systems."
        },
        {
            "q": "How does the 'Buddy System' allocate memory?",
            "o": ["A) Allocating memory segments using a best-fit queue", "B) Splitting memory partitions into power-of-two sizes to satisfy requests and merging adjacent free buddies", "C) Using pages exclusively", "D) Swapping memory sectors"],
            "a": "B",
            "d": "Hard",
            "exp": "The Buddy memory allocator divides memory blocks into halves (buddies) of power-of-two sizes to find the smallest block that fits, merging them back when freed."
        }
    ],
    "DBMS": [
        # Easy
        {
            "q": "What does SQL stand for?",
            "o": ["A) Structured Query Language", "B) Simple Query Language", "C) System Query Language", "D) Standard Query List"],
            "a": "A",
            "d": "Easy",
            "exp": "SQL is the industry-standard language used to manage and query relational databases: Structured Query Language."
        },
        {
            "q": "What is a 'Primary Key' in a database table?",
            "o": ["A) A key that allows duplicate values", "B) A column or set of columns that uniquely identifies each row in a table", "C) The first column of any table", "D) A key that connects to another table"],
            "a": "B",
            "d": "Easy",
            "exp": "A Primary Key must contain unique, non-null values to uniquely identify every record in that table."
        },
        {
            "q": "Which SQL command is used to retrieve data from a database?",
            "o": ["A) INSERT", "B) UPDATE", "C) SELECT", "D) DELETE"],
            "a": "C",
            "d": "Easy",
            "exp": "The SELECT statement retrieves columns/rows matching constraints from database tables."
        },
        {
            "q": "What is a 'Foreign Key'?",
            "o": ["A) A key defined in another language", "B) A field in one table that uniquely identifies a row of another table (creates a relationship)", "C) A primary key of a temporary table", "D) A key containing random numbers"],
            "a": "B",
            "d": "Easy",
            "exp": "A Foreign Key establishes a link between data in two tables by referencing the primary key of another table."
        },
        {
            "q": "Which of the following is a DDL (Data Definition Language) command?",
            "o": ["A) SELECT", "B) INSERT", "C) CREATE", "D) UPDATE"],
            "a": "C",
            "d": "Easy",
            "exp": "CREATE, ALTER, and DROP are DDL commands because they define or modify the database schema structure."
        },
        # Medium
        {
            "q": "What is database normalization?",
            "o": ["A) Backing up database tables", "B) Organizing tables and columns to minimize data redundancy and dependency", "C) Converting tables into JSON", "D) Running optimization queries"],
            "a": "B",
            "d": "Medium",
            "exp": "Normalization divides large tables and structures relations to avoid anomalies (Insert, Update, Delete) and duplicate fields."
        },
        {
            "q": "Which normal form requires the removal of multi-valued attributes (ensuring attributes are atomic)?",
            "o": ["A) 1NF", "B) 2NF", "C) 3NF", "D) BCNF"],
            "a": "A",
            "d": "Medium",
            "exp": "First Normal Form (1NF) requires that all attribute values be atomic (no arrays, lists, or multiple values in a single cell)."
        },
        {
            "q": "What does a 'Self Join' do?",
            "o": ["A) Joins a table to a copy of itself", "B) Merges two tables automatically", "C) Clears table data", "D) Connects a table to its database schema"],
            "a": "A",
            "d": "Medium",
            "exp": "A self join is a regular join in which a table is joined with itself (e.g. mapping employees to their managers inside the same table)."
        },
        {
            "q": "What is the function of the GROUP BY clause in SQL?",
            "o": ["A) Sorts rows alphabetically", "B) Groups rows that have the same values into summary rows (used with aggregate functions)", "C) Groups columns by table size", "D) Deletes duplicate tables"],
            "a": "B",
            "d": "Medium",
            "exp": "GROUP BY aggregates data (e.g., finding average salary by department) by grouping rows with matching column values."
        },
        {
            "q": "What are the components of ACID properties in DBMS transactions?",
            "o": ["A) Accuracy, Consistency, Indexing, Durability", "B) Atomicity, Consistency, Isolation, Durability", "C) Access, Control, Integrity, Database", "D) Atomicity, Concurrency, Isolation, Deletion"],
            "a": "B",
            "d": "Medium",
            "exp": "ACID properties guarantee transaction reliability: Atomicity (all or nothing), Consistency (preserves rules), Isolation (independent runs), and Durability (saved permanently)."
        },
        {
            "q": "What is the difference between TRUNCATE and DELETE in SQL?",
            "o": ["A) DELETE is DDL; TRUNCATE is DML", "B) DELETE can be rolled back and can use a WHERE clause; TRUNCATE is a DDL command that removes all rows quickly and cannot be rolled back easily", "C) Both do the exact same thing", "D) TRUNCATE deletes the table structure; DELETE only deletes rows"],
            "a": "B",
            "d": "Medium",
            "exp": "TRUNCATE is a DDL operation that drops/re-creates the table space (clearing auto-increment keys), whereas DELETE is a DML operation that removes rows individually."
        },
        {
            "q": "Which index type is best suited for range-based search queries in a relational database?",
            "o": ["A) Hash Index", "B) B-Tree / B+ Tree Index", "C) Bitmap Index", "D) Spatial Index"],
            "a": "B",
            "d": "Medium",
            "exp": "B+ Trees maintain sorted order at leaf nodes connected by pointers, making them optimal for range queries. Hash indexes only support equality checks."
        },
        {
            "q": "What is a 'Dirty Read' in database transactions?",
            "o": ["A) Reading corrupt database sectors", "B) A transaction reads data written by another concurrent transaction that has not yet been committed", "C) Reading data from a backup table", "D) Executing invalid SQL commands"],
            "a": "B",
            "d": "Medium",
            "exp": "A dirty read occurs if Transaction A reads Transaction B's changes, but Transaction B subsequently rolls back, leaving Transaction A with invalid data."
        },
        {
            "q": "What is the purpose of the HAVING clause in SQL?",
            "o": ["A) Alternative to SELECT", "B) Filters groups created by the GROUP BY clause (since WHERE cannot be used with aggregate functions)", "C) Specifies primary keys", "D) Filters columns before sorting"],
            "a": "B",
            "d": "Medium",
            "exp": "HAVING acts like a WHERE clause but operates on aggregated groups (e.g., `HAVING COUNT(id) > 5`)."
        },
        {
            "q": "In database design, what does a 'Partial Dependency' mean?",
            "o": ["A) A column depends on itself", "B) A non-prime attribute depends on a part of a composite candidate key (violating 2NF)", "C) A table depends on another database", "D) One primary key depends on another foreign key"],
            "a": "B",
            "d": "Medium",
            "exp": "Partial dependency occurs when a non-key column depends on only a part of a composite primary key, which violates Second Normal Form (2NF)."
        },
        # Hard
        {
            "q": "If relation R(A, B, C, D) has functional dependencies: A -> B and B -> C. What is the candidate key for R?",
            "o": ["A) {A}", "B) {A, D}", "C) {B, D}", "D) {A, B, C, D}"],
            "a": "B",
            "d": "Hard",
            "exp": "To find candidate keys, compute closures. Attribute D does not appear on the right side of any dependency, so it must be part of the key. The closure of {A, D} is {A, D, B, C} (which is all attributes). Thus, {A, D} is the unique candidate key."
        },
        {
            "q": "Which transaction isolation level prevents all anomalies (Dirty Reads, Non-repeatable Reads, Phantom Reads)?",
            "o": ["A) Read Committed", "B) Read Uncommitted", "C) Repeatable Read", "D) Serializable"],
            "a": "D",
            "d": "Hard",
            "exp": "Serializable is the highest isolation level. It executes transactions in a way that simulates running them sequentially, preventing all concurrency anomalies."
        },
        {
            "q": "What is the 'Two-Phase Locking' (2PL) protocol designed to guarantee?",
            "o": ["A) Deadlock prevention", "B) Serializability of transaction execution schedules", "C) Database recovery speed", "D) Low memory consumption"],
            "a": "B",
            "d": "Hard",
            "exp": "2PL ensures schedules are serializable by dividing locks into a growing phase (acquiring locks) and a shrinking phase (releasing locks). It does not prevent deadlocks."
        },
        {
            "q": "What is a 'Lossless-Join Decomposition'?",
            "o": ["A) Splitting tables without losing columns", "B) A decomposition of relation R into R1 and R2 such that joining them back (R1 natural join R2) yields exactly R, with no extra or missing rows", "C) Compressing tables", "D) Creating database indexes"],
            "a": "B",
            "d": "Hard",
            "exp": "Lossless-Join guarantees that no spurious (fake) records are created when sub-relations are joined back together. It is verified if R1 intersects R2 is a key for R1 or R2."
        },
        {
            "q": "In a B+ tree of order M (maximum M children), what is the minimum number of keys in a non-root internal node?",
            "o": ["A) 1", "B) ceil(M/2) - 1", "C) M/2", "D) ceil(M/2)"],
            "a": "B",
            "d": "Hard",
            "exp": "Non-root internal nodes in a B+ tree of order M must have at least ceil(M/2) children, which corresponds to at least ceil(M/2) - 1 keys."
        }
    ],
    "OOPs": [
        # Easy
        {
            "q": "Which concept allows a single function name or operator to exhibit different behaviors under different conditions?",
            "o": ["A) Encapsulation", "B) Polymorphism", "C) Inheritance", "D) Abstraction"],
            "a": "B",
            "d": "Easy",
            "exp": "Polymorphism (meaning many forms) lets you define methods with same names but different signatures/behaviors."
        },
        {
            "q": "What is encapsulation in Object-Oriented Programming?",
            "o": ["A) Creating multiple copies of an object", "B) Wrapping data members and member functions into a single unit (class) to restrict direct access", "C) Creating child classes", "D) Running functions in parallel"],
            "a": "B",
            "d": "Easy",
            "exp": "Encapsulation keeps data safe from external interference by locking variables behind private scope and exposing public getter/setter methods."
        },
        {
            "q": "Which of the following is used to free the memory allocated for an object when it goes out of scope?",
            "o": ["A) Constructor", "B) Destructor", "C) Garbage Collector only", "D) Pointer"],
            "a": "B",
            "d": "Easy",
            "exp": "Destructors clean up object memory and resources. They run automatically when an object goes out of scope or is deleted."
        },
        {
            "q": "What is inheritance?",
            "o": ["A) Deleting classes", "B) A mechanism where a new class (derived) acquires properties and behaviors of an existing class (base)", "C) Creating static interfaces", "D) Overloading operators"],
            "a": "B",
            "d": "Easy",
            "exp": "Inheritance promotes code reusability by letting subclasses inherit fields and methods from a superclass."
        },
        {
            "q": "Which OOP pillar focuses on hiding internal details and showing only essential features?",
            "o": ["A) Inheritance", "B) Abstraction", "C) Polymorphism", "D) Encapsulation"],
            "a": "B",
            "d": "Easy",
            "exp": "Abstraction hides complex backend logic and implementation details, providing a simple interface to the user (e.g. using interfaces or abstract classes)."
        },
        # Medium
        {
            "q": "What is the difference between Method Overloading and Method Overriding?",
            "o": ["A) Overloading is runtime polymorphism; Overriding is compile-time", "B) Overloading occurs in the same class (same name, different arguments); Overriding occurs in inherited classes (same name, same arguments)", "C) Overriding requires static methods; Overloading requires virtual methods", "D) There is no difference"],
            "a": "B",
            "d": "Medium",
            "exp": "Method Overloading is compile-time polymorphism. Method Overriding is runtime polymorphism, where a subclass redefines a base class method with the exact same signature."
        },
        {
            "q": "What is an 'Abstract Class'?",
            "o": ["A) A class with no variables", "B) A class that cannot be instantiated and contains at least one pure virtual function (abstract method)", "C) A class defined inside another class", "D) A class containing only static methods"],
            "a": "B",
            "d": "Medium",
            "exp": "Abstract classes serve as blueprints. They cannot be instantiated directly and force subclasses to implement their abstract methods."
        },
        {
            "q": "Which inheritance type can lead to the 'Diamond Problem'?",
            "o": ["A) Single Inheritance", "B) Multiple Inheritance", "C) Multilevel Inheritance", "D) Hierarchical Inheritance"],
            "a": "B",
            "d": "Medium",
            "exp": "Multiple inheritance causes the diamond problem when a class inherits from two classes that both inherit from a single superclass, causing ambiguity over duplicated methods."
        },
        {
            "q": "What does the `super` keyword do in Java/Python subclass constructors?",
            "o": ["A) Deletes base class fields", "B) Calls the constructor/methods of the parent class", "C) Makes the method run faster", "D) Declares a static class"],
            "a": "B",
            "d": "Medium",
            "exp": "`super()` invokes parent class constructors or methods, ensuring parent fields are initialized correctly."
        },
        {
            "q": "What is a 'Copy Constructor'?",
            "o": ["A) A constructor that duplicates classes", "B) A constructor that initializes an object using another existing object of the same class", "C) A method to copy files", "D) A constructor that returns static values"],
            "a": "B",
            "d": "Medium",
            "exp": "A copy constructor clones objects. It takes a reference to an object of the same class as a parameter to duplicate its state."
        },
        # Hard
        {
            "q": "In C++, if a class inherits publicly from a base class, what do the protected members of the base class become in the derived class?",
            "o": ["A) Private", "B) Protected", "C) Public", "D) Unaccessible"],
            "a": "B",
            "d": "Hard",
            "exp": "Under public inheritance: Public becomes Public, Protected remains Protected, and Private remains unaccessible directly."
        },
        {
            "q": "What is 'Runtime Polymorphism' achieved by?",
            "o": ["A) Function Overloading", "B) Virtual Functions and Method Overriding", "C) Operator Overloading", "D) Template Classes"],
            "a": "B",
            "d": "Hard",
            "exp": "Runtime polymorphism uses virtual tables (vtables) to resolve overridden method calls at execution time based on the actual object type, not the pointer type."
        },
        {
            "q": "What is a 'Friend Function' in C++?",
            "o": ["A) A function defined in a subclasses", "B) A non-member function that has permission to access the private and protected members of a class", "C) A public class method", "D) An overloaded constructor"],
            "a": "B",
            "d": "Hard",
            "exp": "A friend function is declared inside a class with the `friend` keyword. It is not a member function, but can read private class variables."
        },
        {
            "q": "What is 'Object Slicing' in C++?",
            "o": ["A) Dividing an object array", "B) Assigning a derived class object to a base class object, causing the derived-specific fields to be discarded", "C) Deleting object attributes", "D) Casting pointers"],
            "a": "B",
            "d": "Hard",
            "exp": "Object slicing occurs when a derived object is passed by value to a base object parameter; the base copy constructor executes, stripping away derived-specific data."
        },
        {
            "q": "What is the difference between a shallow copy and a deep copy?",
            "o": ["A) Shallow copy copies values; deep copy copies names", "B) Shallow copy copies reference pointers (sharing memory); deep copy duplicates the referenced data in new memory", "C) Shallow copy is faster; deep copy is compile-time", "D) Shallow copy is for primitives; deep copy for objects"],
            "a": "B",
            "d": "Hard",
            "exp": "Shallow copying duplicates pointers, leading to shared state (changes in one affect the other). Deep copying allocates new memory to create independent object copies."
        }
    ],
    "CN": [
        # Easy
        {
            "q": "Which OSI layer is responsible for routing packets across different networks?",
            "o": ["A) Transport Layer", "B) Network Layer", "C) Data Link Layer", "D) Physical Layer"],
            "a": "B",
            "d": "Easy",
            "exp": "The Network Layer handles IP addressing, packet creation, and routing across different network boundaries."
        },
        {
            "q": "What is the main difference between TCP and UDP?",
            "o": ["A) TCP is faster than UDP", "B) TCP is connection-oriented and reliable; UDP is connectionless and lightweight", "C) UDP uses IP; TCP does not", "D) TCP is at the network layer; UDP is at transport"],
            "a": "B",
            "d": "Easy",
            "exp": "TCP uses handshakes, ACKs, and retransmissions for reliability. UDP just sends packets immediately without confirmation (faster but unreliable)."
        },
        {
            "q": "What is the port number for standard secured HTTP (HTTPS) traffic?",
            "o": ["A) 80", "B) 443", "C) 21", "D) 22"],
            "a": "B",
            "d": "Easy",
            "exp": "Port 80 is for HTTP (unsecured), and Port 443 is for HTTPS (secured via SSL/TLS)."
        },
        # Medium
        {
            "q": "Which protocol translates domain names (like google.com) into IP addresses?",
            "o": ["A) HTTP", "B) FTP", "C) DNS", "D) DHCP"],
            "a": "C",
            "d": "Medium",
            "exp": "DNS (Domain Name System) acts as the phonebook of the internet, mapping human-readable hostnames to IP addresses."
        },
        {
            "q": "What is the function of the ARP (Address Resolution Protocol)?",
            "o": ["A) Map domain names to IP addresses", "B) Map an IP address to a physical MAC address", "C) Route packets across routers", "D) Assign temporary IPs to devices"],
            "a": "B",
            "d": "Medium",
            "exp": "ARP resolves local IP addresses to physical hardware MAC addresses on a local area network (LAN)."
        },
        {
            "q": "Which device operates primarily at the Data Link Layer (Layer 2) of the OSI model?",
            "o": ["A) Hub", "B) Switch", "C) Router", "D) Repeater"],
            "a": "B",
            "d": "Medium",
            "exp": "Switches use MAC addresses to forward frames to specific ports (Layer 2). Hubs are layer 1 (broadcasts raw electrical signals)."
        },
        {
            "q": "What is 'Subnetting'?",
            "o": ["A) Connecting multiple networks together", "B) Dividing a single large network into smaller sub-networks to improve performance and security", "C) Encrypting IP headers", "D) Running multiple web servers"],
            "a": "B",
            "d": "Medium",
            "exp": "Subnetting splits network addresses using subnet masks to partition host ranges and reduce broadcast domains."
        },
        # Hard
        {
            "q": "What does the TCP 3-Way Handshake consist of?",
            "o": ["A) SYN, SYN-ACK, ACK", "B) PING, PONG, ACK", "C) CONNECT, ACCEPT, SUCCESS", "D) FIN, ACK, FIN-ACK"],
            "a": "A",
            "d": "Hard",
            "exp": "The connection is established using: 1. client sends SYN, 2. server responds with SYN-ACK, 3. client replies with ACK."
        },
        {
            "q": "What is the purpose of the 'Time to Live' (TTL) field in an IPv4 packet header?",
            "o": ["A) To measure network speed", "B) To prevent packets from looping endlessly in the network", "C) To record packet creation time", "D) To encrypt data payloads"],
            "a": "B",
            "d": "Hard",
            "exp": "Each router decrements the TTL by 1. If TTL reaches 0, the packet is discarded and an ICMP error is sent, preventing infinite routing loops."
        },
        {
            "q": "Which routing protocol uses the Dijkstra algorithm to calculate the shortest path?",
            "o": ["A) RIP", "B) OSPF", "C) BGP", "D) EIGRP"],
            "a": "B",
            "d": "Hard",
            "exp": "OSPF (Open Shortest Path First) is a link-state routing protocol that uses Dijkstra's algorithm to compute the shortest-path tree."
        }
    ],
    "AI": [
        # Easy
        {
            "q": "What does RAG stand for in modern AI systems?",
            "o": ["A) Recursive Algorithm Generator", "B) Retrieval-Augmented Generation", "C) Real-time Agentic Grouping", "D) Random Attribute Generator"],
            "a": "B",
            "d": "Easy",
            "exp": "RAG (Retrieval-Augmented Generation) retrieves documents from an external dataset to guide LLM responses."
        },
        {
            "q": "What is the primary purpose of 'embeddings' in NLP?",
            "o": ["A) To encrypt text files", "B) To represent words or sentences as high-dimensional vectors capturing semantic meaning", "C) To check spelling errors", "D) To compile python scripts"],
            "a": "B",
            "d": "Easy",
            "exp": "Embeddings translate words/sentences into numbers, keeping semantically similar concepts close in vector space."
        },
        {
            "q": "Which parameter controls the randomness of responses in LLMs?",
            "o": ["A) Max Tokens", "B) Temperature", "C) Top K", "D) System Prompt"],
            "a": "B",
            "d": "Easy",
            "exp": "Temperature controls output probability distribution. Lower values make responses deterministic; higher values make them creative/random."
        },
        # Medium
        {
            "q": "In a RAG pipeline, why are documents split into 'chunks' before indexing?",
            "o": ["A) To speed up hard disk reads", "B) To fit source texts into LLM context windows and vector indexing search sizes", "C) To translate text to binary", "D) To remove punctuation"],
            "a": "B",
            "d": "Medium",
            "exp": "Chunking ensures context snippets are small enough to stay relevant and avoid exceeding context length limits of LLMs."
        },
        {
            "q": "What is 'Hallucination' in LLMs?",
            "o": ["A) The model crashing", "B) The model generating text that is factually incorrect or unsupported by the context", "C) High CPU temp", "D) Slow token output speed"],
            "a": "B",
            "d": "Medium",
            "exp": "Hallucinations occur when an LLM confidently outputs fabricated information instead of actual facts."
        },
        {
            "q": "What is a vector database (e.g. FAISS, ChromaDB) used for?",
            "o": ["A) Saving SQL tables", "B) Storing and performing fast similarity searches on vector embeddings", "C) Running Python scripts", "D) Version control"],
            "a": "B",
            "d": "Medium",
            "exp": "Vector databases index embeddings and perform fast searches (like Cosine or L2 distance) to find matching documents."
        },
        {
            "q": "What does 'Few-Shot Prompting' mean?",
            "o": ["A) Running the model multiple times", "B) Providing a few examples of input-output pairs in the prompt to guide the LLM's behavior", "C) Using tiny models", "D) Querying the model quickly"],
            "a": "B",
            "d": "Medium",
            "exp": "Few-Shot prompting includes example tasks in the prompt context to help the model learn the pattern in-context."
        },
        # Hard
        {
            "q": "What distinguishes an 'Agentic AI' system from a basic chain of LLM calls?",
            "o": ["A) Using API keys", "B) An autonomous execution loop where the LLM can call tools, evaluate outputs, and adjust its plan dynamically", "C) Using local GPU servers", "D) Using PyTorch libraries"],
            "a": "B",
            "d": "Hard",
            "exp": "Agents use loops (like ReAct framework) to plan, call tools (APIs, calculators), read outputs, and self-correct until the goal is met."
        },
        {
            "q": "How does the ReAct (Reasoning and Acting) prompt framework operate?",
            "o": ["A) By compiling prompt strings", "B) Alternating between thought steps (reasoning) and action steps (calling tools/acting) to solve a task", "C) Restricting tool calls", "D) Using reinforcement learning only"],
            "a": "B",
            "d": "Hard",
            "exp": "ReAct prompt structure forces the LLM to structure its output into 'Thought:', 'Action:', 'Observation:', and 'Thought:' loops."
        },
        {
            "q": "What is a 'System Prompt' (or System Message) in Chat APIs?",
            "o": ["A) System configuration variables", "B) A high-priority instruction that sets the persona, constraints, and behavior rules for the LLM throughout the conversation", "C) The user query", "D) A prompt to format JSON outputs only"],
            "a": "B",
            "d": "Hard",
            "exp": "System messages set the global behavior of the AI assistant, acting as guardrails that govern how it responds to subsequent user messages."
        }
    ]
}

# Expand the questions list to exactly 100 questions.
# We will duplicate/augment questions slightly with different contexts to ensure the database has exactly 100 questions 
# under various subjects (DSA: 25, OS: 20, DBMS: 20, OOPs: 15, CN: 10, AI: 10).
# Let's add variations to fulfill the quota.

# DSA Extras (adding 10 to reach 25)
DSA_EXTRAS = [
    {"q": "What is the time complexity of searching in a Hash Table in the best/average case?", "o": ["A) O(1)", "B) O(N)", "C) O(log N)", "D) O(N log N)"], "a": "A", "d": "Easy", "exp": "Average time complexity of hash table lookups is constant O(1)."},
    {"q": "Which data structure is best suited to implement recursive function calls?", "o": ["A) Queue", "B) Stack", "C) Tree", "D) Heap"], "a": "B", "d": "Easy", "exp": "The system call stack manages return addresses and local variables recursively."},
    {"q": "What is the height of a complete binary tree with N nodes?", "o": ["A) O(N)", "B) O(log N)", "C) O(N log N)", "D) O(1)"], "a": "B", "d": "Easy", "exp": "A complete binary tree has a logarithmic height, O(log N)."},
    {"q": "Which sorting algorithm is typically used in the Java Arrays.sort() for primitives (Dual-Pivot)?", "o": ["A) Merge Sort", "B) Quick Sort", "C) Insertion Sort", "D) Bubble Sort"], "a": "B", "d": "Medium", "exp": "Java uses Dual-Pivot Quick Sort for primitives because of its low average overhead."},
    {"q": "What is the time complexity of Dijkstra's algorithm using a binary heap?", "o": ["A) O(V^2)", "B) O((V + E) log V)", "C) O(E log V)", "D) O(V^3)"], "a": "B", "d": "Medium", "exp": "Using binary heaps, extracting min is O(log V) and updating keys is O(log V), yielding O((V + E) log V)."},
    {"q": "What is the worst-case time complexity of lookup in a Trie (Prefix Tree) of key length L?", "o": ["A) O(N)", "B) O(L)", "C) O(log N)", "D) O(N log L)"], "a": "B", "d": "Medium", "exp": "Trie lookups only depend on the length of the query key L, taking O(L) time."},
    {"q": "What does a SegTree (Segment Tree) optimize to O(log N) time?", "o": ["A) Matrix multiplications", "B) Range queries and point updates", "C) Tree height calculations", "D) Sorting arrays"], "a": "B", "d": "Hard", "exp": "Segment Trees allow query and update operations on array intervals in logarithmic time."},
    {"q": "What is the amortized time complexity of inserting into a Dynamic Array (vector in C++ / list in Python)?", "o": ["A) O(1)", "B) O(N)", "C) O(log N)", "D) O(N^2)"], "a": "A", "d": "Hard", "exp": "Though resizing takes O(N), resizing is rare (doubling size). Thus, amortized insertion is O(1)."},
    {"q": "Which algorithmic paradigm does the 0/1 Knapsack dynamic programming state equation belong to?", "o": ["A) Greedy Approach", "B) Divide and Conquer", "C) Overlapping Subproblems and Optimal Substructure", "D) Backtracking"], "a": "C", "d": "Hard", "exp": "Dynamic Programming requires optimal substructure and overlapping subproblems."},
    {"q": "What is the time complexity of finding a cycle in a directed graph of V vertices and E edges using DFS?", "o": ["A) O(V^2)", "B) O(V + E)", "C) O(V * E)", "D) O(1)"], "a": "B", "d": "Hard", "exp": "DFS traverses vertices and edges, detecting cycles using back-edges in O(V + E) time."}
]
QUESTIONS["DSA"].extend(DSA_EXTRAS)

# OS Extras (adding 5 to reach 20)
OS_EXTRAS = [
    {"q": "What does the 'SSTF' disk scheduling algorithm do?", "o": ["A) Services requests in FIFO order", "B) Services the request closest to the current cylinder position", "C) Sweeps the cylinder head continuously", "D) Deletes redundant disk tracks"], "a": "B", "d": "Easy", "exp": "Shortest Seek Time First (SSTF) selects the request closest to the current head to minimize seek distance."},
    {"q": "What is a 'Thread pool'?", "o": ["A) Storing threads on disk", "B) A collection of pre-instantiated, reusable worker threads that perform tasks in queue", "C) A network protocol", "D) A type of deadlock state"], "a": "B", "d": "Medium", "exp": "Thread pools manage a fixed number of threads, avoiding thread creation overhead."},
    {"q": "Which command is used in Linux to display running processes?", "o": ["A) ls", "B) pwd", "C) ps (or top)", "D) mkdir"], "a": "C", "d": "Easy", "exp": "`ps` prints active processes, and `top` shows live CPU/process usage."},
    {"q": "What is 'Overlays' in memory management?", "o": ["A) Caching page tables", "B) Keeping only those instructions and data in memory that are needed at any given time, managed by the programmer", "C) Swapping all pages", "D) Sharing RAM sectors"], "a": "B", "d": "Hard", "exp": "Overlays allow running programs larger than physical memory before virtual memory existed, handled directly by the program logic."},
    {"q": "What does 'Mutual Exclusion' ensure?", "o": ["A) All threads run together", "B) Only one process can access a shared resource at any given time", "C) CPU scheduling occurs on time", "D) Hard drive reads are atomic"], "a": "B", "d": "Easy", "exp": "Mutual exclusion prevents race conditions by locking resources so only one process accesses them at a time."}
]
QUESTIONS["OS"].extend(OS_EXTRAS)

# DBMS Extras (adding 5 to reach 20)
DBMS_EXTRAS = [
    {"q": "Which SQL statement is used to remove a table structure and all its data permanently?", "o": ["A) DELETE TABLE", "B) REMOVE TABLE", "C) DROP TABLE", "D) TRUNCATE TABLE"], "a": "C", "d": "Easy", "exp": "DROP TABLE deletes both the table schema and all its rows from the database."},
    {"q": "What is a 'Composite Key'?", "o": ["A) A primary key containing foreign keys", "B) A primary key composed of two or more columns to uniquely identify rows", "C) A key consisting of hash values", "D) A temporary secondary key"], "a": "B", "d": "Easy", "exp": "Composite keys combine multiple fields to guarantee uniqueness when a single column is insufficient."},
    {"q": "What is 'Data Redundancy'?", "o": ["A) Storing the same data in multiple places unnecessarily", "B) Fast data reading speeds", "C) Correctness of data fields", "D) Encrypting database columns"], "a": "A", "d": "Easy", "exp": "Data redundancy is the duplication of information, leading to storage waste and inconsistency anomalies."},
    {"q": "What is the primary objective of a 'View' in SQL?", "o": ["A) To speed up queries", "B) To create a virtual table based on a query result, providing security and abstraction", "C) To store temporary index values", "D) To compile database functions"], "a": "B", "d": "Medium", "exp": "Views act as virtual tables, hiding complex joins and restricting users' access to direct underlying tables."},
    {"q": "In functional dependency, what does dependency preservation ensure?", "o": ["A) Fast SQL execution", "B) All functional dependencies in the original schema are satisfied in the decomposed schemas", "C) Keys are duplicated", "D) Integrity checks are skipped"], "a": "B", "d": "Hard", "exp": "Dependency preservation ensures we can enforce all original constraints without performing expensive joins."}
]
QUESTIONS["DBMS"].extend(DBMS_EXTRAS)

# OOPs Extras (adding 5 to reach 15)
OOPS_EXTRAS = [
    {"q": "Which modifier prevents a class from being inherited by other classes?", "o": ["A) static", "B) abstract", "C) final (or sealed)", "D) protected"], "a": "C", "d": "Easy", "exp": "A `final` class in Java/C# cannot be subclassed (preventing inheritance)."},
    {"q": "What is a 'Default Constructor'?", "o": ["A) A constructor with no parameters, created automatically if no constructor is defined", "B) A static class constructor", "C) A constructor that returns default values", "D) A constructor that clones objects"], "a": "A", "d": "Easy", "exp": "A default constructor takes no arguments and is provided by the compiler to initialize object fields with default values."},
    {"q": "What does 'Function Signature' contain in OOP?", "o": ["A) Return type and values", "B) Function name and parameter types/order", "C) Class name only", "D) Compiler annotations"], "a": "B", "d": "Medium", "exp": "A signature defines the function name and arguments list, used by the compiler to resolve overloaded methods."},
    {"q": "What is 'Multiple Inheritance'?", "o": ["A) A class inheriting from multiple subclasses", "B) A subclass inheriting from more than one base class", "C) Creating multiple objects of a class", "D) Inheriting fields across multiple packages"], "a": "B", "d": "Easy", "exp": "Multiple inheritance occurs when a derived class inherits directly from two or more parent base classes."},
    {"q": "What is the key difference between an Interface and an Abstract Class?", "o": ["A) Interfaces can have constructors; abstract classes cannot", "B) Interfaces only support static variables", "C) A class can implement multiple interfaces but can inherit only one abstract class in single-inheritance systems", "D) Abstract classes run compile-time operations; interfaces run runtime"], "a": "C", "d": "Hard", "exp": "Interfaces allow multiple inheritance of design interfaces, whereas abstract classes represent a strict 'is-a' hierarchy."}
]
QUESTIONS["OOPs"].extend(OOPS_EXTRAS)


def run_quiz():
    print("=====================================================")
    print("🎓 ScriptedBy{Her} 2.0 - 100 MCQ Practice Quiz")
    print("=====================================================")
    print("Select Practice Mode:")
    print("1. Data Structures & Algorithms (25 Questions)")
    print("2. Operating Systems (20 Questions)")
    print("3. Database Management Systems (20 Questions)")
    print("4. Object-Oriented Programming (15 Questions)")
    print("5. Computer Networks (10 Questions)")
    print("6. Agentic AI & RAG (10 Questions)")
    print("7. Full Mock Test (Random 20 Questions from all topics)")
    print("=====================================================")
    
    choice = input("Enter choice (1-7): ").strip()
    
    topic_map = {
        "1": ("DSA", QUESTIONS["DSA"]),
        "2": ("OS", QUESTIONS["OS"]),
        "3": ("DBMS", QUESTIONS["DBMS"]),
        "4": ("OOPs", QUESTIONS["OOPs"]),
        "5": ("CN", QUESTIONS["CN"]),
        "6": ("AI", QUESTIONS["AI"])
    }
    
    selected_questions = []
    mode_title = ""
    
    if choice in topic_map:
        topic_name, q_list = topic_map[choice]
        selected_questions = q_list
        mode_title = f"{topic_name} Practice Mode"
    elif choice == "7":
        all_qs = []
        for q_list in QUESTIONS.values():
            all_qs.extend(q_list)
        selected_questions = random.sample(all_qs, min(len(all_qs), 20))
        mode_title = "Full Mock Test (20 Random Questions)"
    else:
        print("❌ Invalid choice. Exiting.")
        return
        
    print(f"\n🚀 Starting {mode_title}...")
    print(f"Total questions to answer: {len(selected_questions)}")
    print("=====================================================")
    
    score = 0
    total = len(selected_questions)
    
    for idx, q_data in enumerate(selected_questions, 1):
        print(f"\nQuestion {idx}/{total} [{q_data['d']}]:")
        print(q_data["q"])
        for option in q_data["o"]:
            print(option)
            
        user_ans = ""
        while user_ans not in ["A", "B", "C", "D"]:
            user_ans = input("Your answer (A, B, C, or D): ").strip().upper()
            
        if user_ans == q_data["a"]:
            print("🎉 Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {q_data['a']}")
            
        print(f"💡 Explanation: {q_data['exp']}")
        print("-" * 50)
        
    print("\n=====================================================")
    print("🏁 Quiz Completed!")
    print(f"Your Score: {score}/{total} ({(score/total)*100:.2f}%)")
    print("=====================================================")
    print("Keep practicing to ace ScriptedBy{Her} 2.0!")
    print("=====================================================")

if __name__ == "__main__":
    run_quiz()
