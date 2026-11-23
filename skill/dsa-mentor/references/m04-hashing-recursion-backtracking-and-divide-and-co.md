# Module 4 of 11: Hashing, Recursion, Backtracking & Divide-and-Conquer

> Naming note: the study-resources source calls this module "Hashing, Hash Tables & Design". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Hash Tables, Hash Functions & Collision Resolution
- Direct Addressing & Frequency Maps
- Custom Key Hashing & Hash-Based System Design

---

## PART A: Curriculum and Core Practice Bank

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Hashing (HashMap/HashSet) | O(1) amortized lookups | Easy-Med | Arrays | The single biggest complexity-optimizer interviewers reward. | 4 Days | 95% |
| Recursion | Function calling itself, state passing, call-stack intuition | Medium | Stacks | The absolute prerequisite for Trees, Backtracking, and DP. | 5 Days | 90% |
| Backtracking | Explore all paths, prune invalid ones | Hard | Recursion | Standard for permutation/combination/grid problems. | 6 Days | 70% |
| Divide & Conquer | Split, solve independently, merge | Medium | Recursion | The paradigm behind merge sort, quickselect, and several "find the kth X" problems. | 3 Days | 25% |

### Core Practice Bank — Module 4

**Hashing**
- LC 1 — Two Sum (Easy) — https://leetcode.com/problems/two-sum/
- LC 49 — Group Anagrams (Medium) — https://leetcode.com/problems/group-anagrams/
- LC 128 — Longest Consecutive Sequence (Medium) — https://leetcode.com/problems/longest-consecutive-sequence/
- LC 347 — Top K Frequent Elements (Medium) — https://leetcode.com/problems/top-k-frequent-elements/
- LC 380 — Insert Delete GetRandom O(1) (Medium) — https://leetcode.com/problems/insert-delete-getrandom-o1/

**Recursion**
- LC 509 — Fibonacci Number (Easy) — https://leetcode.com/problems/fibonacci-number/ — revisit from Module 1, now as a recursion-first exercise
- LC 70 — Climbing Stairs (Easy) — https://leetcode.com/problems/climbing-stairs/

**Backtracking**
- LC 46 — Permutations (Medium) — https://leetcode.com/problems/permutations/
- LC 78 — Subsets (Medium) — https://leetcode.com/problems/subsets/
- LC 39 — Combination Sum (Medium) — https://leetcode.com/problems/combination-sum/
- LC 22 — Generate Parentheses (Medium) — https://leetcode.com/problems/generate-parentheses/
- LC 51 — N-Queens (Hard) — https://leetcode.com/problems/n-queens/
- LC 79 — Word Search (Medium) — https://leetcode.com/problems/word-search/
- LC 17 — Letter Combinations of a Phone Number (Medium) — https://leetcode.com/problems/letter-combinations-of-a-phone-number/

**Divide & Conquer**
- LC 215 — Kth Largest Element in an Array (Medium) — https://leetcode.com/problems/kth-largest-element-in-an-array/ — Quickselect
- LC 4 — Median of Two Sorted Arrays (Hard) — https://leetcode.com/problems/median-of-two-sorted-arrays/
- LC 912 — Sort an Array (Medium) — https://leetcode.com/problems/sort-an-array/ — implement merge sort *and* quicksort by hand here

---

---

## PART B: Curated study resources

### Topic: Hash Tables, Hash Functions & Collision Resolution

Hash tables provide average $\mathcal{O}(1)$ associative lookups by mapping arbitrary keys to bucket indices using hash functions. Collision handling dictates performance when keys map to identical indices.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Uniform Hashing & Load Factors | MIT OpenCourseWare 6.006: Hashing & Hash Tables | University Course | Mathematical analysis of simple uniform hashing, collision bounds, and dynamic rehashing triggers. | [MIT OCW 6.006 Hashing Lectures](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) |
| Separate Chaining vs. Open Addressing | *Algorithms, 4th Edition* (Sedgewick & Wayne) | Book | Deep comparison between node chaining (with treeification) and linear probing under high load factors. | [Princeton Algs4 Hash Tables](https://algs4.cs.princeton.edu/34hash/) |
| Java `HashMap` Internals | OpenJDK Source: `java.util.HashMap` | Source Code | Production implementation details: red-black tree conversion at bucket size 8, load factor 0.75, bitwise index masking. | OpenJDK `HashMap.java` source code |

#### Recommended Learning Stack
1. **Concept:** MIT 6.006 Lecture on Hashing & Hash Tables.
2. **Implementation:** Sedgewick & Wayne, *Algorithms*, Chapter 3.4; OpenJDK `HashMap` treeification analysis.
3. **Practice:** Core syllabus bank (LC 705, LC 706).

---

### Topic: Direct Addressing & Frequency Maps

Direct addressing maps integer keys straight to array indices, eliminating hash computations and garbage collection overhead. Frequency counting leverages these maps to compute structural equivalences (e.g., anagrams, character shifts).

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Array-Based Hash Maps | USACO Guide: Introduction to Sets & Maps | Guide | Demonstrates when to replace heavyweight Java `HashMap` objects with primitive integer array lookup tables. | [USACO Guide Silver Sets & Maps](https://usaco.guide/silver/sets-maps) |
| Categorization & Invariant Signatures | LeetCode Official Solutions: Group Anagrams | Editorial | Explains canonical representation hashing (e.g., character count strings as map keys). | [LeetCode Problem 49 Editorial](https://leetcode.com/problems/group-anagrams/) |

#### Recommended Learning Stack
1. **Concept:** USACO Guide: Sets & Maps efficiency choices.
2. **Implementation:** Primitive array frequency maps (`int[26]`) for ASCII character processing.
3. **Practice:** Core syllabus bank (LC 1, LC 383, LC 49, LC 128, LC 350, LC 560).

---

### Topic: Custom Key Hashing & Hash-Based System Design

Complex objects used as map keys require custom implementations of `equals()` and `hashCode()` to maintain the hashing contract. Systems-level hashing integrates custom objects to support efficient structural lookup.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Java Hashing Contract & Object Equality | *Effective Java, 3rd Edition* (Joshua Bloch) | Book | Items 10 & 11: "Obey the general contract when overriding `equals`" and "Always override `hashCode` when you override `equals`". | Joshua Bloch, *Effective Java (3rd Edition)* -> Items 10 & 11 |
| Hash-Based In-Memory Indexing | Designing Data-Intensive Applications (Martin Kleppmann) | Book | Chapter 3: In-memory hash indexes, hash-join mechanics, and persistence considerations. | Martin Kleppmann, *DDIA* -> Chapter 3: "Storage and Retrieval" |

#### Recommended Learning Stack
1. **Concept:** Joshua Bloch, *Effective Java*, Items 10 and 11.
2. **Implementation:** Writing robust `hashCode()` implementations for custom Java composite keys using primitive bit shifts and polynomial multipliers (e.g., 31).
3. **Practice:** Core syllabus bank (LC 355, LC 609, LC 535).

---
