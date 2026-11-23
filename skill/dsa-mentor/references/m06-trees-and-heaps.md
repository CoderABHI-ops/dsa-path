# Module 6 of 11: Trees & Heaps

> Naming note: the study-resources source calls this module "Trees, Binary Search Trees & Heaps". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Tree Traversals & Recursion Dynamics
- Binary Search Trees (BST) & Balanced BSTs
- Binary Heaps & Priority Queues

---

## PART A: Curriculum and Core Practice Bank

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Binary Trees | Hierarchical data, traversals | Medium | Recursion | Tests recursion mastery; extremely high ROI. | 5 Days | 85% |
| Binary Search Trees (BST) | Ordered tree structure and its invariants | Medium | Binary Trees | Property-based traversal/validation logic. | 3 Days | 55% |
| Balanced BST Concepts (AVL/Red-Black, `TreeMap`/`TreeSet`) | *Conceptual* understanding of self-balancing — not implementing rotations | Med | BST | You're expected to know *why* `TreeMap` ops are O(log n) even without coding a rotation live. | 1 Day | 25% |
| Heaps / Priority Queues | Efficient "top/bottom K" access | Medium | Trees | The default answer for streaming/"kth" problems. | 4 Days | 70% |

### Core Practice Bank — Module 6

**Binary Trees**
- LC 104 — Maximum Depth of Binary Tree (Easy) — https://leetcode.com/problems/maximum-depth-of-binary-tree/
- LC 226 — Invert Binary Tree (Easy) — https://leetcode.com/problems/invert-binary-tree/
- LC 543 — Diameter of Binary Tree (Easy) — https://leetcode.com/problems/diameter-of-binary-tree/
- LC 236 — Lowest Common Ancestor of a Binary Tree (Medium) — https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
- LC 102 — Binary Tree Level Order Traversal (Medium) — https://leetcode.com/problems/binary-tree-level-order-traversal/
- LC 124 — Binary Tree Maximum Path Sum (Hard) — https://leetcode.com/problems/binary-tree-maximum-path-sum/
- LC 297 — Serialize and Deserialize Binary Tree (Hard) — https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

**BST**
- LC 98 — Validate Binary Search Tree (Medium) — https://leetcode.com/problems/validate-binary-search-tree/
- LC 230 — Kth Smallest Element in a BST (Medium) — https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- LC 235 — Lowest Common Ancestor of a Binary Search Tree (Medium) — https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- LC 108 — Convert Sorted Array to Binary Search Tree (Easy) — https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

**Heaps / Priority Queues**
- LC 215 — Kth Largest Element in an Array (Medium) — https://leetcode.com/problems/kth-largest-element-in-an-array/
- LC 23 — Merge k Sorted Lists (Hard) — https://leetcode.com/problems/merge-k-sorted-lists/
- LC 347 — Top K Frequent Elements (Medium) — https://leetcode.com/problems/top-k-frequent-elements/
- LC 295 — Find Median from Data Stream (Hard) — https://leetcode.com/problems/find-median-from-data-stream/ — the two-heap pattern
- LC 621 — Task Scheduler (Medium) — https://leetcode.com/problems/task-scheduler/

---

---

## PART B: Curated study resources

### Topic: Tree Traversals & Recursion Dynamics

Trees are connected acyclic graph topologies. Tree traversals visit every node in structured orders (Pre-order, In-order, Post-order via DFS, and Level-order via BFS), mapping recursive stack frames to tree depth.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Recursive Traversal Frames & Call Stack Bounds | Stanford CS Library: Binary Trees (Nick Parlante) | Monograph | Visualizes recursive call frames, stack depth limits, tree height, and base-case termination. | [Stanford CS Binary Trees](http://cslibrary.stanford.edu/110/BinaryTrees.html) |
| Iterative Traversals & Morris Traversal | GeeksforGeeks: Inorder Tree Traversal Without Recursion | Guide / Article | Explains iterative stack manipulation and $\mathcal{O}(1)$ space Morris Traversal using threaded binary trees. | [GeeksforGeeks Morris Traversal](https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/) |

#### Recommended Learning Stack
1. **Concept:** Stanford CS Library: *Binary Trees* by Nick Parlante.
2. **Implementation:** Recursive DFS templates and iterative stack/queue traversals in Java.
3. **Practice:** Core syllabus bank (LC 144, LC 94, LC 145, LC 102, LC 104, LC 111, LC 226, LC 112, LC 124, LC 236, LC 105, LC 297).

---

### Topic: Binary Search Trees (BST) & Balanced BSTs

Binary Search Trees maintain the key invariant that for any node $V$, all keys in $V$'s left subtree are strictly smaller than $V$'s key, and all keys in $V$'s right subtree are strictly larger. Balanced variants (AVL, Red-Black) guarantee $\mathcal{O}(\log N)$ operations by preventing tree skew.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| BST Invariants & Operations | Princeton CS: *Algorithms, 4th Edition* (Sedgewick) | Book / Web Portal | Deconstructs insertion, deletion (Hibbard deletion), and in-order predecessor/successor queries. | [Princeton Algs4 BSTs](https://algs4.cs.princeton.edu/32bst/) |
| Balanced BST Rotations (Red-Black / AVL) | MIT OpenCourseWare 6.006: Balanced BSTs | University Course | Mathematical breakdown of tree rotations, balance factors, and color-flip invariants. | [MIT OCW 6.006 AVL & Red-Black Trees](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) |

#### Recommended Learning Stack
1. **Concept:** Princeton Algorithms 4th Edition, Section 3.2.
2. **Implementation:** Writing recursive BST insertion, search, and deletion in Java.
3. **Practice:** Core syllabus bank (LC 700, LC 701, LC 450, LC 98, LC 230, LC 108, LC 173, LC 220).

---

### Topic: Binary Heaps & Priority Queues

Binary heaps are complete binary trees stored array-contiguously. They enforce the heap-order property (parent $\le$ child for min-heaps), enabling $\mathcal{O}(1)$ minimum element retrieval and $\mathcal{O}(\log N)$ insertions and extractions.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Array Storage & Heapify Mechanics | Princeton CS: *Algorithms, 4th Edition* (Sedgewick) | Book | Illustrates parent-child array indexing (`parent = (i-1)/2`, `left = 2i+1`) and linear-time $\mathcal{O}(N)$ bottom-up heap construction. | [Princeton Algs4 Priority Queues](https://algs4.cs.princeton.edu/24pq/) |
| Java `PriorityQueue` Internals | OpenJDK Source: `java.util.PriorityQueue` | Source Code | Production implementation of array-based binary min-heaps, sift-up, and sift-down routines. | OpenJDK `PriorityQueue.java` source code |

#### Recommended Learning Stack
1. **Concept:** Princeton Algorithms 4th Edition, Section 2.4.
2. **Implementation:** Reading OpenJDK `PriorityQueue` source and building a custom min/max heap from scratch.
3. **Practice:** Core syllabus bank (LC 215, LC 703, LC 347, LC 295, LC 378, LC 621).

---
