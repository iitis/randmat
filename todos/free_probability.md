# Free probability support

## Deciders

- Dariusz Kurzyk
- Łukasz Pawela

## Description

Our goal is to have a language for expressing polynomials of random matrices in
the asymptotic regime. This should allow for intuitive definition of polynomials
of random matrices.

## Outcome

We should have the following:

- The concept of asymptotic ensembles
- Sampling of "asymptotic" ensembles - need to decide on value "large enough"
- Allow sampling eigenvalues directly from PDF
- Calculate the PDF of eigenvalue distribution of poynomials of asymptotic random matrices:
  - R transform
  - S transform
  - Cauchy transform
  - Numerical calculation
  - Pre-coded values for known solutions
  - Use sympy for other calculations (can take a long time, needs careful handling)
