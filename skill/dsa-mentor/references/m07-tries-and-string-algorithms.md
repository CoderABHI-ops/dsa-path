# Module 7 of 11: Tries & String Algorithms

> Naming note: the study-resources source calls this module "Advanced Strings & Tries". The syllabus name above is canonical.

Contents: Part A = curriculum, topic table and Core Practice Bank (canonical). Part B = curated study resources.

Part B topics covered by a curated resource:
- Tries (Prefix Trees) & Bitwise Tries
- String Hashing (Polynomial Rolling Hash)
- Pattern Matching: KMP & Z-Algorithm
- Advanced String Algorithms: Rabin-Karp & Manacher's

---

## PART A: Curriculum and Core Practice Bank

| Topic | Purpose | Difficulty | Prereqs | Why It Matters | Effort | Freq |
|---|---|---|---|---|---|---|
| Tries (Prefix Trees) | Efficient string search & prefix matching | Med-Hard | Strings, Trees | Autocomplete, dictionaries, word-search grids. | 3 Days | 40% |
| KMP (Knuth-Morris-Pratt) | Linear-time substring search via the LPS/failure array | Hard | Strings, Recursion | The canonical "beat the O(n·m) naive search" answer. | 3 Days | 15% |
| Rabin-Karp / Rolling Hash | Hash-based substring search and comparison | Medium | Strings | Simpler to reason about than KMP; the go-to for "compare many substrings fast." | 2 Days | 12% |
| Z-Function | Linear-time prefix-matching array, KMP's cleaner cousin | Hard | KMP | Elegant alternative for pattern-matching and period-finding problems. | 2 Days | 8% |
| Manacher's Algorithm | Linear-time longest-palindromic-substring | Hard | Strings, Two Pointers | Upgrades the O(n²) "expand around center" palindrome trick to O(n). | 2 Days | 10% |

### Core Practice Bank — Module 7

**Tries**
- LC 208 — Implement Trie (Prefix Tree) (Medium) — https://leetcode.com/problems/implement-trie-prefix-tree/
- LC 212 — Word Search II (Hard) — https://leetcode.com/problems/word-search-ii/
- LC 211 — Design Add and Search Words Data Structure (Medium) — https://leetcode.com/problems/design-add-and-search-words-data-structure/
- LC 648 — Replace Words (Medium) — https://leetcode.com/problems/replace-words/

**KMP**
- LC 28 — Find the Index of the First Occurrence in a String (Easy) — https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ — implement KMP by hand here, don't just call `indexOf`
- LC 459 — Repeated Substring Pattern (Easy) — https://leetcode.com/problems/repeated-substring-pattern/ — the LPS-array trick in disguise
- LC 686 — Repeated String Match (Medium) — https://leetcode.com/problems/repeated-string-match/

**Rabin-Karp / Rolling Hash**
- LC 187 — Repeated DNA Sequences (Medium) — https://leetcode.com/problems/repeated-dna-sequences/
- LC 1044 — Longest Duplicate Substring (Hard) — https://leetcode.com/problems/longest-duplicate-substring/ — rolling hash + binary search on answer, ties Module 5 back in

**Z-Function**
- LC 28 (revisit) implemented via Z-function instead of KMP, for the compare
- LC 1392 — Longest Happy Prefix (Hard) — https://leetcode.com/problems/longest-happy-prefix/

**Manacher's Algorithm**
- LC 5 — Longest Palindromic Substring (Medium) — https://leetcode.com/problems/longest-palindromic-substring/ — solve it a third time, now in O(n)
- LC 214 — Shortest Palindrome (Hard) — https://leetcode.com/problems/shortest-palindrome/
- LC 647 — Palindromic Substrings (Medium) — https://leetcode.com/problems/palindromic-substrings/

> *Advanced footnote, awareness-level only (very low interview frequency, mostly pure-CP territory): Aho-Corasick (multi-pattern matching) and Suffix Arrays/Suffix Automatons. Know they exist and what problem shape triggers them; don't spend real study days here unless you're specifically CP-training.*

---

---

## PART B: Curated study resources

### Topic: Tries (Prefix Trees) & Bitwise Tries

Tries store character strings along edge paths, allowing prefix searches and string insertions in $\mathcal{O}(L)$ time where $L$ is string length. Bitwise Tries treat integer binary representations as path strings, enabling $\mathcal{O}(32)$ maximum XOR pair lookups.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| N-Ary Trie Operations | USACO Guide (Gold): Introduction to Tries | Guide / Tutorial | Clear structural breakdown of trie node arrays `TrieNode[26]`, child pointers, and terminal flags. | [USACO Guide Tries](https://usaco.guide/gold/modules) |
| Binary Bitwise Tries for Max XOR | CP-Algorithms: Trie Applications | Guide | Shows how inserting 32-bit integers bit-by-bit enables greedy traversal for maximum XOR pair matching. | [CP-Algorithms Trie Applications](https://cp-algorithms.com/) |

#### Recommended Learning Stack
1. **Concept:** USACO Guide (Gold): Introduction to Tries.
2. **Implementation:** Building standard `TrieNode` structures and Bitwise Tries using Java arrays.
3. **Practice:** Core syllabus bank (LC 208, LC 211, LC 212, LC 421, LC 1707).

---

### Topic: String Hashing (Polynomial Rolling Hash)

Polynomial rolling hashes map strings to integer values in $\mathcal{O}(N)$ precomputation time. Subsequent substring hash comparisons run in $\mathcal{O}(1)$ time, turning string equality checks into integer operations.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Polynomial Hash Derivation & Double Hashing | CP-Algorithms: String Hashing | Reference / Guide | Complete derivation of $H(S) = \sum S[i] p^i \pmod m$, prefix hash arrays, and double-hashing collision prevention. | [CP-Algorithms String Hashing](https://cp-algorithms.com/string/string-hashing.html) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: String Hashing mathematical foundations.
2. **Implementation:** Prefix hash array precomputation with modular inverse range calculation in Java.
3. **Practice:** Core syllabus bank (LC 28, LC 1044, LC 1316).

---

### Topic: Pattern Matching: KMP & Z-Algorithm

Knuth-Morris-Pratt (KMP) and Z-algorithms perform single-pattern string matching in linear $\mathcal{O}(N + M)$ time. KMP constructs a Prefix Function ($\pi$-array), while the Z-algorithm builds a Z-array tracking exact prefix matches starting from every index.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| KMP Prefix Function ($\pi$-Array) | CP-Algorithms: Prefix Function (KMP) | Reference / Guide | Detailed derivation of matching state transitions, failure function updates, and optimal string searching. | [CP-Algorithms Prefix Function](https://cp-algorithms.com/string/prefix-function.html) |
| Z-Algorithm & Z-Box Maintenance | CP-Algorithms: Z-Function | Reference / Guide | Clean explanation of maintaining the rightmost matching segment $[L, R]$ to compute prefix matches in linear time. | [CP-Algorithms Z-Function](https://cp-algorithms.com/string/z-function.html) |

#### Recommended Learning Stack
1. **Concept:** CP-Algorithms: Prefix Function and Z-Function articles.
2. **Implementation:** Java implementations of KMP $\pi$-array construction and Z-array matching routines.
3. **Practice:** Core syllabus bank (LC 28, LC 214, LC 1392, LC 3008).

---

### Topic: Advanced String Algorithms: Rabin-Karp & Manacher's

Rabin-Karp uses rolling hashes for multi-pattern search. Manacher's algorithm finds all palindromic substrings in linear $\mathcal{O}(N)$ time by exploiting palindrome symmetry to reuse previously computed radii.

| Subtopic | Best Resource | Type | Why This Resource | Direct Link / Where to Go |
| :--- | :--- | :--- | :--- | :--- |
| Rabin-Karp Rolling Hash Matching | Cormen et al. (CLRS): *Introduction to Algorithms* | Book | Chapter 32: "String Matching", detailing rolling hash window transitions. | CLRS Chapter 32 -> Section 32.2 |
| Manacher's Linear Palindrome Algorithm | CP-Algorithms: Manacher's Algorithm | Reference / Guide | Explains string interspersing with sentinels (`#`) and maintaining the rightmost palindrome center and boundary $(C, R)$. | [CP-Algorithms Manacher's Algorithm](https://cp-algorithms.com/string/manacher.html) |

#### Recommended Learning Stack
1. **Concept:** CLRS Chapter 32 (Rabin-Karp); CP-Algorithms (Manacher's Algorithm).
2. **Implementation:** Writing Java implementations for Rabin-Karp sliding hash and Manacher's palindrome array $P[i]$.
3. **Practice:** Core syllabus bank (LC 187, LC 1044, LC 5, LC 647).

---
