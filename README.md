# CFD & CAE Engineering Portfolio

Welcome to my engineering simulation portfolio.

This repository contains selected projects demonstrating practical experience in **Computational Fluid Dynamics (CFD), compressible and incompressible flow, turbulence modelling, meshing, numerical simulation, post-processing, and engineering analysis**.

The portfolio includes both **open-source CFD workflows** and **ANSYS Fluent simulations**, with emphasis on understanding the physical problem, selecting appropriate numerical models, troubleshooting solver behaviour, and interpreting simulation results.

---

# Projects

## 1. Open-Source CFD Analysis of Flow Through a 90° Pipe Elbow

An end-to-end CFD project demonstrating a completely open-source engineering workflow:

**FreeCAD → SALOME → OpenFOAM → ParaView**

The project includes:

* CAD geometry creation
* CFD mesh generation
* OpenFOAM simulation setup
* Pressure and velocity post-processing
* Flow development through a 90° bend
* Engineering interpretation of internal-flow behaviour

![Pipe Elbow Pressure Distribution](projects/Open_Source_CFD_Analysis/P.jpg)

**Tools:** FreeCAD · SALOME · OpenFOAM · ParaView

[View Full Project →](projects/Open_Source_CFD_Analysis/README.md)

---

## 2. OpenFOAM Turbulence Model Comparison — k-ε vs k-ω SST

A comparative CFD study using the OpenFOAM **pitzDaily** benchmark to investigate the influence of turbulence-model selection on separated turbulent flow.

The study compares:

* k-ε turbulence model
* k-ω SST turbulence model
* Velocity distributions
* Flow separation and recirculation
* Differences in model predictions
* Engineering implications of turbulence-model selection

![Turbulence Model Comparison](projects/Turbulence_model_comparison/k-omega%20vs%20k-epsilon.jpg)

**Tools:** OpenFOAM · ParaView · RANS Turbulence Modelling

[View Full Project →](projects/Turbulence_model_comparison/README.md)

---

## 3. Hypersonic Aerospike CFD — Mach 6.06

A **2D axisymmetric hypersonic CFD benchmark study** of flow over a spiked blunt body using **ANSYS Fluent**.

The simulation reproduces the freestream conditions of the Model 1 aerospike benchmark:

* **Mach number:** 6.06
* **Static pressure:** 1951 Pa
* **Static temperature:** 58.25 K

The project focuses on the practical numerical considerations required for stable high-speed compressible CFD.

Key aspects include:

* Density-based implicit solver
* 2D axisymmetric formulation
* Pressure far-field boundary conditions
* Ideal-gas density
* Sutherland temperature-dependent viscosity
* SST k-ω turbulence modelling
* Courant-number control
* Solver-divergence diagnosis
* Laminar-to-turbulent solution initialisation
* Adaptive Mesh Refinement (AMR)
* Residual and aerodynamic-monitor assessment

![Hypersonic Aerospike Density Contour](projects/Hypersonic_Aerospike_Fluent/Density.PNG)

An important part of this study was troubleshooting an initially diverging Mach 6 solution. A stable solution procedure was obtained by reducing the Courant number to **0.1**, establishing the compressible flow field first with a laminar calculation, and subsequently activating the SST k-ω turbulence model.

The project is presented as a **benchmark reproduction and guided learning study**, with additional quantitative validation and post-processing planned.

> This project was completed as part of the **FlowThermoLab – CFD of High-Speed Aerodynamics** course. Credit for the original educational material and tutorial framework belongs to FlowThermoLab and the respective course instructors.

**Tools:** ANSYS Fluent · Hypersonic CFD · Compressible Flow · SST k-ω · AMR

[View Full Project →](projects/Hypersonic_Aerospike_Fluent/README.md)

---

## 4. RAE2822 Transonic Aerofoil CFD — OpenFOAM

A **2D compressible external-aerodynamics simulation** of the RAE2822 aerofoil under transonic flow conditions using **OpenFOAM**.

The case uses a freestream Mach number of approximately **0.73** and demonstrates acceleration of the flow from subsonic to locally supersonic conditions over the aerofoil, followed by rapid compression.

Key aspects include:

* Compressible external aerodynamics
* Perfect-gas modelling
* k-ω SST turbulence model
* OpenFOAM freestream boundary conditions
* `blockMesh` background-domain generation
* `snappyHexMesh` surface-conforming meshing
* Local mesh refinement around the aerofoil
* Approximately **1.52 million computational cells**
* Mach-number and pressure-field post-processing
* Interpretation of transonic acceleration and compression

![RAE2822 Mach Number](projects/RAE2822_Transonic_OpenFOAM/images/mach.jpeg)

The project also provided practical experience with the OpenFOAM meshing workflow, including creation of a background mesh using `blockMesh` and refinement and snapping of the computational mesh around the aerofoil using `snappyHexMesh`.

> This is a **guided learning project** completed as part of the **FlowThermoLab – CFD of High-Speed Aerodynamics** course. Credit for the original tutorial framework and educational material belongs to FlowThermoLab and the course instructors.

**Tools:** OpenFOAM · `blockMesh` · `snappyHexMesh` · k-ω SST · Compressible Flow · ParaView

[View Full Project →](projects/RAE2822_Transonic_OpenFOAM/README.md)

---

## 5. 3D Fighter Aircraft External Aerodynamics — OpenFOAM

A **3D compressible external-aerodynamics simulation** of a fighter-aircraft geometry using **OpenFOAM**.

This project extends the CFD workflow from two-dimensional aerofoil analysis to a complete three-dimensional aircraft configuration and focuses particularly on complex 3D meshing using `snappyHexMesh`.

Key aspects include:

* Full 3D fighter-aircraft STL geometry
* Compressible steady-state CFD using `rhoSimpleFoam`
* k-ω SST turbulence modelling
* Perfect-gas air model
* Freestream Mach number of approximately **0.73**
* Angle of attack of approximately **2.79°**
* `blockMesh` background-domain generation
* Feature extraction using `surfaceFeatureExtract`
* `snappyHexMesh` surface-conforming meshing
* Explicit feature-edge refinement
* Three nested volumetric refinement regions
* Boundary-layer mesh generation
* Approximately **3.31 million computational cells**
* Parallel decomposition into **32 subdomains**
* 3D Mach-number post-processing in ParaView

![3D Fighter Aircraft Mach Number](projects/3D_Fighter_Aircraft_OpenFOAM/images/m.jpeg)

A lightweight OpenFOAM case is included in the repository so that the case setup and meshing workflow can be inspected and the mesh regenerated without storing the full generated 3.31-million-cell mesh.

> This is a **guided learning project** completed as part of the **FlowThermoLab – CFD of High-Speed Aerodynamics** course. Credit for the original tutorial framework and educational material belongs to FlowThermoLab and the respective course instructors.

**Tools:** OpenFOAM · `rhoSimpleFoam` · `blockMesh` · `snappyHexMesh` · `surfaceFeatureExtract` · k-ω SST · Compressible RANS · Parallel CFD · ParaView

[View Full Project →](projects/3D_Fighter_Aircraft_OpenFOAM/README.md)

[Download Clean OpenFOAM Case →](projects/3D_Fighter_Aircraft_OpenFOAM/3D_Fighter_Aircraft_OpenFOAM_CleanCase.zip)

---

# Technical Skills Demonstrated

## Computational Fluid Dynamics

* Internal and external flow simulation
* 2D and 3D CFD
* Incompressible and compressible CFD
* Transonic and hypersonic aerodynamics
* Steady-state simulations
* Flow separation and recirculation
* Shock and compression-flow physics
* Pressure and velocity analysis
* Numerical convergence assessment
* Solver troubleshooting and stabilisation
* Engineering interpretation of CFD results

## Turbulence Modelling

* Reynolds-Averaged Navier–Stokes (RANS)
* k-ε turbulence model
* k-ω SST turbulence model
* Turbulence-model comparison
* Turbulence initialisation
* Separated turbulent flows
* Near-wall aerodynamic modelling

## High-Speed CFD

* Compressible-flow modelling
* Transonic aerodynamics
* Hypersonic aerodynamics
* Density-based compressible solvers
* Compressible pressure-based OpenFOAM solvers
* Axisymmetric CFD
* 3D external aerodynamics
* Pressure far-field / freestream boundary conditions
* Perfect-gas modelling
* Temperature-dependent viscosity using Sutherland's law
* Courant-number control
* Shock-containing and compression flows
* Adaptive Mesh Refinement

## OpenFOAM

* CFD case setup
* `blockMesh`
* `snappyHexMesh`
* `surfaceFeatureExtract`
* STL surface geometry import
* Explicit feature refinement
* Surface refinement
* Nested volumetric refinement
* Boundary-layer mesh generation
* Freestream boundary conditions
* Thermophysical-property configuration
* Turbulence-model selection
* Compressible-flow simulation
* `rhoSimpleFoam`
* Parallel domain decomposition
* Simulation execution
* Result interpretation

## ANSYS Fluent

* Density-based implicit solver
* Compressible-flow setup
* Axisymmetric modelling
* Energy equation
* SST k-ω turbulence
* Pressure far-field boundaries
* Adaptive Mesh Refinement
* Solver monitoring
* Convergence troubleshooting
* Density and aerodynamic-result post-processing

## CAD & Meshing

* FreeCAD
* SALOME
* STL geometry preparation
* OpenFOAM `blockMesh`
* OpenFOAM `snappyHexMesh`
* Feature-edge extraction
* Geometry preparation
* CFD mesh generation
* Boundary identification
* Surface-based refinement
* Local mesh refinement
* Nested 3D refinement regions
* Boundary-layer generation

## Post-Processing

* ParaView
* ANSYS Fluent
* Pressure contours
* Velocity visualisation
* Mach-number contours
* Density contours
* 3D flow-field visualisation
* Residual monitoring
* Aerodynamic-monitor plots
* CFD result interpretation

---

# Engineering Workflow

The projects in this portfolio generally follow the engineering simulation workflow:

```text
Problem Definition
        ↓
Geometry Preparation
        ↓
Meshing
        ↓
Mesh Quality Assessment
        ↓
Physics & Boundary Conditions
        ↓
Solver Setup
        ↓
Simulation
        ↓
Convergence Assessment
        ↓
Post-Processing
        ↓
Engineering Interpretation
