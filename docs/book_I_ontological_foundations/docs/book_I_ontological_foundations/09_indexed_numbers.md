# Indexed Numbers – Memory in Arithmetic

**Source:** Młynarski, K. (2025). *Indexed Numbers: Post-Quantum Cryptography*. Preprint on RG.

---

## 1. The Problem: Arithmetic Without Memory

Standard arithmetic treats numbers as "bare" values. The equation $2 + 2 = 4$ is true regardless of whether the two came from $1 + 1$ or from $3 - 1$ or from the prime factorization $2 \times 1$. This **lack of memory** is a feature for most calculations, but it becomes a limitation when we want to:

- Model systems where the *history* of a number matters (e.g., quantum states, metastable configurations)
- Build cryptographic systems secure against quantum attacks (where Shor's algorithm exploits the absence of history)
- Capture the intuition that a number can be "the same" but not "identical"

**Indexed numbers** address this gap. They are numbers that carry, in their very structure, information about their origin and about which operations are permitted upon them.

---

## 2. The Discrete Root: A Geometric Perspective

> **Definition 1 (Discrete Root).** For $n \in \mathbb{N}$, the *discrete root* $\sqrt[n]{n}$ is the pair $(p_1, p_2)$ such that:
> 1. $p_1 \cdot p_2 = n$
> 2. $p_1 \leq p_2$
> 3. $|p_2 - p_1| = \min_{d|n} \left| \frac{n}{d} - d \right|$, where $1 \leq d \leq \sqrt{n}$

In other words, the discrete root is the pair of divisors that are *closest to each other* — the "most symmetric" factorization of $n$.

**Examples:**
- For $n = 12$: possible pairs $(1,12)$, $(2,6)$, $(3,4)$. Differences: $11$, $4$, $1$. The discrete root is $(3,4)$.
- For $n = 9$ (a square): $\sqrt[4]{9} = (3,3)$.
- For $n = 7$ (a prime): $\sqrt[4]{7} = (1,7)$.

Each natural number can be plotted as a point $(p_2, p_1)$ in the plane:
- **Primes** lie on the line $y = 1$ (minimal symmetry)
- **Squares** lie on the diagonal $y = x$ (maximal symmetry)
- **Composite numbers** occupy the region $1 < y < x$, with distance from the diagonal measuring "multiplicative asymmetry"

This geometry reveals that numbers are not atomic — they have an internal structure, a "shape" determined by their divisors.

---

## 3. Indexed Numbers: Numbers with Memory

While every number has a discrete root, not every pair of divisors is a discrete root of some number. This observation leads to the concept of **indexed numbers** — numbers that are "frozen" in a specific asymmetric state.

> **Definition 2 (Indexed Number).** An indexed number $n_{(p_i, p_j)}$ is a triple:
> $$(n, (p_i, p_j), \mathcal{D}_{\text{allow}})$$
> where:
> 1. $p_i \cdot p_j = n$
> 2. $(p_i, p_j) \neq \sqrt[n]{n}$ (not the discrete root)
> 3. $\mathcal{D}_{\text{allow}} = \{ d \in \mathbb{N} : d|n \land |d - n/d| \geq |p_i - p_j| \}$

Division is **only permitted** by divisors in $\mathcal{D}_{\text{allow}}$. The number's structure is "frozen" in a state of local equilibrium — operations that would make it *more symmetric* are forbidden.

**Example.** For $12_{(2,6)}$:
- $\mathcal{D}_{\text{allow}} = \{1, 2, 6, 12\}$ (differences $\geq 4$)
- $\mathcal{D}_{\text{forbid}} = \{3, 4\}$ (difference $|3-4| = 1 < 4$)
- The number *cannot* be divided by 3 or 4 — this protects the "less symmetric" pair $(2,6)$.

---

## 4. Numbers with Operation Memory

When we add two indexed numbers, their histories combine. The result should remember both origins.

> **Definition 3 (Memory-Preserving Sum).** The sum of indexed numbers:
> $$n_{(p_i,p_j)} + m_{(z_i,z_j)} = (n + m, [(p_i,p_j),(z_i,z_j)], \mathcal{D}_{\text{allow}}^{\text{sum}})$$
> where:
> - $\mathcal{D}_{\text{allow}}^{\text{sum}} = \mathcal{D}_{\text{allow}}^{n} \cup \mathcal{D}_{\text{allow}}^{m}$
> - The origin $[(p_i,p_j),(z_i,z_j)]$ records the structure of both operands

The resulting number inherits divisibility constraints from both parents. It "remembers" where it came from.

---

## 5. Physical Interpretations

| Physical Concept | Indexed Number Representation |
|:-----------------|:------------------------------|
| **Planck length** | $\ell_P = 1.616255_{(1.616255,1.616255)} \times 10^{-35}\ \text{m}$ — an indivisible unit of space |
| **Metastable state in crystal** | $E_{(4,9)} = 36\ \text{meV}$, $\mathcal{D}_{\text{allow}} = \{1,2,3,4,9,12,18,36\}$ — division by 6 forbidden |
| **Quantum antiresonance** | $\psi_{(3,7)}\Delta t = 21\ \text{fs}$ — a state that cannot transition to a more symmetric resonant state |
| **Bound state** | $\Phi_{(a,b)} = \Phi_a \otimes \Phi_b$ for $|a-b| > \Delta_{\text{crit}}$ — particles that cannot decay into a more symmetric configuration |

---

## 6. Cryptographic Applications: Genesis-DH

> **Protocol 1 (Genesis-DH Key Exchange).**
> 1. **Public parameters:** An indexed generator $g_{(a,b)}$.
> 2. **Alice:** Selects secret $x_A$, computes $A = g^{x_A}$ with genesis $G_A$ (the history of operations).
> 3. **Bob:** Selects secret $x_B$, computes $B = g^{x_B}$ with genesis $G_B$.
> 4. **Exchange:** Alice and Bob exchange $A$ and $B$.
> 5. **Session key:** $K = H(A \oplus B \ ||\ G_A \ ||\ G_B)$, where $H$ is a hash function.

**Security intuition:** To recover the secret, an attacker would need to reconstruct the operation history stored in $G_A$ and $G_B$ — a problem that is provably hard, even for quantum computers.

---

## 7. Non-Standard Arithmetic Operations

> **Definition 4 (Non-Standard Operation).** A non-standard operation $F$ is a quintuple:
> $$F = (\Sigma_{\text{in}}, \Sigma_{\text{out}}, F_{\text{val}}, F_{\text{origin}}, \Phi)$$

**Example: Indexed Exponentiation**
$$F_{\text{exp}}(x_{(a,b)}, y_{(c,d)}) = (x^y, [(a,b),(c,d)], \Phi_{\text{exp}})$$
The inverse problem — recovering $x$ and $y$ from the output — is NP-complete.

**Example: XOR-Dependent Addition**
$$F_{\oplus}(x_{(a,b)}, y_{(c,d)}) = (x + y + (a \oplus d), [G_x \oplus G_y], \Phi_{\oplus})$$
This system is IND-CCA secure.

---

## 8. Summary: From Bare Numbers to Numbers with Memory

The key insight of this chapter is that **numbers can carry memory**. A number is no longer a mere quantity; it is a structured object with:

- A **value** (the usual numeric quantity)
- An **index** (the pair of divisors that defines its asymmetry)
- A **history** (the sequence of operations that produced it)
- A set of **allowed operations** (divisibility constraints)

This framework has profound implications:

- **For mathematics:** A constructive, generative account of numbers aligning with PFS.
- **For physics:** Modeling indivisible units, metastable states, and quantum bound states.
- **For cryptography:** A new paradigm for post-quantum security based on the irreversibility of operation histories.

In the context of *Ars Rerum*, indexed numbers are the mathematical embodiment of **identity with memory** — the recognition that a number, like a person, is shaped by its history.

---

**References:**

[1] K. Młynarski, "Indexed Numbers: Post-Quantum Cryptography," Preprint on RG, 2025.

[2] K. Młynarski, "Potentially Finite Sets (PFS)," Preprint on RG, 2026.

[3] K. Młynarski, "Ontological Identity Theory: Gravity," Preprint on RG, 2026.
