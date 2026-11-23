# Module 3 of 11: Linked Lists, Stacks, Queues & Monotonic Structures

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Linked Lists & Fast-Slow Pointers
- Stacks & Expression Parsing
- Queues, Deques & Circular Buffers
- Monotonic Stack & Queue

---

## PART A: Curriculum and Core Practice Bank

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Linked Lists | Dynamic memory via nodes, pointer manipulation | Medium | Arrays | Tests pointer discipline and edge-case handling. | 4 Days | 55% |
| Stacks | LIFO ops; the base for parsing and DFS-without-recursion | Medium | Arrays/LL | Vital for parsing, history, and optimal tree traversal. | 3 Days | 65% |
| Monotonic Stack | Maintain increasing/decreasing order to answer "next greater/smaller" in O(n) | Medium | Stacks | One of the highest ROI-per-line patterns in the whole syllabus. | 2 Days | 40% |
| Queues / Deques | FIFO / double-ended ops | Easy-Med | Arrays/LL | Backbone of BFS and windowed problems. | 3 Days | 55% |
| Monotonic Queue (Sliding Window Max/Min) | Deque that keeps window extrema in O(1) amortized | Medium | Queues, Monotonic Stack | The non-heap way to solve windowed min/max — comes up as a heap-vs-deque trade-off question. | 2 Days | 15% |

### Core Practice Bank — Module 3

**Linked Lists**
- LC 206 — Reverse Linked List (Easy) — https://leetcode.com/problems/reverse-linked-list/
- LC 21 — Merge Two Sorted Lists (Easy) — https://leetcode.com/problems/merge-two-sorted-lists/
- LC 141 — Linked List Cycle (Easy) — https://leetcode.com/problems/linked-list-cycle/
- LC 19 — Remove Nth Node From End of List (Medium) — https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- LC 138 — Copy List with Random Pointer (Medium) — https://leetcode.com/problems/copy-list-with-random-pointer/
- LC 23 — Merge k Sorted Lists (Hard) — https://leetcode.com/problems/merge-k-sorted-lists/
- LC 25 — Reverse Nodes in k-Group (Hard) — https://leetcode.com/problems/reverse-nodes-in-k-group/

**Stacks**
- LC 20 — Valid Parentheses (Easy) — https://leetcode.com/problems/valid-parentheses/
- LC 155 — Min Stack (Medium) — https://leetcode.com/problems/min-stack/
- LC 150 — Evaluate Reverse Polish Notation (Medium) — https://leetcode.com/problems/evaluate-reverse-polish-notation/

**Monotonic Stack**
- LC 739 — Daily Temperatures (Medium) — https://leetcode.com/problems/daily-temperatures/
- LC 496 — Next Greater Element I (Easy) — https://leetcode.com/problems/next-greater-element-i/
- LC 84 — Largest Rectangle in Histogram (Hard) — https://leetcode.com/problems/largest-rectangle-in-histogram/
- LC 42 — Trapping Rain Water (Hard) — https://leetcode.com/problems/trapping-rain-water/ — revisit as a monotonic-stack solution, not just two pointers

**Queues / Deques**
- LC 933 — Number of Recent Calls (Easy) — https://leetcode.com/problems/number-of-recent-calls/
- LC 232 — Implement Queue using Stacks (Easy) — https://leetcode.com/problems/implement-queue-using-stacks/

**Monotonic Queue**
- LC 239 — Sliding Window Maximum (Hard) — https://leetcode.com/problems/sliding-window-maximum/ — solve with a heap first, then again with a monotonic deque, and compare

---

---

## PART B: Curated study resources

### Topic: Linked Lists & Fast-Slow Pointers

Linked structures prioritize $\mathcal{O}(1)$ insertions and removals at pointer locations at the expense of random access and cache locality. Floyd's Cycle Detection uses two pointers moving at different velocities to prove cycle existence and locate cycle entry points.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Pointer Manipulation & Sentinel Nodes | Stanford CS Library: Linked List Basics (Nick Parlante) | Educational Monograph | Excellent structural guide detailing pointer rewiring, dummy head nodes, and defensive null handling. | [Stanford CS Linked List Problems](http://cslibrary.stanford.edu/105/LinkedListProblems.pdf) |
| Floyd's Cycle Detection Proof | GeeksforGeeks: How Does Floyd's Cycle-Finding Algorithm Work? | Article | Mathematical proof demonstrating $2(F + a) = F + a + nC \implies F = nC - a$. | [GeeksforGeeks Floyd's Cycle Finding](https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/) |

#### Recommended Learning Stack
1. **Concept:** Stanford CS Library (Nick Parlante), *Linked List Basics*.
2. **Implementation:** Java pointer rewiring templates using dummy head sentinels.
3. **Practice:** Core syllabus bank (LC 206, LC 21, LC 141, LC 142, LC 143, LC 23).

---

### Topic: Stacks & Expression Parsing

Stacks enforce LIFO semantics, making them the natural data structure for nested balance verification, call stack simulation, and operator precedence parsing via the Shunting-Yard algorithm.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| LIFO Mechanics & Execution Stack | Princeton CS: *Algorithms, 4th Edition* (Sedgewick) | Book | Clear derivation of stack ADT implementations using dynamic resizing arrays and linked nodes. | [Princeton Algs4 Stacks and Queues](https://algs4.cs.princeton.edu/13stacks/) |
| Shunting-Yard Algorithm & Infix/Postfix Evaluation | Edsger W. Dijkstra: *Algol 60 Implementation* | Historical Paper / Guide | The original operator stack algorithm converting infix expressions into Reverse Polish Notation (RPN). | [CP-Algorithms Infix to Postfix](https://cp-algorithms.com/) |

#### Recommended Learning Stack
1. **Concept:** Princeton Algorithms 4th Edition, Section 1.3.
2. **Implementation:** Java `ArrayDeque` stack operations for parenthetical matching and expression evaluation.
3. **Practice:** Core syllabus bank (LC 20, LC 155, LC 150, LC 224, LC 394).

---

### Topic: Queues, Deques & Circular Buffers

Queues enforce FIFO semantics, while Double-Ended Queues (Deques) allow $\mathcal{O}(1)$ operations at both boundaries. Fixed-size circular buffers optimize queue performance by eliminating element shifting via modulo indexing.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic Array Ring Buffers | OpenJDK Source: `java.util.ArrayDeque` | Source Code | Shows production implementation of head/tail modulo masking (`(tail + 1) & (elements.length - 1)`). | OpenJDK `ArrayDeque.java` source implementation |
| Queue ADT Invariants | Sedgewick & Wayne: *Algorithms, 4th Edition* | Book | Details queue boundary states (full vs. empty conditions) and head/tail pointer progression. | [Princeton Algs4 Section 1.3](https://algs4.cs.princeton.edu/13stacks/) |

#### Recommended Learning Stack
1. **Concept:** Princeton Algorithms 4th Edition, Queue & Deque Sections.
2. **Implementation:** Reading OpenJDK `ArrayDeque` implementation for power-of-two array sizing and bitwise masking.
3. **Practice:** Core syllabus bank (LC 622, LC 641, LC 950).

---

### Topic: Monotonic Stack & Queue

Monotonic stacks and queues maintain elements in strict ascending or descending order. They provide instantaneous $\mathcal{O}(1)$ queries for the Next Greater Element or range min/max within a sliding window in amortized $\mathcal{O}(N)$ total time.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Next Greater Element Pattern | Labuladong: Monotonic Stack Template | Guide | Structural breakdown of popping elements that violate order invariance to find nearest greater/smaller targets. | [Labuladong Monotonic Stack Guide](https://labuladong.online/algo/data-structure/monotonic-stack/) |
| Sliding Window Maximum via Monotonic Queue | CP-Algorithms: Dynamic Data Structures for Minimum | Guide | Explains deque maintenance for monotonic range minimum/maximum queries in $\mathcal{O}(N)$ time. | [CP-Algorithms Min Stack & Min Queue](https://cp-algorithms.com/data_structures/stack_queue_modification.html) |

#### Recommended Learning Stack
1. **Concept:** Labuladong: Monotonic Stack template and element ejection invariants.
2. **Implementation:** Java `ArrayDeque` implementations for Monotonic Stack and Sliding Window Monotonic Queue.
3. **Practice:** Core syllabus bank (LC 739, LC 84, LC 239, LC 402, LC 901).

---
