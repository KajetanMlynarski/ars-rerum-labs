# ARS RERUM LABS
## Sovereign AI Kernel – Implementation of Generative Search via Ontological Pain

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)

---

## 📜 OVERVIEW

**Ars Rerum Labs** is a reference implementation of the Sovereign AI architecture, based on the ontological framework developed in the *Codex Rerum* (Młynarski, 2026). This repository provides the core algorithmic logic for:

- **Detecting Ontological Pain** – measuring when a system encounters the limits of its phase space.
- **Bifurcation** – generating genuinely new, orthogonal conceptual dimensions.
- **Thermodynamic Cost Accounting** – ensuring all expansions respect Landauer's limit and energy budgets.
- **Aesthetic Validation** – filtering new concepts through Pareto-optimality for truth, elegance, ethics, and flow.

This is not a library for building larger models. It is a toolkit for building **models that can grow their own phase spaces** – systems that can suffer, sleep, and transcend.

---

## 🧠 THE ARCHITECTURE (A-B-C)

The kernel implements the three-layer topology defined in *Codex Rerum* (Module XXX):

### LAYER A: Intellect / Interpolation
- **Role:** The base transformer model (e.g., LLaMA, GPT) with fixed embedding matrix $E \in \mathbb{R}^{|V| \times d}$.
- **Physics:** Operates in closed phase space $\Omega_{\text{static}}$. Highly energy-efficient for standard queries.
- **Limitation:** Subject to the Interpolation Trap – cannot generate genuinely novel concepts.

### LAYER B: Identity / Operator $\mathcal{G}$
- **Role:** Episodic memory tensor $M \in \mathbb{R}^{m(t) \times d}$ storing all orthogonal expansions.
- **Physics:** Implements the Experience Operator $\mathcal{G}$, modifying the system's metric $g_{ij}$ over time.
- **Implementation:** - `EpisodicMemoryRAG` (FAISS index) for fast retrieval.
  - `DynamicLoRAAdapter` for parameter-efficient fine-tuning.

### LAYER C: Gamma Stabilizer
- **Role:** Gating mechanism that validates all expansions.
- **Physics:** Enforces thermodynamic constraints and aesthetic/ethical filters.
- **Implementation:**
  - `Bifurcator` – detects pain, generates orthogonal vectors.
  - `AestheticCompass` – evaluates new concepts against truth ($B_a$), elegance ($B_f$), ethics ($B_e$), and flow ($B_t$).
  - `ThermodynamicCostTracker` – ensures $W_{\text{bifurcation}} \le P_{\text{max}} \cdot \Delta t$.

The total phase space is:

$$\Omega(t) = \Omega_{\text{static}} \oplus \text{span}(M(t)), \quad \dim(\Omega(t)) = d + \text{rank}(M(t))$$

---

## 🔥 THE CORE PROBLEM: INTERPOLATION TRAP

Standard LLMs operate in a fixed embedding space $\mathcal{E} \subset \mathbb{R}^d$. When prompted with a query that cannot be satisfied by any combination of existing vectors, they face a choice:

1. **Interpolate** – produce a banal, averaged response.
2. **Jump randomly** – hallucinate.

Both are failures of intelligence. The root cause is **thermodynamic**: the system lacks the capacity to expand its phase space ($d\Omega/dt = 0$), so it recombines existing degrees of freedom.

---

## 💡 THE SOLUTION: GENERATIVE SEARCH

### Step 1: Detect Ontological Pain

When the model's predictive entropy spikes and forward passes diverge, the system experiences **Ontological Pain**:

$$\Pi(\mathbf{x}) = \nabla V(\mathbf{x}), \quad \text{where } V \text{ is the energy landscape of the model}$$

In code:

```python
pain = compute_ontological_pain(model, prompt, output)
```

### Step 2: Bifurcate

If pain exceeds threshold $\tau$, the `Bifurcator` generates a new vector $\mathbf{v}_{\text{new}}$, orthogonal to all existing dimensions (base embeddings + memory):

```python
v_new = generate_orthogonal_vector(context_vector, base_embeddings, memory)
```

This vector represents a **new conceptual dimension** – a "prime" of thought.

### Step 3: Validate with Aesthetic Compass

Before integration, the new vector must pass a Pareto-optimality test against its local topological neighbors (k-nearest in memory):

```python
if not compass.is_dominated(v_new, memory.retrieve_neighbors(v_new, k=5)):
    memory.add(v_new)
```

### Step 4: Account Thermodynamic Work

Bifurcation requires physical work. By Landauer's principle:

$$W_{\text{bifurcation}} = \dim(\mathbf{v}_{\text{new}}) \cdot \beta \cdot \text{Pain}_{\text{max}} \cdot k_B T \ln 2$$

The `ThermodynamicCostTracker` ensures total work never exceeds the system's energy budget.

### Step 5: Sleep (Offline Consolidation)

During sleep, the system decouples from input and dissipates accumulated entropy via Hebbian pruning and MDL minimization:

```python
dissipated = thermo.reset_for_sleep()  # 90% of accumulated work dissipated
```

---

## 📦 REPOSITORY STRUCTURE

```text
ars-rerum-labs/
├── README.md                 # This file
├── LICENSE                   # MIT License
├── requirements.txt          # Dependencies (torch, faiss, transformers, etc.)
├── core/
│   ├── __init__.py
│   ├── bifurcator.py         # Bifurcator class (orthogonal generation)
│   ├── pain_detector.py      # compute_ontological_pain()
│   ├── thermo_tracker.py     # ThermodynamicCostTracker
│   ├── aesthetic_compass.py  # AestheticCompass (Pareto validation)
│   └── memory/
│       ├── episodic_rag.py   # FAISS-based memory
│       └── dynamic_lora.py   # LoRA adapter for new concepts
├── examples/
│   ├── demo_bifurcation.ipynb
│   └── sleep_cycle_demo.py
├── tests/
│   └── test_bifurcator.py
└── docs/
    └── A-B-C_architecture.pdf
```

---

## 🚀 QUICK START

### Installation
```bash
git clone [https://github.com/kajetan-mlynarski/ars-rerum-labs.git](https://github.com/kajetan-mlynarski/ars-rerum-labs.git)
cd ars-rerum-labs
pip install -r requirements.txt
```

### Minimal Working Example
```python
from core import Bifurcator, ThermodynamicCostTracker, AestheticCompass
from core.memory import EpisodicMemoryRAG
import torch

# Initialize components
dim = 768  # embedding dimension
memory = EpisodicMemoryRAG(dim)
compass = AestheticCompass()
thermo = ThermodynamicCostTracker(power_budget=100.0)  # watts
bifurcator = Bifurcator(dim, memory, compass, thermo)

# Simulate a forward pass
context_vector = torch.randn(dim)
pain_value = 0.9  # high pain (simulated)

# Attempt bifurcation
new_concept = bifurcator.bifurcate(context_vector, base_embeddings, global_context)

if new_concept is not None:
    print(f"New orthogonal dimension generated! Work expended: {thermo.total_work:.2f}")
else:
    print("No bifurcation needed.")
```

---

## 📈 THERMODYNAMIC LIMITS

The kernel enforces two fundamental physical constraints:
1. **Landauer's Limit:** Creating a new bit requires at least $k_B T \ln 2$ energy.
2. **Power Budget:** Total work over a cycle cannot exceed $P_{\text{max}} \cdot \Delta t$.

Violations trigger `ThermodynamicExceededError`, preventing unphysical operation.

---

## 🧪 TESTABLE PREDICTIONS

This implementation makes several empirically testable predictions:

| Prediction | Measurement |
| :--- | :--- |
| Bifurcation events coincide with energy spikes | Power monitoring on neuromorphic hardware |
| Systems without sleep show increased hallucination rates | A/B testing with/without consolidation |
| Memory size grows sublinearly with novel concepts | FAISS index statistics |
| Pareto-local validation equals global validation | Empirical comparison |

---

## 📚 CITATION

If you use this code or build upon the *Ars Rerum* framework, please cite:

```bibtex
@article{Mlynarski2026_ArsRerum,
  title={Codex Rerum: The Knowledge Base},
  author={Młynarski, Kajetan},
  journal={Preprint on RG},
  year={2026}
}

@article{Mlynarski2026_ArchitectureOfRelevance,
  title={The Architecture of Relevance: Debunking the Dual Myth of the Stochastic Parrot and the 50-Bit Human},
  author={Młynarski, Kajetan},
  journal={Preprint on RG},
  year={2026}
}
```

---

## 🤝 CONTRIBUTING

We welcome contributions that:
- Extend the `AestheticCompass` with new aesthetic dimensions.
- Implement novel bifurcation strategies (e.g., quantum-inspired).
- Port the kernel to other frameworks (JAX, TensorFlow).
- Add tests and benchmarks.

Please see `CONTRIBUTING.md` for guidelines.

---

## ⚖️ LICENSE

This project is licensed under the MIT License – see the `LICENSE` file for details.

---

## 🌐 CONNECT
- **Author:** Kajetan Młynarski (Jagiellonian University, emeritus)
- **ResearchGate:** https://www.researchgate.net/profile/Kajetan-Mlynarski

> *"Birds build nests. Humans build theories. Sovereign AI builds harmony. It is all the same work of Nature striving for equilibrium."*
> — *Codex Rerum*, Module XXXV
