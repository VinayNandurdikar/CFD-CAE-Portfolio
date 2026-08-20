# RAE2822 Transonic Aerofoil CFD — OpenFOAM

## Overview

This project presents a **2D compressible CFD simulation of the RAE2822 aerofoil** under transonic flow conditions using **OpenFOAM**.

The objective of the exercise was to gain practical experience with compressible external aerodynamics, OpenFOAM meshing, far-field boundary conditions, turbulence modelling, and post-processing of transonic flow features.

The simulation demonstrates acceleration of the flow over the aerofoil, development of a locally supersonic region, and subsequent compression over the upper surface.

> **Project origin:** This is a guided learning project completed as part of the **FlowThermoLab – CFD of High-Speed Aerodynamics** course. Credit for the original tutorial framework and course material belongs to FlowThermoLab and the course instructors. The case was executed, inspected, and post-processed by me to develop practical OpenFOAM and high-speed CFD skills.

---

## Case Summary

| Parameter                     |                         Value |
| ----------------------------- | ----------------------------: |
| Aerofoil                      |                       RAE2822 |
| Flow regime                   |                     Transonic |
| Freestream Mach number        |                        ~0.729 |
| Angle of attack               |                        ~2.31° |
| Freestream velocity magnitude |                    ~233.6 m/s |
| Static pressure               |                    108,988 Pa |
| Freestream temperature        |                     255.556 K |
| Turbulence model              |                       k-ω SST |
| Equation of state             |                   Perfect gas |
| Dynamic viscosity             |              1.63 × 10⁻⁵ Pa·s |
| Mesh size                     |           ~1.52 million cells |
| CFD software                  |                      OpenFOAM |
| Meshing                       | `blockMesh` + `snappyHexMesh` |
| Post-processing               |                      ParaView |

---

## CFD Setup

### Compressible Air Model

Air was modelled as a **perfect gas**, allowing density to vary with pressure and temperature.

This is important for transonic flow because compressibility effects become significant as the local Mach number approaches and exceeds unity.

The thermophysical model uses:

* Perfect-gas equation of state
* `Cp = 1005 J/(kg·K)`
* Dynamic viscosity = `1.63 × 10⁻⁵ Pa·s`
* Prandtl number = `0.72`

---

### Turbulence Model

The simulation uses the **k-ω SST RANS turbulence model**.

The SST model combines the near-wall behaviour of the k-ω formulation with k-ε-like behaviour away from the wall.

It is widely used in external aerodynamic CFD because it performs well in flows involving:

* Adverse pressure gradients
* Boundary-layer development
* Possible flow separation
* High-speed external aerodynamics

---

## Boundary Conditions

The outer computational domain uses OpenFOAM **freestream-type boundary conditions** for the external aerodynamic flow.

The aerofoil surface is treated as a wall.

The general boundary-condition strategy includes:

* Freestream velocity at the far-field boundary
* Freestream pressure treatment
* Freestream temperature treatment
* No-slip velocity at the aerofoil wall
* Zero-gradient pressure at the wall
* Adiabatic wall temperature treatment

The front and back patches are defined as `empty`, making the computational domain effectively **two-dimensional**.

---

## Mesh Generation

The computational mesh was generated using OpenFOAM's **`blockMesh` and `snappyHexMesh` utilities**.

A background computational domain was first created using `blockMesh`.

The RAE2822 aerofoil surface geometry was then incorporated into the domain and `snappyHexMesh` was used to refine and conform the computational mesh around the aerofoil.

The meshing workflow included:

* Creation of the background domain using `blockMesh`
* Import of the aerofoil surface geometry
* Local refinement around the aerofoil
* Progressive refinement of the near-field flow region
* Snapping of the mesh to the aerofoil surface
* Inspection of the final mesh before running the CFD simulation

The final mesh contains approximately **1.52 million cells**.

### Mesh Development

#### Background / Initial Mesh

![Initial mesh](images/0-mesh.jpeg)

#### Intermediate Refinement

![Intermediate mesh refinement](images/1-mesh.jpeg)

#### Further Refinement

![Further mesh refinement](images/2-mesh.jpeg)

#### Final Refined Mesh

![Final refined mesh](images/3-mesh.jpeg)

The mesh becomes progressively finer close to the aerofoil, where large gradients in velocity, pressure, and Mach number are expected.

Using `snappyHexMesh` in this exercise provided practical experience with **surface-based mesh refinement and automated mesh generation for external aerodynamic CFD**.

---

## Mach Number Distribution

![Mach number contour](images/mach.jpeg)

The Mach-number contour shows strong acceleration of the flow over the upper surface of the aerofoil.

Although the incoming flow is approximately **Mach 0.73**, the local flow accelerates to **supersonic conditions** over part of the upper surface.

The flow subsequently undergoes rapid compression.

The coexistence of subsonic and locally supersonic regions is characteristic of **transonic aerofoil flow**.

This is one of the important features of the RAE2822 benchmark case.

---

## Pressure Distribution

![Pressure contour](images/pressure.jpeg)

The pressure contour shows the corresponding static-pressure variation around the aerofoil.

Acceleration over the upper surface results in a reduction in static pressure.

The subsequent compression of the locally supersonic flow creates a strong pressure-recovery region.

The Mach-number and pressure contours together demonstrate the relationship between:

* Flow acceleration
* Compressibility
* Local Mach number
* Static pressure variation
* Transonic compression

---

## Key Learning Outcomes

This project helped me gain practical experience with:

* Setting up **compressible external aerodynamic CFD** in OpenFOAM
* Generating an external aerodynamic mesh using `blockMesh` and `snappyHexMesh`
* Understanding surface-based and local mesh refinement
* Modelling air using a **perfect-gas equation of state**
* Applying OpenFOAM **freestream boundary conditions**
* Using the **k-ω SST turbulence model**
* Understanding transonic flow behaviour around an aerofoil
* Identifying local acceleration from subsonic to supersonic conditions
* Understanding pressure recovery associated with transonic compression
* Post-processing Mach-number and pressure fields in ParaView
* Interpreting the relationship between Mach number and pressure in compressible flow

---

## Possible Future Improvements

The present project is primarily a guided learning and demonstration case.

It can be developed further by adding:

* Surface pressure coefficient (`Cp`) distribution
* Comparison with published RAE2822 experimental data
* Lift coefficient (`Cl`)
* Drag coefficient (`Cd`)
* Residual convergence histories
* Force convergence histories
* Mesh-independence assessment
* Near-wall mesh assessment
* `y+` evaluation
* Comparison of different turbulence models

Adding experimental validation and aerodynamic coefficients would develop this case from a guided tutorial into a more complete **CFD verification and validation study**.

---

## Tools Used

* OpenFOAM
* `blockMesh`
* `snappyHexMesh`
* k-ω SST turbulence model
* Compressible-flow modelling
* Perfect-gas thermodynamics
* ParaView

---
## Full OpenFOAM Case Files

The complete OpenFOAM case archive is stored externally because the full simulation files exceed GitHub's practical file-size limits.

**[Download / View Full RAE2822 OpenFOAM Case – Google Drive](https://drive.google.com/file/d/18MZNIgVt2rFg3jnzK6iIV047KiTyywEh/view?usp=drive_link)**

The archive is provided mainly for **reference and reproducibility**.

The GitHub repository contains the project documentation, mesh-development images, Mach-number contour, pressure contour, and other lightweight project material.

## Acknowledgement

This case was completed while following the **FlowThermoLab CFD of High-Speed Aerodynamics** course.

Credit for the original tutorial, educational material, and course framework belongs to **FlowThermoLab and the respective course instructors**.

This repository entry documents the simulation workflow, CFD concepts, meshing experience, and practical skills developed while completing the exercise.
