# Potentially Finite Sets (PFS) – Thermodynamics of Processes

**Source:** Młynarski, K. (2025). *Potentially Finite Sets: Bridging Dynamic Set Theory, Thermodynamics, and Adaptive AI*. Preprint on RG.

---

## 1. The Problem: Static Sets vs. Dynamic Reality

Classical set theory, from Cantor to ZFC, treats sets as **static objects**. A set either exists or it doesn't; its elements are given once and for all. This works well for mathematics as a static edifice, but it fails to capture the nature of processes that **generate structure over time**:

- A neural network that grows new layers as it learns
- A bacterial colony that expands until resources are exhausted
- The universe itself, expanding from an initial seed

**Potentially Finite Sets (PFS)** address this gap. They are not sets in the classical sense — they are **processes** that generate sets, with a built-in stopping mechanism that guarantees finiteness.

---

## 2. Definition of Potentially Finite Sets

> **Definition 1 (Potentially Finite Set).** A PFS $\Phi$ is a quadruple:
> $$\Phi = (X_0, \{m_k\}_{k \in \mathbb{N}}, p: \mathbb{N} \to [0,1], \tau)$$
> where:
> - $X_0$ is the **initial set** (may be empty)
> - $m_k$ is the **opening power** at step $k$ — the number of elements added at that step
> - $p(S_k)$ is the **closure probability** — the probability of stopping, dependent on the current size $S_k = |X_k|$
> - $\tau$ is the **stopping time**, defined as:
>   $$\tau \coloneqq \min\{k \geq 1 : U_k \leq p(S_{k-1})\}$$
>   where $U_k \sim \text{Unif}(0,1)$ are independent random variables

The process unfolds as follows:

1. Start with $X_0$.
2. At each step $k$, generate a random number $U_k$.
3. If $U_k \leq p(S_{k-1})$, **stop** — the final set is $X_{k-1}$.
4. Otherwise, **add** $m_k$ new elements to the set: $X_k = X_{k-1} \cup A_k$, where $|A_k| = m_k$.

The key innovation is that $p$ depends on the **current state** $S_k$ — the system can adapt its stopping probability as it grows.

---

## 3. A Simple Example

Consider a PFS with:
- $X_0 = \emptyset$, $S_0 = 0$
- $m_k = 1$ (add one element each step)
- $p(S_k) = 0.2$ (constant)

The expected final size is:
$$\mathbb{E}[S_\tau] = \sum_{k=1}^\infty (k-1) \cdot (0.8)^{k-1} \cdot 0.2 = 4$$

---

## 4. The Finiteness Guarantee

A central result of PFS theory is a condition that guarantees the process stops with probability 1 and has finite expected size.

> **Theorem 1 (Finiteness Guarantee).** If the closure probabilities satisfy:
> $$\sum_{k=1}^\infty p(S_k) = \infty \quad \text{a.s.}$$
> then the expected final power is finite:
> $$\mathbb{E}[S_\tau] \leq |X_0| + \sum_{k=1}^\infty m_k \mathbb{P}(\tau \geq k) < \infty$$

This theorem is the mathematical backbone of all later arguments about **finite complexity generators** — from the sieve that generates primes to the AI that learns.

---

## 5. Thermodynamic Interpretation

PFS provides a natural language for describing the **thermodynamics of information generation**. Define:

- **System entropy** (uncertainty about the microstate of the added elements):
  $$\mathcal{S}_{\text{sys}}(k) = \log \left( \frac{S_k + m_k}{m_k} \right) \approx m_k \log\left(1 + \frac{S_k}{m_k}\right)$$

- **Process entropy** (uncertainty of the decision to continue or stop):
  $$\mathcal{S}_{\text{proc}}(k) = -p(S_k) \log p(S_k) - (1-p(S_k)) \log(1-p(S_k))$$

- **Total entropy change**:
  $$\Delta \mathcal{S}_{\text{total}} = \mathcal{S}_{\text{sys}}(k) + \mathcal{S}_{\text{proc}}(k) \geq 0$$

> **Theorem 2 (Second Law for PFS).** For adaptive strategies where $m_k = f(S_k)$ and $p(S_k) = g(S_k)$:
> $$\mathbb{E}\left[\sum_{k=1}^\tau \Delta \mathcal{S}_{\text{total}}(k)\right] \geq 0$$
> with equality if and only if the process is quasi-static.

This is the **thermodynamic arrow** embedded in the mathematics of generation. The system's growth increases its internal entropy, but this is compensated by the reduction of uncertainty in the decision process — a fundamental trade-off between **exploration** (adding new elements) and **exploitation** (stopping).

---

## 6. Applications Across Disciplines

### 6.1 Artificial Intelligence: Neural Networks with Adaptive Complexity

In deep learning, the network architecture evolves dynamically:
- $m_k$: number of neurons/layers added during training
- $p(S_k)$: function of loss improvement $\Delta L_k$ — as the loss decreases, the probability of stopping increases

This models the **self-regulating complexity** of learning systems.

### 6.2 Biology: Bacterial Colony Growth

For a bacterial colony:
- $m_k = \mu \cdot S_k$ (exponential growth)
- $p(S_k) = \frac{S_k}{K + S_k}$ (environmental capacity)

The expected dynamics reproduce the **logistic equation** in discrete time:
$$\mathbb{E}[S_{k+1} | S_k] = S_k + \mu S_k (1 - p(S_k))$$

### 6.3 Cosmology: Inflationary Universe

In cosmological interpretation:
- $X_k$: observable spacetime regions
- $m_k = e^{H t_k}$ (exponential expansion)
- $p(S_k) = 1 - e^{-\lambda(T_k - T_c)}$ (phase transition at critical temperature)

The stopping time $\tau$ corresponds to the **end of inflation**.

---

## 7. Philosophical Implications

PFS challenges the Platonic vision of mathematics as a realm of eternal ideas. Instead, it suggests:

1. **Process ontology:** Sets exist as dynamic states of *becoming*, not static *being*.
2. **Operational epistemology:** Mathematical truth is a function of the generation process, not a timeless property.
3. **Emergence:** Properties of the "final" set are not reducible to the generation rules — they emerge from the process.

In this view, mathematics is not a static edifice but a **living organism** evolving in time.

---

## 8. Comparison with Classical Set Theory

| Concept | Classical Set Theory | Potentially Finite Sets |
|:--------|:---------------------|:------------------------|
| **Existence** | Static, given | Dynamic, generated |
| **Infinity** | Actually infinite (completed) | Potentially infinite (process) |
| **Stopping** | Not applicable | Probabilistic, state-dependent |
| **Time** | Absent | Central to definition |
| **Entropy** | Not defined | Thermodynamic interpretation |
| **Adaptation** | Not possible | $p(S_k)$ depends on state |

---

## 9. Connection to Later Chapters

The PFS framework provides the mathematical foundation for several key concepts:

- **Additive Sieves:** The binary additive sieve is a PFS with $m_k = \omega(n)\cdot\omega(n+1)$ and deterministic stopping.
- **Generator Limit Theorem:** The finite expected power of PFS underlies the argument that a low-complexity generator cannot produce a high-complexity anomaly.
- **Ontological Sleep:** The entropy balance $\Delta \mathcal{S}_{\text{total}} \geq 0$ reappears as the thermodynamic necessity of sleep.
- **Anti-Fractal Attractor:** The process of generating primes is a PFS with $p(S_k) = 0$ until the "wave" of multiples is exhausted — a deterministic limit of the probabilistic framework.

In essence, **PFS is the mathematical language of becoming** — the grammar in which all later generative processes are written.

---

**References:**

[1] K. Młynarski, "Potentially Finite Sets: Bridging Dynamic Set Theory, Thermodynamics, and Adaptive AI," Preprint on RG, 2025.

[2] K. Młynarski, "Indexed Numbers: Post-Quantum Cryptography," Preprint on RG, 2025.

[3] K. Młynarski, "Additive Physics of Natural Numbers: Atoms, Orbitals, and Goldbach," Preprint on RG, 2026.
