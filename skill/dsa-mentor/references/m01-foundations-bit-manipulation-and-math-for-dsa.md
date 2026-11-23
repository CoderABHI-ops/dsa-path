# Module 1 of 11: Foundations, Bit Manipulation & Math for DSA

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Time & Space Complexity
- Java Foundations
- Bit Manipulation
- Modular Arithmetic & Fast Exponentiation
- Combinatorics for DSA
- Catalan Numbers & Structural Counting
- Matrix Exponentiation
- Probability & Expected Value
- Game Theory: Nim & Sprague-Grundy

---

## PART A: Curriculum and Core Practice Bank

Math is placed first because everything downstream borrows from it silently — a DP transition that needs `% (1e9+7)`, a "count the ways" problem that's secretly `nCr`, a Fibonacci-style recurrence that's secretly a matrix. Skipping this module doesn't stop you from solving those problems; it stops you from solving them *fast* and *correctly at scale*.

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Time & Space Complexity | Measure algorithm efficiency | Easy | None | The language of performance; every solution you ever give is judged against this. | 3 Days | 100% |
| Java Foundations | Syntax, memory model, primitives vs. objects, I/O, collections overview | Easy | None | You can't implement optimally if you're fighting the language mid-interview. | 3 Days | N/A |
| Bit Manipulation | AND/OR/XOR/shift tricks, masks, subset-via-bitmask | Medium | Java Foundations | O(1)-space tricks; the quiet backbone of bitmask DP later. | 3 Days | 40% |
| GCD, LCM & the Euclidean Algorithm | Divisibility, `gcd(a,b)`, Extended Euclid | Easy-Med | Java Foundations | Building block for modular arithmetic and every number-theory problem after it. | 1 Day | 20% |
| Sieve of Eratosthenes & Primality | Fast prime generation/checking/factorization | Easy-Med | GCD/LCM | Classic "precompute once, query fast" — shows up disguised in medium/hard problems. | 2 Days | 20% |
| Modular Arithmetic & Fast Exponentiation | Binary exponentiation; modular inverse via Fermat's Little Theorem and Extended Euclid | Medium | GCD/LCM | The `% (1e9+7)` pattern; prevents overflow in every "count the ways" problem. | 2 Days | 30% |
| Combinatorics for DSA | Permutations, combinations, `nCr` (with mod), Pascal's Triangle, binomial theorem | Medium | Modular Arithmetic | Turns exponential "count the arrangements" brute force into an O(1) formula. | 3 Days | 25% |
| Catalan Numbers & Structural Counting | Recognizing the Catalan recurrence (balanced parens, BST shapes, polygon triangulation) | Med-Hard | Combinatorics | A recurring "click" pattern — collapses a hard-looking DP into a known closed form. | 1 Day | 10% |
| Matrix Exponentiation *(teach after Module 4 — see note above)* | Solving linear recurrences in O(log n) via matrix powers | Hard | Modular Arithmetic & Fast Exponentiation | Upgrades an O(n) Fibonacci-style DP to O(log n); a strong signal of depth in hard rounds. | 2 Days | 8% |
| Probability & Expected Value (light) | Basic probability, linearity of expectation, reservoir sampling | Medium | Combinatorics | Shows up in "randomized" and "design a random X" questions, especially Google/Meta. | 2 Days | 10% |
| Game Theory: Nim & Sprague-Grundy *(pure-math part now; DP-flavored games in Module 8)* | Winning/losing positions, XOR-of-piles insight | Med-Hard | Combinatorics | Rare, but a clean "thinks differently" filter question when it appears. | 1 Day | 5% |

### Core Practice Bank — Module 1

**Bit Manipulation**
- LC 136 — Single Number (Easy) — https://leetcode.com/problems/single-number/
- LC 191 — Number of 1 Bits (Easy) — https://leetcode.com/problems/number-of-1-bits/
- LC 338 — Counting Bits (Easy) — https://leetcode.com/problems/counting-bits/
- LC 78 — Subsets (Medium) — https://leetcode.com/problems/subsets/ — solve it via bitmask, not just backtracking
- LC 260 — Single Number III (Medium) — https://leetcode.com/problems/single-number-iii/
- LC 201 — Bitwise AND of Numbers Range (Medium) — https://leetcode.com/problems/bitwise-and-of-numbers-range/

**GCD/LCM & Sieve**
- LC 1071 — Greatest Common Divisor of Strings (Easy) — https://leetcode.com/problems/greatest-common-divisor-of-strings/
- LC 204 — Count Primes (Medium) — https://leetcode.com/problems/count-primes/ — the canonical Sieve problem
- LC 2427 — Number of Common Factors (Easy) — https://leetcode.com/problems/number-of-common-factors/
- CSES *Mathematics* section (hub, not a single problem): https://cses.fi/problemset/list/ — look for "Common Divisors" and "Prime Multiples" for pure Sieve/GCD drilling beyond LeetCode's thinner coverage here.

**Modular Arithmetic, Fast Exponentiation & Modular Inverse**
- LC 50 — Pow(x, n) (Medium) — https://leetcode.com/problems/powx-n/ — binary exponentiation, the core template
- LC 372 — Super Pow (Medium) — https://leetcode.com/problems/super-pow/ — modular exponentiation with a huge exponent
- LC 1922 — Count Good Numbers (Medium) — https://leetcode.com/problems/count-good-numbers/ — fast exponentiation + counting combined
- CSES *Mathematics*: "Exponentiation" and "Exponentiation II" (the second one is specifically Fermat's Little Theorem / modular inverse) — https://cses.fi/problemset/list/

**Combinatorics / Pascal's Triangle**
- LC 118 — Pascal's Triangle (Easy) — https://leetcode.com/problems/pascals-triangle/
- LC 119 — Pascal's Triangle II (Easy) — https://leetcode.com/problems/pascals-triangle-ii/
- LC 62 — Unique Paths (Medium) — https://leetcode.com/problems/unique-paths/ — solve it both as DP *and* as a closed-form `nCr`
- LC 1922 (revisit) and CSES "Creating Strings" / "Binomial Coefficients" for pure combinatorics reps.

**Catalan Numbers**
- LC 96 — Unique Binary Search Trees (Medium) — https://leetcode.com/problems/unique-binary-search-trees/ — the textbook Catalan problem
- LC 22 — Generate Parentheses (Medium) — https://leetcode.com/problems/generate-parentheses/
- LC 95 — Unique Binary Search Trees II (Medium) — https://leetcode.com/problems/unique-binary-search-trees-ii/

**Matrix Exponentiation**
- LC 509 — Fibonacci Number (Easy) — https://leetcode.com/problems/fibonacci-number/ — do the O(n) DP first, then redo it as matrix power
- LC 70 — Climbing Stairs (Easy) — https://leetcode.com/problems/climbing-stairs/ — same recurrence, same upgrade path
- LC 935 — Knight Dialer (Medium) — https://leetcode.com/problems/knight-dialer/ — a linear-recurrence-in-disguise problem that genuinely needs matrix exponentiation at scale
- LC 1220 — Count Vowels Permutation (Hard) — https://leetcode.com/problems/count-vowels-permutation/

**Probability & Expected Value**
- LC 382 — Linked List Random Node (Medium) — https://leetcode.com/problems/linked-list-random-node/ — reservoir sampling
- LC 398 — Random Pick Index (Medium) — https://leetcode.com/problems/random-pick-index/
- LC 470 — Implement Rand10() Using Rand7() (Medium) — https://leetcode.com/problems/implement-rand10-using-rand7/ — rejection sampling

**Game Theory (Nim / Grundy — pure math track)**
- LC 292 — Nim Game (Easy) — https://leetcode.com/problems/nim-game/
- LC 1025 — Divisor Game (Easy) — https://leetcode.com/problems/divisor-game/
- *(Stone Game series is intentionally deferred to Module 8 — those need real DP, not just the XOR insight.)*

---

---

## PART B: Curated study resources

Mathematical foundations establish the asymptotic limits and algebraic structures that govern downstream algorithmic transitions. Mastery of discrete structures, modular arithmetic, and combinatorial enumeration eliminates computational bottlenecks and integer overflow in complex dynamic programming and graph traversals.

### Topic: Time & Space Complexity

Asymptotic analysis formalizes the resource consumption of algorithms under the Word-RAM model, where operations on word-sized integers execute in constant time while memory access across $N$ words incurs linear scale. Deriving time and space complexity demands operational accounting across recursion trees rather than superficial loop counting.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Asymptotic Bounds ($\mathcal{O}$, $\Omega$, $\Theta$) | MIT OpenCourseWare 6.006: Introduction to Algorithms | University Course | Establishes mathematical rigor on operational bounds, machine-independent cost models, and tight asymptotic dominance. | [MIT OCW 6.006 Lecture 1](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-1-algorithms-and-computation/) |
| Master Theorem & Recurrence Trees | Tim Roughgarden: *Algorithms Illuminated (Part 1)* | Book | Synthesizes divide-and-conquer recursion tree branching factors with master recurrence derivations. | Tim Roughgarden, *Algorithms Illuminated (Part 1)* -> Chapter 2: "Divide-and-Conquer Algorithms" |
| Amortized Analysis (Aggregate & Potential) | Cornell CS 3110: Data Structures & Functional Programming | University Notes | Presents the clearest distinction between aggregate, accounting, and physicist potential methods for dynamic resizes. | Cornell CS 3110 course site (homepage only; no verified deep link to the amortized-analysis notes, so navigate from the course site or search 'CS 3110 amortized analysis') |

#### Recommended Learning Stack
1. **Concept:** MIT 6.006, Lecture 1 (Prof. Jason Ku), covering Word-RAM computational assumptions and operational step counting.
2. **Intuition/Visualization:** Tim Roughgarden's *Algorithms Illuminated (Part 1)*, Chapter 2, visualizing work distribution across recursive tree depths.
3. **Reference:** Cormen, Leiserson, Rivest, and Stein (CLRS), *Introduction to Algorithms*, Chapter 3: "Characterizing Running Times".
4. **Practice:** The syllabus problem bank sufficiently assesses runtime evaluation; supplemental formal proofs are available in MIT 6.006 Problem Set 1.

---

### Topic: Java Foundations

Language fundamentals dictate implementation efficiency in technical environments. In Java, understanding the boundary between stack-allocated primitives and heap-allocated objects directly informs memory footprints and garbage collection overhead in performance-critical loops.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| JVM Memory Model & Primitives vs. Objects | Princeton CS: *Algorithms, 4th Edition* (Sedgewick & Wayne) | Book / Web Portal | Deconstructs JVM object memory overhead, reference semantics, and array memory layout. | [Princeton Algs4 Section 1.1–1.2](https://algs4.cs.princeton.edu/11model/) |
| Java Collections Framework Internals | *Core Java Volume I: Fundamentals* (Cay S. Horstmann) | Book | Exhaustive coverage of load factors, treeification thresholds in `HashMap`, and bitwise resizing in collections. | Cay S. Horstmann, *Core Java Volume I* -> Chapter 9: "Collections" |
| Fast I/O & Stream Tokenization | CP-Algorithms: Java Competitive Programming I/O | Guide | Details memory-efficient replacements for `Scanner` using `BufferedReader` and custom integer parsers. | No verified link (the original CP-Algorithms URL pointed to an unrelated stack/queue page). Explain BufferedReader + StringTokenizer/StreamTokenizer fast input directly in chat. |

#### Recommended Learning Stack
1. **Concept:** Sedgewick & Wayne, *Algorithms, 4th Edition*, Chapter 1.1, clarifying memory overheads and primitive wrappers.
2. **Implementation:** Cay S. Horstmann's *Core Java*, Chapter 9, detailing collections resizing dynamics.
3. **Practice:** The syllabus's core practice bank provides sufficient reinforcement, provided solutions are authored using native primitive structures.

---

### Topic: Bit Manipulation

Bitwise arithmetic enables $\mathcal{O}(1)$ space representation of boolean states, power-of-two boundaries, and discrete subsets. The core mental model relies on interpreting binary representations as characteristic vectors of mathematical sets.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Fundamental Bitwise Operations & Masks | *Hacker's Delight* (Henry S. Warren, Jr.) | Book | The seminal reference for low-level integer logic, two's complement identities, and arithmetic optimization. | Henry S. Warren, Jr., *Hacker's Delight* -> Chapter 2 ("Basics") & Chapter 3 ("Power-of-2 Boundaries") |
| Bit Twiddling Hacks | Sean Eron Anderson (Stanford University) | Web Reference | The definitive compendium of branchless bitwise routines, including lowest-set-bit isolation and sign manipulation. | [Stanford Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html) |
| Subset Iteration via Bitmasks | USACO Guide (Silver): Introduction to Bitwise Operators | Guide / Tutorial | Explains the structural isomorphism between integers and boolean sets, including submask enumeration in $\mathcal{O}(3^N)$. | [USACO Guide Bitwise Operators](https://usaco.guide/silver/bitwise-expr) |

#### Recommended Learning Stack
1. **Concept:** Sean Eron Anderson's Bit Twiddling Hacks, focusing on `x & (-x)` for least-significant bit isolation and `x & (x - 1)` for bit clearing.
2. **Intuition/Visualization:** VisuAlgo (Bitmask Module), demonstrating integer transitions representing set operations.
3. **Implementation:** *Hacker's Delight*, Chapters 2 and 3.
4. **Practice:** Core syllabus bank (LC 136, LC 191, LC 338, LC 78 via bitmasks, LC 260, LC 201).

---

### Topic: Modular Arithmetic & Fast Exponentiation

Modular arithmetic transforms unbounded numerical growth into finite ring spaces $\mathbb{Z}_m$. Binary exponentiation leverages repeated squaring to evaluate $a^b \pmod m$ in $\mathcal{O}(\log b)$ time.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Modular Congruence & Ring Arithmetic | Khan Academy: Journey into Cryptography | Interactive Course | Clear conceptual foundation on modular reduction, clock arithmetic, and multiplicative inverses. | [Khan Academy Modular Arithmetic](https://www.khanacademy.org/computing/computer-science/cryptography) |
| Binary Exponentiation ($\mathcal{O}(\log N)$) | CP-Algorithms: Binary Exponentiation | Reference / Guide | Derives the iterative bit-scanning approach for fast powers and modular multiplication. | [CP-Algorithms Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html) |
| Euclidean & Extended Euclidean Algorithm | CP-Algorithms: Extended Euclidean Algorithm | Reference / Guide | Demonstrates derivation of Bezout's identity $ax + by = \gcd(a, b)$ and modular multiplicative inverses. | [CP-Algorithms Extended Euclidean](https://cp-algorithms.com/algebra/extended-euclidean-algorithm.html) |

#### Recommended Learning Stack
1. **Concept:** Khan Academy: Modular congruence and ring properties.
2. **Implementation:** CP-Algorithms: Binary Exponentiation iterative bit-scanning pattern.
3. **Practice:** Core syllabus bank (LC 50, LC 372, LC 1922, CSES Exponentiation I & II).

---

### Topic: Combinatorics for DSA

Combinatorial formulas reduce exponential brute-force enumeration of arrangements into instantaneous $\mathcal{O}(1)$ factorial lookups.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Permutations, Combinations & $n\text{C}r$ | CP-Algorithms: Binomial Coefficients | Reference / Guide | Explains precomputation of factorial and inverse factorial arrays to answer $n\text{C}r \pmod p$ in $\mathcal{O}(1)$ time. | [CP-Algorithms Binomial Coefficients](https://cp-algorithms.com/combinatorics/binomial-coefficients.html) |
| Pascal's Triangle & Binomial Theorem | MIT OpenCourseWare 6.042J: Mathematics for CS | University Course | Rigorous proof of binomial expansion, algebraic identities, and combinatorial recurrence relations. | [MIT OCW 6.042J Mathematics for CS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/) |

#### Recommended Learning Stack
1. **Concept:** MIT 6.042J Lecture Notes on Counting & Combinatorics.
2. **Implementation:** CP-Algorithms: Binomial Coefficients precomputation patterns.
3. **Practice:** Core syllabus bank (LC 118, LC 119, LC 62).

---

### Topic: Catalan Numbers & Structural Counting

Catalan numbers emerge whenever valid parenthesization, non-crossing partitions, or binary tree shapes are recursively constructed. Identifying the Catalan recurrence collapses complex search spaces into known closed forms.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Catalan Recurrence & Closed Form | Tom Davis: *Catalan Numbers* | Academic Paper | The definitive geometric and combinatorial treatment of Dyck paths, polygon triangulations, and tree structures. | [Tom Davis Catalan Monograph](https://geometer.org/mathcircles/catalan.pdf) |
| Algorithmic Applications & Modulo Calculation | CP-Algorithms: Catalan Numbers | Reference / Guide | Demonstrates DP transitions $C_n = \sum C_i C_{n-1-i}$ and analytical computation via binomial coefficients. | [CP-Algorithms Catalan Numbers](https://cp-algorithms.com/combinatorics/catalan-numbers.html) |

#### Recommended Learning Stack
1. **Concept:** Tom Davis: *Catalan Numbers*, Sections 1–4 (Visual Dyck path reflections).
2. **Implementation:** CP-Algorithms: Catalan Numbers analytical calculation.
3. **Practice:** Core syllabus bank (LC 96, LC 22, LC 95).

---

### Topic: Matrix Exponentiation

Linear recurrences of the form $\vec{v}_k = M \vec{v}_{k-1}$ can be advanced across $N$ transitions in $\mathcal{O}(d^3 \log N)$ time by taking powers of the transformation matrix through binary exponentiation. This bridges simple recursion and logarithmic execution.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Transition Matrix Derivation & Linear Recurrences | Errichto Algorithms: Matrix Exponentiation | YouTube Masterclass | World-class derivation showing how recurrence equations and state machines translate into matrix transformations. | [Errichto Matrix Exponentiation GitHub](https://github.com/Errichto/youtube/tree/master/matrix-exponentiation) |
| Graph Paths of Length $k$ | CP-Algorithms: Binary Exponentiation (Applications) | Reference / Guide | Shows how powers of an adjacency matrix count paths of exact length $k$ between vertex pairs. | [CP-Algorithms Binary Exponentiation Applications](https://cp-algorithms.com/algebra/binary-exp.html) |

#### Recommended Learning Stack
1. **Concept & Derivation:** Errichto Algorithms: Matrix Exponentiation tutorial.
2. **Implementation:** Errichto's GitHub repository (`d.cpp`) providing clean C++/Java matrix structures with overloaded multiplication and exponentiation.
3. **Practice:** Core syllabus bank (LC 509, LC 70, LC 935, LC 1220; Codeforces Contest 102644).

---

### Topic: Probability & Expected Value

Randomized algorithms and probabilistic expectations evaluate the behavior of structures under non-deterministic inputs. Linearity of Expectation guarantees that the expected value of a sum is the sum of expectations regardless of variable independence.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Linearity of Expectation | Brilliant.org: Linearity of Expectation | Interactive Course | Intuitive treatment of decomposing complex random variables into indicator variables. | [Brilliant Linearity of Expectation](https://brilliant.org/wiki/linearity-of-expectation/) |
| Reservoir Sampling Mechanics | Jeffrey S. Vitter: *Random Sampling with a Reservoir* (1985) | Primary Paper | Inductive proof that maintaining a stream buffer of size $k$ guarantees uniform selection probability $k/N$. | ACM Transactions on Mathematical Software, Vol. 11, No. 1, March 1985 |
| Rejection Sampling & Geometric Distribution | LeetCode Official Solution: Implement Rand10() Using Rand7() | Guide / Editorial | Explains rejection regions and minimal sample generation bounds. | [LeetCode Problem 470 Editorial](https://leetcode.com/problems/implement-rand10-using-rand7/) |

#### Recommended Learning Stack
1. **Concept:** Brilliant.org: Linearity of Expectation.
2. **Implementation:** Vitter's Reservoir Sampling algorithm for streaming iterators.
3. **Practice:** Core syllabus bank (LC 382, LC 398, LC 470).

---

### Topic: Game Theory: Nim & Sprague-Grundy

Impartial two-player games with perfect information reduce to identifying kernel states where transitions cannot force an opponent win. The Bouton Theorem for Nim proves that states with an XOR sum of zero are losing positions.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Nim & Bitwise XOR Sum Invariant | CP-Algorithms: Sprague-Grundy Theorem & Nim | Reference / Guide | Complete mathematical proof of the symmetric strategy that returns non-zero XOR sums back to zero. | [CP-Algorithms Sprague-Grundy & Nim](https://cp-algorithms.com/game_theory/sprague_grundy_nim.html) |
| Sprague-Grundy Theorem & Mex Function | Thomas S. Ferguson: *Game Theory* (UCLA Math) | Academic Monograph | Formal treatment showing every impartial game is equivalent to a Nim pile defined by the minimal excludant ($\text{mex}$) of reachable states. | UCLA Math -> Ferguson Text -> Part I: Impartial Games |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Sprague-Grundy theorem and Nim.
2. **Intuition:** Ferguson's *Game Theory*, Chapter 1, showing game directed acyclic graph (DAG) reductions.
3. **Practice:** Core syllabus bank (LC 292, LC 1025; CSES Nim Game I & II).

---
