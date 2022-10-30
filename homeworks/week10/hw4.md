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

<div style="page-break-after: always"></div>

### **2. [ACID vs BASE]: Data Consistency**

#### a. CAP Theorem

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

  - data is always available for each server, but is not guaranteed to be up-to-date without *replication and verification*.

- **C**onsistency and **P**artition Tolerence (forfeiting **A**)

  - data needs to be consistent across all three servers, for which the system must perform *replication and verification*, during which the data is inaccessible.

- **C**onsistency and **A**vailability (forfeiting **P**)

  - data is always available and consistent for one server, but this state is not guaranteed to hold across all three servers, and thus needs to be *replicated and verified* for the other two.

#### b. Show ACID can be violated using the relation Accounts.

> A database requires 4 properties:
> - **A***tomicity*: when an update happens, it is *all updated or nothing is updated*.
> - **C***onsistency*: the states of various tables must be consistent (relations, constraints) at all times.
> - **I***solation*: concurrent execution of transactions produces the same outcome as if done sequentially.
> - **D***urability*: once commmitted, the outcome of a transaction is immutable to problems like power outage, etc.

The commit has two statements, so they are not atomic. This commit is not resistent to a power outage, which might cause only one statement to be committed successfully, regardless whether they were submitted sequentially or concurrently.  This situation in turn cause the accounts to be inconsistent.

#### c. ACID vs BASE

**BASE** database model fundamentally forfeits **C**onsistency and **I**solation for **A**vailability:

> **B**asically **A**vailable,
> **S**oft state,
> **E**ventually consistent

A BASE model allows for:

- stale data (weak consistency)
- prioritizing availability
- best effort
- approximate answers
- simpler and faster than ACID

<div style="page-break-after: always"></div>

### **3. Quorum Consensus**

**Quorum Concensus** is a voting model to improve fault tolerance and consistency. A quorum is the minimum number of majority votes to win any transaction commit. A quorum must be defined for every system, typically $W + R > N$ where $N$ is the number of servers in the system.

This model contains two sequential operations, **put** and **get**, and a final vote count. A **put** request is sent to multiple servers so that in the case one server fails other servers still hold copies of data. Next, a **get** request is sent to multiple servers containing the redundant data. Finally, the commit is granted if and only if the sum of successful **put** and **get** requests is larger than the total number of servers. 

This model works because it satisfies all ACID properties.

<div style="page-break-after: always"></div>

### **4. Column Store**


