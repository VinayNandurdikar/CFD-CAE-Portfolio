# RAE2822 Transonic Aerofoil CFD — OpenFOAM

## Overview

This project demonstrates a **2D compressible CFD simulation of the RAE2822 aerofoil** under transonic flow conditions using **OpenFOAM**.

The objective was to develop practical experience with compressible external aerodynamics, OpenFOAM meshing, far-field boundary conditions, turbulence modelling, and post-processing of transonic flow features.

The simulation captures acceleration of the flow over the aerofoil and the development of locally supersonic flow followed by compression across the upper surface.

> **Project origin:** This is a guided learning project completed as part of the **FlowThermoLab – CFD of High-Speed Aerodynamics** course. The tutorial framework and learning material are credited to FlowThermoLab. The case was executed, inspected and post-processed by me as part of developing practical OpenFOAM and high-speed CFD skills.

---

## Case

| Parameter                     |               Value |
| ----------------------------- | ------------------: |
| Aerofoil                      |             RAE2822 |
| Flow regime                   |           Transonic |
| Freestream Mach number        |              ~0.729 |
| Angle of attack               |              ~2.31° |
| Freestream velocity magnitude |          ~233.6 m/s |
| Static pressure               |          108,988 Pa |
| Freestream temperature        |           255.556 K |
| Turbulence model              |             k-ω SST |
| Equation of state             |         Perfect gas |
| Dynamic viscosity             |    1.63 × 10⁻⁵ Pa·s |
| Mesh size                     | ~1.52 million cells |
| CFD software                  |            OpenFOAM |
| Post-processing               |            ParaView |

---

## CFD Setup

### Compressible Air

Air was modelled as a **perfect gas**, allowing density to vary with pressure and temperature. This is necessary for transonic flow where compressibility effects become significant.

The thermophysical model uses:

* Perfect-gas equation of state
* (C_p = 1005) J/(kg·K)
* Dynamic viscosity = (1.63\times10^{-5}) Pa·s
* Prandtl number = 0.72

### Turbulence Model

The simulation uses the **k-ω SST RANS turbulence model**.

The SST model combines the near-wall behaviour of the k-ω formulation with k-ε-like behaviour away from the wall and is widely used for external aerodynamic flows involving adverse pressure gradients and possible flow separation.

### Boundary Conditions

The outer domain uses OpenFOAM **freestream boundary conditions** for velocity, pressure and temperature.

The aerofoil surface is defined as:

* No-slip wall for velocity
* Zero-gradient pressure
* Adiabatic wall for temperature

The front and back surfaces are defined as `empty`, making the case effectively **two-dimensional**.

---

## Mesh

The aerofoil was meshed using OpenFOAM meshing tools with local refinement around the aerofoil surface.

The final mesh contains approximately **1.52 million cells**, with considerably finer resolution near the aerofoil compared with the far-field region.

![Mesh](images/mesh.jpeg)

Local refinement is important in this case because strong gradients in velocity, pressure and Mach number occur close to the aerofoil and particularly around transonic compression regions.

---

## Mach Number

![Mach Number](images/mach_contour.jpeg)

The Mach-number contour shows acceleration of the flow over the aerofoil upper surface.

Although the incoming flow is approximately **Mach 0.73**, the local flow accelerates to **supersonic conditions** over part of the upper surface before undergoing rapid compression.

This coexistence of subsonic and locally supersonic regions is characteristic of **transonic aerofoil flow**.

---

## Pressure

![Pressure](images/pressure_contour.jpeg)

The pressure contour shows the corresponding pressure variation around the aerofoil.

Acceleration over the upper surface produces a reduction in static pressure. The subsequent compression of the locally supersonic flow creates a strong pressure recovery region.

The relationship between the Mach and pressure contours illustrates the coupling between flow acceleration and pressure variation in compressible aerodynamics.

---

## Key Learning Outcomes

This project helped me gain practical experience with:

* Setting up **compressible external aerodynamic CFD** in OpenFOAM
* Using a **perfect-gas thermodynamic model**
* Applying OpenFOAM **freestream boundary conditions**
* Understanding the role of the **k-ω SST turbulence model**
* Generating and inspecting locally refined meshes
* Understanding **transonic acceleration and compression**
* Post-processing Mach-number and pressure fields in ParaView
* Interpreting the relationship between Mach number and pressure in high-speed flows

---

## Possible Future Improvements

The current project is primarily a learning and demonstration case. Future extensions could include:

* Surface pressure coefficient (C_p) extraction
* Comparison with published RAE2822 experimental data
* Lift and drag coefficient evaluation
* Residual and force convergence monitoring
* Mesh-independence assessment
* Near-wall resolution and (y^+) assessment
* Comparison of turbulence models

These additions would allow the case to be developed from a guided tutorial into a more complete **CFD verification and validation study**.

---

## Acknowledgement

This case was completed while following the **FlowThermoLab CFD of High-Speed Aerodynamics course**. Credit for the original tutorial and educational material belongs to FlowThermoLab and the respective course instructors.

The project is included here to document the CFD workflow, simulation experience and technical concepts learned during the exercise.

