# Module 5 of 11: Searching & Sorting

> Naming note: the study-resources source calls this module "Binary Search, Binary Search on Answer & Ternary Search". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Binary Search Fundamentals & Invariants
- Binary Search on Answer Space
- Rotated Arrays, Search Inverses & Ternary Search

---

## PART A: Curriculum and Core Practice Bank

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Sorting Algorithms | Merge, Quick, Counting, Radix, Insertion — and Java's actual sort internals | Medium | Arrays, Recursion | Understanding what `Arrays.sort()`/`Collections.sort()` do under the hood (dual-pivot quicksort for primitives, Timsort for objects). | 5 Days | 40% |
| Binary Search | O(log n) search on sorted/monotonic space | Medium | Arrays | Extremely high frequency; almost always fumbled on boundary conditions. | 4 Days | 85% |
| Binary Search on Answer / Variants | Searching a monotonic *answer* space, not just an array | Hard | Binary Search | A favorite FAANG move to disguise a hard problem as a search problem. | 5 Days | 60% |

### Core Practice Bank — Module 5

**Sorting**
- LC 912 — Sort an Array (Medium) — https://leetcode.com/problems/sort-an-array/
- LC 75 — Sort Colors (Medium) — https://leetcode.com/problems/sort-colors/ — Dutch national flag
- LC 179 — Largest Number (Medium) — https://leetcode.com/problems/largest-number/ — custom comparator

**Binary Search**
- LC 704 — Binary Search (Easy) — https://leetcode.com/problems/binary-search/
- LC 33 — Search in Rotated Sorted Array (Medium) — https://leetcode.com/problems/search-in-rotated-sorted-array/
- LC 153 — Find Minimum in Rotated Sorted Array (Medium) — https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- LC 34 — Find First and Last Position of Element in Sorted Array (Medium) — https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- LC 162 — Find Peak Element (Medium) — https://leetcode.com/problems/find-peak-element/

**Binary Search on Answer**
- LC 875 — Koko Eating Bananas (Medium) — https://leetcode.com/problems/koko-eating-bananas/
- LC 1011 — Capacity To Ship Packages Within D Days (Medium) — https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- LC 4 — Median of Two Sorted Arrays (Hard) — https://leetcode.com/problems/median-of-two-sorted-arrays/ — revisit as a binary-search-on-answer problem

---

---

## PART B: Curated study resources

### Topic: Binary Search Fundamentals & Invariants

Binary search cuts sorted search spaces in half each iteration by evaluating a mid-point predicate, executing in $\mathcal{O}(\log N)$ time. Strict boundary invariants eliminate infinite loops and off-by-one errors.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Invariant Boundary Tracking | TopCoder Data Science Tutorials: Binary Search | Technical Article | The classic guide for defining boundary search ranges $[L, R]$, $[L, R)$, and monotonic predicates. | [Topcoder Binary Search Tutorial](https://www.topcoder.com/thrive/articles/Binary%20Search) |
| Lower & Upper Bound Implementations | CP-Algorithms: Binary Search | Reference / Guide | Details exact Java implementations for `lower_bound` (first index $\ge \text{target}$) and `upper_bound` (first index $> \text{target}$). | [CP-Algorithms Binary Search](https://cp-algorithms.com/) |

#### Recommended Learning Stack
1. **Concept:** TopCoder Binary Search Guide on boundary invariants and predicate construction.
2. **Implementation:** Standardizing on a single invariant style: `low = 0, high = N - 1` while `low <= high`.
3. **Practice:** Core syllabus bank (LC 704, LC 34, LC 35, LC 74).

---

### Topic: Binary Search on Answer Space

When a decision function $P(x)$ is monotonic (if $P(x)$ is true, $P(x+1)$ is also true), binary search can find the minimum valid answer $x$ without an explicit input array.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Monotonic Predicate Formulation | USACO Guide (Silver): Binary Search | Guide / Tutorial | Exhaustive explanations on identifying implicit search bounds $[L_{\min}, R_{\max}]$ and building monotonic predicate functions. | [USACO Guide Binary Search](https://usaco.guide/silver/binary-search) |
| Minimax Optimization | Labuladong: Binary Search Applications | Guide | Shows how to transform "minimize maximum" or "maximize minimum" problem prompts into binary search predicates. | [Labuladong Binary Search Applications](https://labuladong.online/algo/frequency-interview/binary-search-in-action/) |

#### Recommended Learning Stack
1. **Concept:** USACO Guide (Silver): Binary Search predicate evaluation.
2. **Implementation:** Writing modular Java helper functions `boolean isValid(int target, ...)` to encapsulate predicate logic.
3. **Practice:** Core syllabus bank (LC 875, LC 1011, LC 410, LC 1482, LC 1552).

---

### Topic: Rotated Arrays, Search Inverses & Ternary Search

Rotated sorted arrays break global monotonicity while retaining piecewise monotonicity. Ternary search divides search spaces into three parts to locate unimodal function extrema in $\mathcal{O}(\log N)$ time.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Piecewise Sorted Invariant Search | LeetCode Official Solutions: Search in Rotated Sorted Array | Editorial | Details how comparing `nums[mid]` against `nums[low]` isolates which half of a rotated array remains strictly sorted. | [LeetCode Problem 33 Editorial](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| Ternary Search on Unimodal Functions | CP-Algorithms: Ternary Search | Reference / Guide | Mathematical breakdown of evaluating $m_1 = l + (r - l)/3$ and $m_2 = r - (r - l)/3$ to find function peaks. | [CP-Algorithms Ternary Search](https://cp-algorithms.com/num_methods/ternary_search.html) |

#### Recommended Learning Stack
1. **Concept:** LeetCode Problem 33 & 81 editorials for rotated array invariants.
2. **Implementation:** CP-Algorithms: Ternary search template for continuous and discrete domains.
3. **Practice:** Core syllabus bank (LC 33, LC 81, LC 153, LC 154, LC 162, LC 852).

---
