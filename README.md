# CFD-CAE Portfolio

Welcome to my CFD and CAE portfolio. This repository showcases my engineering simulation projects, including CFD, FEA, numerical methods, parametric studies, automation, and optimisation workflows.

---

# Projects

## 1. CFD Analysis of Flow Through a 90° Pipe Elbow

A complete open-source CFD workflow demonstrating geometry creation, mesh generation, simulation, and post-processing for incompressible flow through a 90° pipe elbow.

**View Full Project Repository**  
https://github.com/VinayNandurdikar/openfoam-elbow-cfd

![Elbow CFD](https://github.com/VinayNandurdikar/openfoam-elbow-cfd/raw/main/P.jpg)

### Skills Demonstrated

- Geometry creation using FreeCAD
- Mesh generation using SALOME
- OpenFOAM simulation setup
- ParaView post-processing
- Pressure-drop analysis
- Engineering interpretation

---

## 2. OpenFOAM Turbulence Model Comparison

Compared k-epsilon and k-omega SST turbulence models using the OpenFOAM pitzDaily benchmark case.

The project demonstrates how turbulence-model selection affects velocity prediction in separated turbulent flow.

### Key Features

- Turbulence model comparison
- Velocity profile analysis
- Engineering interpretation of separated flow
- OpenFOAM simulation workflow
- ParaView post-processing

### Skills Demonstrated

- OpenFOAM
- ParaView
- Turbulence modelling
- CFD post-processing
- Engineering interpretation

### Project Link

[View Project](projects/Turbulence_model_comparison/README.md)

---

## 3. OpenFOAM Automation Project

Automated generation of multiple OpenFOAM cases using Python, followed by batch simulation and dataset extraction for downstream analysis and machine learning.

### Skills Demonstrated

- Python scripting
- OpenFOAM automation
- Parametric case generation
- Batch processing
- Dataset creation
- Scientific computing

### Project Link

[View Project](./04_OpenFOAM_Automation_Project)

---

## 4. ANN-Based Thermal Insulation Design Optimisation

A beginner-friendly artificial neural network project demonstrating how ANN can be used as a surrogate model for engineering design optimisation.

The project trains a small neural network to learn the relationship between insulation thickness and heat loss. The trained ANN is then used to predict heat loss for different candidate thickness values and select the best design under a cost constraint.

### Project Idea

In thermal insulation design:

- Increasing insulation thickness reduces heat loss
- Increasing insulation thickness increases cost
- The goal is to minimise heat loss while keeping cost within an allowed limit

### Workflow

1. Generate simple thermal insulation data
2. Train an ANN to predict heat loss from insulation thickness
3. Use the trained ANN as a surrogate model
4. Test many candidate thickness values
5. Select the best feasible thickness under a cost constraint

### Skills Demonstrated

- Artificial Neural Networks
- PyTorch
- Surrogate modelling
- Engineering design optimisation
- Cost-constrained optimisation
- Python programming
- Scientific computing
- Data visualisation

### Project Link

[View Project](projects/ANN_Thermal_Insulation_Optimisation)

---

## 5. CAE Parametric Optimisation of a Mechanical Bracket

A CAE-based parametric optimisation study of a mechanical bracket, including geometry parameterisation, meshing, deformation analysis, and result comparison.

[View Project Documentation](projects/cae-parametric-optimization-bracket.md)

[View Full Project Repository](https://github.com/VinayNandurdikar/CAE-Parametric-Optimization-Bracket)

### Skills Demonstrated

- CFD and CAE workflow documentation
- Finite Element Analysis, FEA
- Parametric design study
- Engineering optimisation
- Simulation result interpretation

---

## 6. CFD From Scratch using Python

A learning-based CFD project where I implement fundamental numerical methods from scratch using Python.

The project starts with finite difference methods and gradually builds toward solving basic CFD equations.

[View Project Documentation](CFD_From_Scratch/README.md)

[View Full Project Folder](CFD_From_Scratch)

### Skills Demonstrated

- Python programming for engineering applications
- Finite Difference Method, FDM
- Numerical solution of partial differential equations, PDEs
- Scientific computing using NumPy and Matplotlib
- CFD fundamentals and discretisation techniques
- Engineering data visualisation
