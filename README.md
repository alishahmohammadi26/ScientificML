# Scientific Machine Learning for Biopharmaceutical Process Development

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?logo=pytorch)](https://pytorch.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/alishahmohammadi22/ScientificML?style=social)](https://github.com/alishahmohammadi22/ScientificML)

A curated collection of **Scientific Machine Learning (SciML)** notebooks and tools designed for
pharmaceutical process development — from Physics-Informed Neural Networks (PINNs) to
data-driven dynamics and hybrid physics-ML models.

---

## What's Inside

### 📂 `data_driven_dynamics/`
Notebooks on **data-driven dynamic systems** modeling for biopharmaceutical processes:
- System identification from process data
- Koopman operator methods for nonlinear dynamics
- Neural ODE / Neural SDE for process state estimation

### Planned Modules
| Module | Description | Status |
|---|---|---|
| `pinns/` | Physics-Informed Neural Networks for PDEs/ODEs | 🚧 In Progress |
| `hybrid_models/` | Hybrid ML + mechanistic models | 📋 Planned |
| `uncertainty/` | Bayesian ML and conformal prediction | 📋 Planned |
| `continuous_mfg/` | Digital twin components for continuous manufacturing | 📋 Planned |

---

## Quick Start

### Install

```bash
# Clone the repo
git clone https://github.com/alishahmohammadi22/ScientificML.git
cd ScientificML

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Notebooks

```bash
jupyter notebook data_driven_dynamics/
```

### Install as a Package (for reuse in your projects)

```bash
pip install git+https://github.com/alishahmohammadi22/ScientificML.git
```

---

## Core Concepts Covered

### Physics-Informed Neural Networks (PINNs)
Embed physical laws (PDEs/ODEs) as constraints in the neural network loss function — enabling models to be trained with minimal data while remaining physically consistent.

```python
# Example: PINN for reaction kinetics
def pinn_loss(model, t, u_measured, k_true=None):
    u_pred = model(t)
    # Data loss
    data_loss = mse(u_pred, u_measured)
    # Physics residual: du/dt = -k * u  (first-order reaction)
    dudt = torch.autograd.grad(u_pred.sum(), t, create_graph=True)[0]
    k = model.k  # learnable parameter
    physics_loss = mse(dudt + k * u_pred, torch.zeros_like(u_pred))
    return data_loss + physics_loss
```

### Data-Driven Dynamics
Learn process dynamics directly from experimental data — useful when first-principles models are incomplete or too expensive to compute.

### Hybrid Physics-ML Models
Combine mechanistic process knowledge with data-driven ML to get the best of both worlds: generalizability from physics + accuracy from data.

---

## Applications in Pharma

- **Continuous Manufacturing** — Real-time process monitoring and control
- **mRNA Process Development** — IVT reaction optimization, stability prediction
- **Cell Therapy** — Assay outcome prediction, scale-up modeling
- **Crystallization** — Nucleation kinetics modeling with PINNs
- **Drug Stability** — Shelf-life prediction under accelerated conditions

---

## Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-topic`)
3. Add your notebook or module
4. Open a pull request with a description

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## Author

**Ali Shahmohammadi, Ph.D.**  
Associate Director, FAIR Data Strategy · Takeda Pharmaceutical  
[LinkedIn](https://linkedin.com/in/alishahmohammadi) · [Portfolio](https://alishahmohammadi22.github.io)

---

## License

[MIT License](LICENSE) — free to use, modify, and distribute with attribution.
