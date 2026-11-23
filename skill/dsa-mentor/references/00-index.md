# Index: read this first in every new session

## Legend (columns in each module's Part A table)
- **Difficulty**: conceptual difficulty to learn, not to implement.
- **Prereqs**: topics that should be finished first.
- **Effort**: rough focused-study days for a first pass.
- **Freq**: directional estimate of how often the topic appears in FAANG-tier loops. Use relative order, not the exact number.

## Module map (11 modules, 60 topics)

| # | Module | File |
|---|---|---|
| 1 | Foundations, Bit Manipulation & Math for DSA | m01-foundations-bit-manipulation-and-math-for-dsa.md |
| 2 | Arrays, Strings & Core Array Patterns | m02-arrays-strings-and-core-array-patterns.md |
| 3 | Linked Lists, Stacks, Queues & Monotonic Structures | m03-linked-lists-stacks-queues-and-monotonic-structu.md |
| 4 | Hashing, Recursion, Backtracking & Divide-and-Conquer | m04-hashing-recursion-backtracking-and-divide-and-co.md |
| 5 | Searching & Sorting | m05-searching-and-sorting.md |
| 6 | Trees & Heaps | m06-trees-and-heaps.md |
| 7 | Tries & String Algorithms | m07-tries-and-string-algorithms.md |
| 8 | Greedy & Dynamic Programming | m08-greedy-and-dynamic-programming.md |
| 9 | Graph Theory | m09-graph-theory.md |
| 10 | Advanced Data Structures | m10-advanced-data-structures.md |
| 11 | Design Problems | m11-design-problems.md |

Also: `appendix-mental-models-boilerplates.md` (sequencing logic, mental models, boilerplates to memorize, never-memorize list, interview pitfalls). Read it at Stage 4.

Counts: the topic tables hold 60 topics (the original documents said 62, which does not match the tables). The Core Practice Bank lists 192 entries, 175 unique LeetCode problems (some repeat across modules).

## Depth tiers (opt-in only; the default is the full 5-stage protocol for every topic)
Use only if the learner asks for a faster pace. Use the Freq column of the topic being taught.
- **Full** (Freq 25% or more): all 5 stages.
- **Lite** (10% to 24%): Stage 1 (short anchor + study brief), one guided problem, Stage 4 and Stage 5 merged into one short round.
- **Awareness** (under 10%): concept and mental model, one canonical problem, one-line recognition clue. Offer to go deeper later.

## Optional "interview-core-first" path
If the learner wants to be interview-ready sooner, offer this order at Phase 0 instead of strict module order. Syllabus order stays the default.
1. Module 1: Time & Space Complexity, Java Foundations, Bit Manipulation only.
2. Modules 2, 3, 4, 5, 6 in order.
3. Module 9: Graph Fundamentals & Traversals, Topological Sort, Union-Find.
4. Module 8: Greedy, DP 1D, DP 2D & Knapsack.
5. Remaining Module 9, then remaining Module 8, then Module 7.
6. Remaining Module 1 (math), then Modules 10 and 11.
Matrix Exponentiation and Game Theory (Module 1) are best taught after DP 1D regardless of path.

## Known resource gaps (Part B has no dedicated section)
For these topics there is no curated resource. Do not invent URLs. Use the fallback sentence from Stage 1 ("No external curated material found for this topic, so let's cover it directly in chat"), or a navigation breadcrumb. Breadcrumbs below are from memory and unverified, so present them as "search for", not as links.

| Topic | Suggested breadcrumb or fallback |
|---|---|
| GCD, LCM & Euclid | CP-Algorithms, Algebra section, Euclidean algorithm and Extended Euclid (Extended Euclid is already in Module 1 Part B) |
| Sieve of Eratosthenes & Primality | CP-Algorithms, Algebra section, Sieve of Eratosthenes |
| Cyclic Sort | Chat fallback |
| Merge Intervals | Chat fallback (sort by start, then sweep) |
| Recursion | Chat fallback; Roughgarden, Algorithms Illuminated Part 1 (divide-and-conquer chapters) for the mindset |
| Backtracking | Chat fallback; use the backtracking template in the appendix |
| Divide & Conquer | Roughgarden, Algorithms Illuminated Part 1 (merge sort, master method) |
| Sorting Algorithms | Sedgewick & Wayne, Algorithms 4th ed., Chapter 2 (Sorting) |

## Link hygiene
- Two bad links in the original curation file were removed: the Java Fast I/O row (it pointed at an unrelated CP-Algorithms stack/queue page) and the Cornell CS 3110 amortized-analysis row (homepage only).
- Other URLs were not re-verified. If a link looks wrong, or the learner reports a 404, give the exact resource title plus a navigation path instead.
- LeetCode problems: the number and exact title are the reliable part. If a link fails, search `leetcode <number>`.
- The CSES and Codeforces entries point to hub pages on purpose.

## Module naming differences between the two source files
The syllabus names are canonical. The study-resources source named Modules 4, 5, 6, 7, 8, 9, 10 and 11 slightly differently (for example Module 4 as "Hashing, Hash Tables & Design" and Module 5 as "Binary Search, Binary Search on Answer & Ternary Search"). Each module file notes this at the top. Part B only covers some topics of a module, so always check Part A's topic table for the full list.
