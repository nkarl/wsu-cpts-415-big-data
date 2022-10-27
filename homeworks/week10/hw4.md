# CptS 415 | Assignment-04

## Charles Nguyen, \#011606177

### **1. Parallel Data Model**

a. Amdahl's Law.

b. Describe and compare the pros and cons of the three architectures for parallel systems.

- Shared Memory:
  - efficient communication, because memory is accessible to all processors.
  - **low scalability** since the shared memory and network capacity end up becoming the bottleneck of communication.
  - even if memory cache is added for each processor, there is still the problem of data consistency whenever data needs to be updated across all processors. 
  - upperbound of scalability is 32/64 processors.

- Shared Disk
  - high fault tolerance, because other processors can take over when one processor fails.
  - **better scalability** because data is now resident on disk without being dependent on memory.
  - is still reliant on network capacity.
  - upperbound of scalability is a couple hundred processors.

- Shared Nothing
  - **only queries** are passed through the network
  - theoretically **no upper limit to scalability**

### **2. [ACID vs BASE]: Data Consistency**

a. CAP Theory

b. Relation Accounts.

### **3. Quorum Consensus**

### **4. Column Store**
