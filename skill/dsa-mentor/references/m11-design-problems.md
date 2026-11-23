# Module 11 of 11: Design Problems

> Naming note: the study-resources source calls this module "Specialized Topics & System-Level DSA Design". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- LRU & LFU Cache Design
- Skip Lists & Probabilistic Structures
- String-System Hybrid Structures & External Sorting

---

## PART A: Curriculum and Core Practice Bank

A real, recurring category, especially at Amazon, where "design a data structure that supports X, Y, Z each in O(1)/O(log n)" is a standing interview archetype in its own right — distinct from a one-off hard problem because it tests composition of structures, not recall of one.

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Design Problems (LRU/LFU Cache, rate limiters, streaming structures) | Combine 2+ data structures to hit specific complexity targets per operation | Hard | Hashing, Linked Lists, Heaps | Its own interview archetype, not just "a hard problem" — tests whether you can *compose* structures, not just recall one. | 4 Days | 35% |

### Core Practice Bank — Module 11

- LC 146 — LRU Cache (Medium) — https://leetcode.com/problems/lru-cache/ — the single most-asked design problem on LeetCode; know it cold
- LC 460 — LFU Cache (Hard) — https://leetcode.com/problems/lfu-cache/
- LC 355 — Design Twitter (Medium) — https://leetcode.com/problems/design-twitter/
- LC 706 — Design HashMap (Easy) — https://leetcode.com/problems/design-hashmap/ — deceptively useful for confirming you actually understand hashing internals
- LC 895 — Maximum Frequency Stack (Hard) — https://leetcode.com/problems/maximum-frequency-stack/

---

---

## PART B: Curated study resources

### Topic: LRU & LFU Cache Design

Caching systems leverage fast memory buffers to serve frequently accessed records. Least Recently Used (LRU) evicts the oldest unaccessed item; Least Frequently Used (LFU) evicts the item with the lowest access count, breaking ties by recency.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Doubly Linked List + HashMap Mechanics | GeeksforGeeks: Design an LRU Cache | Guide | Demonstrates combining a doubly linked list ($\mathcal{O}(1)$ node removal/insertion) with a Java `HashMap` ($\mathcal{O}(1)$ node lookup). | [GeeksforGeeks LRU Cache](https://www.geeksforgeeks.org/lru-cache-implementation/) |
| Frequency Bucket Map Alignment | LeetCode Official Solution: LFU Cache | Editorial | Explains multi-frequency doubly linked list buckets maintaining global minimum frequency markers in $\mathcal{O}(1)$ time. | [LeetCode Problem 460 Editorial](https://leetcode.com/problems/lfu-cache/) |

#### Recommended Learning Stack
1. **Concept:** GeeksforGeeks LRU Cache & LeetCode LFU Cache editorials.
2. **Implementation:** Authoring custom inner classes `Node` and `DoublyLinkedList` in Java to implement `LRUCache` and `LFUCache`.
3. **Practice:** Core syllabus bank (LC 146, LC 460, LC 432).

---

### Topic: Skip Lists & Probabilistic Structures

Skip Lists leverage probabilistic randomized balance to support $\mathcal{O}(\log N)$ search, insertion, and deletion using linked nodes with variable height forward pointer arrays, eliminating the complex tree rebalancing required by AVL or Red-Black trees.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Probabilistic Tower Heights & Forward Pointers | William Pugh: *Skip Lists: A Probabilistic Alternative to Balanced Trees* (1990) | Original Academic Paper | The primary paper introducing Skip List invariants, coin-flip height generation, and expected performance proofs. | Communications of the ACM, June 1990 |

#### Recommended Learning Stack
1. **Concept:** William Pugh's seminal 1990 Skip List paper.
2. **Implementation:** Writing custom `Node` structures with `Node[] forward` pointer arrays and coin-toss level generation in Java.
3. **Practice:** Core syllabus bank (LC 1206).

---

### Topic: String-System Hybrid Structures & External Sorting

System-level algorithms handle inputs that exceed main memory bounds. External Merge Sort divides vast datasets into memory-sized chunks, sorts them locally, and uses a min-heap to perform a $K$-way merge across disk streams.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| $K$-Way Stream Merging & Disk Buffering | *Database Management Systems, 3rd Edition* (Ramakrishnan & Gehrke) | Book | Chapter 13: "External Sorting", detailing run generation, buffer allocation, and tournament tree/heap merges. | Ramakrishnan & Gehrke -> Chapter 13 |

#### Recommended Learning Stack
1. **Concept:** Ramakrishnan & Gehrke, *Database Management Systems*, Chapter 13.
2. **Implementation:** Priority Queue $K$-way stream reader merging routines in Java.
3. **Practice:** Core syllabus bank (LC 23, LC 355).
