# CFD & CAE Engineering Portfolio

Welcome to my engineering simulation portfolio.

This repository contains selected projects demonstrating my work in **Computational Fluid Dynamics (CFD), OpenFOAM, turbulence modelling, meshing, post-processing, and engineering analysis**.

The current portfolio focuses on practical CFD studies using both standard benchmark cases and complete open-source simulation workflows.

---

## Projects

### 1. Open-Source CFD Analysis of Flow Through a 90° Pipe Elbow

An end-to-end CFD project demonstrating a complete open-source engineering workflow:

**FreeCAD → SALOME → OpenFOAM → ParaView**

The study covers:

* CAD geometry creation
* CFD mesh generation
* OpenFOAM simulation
* Pressure and velocity post-processing
* Engineering interpretation of internal flow through a pipe bend

![Pipe Elbow Pressure Distribution](projects/Open_Source_CFD_Analysis/P.jpg)

**Tools:** FreeCAD · SALOME · OpenFOAM · ParaView

[View Full Project →](projects/Open_Source_CFD_Analysis/README.md)

---

### 2. OpenFOAM Turbulence Model Comparison — k-ε vs k-ω SST

A comparative CFD study using the OpenFOAM **pitzDaily** benchmark to investigate how turbulence-model selection influences predictions in separated turbulent flow.

The study compares:

* k-ε turbulence model
* k-ω SST turbulence model
* Velocity profiles
* Separated-flow behaviour
* Engineering implications of turbulence-model selection

![Turbulence Model Comparison](projects/Turbulence_model_comparison/k-omega%20vs%20k-epsilon.jpg)

**Tools:** OpenFOAM · ParaView · RANS Turbulence Modelling

[View Full Project →](projects/Turbulence_model_comparison/README.md)

---

## Technical Skills Demonstrated

### CFD

* Computational Fluid Dynamics
* Internal-flow analysis
* Turbulent-flow modelling
* RANS turbulence models
* Flow separation and recirculation
* Pressure and velocity analysis

### OpenFOAM

* CFD case setup
* Turbulence-model selection
* Mesh import and preparation
* Simulation execution
* Result interpretation

### Pre-Processing

* FreeCAD
* SALOME
* Geometry preparation
* Mesh generation

### Post-Processing

* ParaView
* Pressure contours
* Velocity-field visualisation
* Velocity-profile comparison
* CFD result interpretation

---

## Engineering Workflow

```text
Geometry
   ↓
Meshing
   ↓
CFD Setup
   ↓
Simulation
   ↓
Post-Processing
   ↓
Engineering Interpretation
```

---

## About This Portfolio

The objective of this repository is to document selected engineering simulation studies with emphasis on:

* Clear CFD methodology
* Reproducible workflows
* Open-source engineering tools
* Physical interpretation of simulation results
* Continuous development of practical CFD skills

Additional CFD and CAE studies will be added as the portfolio develops.

---

## Current Tools

`OpenFOAM` · `ParaView` · `FreeCAD` · `SALOME` · `CFD` · `RANS` · `Turbulence Modelling`

---

## Repository Structure

```text
CFD-CAE-Portfolio/
│
├── README.md
│
└── projects/
    │
    ├── Open_Source_CFD_Analysis/
    │   ├── README.md
    │   ├── Geom.FCStd
    │   ├── Geom-Sweep.step
    │   ├── Mesh_3.unv
    │   ├── P.jpg
    │   ├── U.jpg
    │   └── elb.pvsm
    │
    └── Turbulence_model_comparison/
        ├── README.md
        ├── pitzDaily_eps.7z
        ├── pitzDaily_omega.7z
        └── k-omega vs k-epsilon.jpg
```

---

**More CFD and CAE projects will be added progressively.**
