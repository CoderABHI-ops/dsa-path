# Module 10 of 11: Advanced Data Structures

> Naming note: the study-resources source calls this module "Advanced Data Structures & Range Queries". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Segment Tree (Point/Range Updates & Lazy Propagation)
- Fenwick Tree (Binary Indexed Tree - BIT)
- Sparse Table & Range Minimum Queries (RMQ)
- Square Root Decomposition & Heavy-Light Decomposition (HLD)

---

## PART A: Curriculum and Core Practice Bank

This module is "optional but FAANG+" — true for most companies, but multiple 2026 sources specifically call out range-query structures (segment trees / BIT) as a **Google-distinctive** category, so if Google is anywhere on your target list, don't treat this module as truly optional.

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Segment Trees (incl. Lazy Propagation) | Range queries + range/point updates in O(log n) | Very Hard | Trees, Recursion | The general-purpose range-query structure; supports far more operations than a Fenwick Tree. | 4 Days | 20% |
| Fenwick Tree (Binary Indexed Tree) | Range sum/frequency queries + point updates in O(log n), simpler and more space-efficient than a segment tree | Hard | Prefix Sum, Bit Manipulation | Faster to code under interview pressure than a segment tree when you only need point updates. | 3 Days | 15% |
| Sparse Table | O(1) range queries on **static** (immutable) data after O(n log n) preprocessing | Medium | Prefix Sum | The right tool when updates never happen — cheaper than a segment tree for that case. | 1 Day | 5% |
| Sqrt Decomposition | Block-based range queries as a simpler (if asymptotically weaker) alternative to a segment tree | Medium | Arrays | Good fallback when you can recall the idea but not the segment-tree code under pressure. | 1 Day | 3% |

### Core Practice Bank — Module 10

**Segment Trees / Fenwick Trees**
- LC 307 — Range Sum Query - Mutable (Medium) — https://leetcode.com/problems/range-sum-query-mutable/ — build this with *both* a Fenwick Tree and a Segment Tree; feel the difference
- LC 315 — Count of Smaller Numbers After Self (Hard) — https://leetcode.com/problems/count-of-smaller-numbers-after-self/ — BIT applied to an indirect "count" query
- LC 327 — Count of Range Sum (Hard) — https://leetcode.com/problems/count-of-range-sum/
- LC 732 — My Calendar III (Hard) — https://leetcode.com/problems/my-calendar-iii/ — segment tree with lazy propagation on a coordinate-compressed range
- LC 218 — The Skyline Problem (Hard) — https://leetcode.com/problems/the-skyline-problem/

**Deeper range-query practice:** CSES *Range Queries* section (hub) — https://cses.fi/problemset/list/ — this section is specifically built around segment trees, Fenwick trees, and sparse tables and has far more depth than LeetCode alone offers here. For open-ended tag practice on Codeforces, use the tag-filtered problemset rather than a single link, e.g. `codeforces.com/problemset?tags=data+structures` and `tags=dsu`.

---

---

## PART B: Curated study resources

### Topic: Segment Tree (Point/Range Updates & Lazy Propagation)

Segment Trees are full binary tree structures built over array ranges, enabling range queries and point/range updates in $\mathcal{O}(\log N)$ time. Lazy propagation defers updates to subtrees until necessary, maintaining logarithmic efficiency for range updates.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Tree Construction & Range Queries | CP-Algorithms: Segment Tree | Reference / Guide | The gold-standard Segment Tree reference covering array-backed storage ($4N$ space), build routines, and point updates. | [CP-Algorithms Segment Tree](https://cp-algorithms.com/data_structures/segment_tree.html) |
| Lazy Propagation Mechanics | USACO Guide (Plat): Segment Tree with Lazy Propagation | Guide / Tutorial | Detailed guide on deferring array updates via `lazy[]` arrays and pushing updates down during queries. | [USACO Guide Segment Tree Lazy](https://usaco.guide/plat/seg-lazy) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Segment Tree core principles.
2. **Implementation:** Java Segment Tree class array implementation supporting point updates, range queries, and lazy propagation arrays.
3. **Practice:** Core syllabus bank (LC 307, LC 218, LC 699, LC 715, LC 1622).

---

### Topic: Fenwick Tree (Binary Indexed Tree - BIT)

A Fenwick Tree (Binary Indexed Tree) evaluates prefix sums and point updates in $\mathcal{O}(\log N)$ time with minimal code overhead. It uses bitwise least significant bit operations (`i & (-i)`) to traverse implicit tree ranges across standard array indices.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Bitwise Range Indexing (`i & -i`) | TopCoder Data Science Tutorials: Binary Indexed Trees | Technical Article | The seminal paper explaining array index tree mappings, prefix sum queries, and point updates. | [Topcoder BIT Tutorial](https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees) |

#### Recommended Learning Stack
1. **Concept:** TopCoder BIT Tutorial by Peter Morris.
2. **Implementation:** Concise 1-based indexing Java BIT class with `update(idx, val)` and `query(idx)` methods.
3. **Practice:** Core syllabus bank (LC 307, LC 315, LC 493, LC 327).

---

### Topic: Sparse Table & Range Minimum Queries (RMQ)

A Sparse Table precomputes range queries over static arrays in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(1)$ query time. It applies to idempotent range functions (where $f(a, a) = a$, such as $\min$, $\max$, and $\gcd$) by combining overlapping power-of-two ranges.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Precomputation & Idempotent Range Overlaps | CP-Algorithms: Sparse Table | Reference / Guide | Complete derivation of $ST[i][j]$ representing range $[i, i + 2^j - 1]$ and constant-time RMQ queries. | [CP-Algorithms Sparse Table](https://cp-algorithms.com/data_structures/sparse-table.html) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Sparse Table.
2. **Implementation:** Java 2D precomputed array `st[N][LOGN]` and precomputed integer log lookup arrays.
3. **Practice:** Core syllabus bank (LC 239 via RMQ, LC 1521; CSES Range Minimum Queries I).

---

### Topic: Square Root Decomposition & Heavy-Light Decomposition (HLD)

Square Root Decomposition divides an array of size $N$ into blocks of size $\approx \sqrt{N}$, achieving $\mathcal{O}(\sqrt{N})$ query and update times. Heavy-Light Decomposition (HLD) partitions tree nodes into heavy chains and light edges, enabling path queries on trees in $\mathcal{O}(\log^2 N)$ time via Segment Trees.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| $\sqrt{N}$ Block Partitioning | CP-Algorithms: Sqrt Decomposition | Reference / Guide | Structural breakdown of block updating, boundary handling, and Mo's Algorithm offline processing. | [CP-Algorithms Sqrt Decomposition](https://cp-algorithms.com/data_structures/sqrt_decomposition.html) |
| Heavy-Light Chain Decomposition | CP-Algorithms: Heavy-Light Decomposition | Reference / Guide | Shows how subtree size dictates heavy edge selection, flattening trees into contiguous segment tree ranges. | [CP-Algorithms Heavy-Light Decomposition](https://cp-algorithms.com/graph/hld.html) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Sqrt Decomposition & Heavy-Light Decomposition.
2. **Implementation:** Block array construction for Sqrt Decomposition; 2-pass DFS heavy-chain assignment for HLD in Java.
3. **Practice:** Core syllabus bank (LC 307 via Sqrt Decomposition; CSES Path Queries I & II).

---
