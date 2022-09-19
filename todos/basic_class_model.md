# Simple model of random matrix ensembles types

## Deciders

- Dariusz Kurzyk
- Łukasz Pawela

## Description

We need to decide on a simple class structure and behavior for basic random
matrix ensembles.

## Outcome

We should have the following:

- Basic class hierarchy for matrix ensembles:
  - Ginibre ensemble
  - Wishart ensemble
  - General MANOVA?
  - Circular ensembles
  - Gaussian ensembles
- Basic class hierarchy for random quantum objects:
  - pure states
  - mixed states
  - channels
  - superchannels
  - process matrices
- Additional random objects from classical probability theory:
  - random probability vectors
  - random stochastic matrices (Dirichlet distribution)
  - random bistochastic matrices (Sinkhorn's algorithm)
  
- Initial versions of methods
- Additional helpers:
  - plotting of eigenvalues/singular values
  - batch sampling

Ideally we should have something like this
```python
from randmat import WishartEnsemble

wishart = WishartEnsemble(d=2, beta=2, env_dim=20)
matrices = wishart.sample(n=10)
plot_spectrum_histogram(matrices)
plot_pdf(wishart)
```
### Things needing clarification

- How to work with joint PDFs of eigenvalues
- Visualzation of pdfs
- Support for GPU sampling