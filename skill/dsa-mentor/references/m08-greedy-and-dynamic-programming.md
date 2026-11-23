# Module 8 of 11: Greedy & Dynamic Programming

> Naming note: the study-resources source calls this module "Dynamic Programming & Greedy Algorithms". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Greedy Choice & Exchange Arguments
- 1D Dynamic Programming & Linear Recurrences
- 2D DP & Knapsack Variants
- Interval & Subsequence DP
- Tree DP & Rerooting Techniques
- Bitmask DP & State Compression
- Digit DP & Combinatorial State Search
- Game DP & Minimax Search

---

## PART A: Curriculum and Core Practice Bank

This is the biggest single filter in top-tech interviews, and where most study time should concentrate. DP 1D and DP 2D carry the heaviest effort load, and the *advanced DP shapes* below are broken out individually rather than buried inside a generic "DP 2D/3D" bucket, precisely because they're the ones that catch people cold in an interview if never seen before.

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Greedy Algorithms | Local optimum → global optimum, with proof-by-counterexample discipline | Medium | Sorting, Heaps | Short to implement, tricky to prove correct — exactly what interviewers probe. | 4 Days | 55% |
| Dynamic Programming (1D) | Memoization & tabulation over a single state dimension | Hard | Recursion | The biggest single filter in FAANG interviews. | 7 Days | 80% |
| Dynamic Programming (2D) & Knapsack Variants | Grids, strings, 0/1 and unbounded knapsack | Very Hard | DP 1D | Requires real state design; standard in "hard" rounds. | 7 Days | 70% |
| Interval DP | DP over `[i, j]` ranges with a split point | Very Hard | DP 2D | A distinct state-design shape (matrix-chain style) that trips people who only know linear DP. | 3 Days | 15% |
| DP on Trees | DP where the state flows along tree edges, not array indices | Hard | DP 1D, Binary Trees | Ties Module 6 and Module 8 together; a common "did they *really* get DP" check. | 3 Days | 15% |
| Bitmask DP | DP where the state is a subset, encoded as an integer bitmask | Very Hard | DP 1D, Bit Manipulation | Standard tool for small-N "visit every X" (TSP-shaped) problems. | 4 Days | 12% |
| Digit DP | DP over the digits of a number, tracking a "tight" bound flag | Very Hard | DP 1D, Bit Manipulation | Rare outside Google-style rounds, but unlocks an entire category of "count numbers with property X up to N" problems that are otherwise infeasible. | 3 Days | 6% |
| Game Theory + DP (optimal-play games) | Modeling two-player optimal play as a DP/minimax recurrence | Hard | DP 1D, Module 1 Game Theory | The DP-flavored half of game theory — this is where Nim's XOR insight graduates into real state design. | 2 Days | 8% |

### Core Practice Bank — Module 8

**Greedy**
- LC 55 — Jump Game (Medium) — https://leetcode.com/problems/jump-game/
- LC 45 — Jump Game II (Medium) — https://leetcode.com/problems/jump-game-ii/
- LC 763 — Partition Labels (Medium) — https://leetcode.com/problems/partition-labels/
- LC 134 — Gas Station (Medium) — https://leetcode.com/problems/gas-station/
- LC 621 — Task Scheduler (Medium) — https://leetcode.com/problems/task-scheduler/

**DP (1D)**
- LC 70 — Climbing Stairs (Easy) — https://leetcode.com/problems/climbing-stairs/
- LC 198 — House Robber (Medium) — https://leetcode.com/problems/house-robber/
- LC 213 — House Robber II (Medium) — https://leetcode.com/problems/house-robber-ii/
- LC 322 — Coin Change (Medium) — https://leetcode.com/problems/coin-change/
- LC 300 — Longest Increasing Subsequence (Medium) — https://leetcode.com/problems/longest-increasing-subsequence/ — revisit with a Fenwick Tree in Module 10
- LC 139 — Word Break (Medium) — https://leetcode.com/problems/word-break/

**DP (2D) & Knapsack**
- LC 62 — Unique Paths (Medium) — https://leetcode.com/problems/unique-paths/
- LC 1143 — Longest Common Subsequence (Medium) — https://leetcode.com/problems/longest-common-subsequence/
- LC 72 — Edit Distance (Medium) — https://leetcode.com/problems/edit-distance/
- LC 416 — Partition Equal Subset Sum (Medium) — https://leetcode.com/problems/partition-equal-subset-sum/ — 0/1 knapsack
- LC 518 — Coin Change II (Medium) — https://leetcode.com/problems/coin-change-ii/ — unbounded knapsack
- LC 10 — Regular Expression Matching (Hard) — https://leetcode.com/problems/regular-expression-matching/

**Interval DP**
- LC 312 — Burst Balloons (Hard) — https://leetcode.com/problems/burst-balloons/
- LC 516 — Longest Palindromic Subsequence (Medium) — https://leetcode.com/problems/longest-palindromic-subsequence/
- LC 1039 — Minimum Score Triangulation of Polygon (Medium) — https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

**DP on Trees**
- LC 337 — House Robber III (Medium) — https://leetcode.com/problems/house-robber-iii/
- LC 124 — Binary Tree Maximum Path Sum (Hard) — https://leetcode.com/problems/binary-tree-maximum-path-sum/ — revisit as DP-on-trees
- LC 968 — Binary Tree Cameras (Hard) — https://leetcode.com/problems/binary-tree-cameras/

**Bitmask DP**
- LC 698 — Partition to K Equal Sum Subsets (Medium) — https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
- LC 847 — Shortest Path Visiting All Nodes (Hard) — https://leetcode.com/problems/shortest-path-visiting-all-nodes/
- LC 943 — Find the Shortest Superstring (Hard) — https://leetcode.com/problems/find-the-shortest-superstring/

**Digit DP**
- LC 233 — Number of Digit One (Hard) — https://leetcode.com/problems/number-of-digit-one/
- LC 902 — Numbers At Most N Given Digit Set (Hard) — https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
- LC 357 — Count Numbers with Unique Digits (Medium) — https://leetcode.com/problems/count-numbers-with-unique-digits/ — a gentler on-ramp before the two above

**Game Theory + DP**
- LC 877 — Stone Game (Medium) — https://leetcode.com/problems/stone-game/
- LC 1140 — Stone Game II (Medium) — https://leetcode.com/problems/stone-game-ii/
- LC 486 — Predict the Winner (Medium) — https://leetcode.com/problems/predict-the-winner/

---

---

## PART B: Curated study resources

### Topic: Greedy Choice & Exchange Arguments

Greedy algorithms build optimal solutions by making locally optimal choices at each step. Correctness requires proving the Greedy Choice Property and Optimal Substructure, typically via exchange arguments.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Exchange Argument Proof Mechanics | Tim Roughgarden: *Algorithms Illuminated (Part 3)* | Book | Clear framework for proving greedy correctness: transform any optimal solution into the greedy solution without degrading quality. | Tim Roughgarden, *Algorithms Illuminated (Part 3)* -> Chapter 13 |
| Interval Scheduling & Fractional Knapsack | USACO Guide (Silver): Greedy Algorithms | Guide / Tutorial | Explains optimal sorting strategies (e.g., sorting intervals by end time vs. start time). | [USACO Guide Greedy Algorithms](https://usaco.guide/silver/greedy) |

#### Recommended Learning Stack
1. **Concept:** Tim Roughgarden: *Algorithms Illuminated (Part 3)*, Chapter 13.
2. **Implementation:** Standard Java sorting comparators combined with single-pass greedy scanning.
3. **Practice:** Core syllabus bank (LC 455, LC 435, LC 452, LC 134, LC 55, LC 45, LC 135).

---

### Topic: 1D Dynamic Programming & Linear Recurrences

Dynamic programming solves complex optimization problems by overlapping subproblem evaluations. 1D DP stores state in a linear array, replacing exponential recursive search trees with polynomial evaluations.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Overlapping Subproblems & Memoization vs. Tabulation | MIT OpenCourseWare 6.006: Dynamic Programming | University Course | Prof. Erik Demaine's 5-step DP framework: Define subproblems, guess choices, combine recurrences, solve base cases, check DAG order. | [MIT OCW 6.006 DP Lectures](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) |
| State Compression (Space Optimization) | Labuladong: Dynamic Programming Core Principles | Guide / Article | Details state space reduction (e.g., shrinking an $\mathcal{O}(N)$ array to two scalar variables when evaluating $DP[i] = DP[i-1] + DP[i-2]$). | [Labuladong DP Framework](https://labuladong.online/algo/essential-technique/dynamic-programming-framework/) |

#### Recommended Learning Stack
1. **Concept:** MIT 6.006 DP Lectures by Erik Demaine (5-step framework).
2. **Implementation:** Writing both top-down memoized recursion and bottom-up space-optimized tabulation in Java.
3. **Practice:** Core syllabus bank (LC 70, LC 746, LC 198, LC 213, LC 139, LC 300, LC 322, LC 518).

---

### Topic: 2D DP & Knapsack Variants

2D DP models state optimization across two independent parameters (e.g., item index vs. remaining capacity, or string index $i$ vs. string index $j$). Knapsack variants serve as foundational archetypes.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| 0/1 Knapsack & Unbounded Knapsack Mechanics | USACO Guide (Gold): Knapsack DP | Guide / Tutorial | Visual breakdowns of state progression $DP[i][w] = \max(DP[i-1][w], v_i + DP[i-1][w - w_i])$ and 1D reverse iteration tricks. | [USACO Guide Knapsack DP](https://usaco.guide/gold/knapsack) |
| Grid Paths & Edit Distance | Labuladong: 2D Dynamic Programming Patterns | Guide | Clear templates for matrix traversal DP and 2-string alignment algorithms (LCS, Edit Distance). | [Labuladong 2D DP Guide](https://labuladong.online/algo/italy-cheatsheet/edit-distance/) |

#### Recommended Learning Stack
1. **Concept:** USACO Guide (Gold): Knapsack DP; Labuladong 2D DP patterns.
2. **Implementation:** Java 2D array allocation and 1D space optimization via reverse array iteration.
3. **Practice:** Core syllabus bank (LC 62, LC 63, LC 64, LC 416, LC 494, LC 1143, LC 72, LC 1092, LC 518).

---

### Topic: Interval & Subsequence DP

Interval DP computes optimal values over contiguous subsegments $[i, j]$, combining smaller subsegments to resolve larger ranges. Subsequence DP evaluates non-contiguous optimal subsets.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Subsegment State Transitions ($[i, j]$) | CP-Algorithms: Matrix Chain Multiplication / Interval DP | Guide | Derives subsegment evaluation loops: iterate over interval length $L$, then left boundary $i$, then partition point $k$. | [CP-Algorithms Interval DP](https://cp-algorithms.com/) |
| Longest Common Subsequence & Variations | *Algorithms, 4th Edition* (Sedgewick) | Book | Exhaustive coverage of string matching states and optimal alignment subproblems. | [Princeton Algs4 DP](https://algs4.cs.princeton.edu/) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Interval DP loop structures.
2. **Implementation:** 2D interval DP initialization ($DP[i][i]$ base cases) and length-based outer loops in Java.
3. **Practice:** Core syllabus bank (LC 516, LC 312, LC 1000, LC 678, LC 1035).

---

### Topic: Tree DP & Rerooting Techniques

Tree DP formulates dynamic programming state over hierarchical tree topologies, computing values bottom-up from leaves to root using post-order DFS. Rerooting techniques allow recomputing tree results for all candidate roots in $\mathcal{O}(N)$ time.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Post-Order Tree State Aggregation | USACO Guide (Gold): Tree DP | Guide / Tutorial | Explains parent-child state passing, subtree sum aggregations, and tree independent sets. | [USACO Guide Tree DP](https://usaco.guide/gold/tree-dp) |
| All-Pairs Tree Rerooting Technique | Codeforces Tutorial: Tree DP and Rerooting | Technical Article | Derives the 2-pass tree DP pattern: Pass 1 computes subtree values bottom-up; Pass 2 passes outer context top-down. | [Codeforces Tree DP Tutorial](https://codeforces.com/blog/entry/20935) |

#### Recommended Learning Stack
1. **Concept:** USACO Guide Tree DP; Codeforces Tree DP & Rerooting guide.
2. **Implementation:** Recursive post-order DFS algorithms in Java utilizing adjacency lists.
3. **Practice:** Core syllabus bank (LC 337, LC 543, LC 124, LC 834, LC 968).

---

### Topic: Bitmask DP & State Compression

Bitmask DP uses integer bitmasks to represent boolean subsets in state representations, compressing $N$ boolean decisions into an integer scalar for problems over small set sizes ($N \le 20$).

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Subset State Transitions & TSP | CP-Algorithms: Dynamic Programming on Subsets (Bitmasks) | Reference / Guide | Formal derivation of Traveling Salesperson Problem (TSP) in $\mathcal{O}(2^N \cdot N^2)$ time using bitmasks. | [CP-Algorithms Bitmask DP](https://cp-algorithms.com/) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Dynamic Programming on Subsets.
2. **Implementation:** Java loop templates iterating over submasks: `for (int sub = mask; sub > 0; sub = (sub - 1) & mask)`.
3. **Practice:** Core syllabus bank (LC 847, LC 980, LC 1879, LC 1494, LC 1125).

---

### Topic: Digit DP & Combinatorial State Search

Digit DP counts valid numbers within a numerical range $[L, R]$ by building valid digits top-down from most-significant to least-significant, maintaining tight-bound flags and leading-zero flags.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Digit State Template (`pos`, `tight`, `leading_zero`) | Codeforces Tutorial: Digit DP | Technical Article | The canonical breakdown of digit recursion parameters: `solve(idx, tight, is_leading, state)`. | [GeeksforGeeks Digit DP Guide](https://www.geeksforgeeks.org/digit-dp-introduction/) |

#### Recommended Learning Stack
1. **Concept:** Codeforces / GeeksforGeeks Digit DP state formulation.
2. **Implementation:** Memoized 4D array recursion (`Integer[pos][tight][leading][state]`) in Java.
3. **Practice:** Core syllabus bank (LC 233, LC 600, LC 902, LC 1012, LC 2719).

---

### Topic: Game DP & Minimax Search

Game DP models sequential optimal strategy games between two competing players using Minimax transitions ($DP[\text{state}] = \max_{\text{moves}} (1 - DP[\text{next\_state}])$).

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Minimax Optimization & Game Graphs | GeeksforGeeks: Minimax Algorithm in Game Theory | Guide | Explains state-tree minimization and maximization layers for finite turn games. | [GeeksforGeeks Minimax](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/) |

#### Recommended Learning Stack
1. **Concept:** GeeksforGeeks Minimax Algorithm breakdown.
2. **Implementation:** Top-down memoized recursion for turn-based state evaluation in Java.
3. **Practice:** Core syllabus bank (LC 877, LC 464, LC 294, LC 1406, LC 1140).

---
