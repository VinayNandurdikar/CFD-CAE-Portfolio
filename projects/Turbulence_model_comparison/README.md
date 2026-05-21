# OpenFOAM Turbulence Model Comparison

## Overview

This project compares two turbulence models in OpenFOAM:

- k-epsilon
- k-omega SST

using the pitzDaily benchmark case.

The objective is to understand how turbulence-model selection affects velocity prediction in separated turbulent flow.

---

# Software Used

- OpenFOAM
- ParaView
- GitHub

---

# Case Description

The pitzDaily case is a standard CFD benchmark used for studying:

- flow separation
- recirculation
- turbulent mixing
- turbulent shear-layer behaviour

The same geometry, mesh, solver settings, and boundary conditions were used for both simulations.

Only the turbulence model was changed.

---

# Turbulence Models

## k-epsilon Model

The k-epsilon model solves transport equations for:

- Turbulent kinetic energy (k)
- Turbulence dissipation rate (epsilon)

The turbulent viscosity is estimated using:

\[
\mu_t = C_\mu \rho \frac{k^2}{\epsilon}
\]

The model is widely used in industrial CFD because it is robust and computationally stable.

However, it may become more diffusive in separated-flow regions.

---

## k-omega SST Model

The k-omega SST (Shear Stress Transport) model combines the advantages of:

- k-omega behaviour near walls
- k-epsilon behaviour in the free-stream region

The turbulent viscosity is estimated using:

\[
\mu_t = \rho \frac{k}{\omega}
\]

The SST formulation improves prediction of:

- separated flow
- adverse pressure gradients
- near-wall turbulence behaviour

and is widely used in industrial CFD applications.

---

# Velocity Profile Comparison

![Velocity comparison](results/komega_vs_kepsilon_velocity_profile.jpg)

---

# Observations

The k-omega SST model predicts slightly higher velocity compared to the k-epsilon model over most of the sampled region.

The k-epsilon model shows smoother and more diffusive behaviour.

This difference occurs because the turbulence viscosity formulation differs between the two models.

The sharp velocity drop near the downstream region indicates that the sampled line approaches a low-velocity or near-wall recirculation region.

---

# Engineering Interpretation

The pitzDaily benchmark contains separated-flow and recirculation regions.

These regions are highly sensitive to turbulence-model assumptions.

The k-
