# Appendix: Sequencing Logic, Mental Models, Boilerplates & Pitfalls

### Sequencing Logic
- **No Magic:** never use a tool not conceptually understood. Arrays before Hashing, Recursion before Trees, Trees before Graphs (as per the module order).
- **The Math Exception:** Matrix Exponentiation and DP-flavored Game Theory are catalogued in Module 1 but are genuinely easier to *teach* after Recursion (Module 4) and DP 1D (Module 8) respectively. Don't force strict table order here.
- **The DP Cliff:** most students fail DP by jumping into tabulation without mastering Recursion and state representation first. Spend real time on Recursion before DP — and now, specifically, spend real time on *DP 1D* before touching Bitmask DP, Digit DP, or Interval DP; those are a second, steeper cliff of their own.
- **The Graph Transition:** graphs are trees with cycles. Master BFS/DFS on trees before adding adjacency lists and cycle detection.
- **The Advanced-DS Gate:** don't start Module 10 (Segment Trees/Fenwick/Sparse Table) before Module 8's DP is solid — half of their hardest practice problems (LIS via BIT, Count of Smaller Numbers After Self) are really "a DP problem wearing a data-structure costume."

### Mental Models
- **Arrays/Strings:** a physical tape — run pointers across it (Two Pointers, Sliding Window).
- **Recursion:** a "trust the function" leap; a tree of decisions (state-space tree).
- **Dynamic Programming:** recursion plus a memory notebook; shortest path in a DAG of states.
- **Graphs:** states and transitions. A maze is a graph. Word transformations are a graph.
- **Modular Arithmetic:** a clock face — numbers wrap, and multiplication needs its own "undo" button (the modular inverse), because normal division doesn't exist mod `m`.
- **Matrix Exponentiation:** repeated squaring is binary search's cousin — "can I get to `n` steps by doubling instead of counting one at a time?"
- **Segment Trees / Fenwick Trees:** prefix sums that learned to update themselves in O(log n) instead of O(n).

### Boilerplates to Strictly Memorize (extended)
1. Standard Binary Search template (avoiding infinite loops)
2. BFS/DFS traversal structures (incl. multi-source BFS)
3. Kahn's Algorithm for Topological Sort
4. Union-Find template with Path Compression and Union by Rank
5. Dijkstra's Algorithm
6. Binary (fast) exponentiation template, iterative and recursive
7. Backtracking template (choose → explore → un-choose)
8. Monotonic stack template (next-greater-element shape)
9. Fenwick Tree update/query template
10. KMP LPS-array construction

### Things That Should NEVER Be Memorized
- **Dynamic Programming transitions** — must be derived logically, every time, for every new problem.
- **Greedy proofs** — must be tested with counter-examples on the spot.
- **Backtracking pruning logic** — the template is standard; the pruning condition changes per problem.
- **The base matrix for Matrix Exponentiation** — must be derived from the recurrence, not recalled from a past problem; the derivation *is* the skill being tested.

### Common Interview Pitfalls to Attack
- **Rushing to code:** state the brute force and its complexity out loud before optimizing — this is now explicitly called out as best practice across FAANG loops in 2026, not just good hygiene.
- **Edge-case blindness:** empty arrays, negatives, single-node trees, integer overflow (this is exactly why Module 1's modular arithmetic matters).
- **Complexity illiteracy:** know your solution's Big-O before you finish writing it, not after.
- **Silent coding:** 2026 interview feedback consistently docks candidates who solve a hard problem silently over one who narrates a medium problem clearly — communication is now explicitly evaluated, not just a tiebreaker.

### A note on where this sits in 2026
Multiple independent 2026 sources agree on two things worth internalizing: (1) the *core topic list* in this document — arrays/strings, hashing, trees/graphs, DP — is still squarely the center of gravity for FAANG coding rounds, so the comprehensiveness here is well spent; and (2) *how* you talk through a solution (brute force first, narrate trade-offs, handle an interviewer's live curveballs) is being weighted more heavily than it used to be, alongside — not instead of — the DSA knowledge itself. The mentor's Stage 5 debrief (Interview Insights) and Stage 4 (recognition signals and tips) already cover this. Two things this syllabus deliberately stays out of, since this mentor is scoped to DSA specifically: System Design (a real, weighted round from mid-level up, but not a DSA topic) and behavioral/leadership-principle prep (Amazon in particular weights this heavily) — worth a separate track, not a bloated addition to this one.
