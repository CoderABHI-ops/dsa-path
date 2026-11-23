# Module 9 of 11: Graph Theory

> Naming note: the study-resources source calls this module "Graph Algorithms & Network Structures". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Graph Representations, BFS & DFS
- Topological Sort & Dependency DAGs
- Union-Find (Disjoint Set Union - DSU)
- Bipartite Graphs & Cycle Detection
- Shortest Paths: Dijkstra, Bellman-Ford & Floyd-Warshall
- Minimum Spanning Trees (Kruskal & Prim)
- Advanced Graph Topologies: Tarjan's SCC & Bridges

---

## PART A: Curriculum and Core Practice Bank

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Graph Fundamentals & Traversals | BFS, DFS, adjacency list/matrix, multi-source BFS | Medium | Trees, Queues | Represents networks, grids, and relationships; very high frequency. | 5 Days | 80% |
| Topological Sort | Dependency resolution (Kahn's algorithm and DFS-based) | Medium | Graph Fundamentals | Essential for scheduling/prerequisite/build-system problems. | 2 Days | 55% |
| Union-Find (Disjoint Set) | Cycle detection, dynamic connectivity, with path compression + union by rank | Medium | Graph Fundamentals | Very common for clustering/dynamic-component problems. | 3 Days | 55% |
| Bipartite Graphs & Graph Coloring | 2-coloring via BFS/DFS to test bipartiteness | Medium | Graph Fundamentals | A clean, fast "is this graph 2-colorable" check that shows up more than people expect. | 1 Day | 20% |
| Shortest Paths | Dijkstra, Bellman-Ford, Floyd-Warshall | Hard | Graph Fundamentals, Heaps | Often wrapped in real-world scenarios (maps, network cost, currency exchange). | 5 Days | 45% |
| Minimum Spanning Trees | Kruskal's, Prim's | Hard | Graphs, Union-Find, Heaps | Connecting networks at minimum cost. | 3 Days | 25% |
| Strongly Connected Components & Bridges/Articulation Points | Tarjan's (SCC and bridges), Kosaraju's (SCC) | Very Hard | Graph Fundamentals | Rare, but exactly what shows up in the "impossible-looking" hard graph problem. | 4 Days | 8% |

### Core Practice Bank — Module 9

**Graph Fundamentals**
- LC 200 — Number of Islands (Medium) — https://leetcode.com/problems/number-of-islands/
- LC 133 — Clone Graph (Medium) — https://leetcode.com/problems/clone-graph/
- LC 994 — Rotting Oranges (Medium) — https://leetcode.com/problems/rotting-oranges/ — multi-source BFS
- LC 417 — Pacific Atlantic Water Flow (Medium) — https://leetcode.com/problems/pacific-atlantic-water-flow/
- LC 127 — Word Ladder (Hard) — https://leetcode.com/problems/word-ladder/

**Topological Sort**
- LC 207 — Course Schedule (Medium) — https://leetcode.com/problems/course-schedule/
- LC 210 — Course Schedule II (Medium) — https://leetcode.com/problems/course-schedule-ii/
- LC 802 — Find Eventual Safe States (Medium) — https://leetcode.com/problems/find-eventual-safe-states/

**Union-Find**
- LC 684 — Redundant Connection (Medium) — https://leetcode.com/problems/redundant-connection/
- LC 721 — Accounts Merge (Medium) — https://leetcode.com/problems/accounts-merge/
- LC 547 — Number of Provinces (Medium) — https://leetcode.com/problems/number-of-provinces/
- LC 399 — Evaluate Division (Medium) — https://leetcode.com/problems/evaluate-division/ — weighted union-find

**Bipartite / Graph Coloring**
- LC 785 — Is Graph Bipartite? (Medium) — https://leetcode.com/problems/is-graph-bipartite/
- LC 886 — Possible Bipartition (Medium) — https://leetcode.com/problems/possible-bipartition/

**Shortest Paths**
- LC 743 — Network Delay Time (Medium) — https://leetcode.com/problems/network-delay-time/ — Dijkstra
- LC 787 — Cheapest Flights Within K Stops (Medium) — https://leetcode.com/problems/cheapest-flights-within-k-stops/ — Bellman-Ford-shaped
- LC 1334 — Find the City With the Smallest Number of Neighbors at a Threshold Distance (Medium) — https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/ — Floyd-Warshall

**Minimum Spanning Trees**
- LC 1584 — Min Cost to Connect All Points (Medium) — https://leetcode.com/problems/min-cost-to-connect-all-points/

**SCC / Bridges**
- LC 1192 — Critical Connections in a Network (Hard) — https://leetcode.com/problems/critical-connections-in-a-network/ — Tarjan's bridge-finding, the canonical LeetCode representative of this whole topic

---

---

## PART B: Curated study resources

### Topic: Graph Representations, BFS & DFS

Graphs consist of vertices connected by edges. Adjacency lists provide optimal $\mathcal{O}(V + E)$ spatial efficiency for sparse graphs, supporting level-by-level BFS expansions and deep recursive DFS searches.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Adjacency Lists vs. Matrices & Traversals | MIT OpenCourseWare 6.006: Graph Search, BFS & DFS | University Course | Prof. Erik Demaine's breakdown of frontier expansions, parent pointers, discovery times, and search invariants. | [MIT OCW 6.006 Graph Search](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) |
| Grid Flood Fill Mechanics | USACO Guide (Bronze): Flood Fill | Guide / Tutorial | Practical guide to matrix traversal grids using directional offset arrays (`dx[]`, `dy[]`). | [USACO Guide Flood Fill](https://usaco.guide/bronze/flood-fill) |

#### Recommended Learning Stack
1. **Concept:** MIT 6.006: Graph Search (BFS & DFS).
2. **Implementation:** Java `List<List<Integer>>` adjacency lists and `ArrayDeque` BFS frontiers.
3. **Practice:** Core syllabus bank (LC 200, LC 133, LC 695, LC 733, LC 547, LC 994, LC 127).

---

### Topic: Topological Sort & Dependency DAGs

Topological sorting orders vertices in a Directed Acyclic Graph (DAG) such that every directed edge $u \to v$ places vertex $u$ before $v$. Kahn's algorithm processes nodes via in-degree tracking; DFS builds orders via post-order reversal.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Kahn's Algorithm & DFS Post-Order Reversal | CP-Algorithms: Topological Sorting | Reference / Guide | Complete breakdown of in-degree queue processing, cycle detection via node counting, and DFS post-order reversals. | [CP-Algorithms Topological Sorting](https://cp-algorithms.com/graph/topological-sort.html) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Topological Sorting derivations.
2. **Implementation:** Kahn's Algorithm template using in-degree arrays and Java `ArrayDeque`.
3. **Practice:** Core syllabus bank (LC 207, LC 210, LC 310, LC 1203, LC 269).

---

### Topic: Union-Find (Disjoint Set Union - DSU)

DSU tracks partitioned dynamic equivalence sets over $N$ elements. Path Compression and Union by Rank/Size yield near-instantaneous amortized $\mathcal{O}(\alpha(N))$ operations, where $\alpha$ is the Inverse Ackermann Function.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Path Compression & Union by Rank Proof | Princeton CS: *Algorithms, 4th Edition* (Sedgewick) | Book / Web Portal | Excellent visual and structural breakdown of disjoint forests, root pointers, and flattening mechanics. | [Princeton Algs4 Union-Find](https://algs4.cs.princeton.edu/15uf/) |
| Inverse Ackermann Function Bounds | Tim Roughgarden: *Algorithms Illuminated (Part 2)* | Book | Mathematical explanation of why path compression with union by rank produces effectively constant amortized runtime. | Tim Roughgarden, *Algorithms Illuminated (Part 2)* -> Chapter 10 |

#### Recommended Learning Stack
1. **Concept:** Princeton Algorithms 4th Edition, Section 1.5; Roughgarden Chapter 10.
2. **Implementation:** Clean Java class `UnionFind` implementing `find()` with recursive path compression and `union()` by rank/size.
3. **Practice:** Core syllabus bank (LC 547, LC 684, LC 1319, LC 721, LC 990, LC 305).

---

### Topic: Bipartite Graphs & Cycle Detection

A graph is bipartite if its vertices can be partitioned into two sets such that no two adjacent vertices share a color. A graph is bipartite if and only if it contains no odd-length cycles.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Two-Coloring BFS/DFS & 3-Color Cycle Marking | CP-Algorithms: Checking a Graph for Bipartiteness | Reference / Guide | Explains graph two-coloring techniques and 3-color DFS state marking (`0=unvisited`, `1=visiting`, `2=visited`) for cycle isolation. | [CP-Algorithms Bipartite Check](https://cp-algorithms.com/graph/bipartite-check.html) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Bipartite Graph Checking & Cycle Detection.
2. **Implementation:** Java BFS/DFS two-coloring array routines (`int[] color`).
3. **Practice:** Core syllabus bank (LC 785, LC 886, LC 261, LC 685).

---

### Topic: Shortest Paths: Dijkstra, Bellman-Ford & Floyd-Warshall

Single-Source Shortest Path (SSSP) algorithms find minimum path weights. Dijkstra uses a min-priority queue for non-negative weights in $\mathcal{O}((V + E) \log V)$. Bellman-Ford handles negative weights and detects negative cycles in $\mathcal{O}(V \cdot E)$. Floyd-Warshall computes All-Pairs Shortest Paths (APSP) in $\mathcal{O}(V^3)$ time.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Dijkstra's Priority Queue Relaxation | MIT OpenCourseWare 6.006: Dijkstra & Shortest Paths | University Course | Proof of edge relaxation invariants and non-negative weight assumptions. | [MIT OCW 6.006 Dijkstra Lecture](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) |
| Bellman-Ford & Negative Cycle Detection | CP-Algorithms: Bellman-Ford Algorithm | Reference / Guide | Formal breakdown of iterating $V-1$ relaxation passes across all edges to detect negative cycles. | [CP-Algorithms Bellman-Ford](https://cp-algorithms.com/graph/bellman_ford.html) |
| Floyd-Warshall Dynamic Programming | CP-Algorithms: Floyd-Warshall Algorithm | Reference / Guide | Explains 3-loop dynamic programming optimization over intermediate vertex subproblems $k \in \{1 \dots V\}$. | [CP-Algorithms Floyd-Warshall](https://cp-algorithms.com/graph/all-pairs-shortest-path-floyd-warshall.html) |

#### Recommended Learning Stack
1. **Concept:** MIT 6.006 Dijkstra Lecture; CP-Algorithms (Bellman-Ford & Floyd-Warshall).
2. **Implementation:** Writing Java implementations using `PriorityQueue` for Dijkstra and 3D/2D arrays for Floyd-Warshall.
3. **Practice:** Core syllabus bank (LC 743, LC 787, LC 1631, LC 778, LC 1334, LC 882).

---

### Topic: Minimum Spanning Trees (Kruskal & Prim)

A Minimum Spanning Tree (MST) connects all vertices in a weighted undirected graph with minimum total edge weight. Kruskal's algorithm greedily adds edges using Union-Find in $\mathcal{O}(E \log E)$; Prim's algorithm grows a tree from a start vertex using a min-heap in $\mathcal{O}(E \log V)$.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Cut & Cycle Property Proofs | Tim Roughgarden: *Algorithms Illuminated (Part 2)* | Book | Chapter 8: Derives the Cut Property proving greedy MST choices are universally correct. | Tim Roughgarden, *Algorithms Illuminated (Part 2)* -> Chapter 8 |
| Kruskal & Prim Algorithmic Patterns | CP-Algorithms: Minimum Spanning Tree - Kruskal / Prim | Reference / Guide | Step-by-step implementation breakdown for both Kruskal's (edge sorting + DSU) and Prim's (min-heap cut expansion). | [CP-Algorithms Minimum Spanning Tree](https://cp-algorithms.com/graph/mst_kruskal.html) |

#### Recommended Learning Stack
1. **Concept:** Tim Roughgarden: *Algorithms Illuminated (Part 2)*, Chapter 8.
2. **Implementation:** Writing Java implementations for Kruskal's (using DSU) and Prim's (using `PriorityQueue`).
3. **Practice:** Core syllabus bank (LC 1584, LC 1135, LC 1489).

---

### Topic: Advanced Graph Topologies: Tarjan's SCC & Bridges

Strongly Connected Components (SCCs) are maximal subgraphs in directed graphs where every vertex is reachable from every other vertex. Tarjan's algorithm isolates SCCs, Bridges, and Articulation Points in a single DFS pass using discovery timestamps `tin[]` and low-link values `low[]`.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Low-Link Values & Discovery Times | CP-Algorithms: Finding Bridges in Linear Time | Reference / Guide | Explains condition `low[v] > tin[u]` proving edge $(u, v)$ is a critical bridge. | [CP-Algorithms Finding Bridges](https://cp-algorithms.com/graph/bridge-searching.html) |
| Tarjan's SCC Algorithm | CP-Algorithms: Strongly Connected Components | Reference / Guide | Complete derivation of stack-based component isolation via back-edge low-link updates. | [CP-Algorithms Tarjan SCC](https://cp-algorithms.com/graph/strongly-connected-components.html) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Bridge searching and Tarjan's SCC guides.
2. **Implementation:** Java DFS implementation maintaining global timer, `tin[]`, `low[]`, and stack arrays.
3. **Practice:** Core syllabus bank (LC 1192, LC 1568, LC 1489).

---
