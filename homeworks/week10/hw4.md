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

a. CAP Theorem

> A system can have at most 2 out of 3 properties:
> - **C***onsistency*: each client can always read and write
> - **A***vailability*: all clients always have the same view of data.
> - **P***artition Tolerance*: the system produces deterministic outcomes despite physical network partitions.

```txt
Assumptions:
  - a system with three geographically distributed servers S1 and S2 and S3.
  - data is partitioned across all three servers.
```
  
- **A**vailability and **P**artition Tolerence (forfeiting **C**)

  - data is always available for each server, but is not guaranteed to be consistent without *replication and verification*.

- **C**onsistency and **P**artition Tolerence (forfeiting **A**)

  - data needs to be consistent across all three servers, for which the system must perform *replication and verification*, during which the data is inaccessible.

- **C**onsistency and **A**vailability (forfeiting **P**)

  - data is always available and consistent for one server, but this state is not guaranteed to hold across the other two servers and thus needs to be *replicated and verified*.

b. Relation Accounts.

### **3. Quorum Consensus**

### **4. Column Store**
