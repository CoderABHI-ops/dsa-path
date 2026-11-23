# Module 2 of 11: Arrays, Strings & Core Array Patterns

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Arrays (1D/2D) & Strings
- Two Pointers & Sliding Window
- Prefix Sums & Difference Arrays
- Subarray & Kadane-Style Search

---

## PART A: Curriculum and Core Practice Bank

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Arrays (1D/2D) | Contiguous memory, indexing, in-place ops | Easy | Module 1 | The base structure for DP, heaps, and strings. | 4 Days | 95% |
| Strings | Char arrays, Java immutability, `StringBuilder` | Easy-Med | Arrays | Heaviest single category at Amazon/Google. | 4 Days | 85% |
| Two Pointers | Opposing/same-direction pointers over a sorted or linear structure | Medium | Arrays | Turns O(n²) pair/triplet problems into O(n). | 3 Days | 75% |
| Sliding Window | Maintain a shrinking/growing window with a running invariant | Medium | Two Pointers | The single most common category across all FAANG per 2026 hiring-loop write-ups. | 4 Days | 80% |
| Prefix Sum & Difference Arrays | Precompute cumulative sums for O(1) range queries/updates | Easy-Med | Arrays | The "before you reach for a segment tree" tool — check this first. | 2 Days | 55% |
| Kadane's Algorithm (Max Subarray family) | Running-best local/global tracking | Medium | Arrays | The canonical greedy-DP hybrid; template for a whole family of "best subarray" problems. | 1 Day | 40% |
| Cyclic Sort | In-place placement when values live in `[1, n]` | Medium | Arrays | Clean O(n)/O(1) trick for "find missing/duplicate in range" problems. | 1 Day | 20% |
| Merge Intervals | Sort + sweep over overlapping ranges | Medium | Sorting (Module 5, soft ref) | Calendar/scheduling-flavored problems love this; frequent at Google. | 2 Days | 35% |

### Core Practice Bank — Module 2

**Arrays**
- LC 1 — Two Sum (Easy) — https://leetcode.com/problems/two-sum/
- LC 238 — Product of Array Except Self (Medium) — https://leetcode.com/problems/product-of-array-except-self/
- LC 189 — Rotate Array (Medium) — https://leetcode.com/problems/rotate-array/
- LC 41 — First Missing Positive (Hard) — https://leetcode.com/problems/first-missing-positive/

**Strings**
- LC 49 — Group Anagrams (Medium) — https://leetcode.com/problems/group-anagrams/
- LC 242 — Valid Anagram (Easy) — https://leetcode.com/problems/valid-anagram/
- LC 5 — Longest Palindromic Substring (Medium) — https://leetcode.com/problems/longest-palindromic-substring/ — revisit with Manacher's in Module 7
- LC 443 — String Compression (Medium) — https://leetcode.com/problems/string-compression/

**Two Pointers**
- LC 167 — Two Sum II - Input Array Is Sorted (Medium) — https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- LC 15 — 3Sum (Medium) — https://leetcode.com/problems/3sum/
- LC 11 — Container With Most Water (Medium) — https://leetcode.com/problems/container-with-most-water/
- LC 42 — Trapping Rain Water (Hard) — https://leetcode.com/problems/trapping-rain-water/
- LC 125 — Valid Palindrome (Easy) — https://leetcode.com/problems/valid-palindrome/

**Sliding Window**
- LC 3 — Longest Substring Without Repeating Characters (Medium) — https://leetcode.com/problems/longest-substring-without-repeating-characters/
- LC 76 — Minimum Window Substring (Hard) — https://leetcode.com/problems/minimum-window-substring/
- LC 209 — Minimum Size Subarray Sum (Medium) — https://leetcode.com/problems/minimum-size-subarray-sum/
- LC 424 — Longest Repeating Character Replacement (Medium) — https://leetcode.com/problems/longest-repeating-character-replacement/
- LC 567 — Permutation in String (Medium) — https://leetcode.com/problems/permutation-in-string/

**Prefix Sum / Difference Arrays**
- LC 303 — Range Sum Query - Immutable (Easy) — https://leetcode.com/problems/range-sum-query-immutable/
- LC 560 — Subarray Sum Equals K (Medium) — https://leetcode.com/problems/subarray-sum-equals-k/
- LC 1094 — Car Pooling (Medium) — https://leetcode.com/problems/car-pooling/ — difference array

**Kadane's Algorithm**
- LC 53 — Maximum Subarray (Medium) — https://leetcode.com/problems/maximum-subarray/ — the definition of this pattern
- LC 152 — Maximum Product Subarray (Medium) — https://leetcode.com/problems/maximum-product-subarray/
- LC 918 — Maximum Sum Circular Subarray (Medium) — https://leetcode.com/problems/maximum-sum-circular-subarray/

**Cyclic Sort**
- LC 268 — Missing Number (Easy) — https://leetcode.com/problems/missing-number/
- LC 287 — Find the Duplicate Number (Medium) — https://leetcode.com/problems/find-the-duplicate-number/
- LC 448 — Find All Numbers Disappeared in an Array (Easy) — https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

**Merge Intervals**
- LC 56 — Merge Intervals (Medium) — https://leetcode.com/problems/merge-intervals/
- LC 57 — Insert Interval (Medium) — https://leetcode.com/problems/insert-interval/
- LC 435 — Non-overlapping Intervals (Medium) — https://leetcode.com/problems/non-overlapping-intervals/

---

---

## PART B: Curated study resources

Module 2 centers on pointer mechanics, cache locality, and window-state maintenance across contiguous memory.

### Topic: Arrays (1D/2D) & Strings

Arrays represent contiguous memory blocks optimized for sequential hardware prefetching. String processing requires careful handling of character encodings, immutability costs, and memory fragmentation.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Contiguous Layout & In-Place Operations | UC Berkeley CS61B: Data Structures (Josh Hug) | University Course | Unmatched breakdown of array pointers, object headers, primitive storage, and geometric resizing invariants. | [UC Berkeley CS61B Spring 2021](https://sp21.datastructur.es/) |
| Java String Immutability & StringBuilder Internals | *Inside the Java Virtual Machine* (Bill Venners) | Technical Book | Explains string interning, byte arrays, compact strings, and buffer expansion policies. | Bill Venners, *Inside the JVM* -> Chapter 5: "The Java Virtual Machine" |

#### Recommended Learning Stack
1. **Concept:** UC Berkeley CS61B, Lectures 2 and 3.
2. **Implementation:** OpenJDK source analysis of `StringBuilder` capacity growth.
3. **Practice:** Core syllabus bank (LC 1, LC 238, LC 189, LC 41, LC 49, LC 242, LC 5, LC 443).

---

### Topic: Two Pointers & Sliding Window

Two pointers and sliding windows optimize brute-force search over sequences by maintaining running state invariants over contiguous intervals. This transforms nested quadratic scans into linear evaluations.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Inward & Same-Direction Two Pointers | Grokking the Coding Interview: Patterns for Coding Questions | Course Module | Establishes standard taxonomy of convergent, collinear, and fast-slow pointers across sorted domains. | Grokking Patterns -> Two Pointers |
| Universal Sliding Window Framework | Labuladong's Algorithm Cheat Sheet | Guide / Article | Presents a standardized code template for dynamic window expansion, contraction, and target matching. | [Labuladong Sliding Window Guide](https://labuladong.online/algo/essential-technique/sliding-window-framework/) |

#### Recommended Learning Stack
1. **Concept:** Grokking Patterns: Two Pointers & Sliding Window.
2. **Implementation:** Labuladong's universal sliding window Java template.
3. **Practice:** Core syllabus bank (LC 15, LC 11, LC 42, LC 3, LC 76, LC 209).

---

### Topic: Prefix Sums & Difference Arrays

Prefix sum arrays reduce range sum queries to $\mathcal{O}(1)$ time using spatial precomputation. Difference arrays invert this operation, turning dynamic range updates into $\mathcal{O}(1)$ boundary modifications.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| 1D & 2D Prefix Sum Invariants | USACO Guide (Bronze): Prefix Sums | Guide / Tutorial | Visual explanations of 2D region sum inclusion-exclusion ($S[r2][c2] - S[r1-1][c2] - S[r2][c1-1] + S[r1-1][c1-1]$). | [USACO Guide Prefix Sums](https://usaco.guide/bronze/prefix-sums) |
| Difference Array Range Updates | Labuladong: Difference Array Technique | Article | Clean structural framework for applying continuous range mutations $\Delta[L] += v$ and $\Delta[R+1] -= v$. | [Labuladong Difference Array Guide](https://labuladong.online/algo/data-structure/difference-array/) |

#### Recommended Learning Stack
1. **Concept:** USACO Guide (Bronze): Prefix Sums & 2D Inclusion-Exclusion.
2. **Implementation:** Labuladong: Difference Array template.
3. **Practice:** Core syllabus bank (LC 303, LC 304, LC 560, LC 1109, LC 370).

---

### Topic: Subarray & Kadane-Style Search

Kadane's algorithm leverages dynamic programming over local linear choices: at index $i$, either extend the existing running sum or start a fresh contiguous subarray.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Optimal Subarray Sum Invariant | GeeksforGeeks: Kadane's Algorithm | Tutorial | Explains the structural transition $f(i) = \max(A[i], A[i] + f(i-1))$ and local vs. global maximum tracking. | [GeeksforGeeks Kadane's Algorithm](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/) |
| Circular & Double-Ended Subarray Maxima | CP-Algorithms: Maximum Subarray Sum | Guide | Extends Kadane to circular arrays via maximum total sum minus minimum inner subarray sum. | [CP-Algorithms Maximum Subarray Sum](https://cp-algorithms.com/) |

#### Recommended Learning Stack
1. **Concept:** GeeksforGeeks Kadane's Algorithm breakdown.
2. **Implementation:** Standard single-pass Kadane template with trackable boundary indices.
3. **Practice:** Core syllabus bank (LC 53, LC 918, LC 152).

---
