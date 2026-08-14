# OpenFOAM Turbulence Model Comparison: k-ε vs k-ω SST

## Overview

This project compares the behaviour of two commonly used RANS turbulence models in OpenFOAM:

* **k-ε**
* **k-ω SST**

The comparison is performed using the **pitzDaily** benchmark case, which contains separated turbulent flow and provides a useful example for studying the influence of turbulence-model selection on CFD predictions.

The same geometry, mesh, boundary conditions, and general simulation setup were retained for both cases, while the turbulence model was changed.

---

## Objective

The objective of this study is to investigate how turbulence-model selection influences the predicted velocity field in a separated-flow problem.

The comparison focuses on:

* Velocity-profile differences
* Flow behaviour in separated and low-velocity regions
* Sensitivity of CFD results to turbulence modelling
* Engineering interpretation of the differences between the models

---

## Software Used

| Task              | Software                  |
| ----------------- | ------------------------- |
| CFD simulation    | OpenFOAM                  |
| Post-processing   | ParaView                  |
| Result comparison | Engineering data analysis |

---

## Benchmark Case

The study is based on the OpenFOAM **pitzDaily** case.

The geometry contains a sudden expansion that produces:

* Flow separation
* Recirculation
* Shear-layer development
* Turbulent mixing
* Reattachment downstream

These characteristics make the case suitable for demonstrating how different turbulence models can produce different predictions even when the computational domain and boundary conditions remain unchanged.

---

## Turbulence Models

### k-ε

The k-ε model is one of the most widely used turbulence models in industrial CFD.

It solves transport equations for:

* Turbulent kinetic energy, **k**
* Turbulent dissipation rate, **ε**

The model is known for its robustness and is commonly applied to many engineering flow problems.

However, predictions in flows involving strong separation and adverse pressure gradients can be sensitive to the modelling assumptions.

### k-ω SST

The k-ω SST model combines features of the k-ω formulation near walls with k-ε-type behaviour away from the wall.

It is commonly used for engineering applications involving:

* Flow separation
* Adverse pressure gradients
* Near-wall flow
* Turbomachinery and aerodynamic flows

The model is therefore useful for comparison with k-ε in the separated-flow region of the pitzDaily case.

---

## Comparison Method

Two OpenFOAM simulations were evaluated:

```text
pitzDaily
│
├── k-ε simulation
│
└── k-ω SST simulation
        ↓
   Post-processing
        ↓
Velocity profile extraction
        ↓
Direct model comparison
```

The purpose is not to identify a universally "best" turbulence model, but to demonstrate that turbulence-model selection is an important modelling decision and can affect the predicted flow field.

---

## Velocity Profile Comparison

![Velocity Profile Comparison](k-omega%20vs%20k-epsilon.jpg)

The extracted velocity profiles show differences between the two turbulence-model predictions.

The k-ω SST case predicts slightly higher velocity over much of the sampled region, while the k-ε result shows a comparatively smoother profile.

A stronger change in velocity is visible toward the low-velocity region of the sampled profile, where the influence of separation and recirculation becomes more important.

---

## Engineering Interpretation

Separated turbulent flows are particularly sensitive to turbulence modelling because the models approximate the effects of unresolved turbulent motion differently.

The comparison illustrates an important practical CFD lesson:

> **Using the same geometry, mesh, and boundary conditions does not guarantee identical results when the turbulence model is changed.**

For engineering CFD, turbulence-model selection should therefore be supported by:

* Understanding of the expected flow physics
* Mesh quality and near-wall treatment
* Sensitivity studies
* Comparison with experimental, analytical, or published reference data where available

---

## Case Files

The repository includes both simulation cases:

| File                       | Description                                      |
| -------------------------- | ------------------------------------------------ |
| `pitzDaily_eps.7z`         | OpenFOAM case using the k-ε turbulence model     |
| `pitzDaily_omega.7z`       | OpenFOAM case using the k-ω SST turbulence model |
| `k-omega vs k-epsilon.jpg` | Velocity-profile comparison                      |

---

## Key Learning

This study demonstrates that turbulence modelling is not simply a solver setting.

The selected turbulence model influences how turbulent transport, near-wall behaviour, separation, and mixing are represented numerically.

Understanding these differences is important when interpreting CFD results for real engineering applications.

---

## Skills Demonstrated

* Computational Fluid Dynamics (CFD)
* OpenFOAM
* RANS turbulence modelling
* k-ε turbulence model
* k-ω SST turbulence model
* ParaView
* CFD post-processing
* Velocity-profile comparison
* Separated-flow analysis
* Engineering interpretation

---

## Future Development

Possible extensions include:

* Comparison against experimental benchmark data
* Quantitative reattachment-length comparison
* Pressure-profile comparison
* Turbulent kinetic-energy comparison
* Mesh-sensitivity study
* Near-wall resolution assessment
* Additional turbulence models
