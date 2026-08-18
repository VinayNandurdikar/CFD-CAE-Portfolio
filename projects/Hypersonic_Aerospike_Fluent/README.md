# Hypersonic Aerospike CFD — Mach 6.06

A 2D axisymmetric CFD study of hypersonic flow over a spiked blunt body using **ANSYS Fluent 2022 R1**.

The study is based on the **Model 1 aerospike benchmark** reported by Roveda (AIAA 2009-367) and was carried out while learning high-speed CFD through the **Flowthermolab – CFD of High-Speed Aerodynamics** course.

The main focus of this project was not only obtaining the flow solution, but understanding the modelling and numerical choices required for a stable Mach 6 compressible-flow simulation.

---

## Benchmark Conditions

The freestream conditions used were:

| Parameter          |   Value |
| ------------------ | ------: |
| Mach number        |    6.06 |
| Static pressure    | 1951 Pa |
| Static temperature | 58.25 K |
| Angle of attack    |      0° |

---

## CFD Setup

**Software:** ANSYS Fluent 2022 R1

| Setting             | Selection              |
| ------------------- | ---------------------- |
| Simulation          | Steady                 |
| Solver              | Density-Based Implicit |
| Space               | 2D Axisymmetric        |
| Energy Equation     | Enabled                |
| Turbulence Model    | SST k-ω                |
| Density             | Ideal Gas              |
| Viscosity           | Sutherland             |
| Operating Pressure  | 0 Pa                   |
| Freestream Boundary | Pressure Far Field     |
| Courant Number      | 0.1                    |

### Mesh

The current Fluent report contains approximately:

* **248,405 cells**
* **504,133 faces**
* **255,729 nodes**

The mesh was refined around the aerospike and forebody where strong gradients and shock structures are expected.

Adaptive Mesh Refinement (AMR) was also used during the solution workflow to increase resolution in important flow regions without uniformly refining the complete domain.

---

## Key Modelling Choices

### Axisymmetric Formulation

The geometry is a body of revolution at zero angle of attack, so a **2D axisymmetric** model was used.

The centreline was defined using an **Axis** boundary rather than a normal symmetry boundary.

This retains the axisymmetric form of the governing equations while greatly reducing computational cost compared with a full 3D simulation.

### Ideal-Gas Density

At Mach 6, density changes significantly because of large pressure and temperature variations.

Therefore air was modelled as an **ideal gas** rather than using constant density.

### Sutherland Viscosity

The viscosity of air changes with temperature.

Because hypersonic flows contain large temperature variations, **Sutherland's law** was used instead of a constant viscosity value.

### Operating Pressure

The operating pressure was set to:

```text
0 Pa
```

This allowed the specified freestream pressure of **1951 Pa** to be treated directly as the required pressure for the compressible-flow calculation.

### Pressure Far-Field Boundary

The project was also my first practical use of a **Pressure Far-Field** boundary condition for external compressible CFD.

The freestream was defined using:

```text
Mach Number       = 6.06
Static Pressure   = 1951 Pa
Static Temperature = 58.25 K
```

---

## Solver Divergence and Stabilisation

One of the main learning outcomes of this project was troubleshooting solver divergence.

The initial turbulent calculation became unstable within only a few iterations. Fluent reported:

* excessive temperature changes,
* pressure and temperature limiting,
* turbulent-viscosity limiting,
* divergence in the `omega` AMG solver,
* and finally a floating-point exception.

The solution was stabilised using a more gradual approach.

### Step 1 — Reduce CFL

The density-based Courant number was reduced to:

```text
CFL = 0.1
```

This made the pseudo-time advancement less aggressive.

### Step 2 — Start Laminar

The flow was initially solved without the turbulence model.

This allowed the principal compressible-flow and shock structure to develop before introducing the additional turbulence equations.

### Step 3 — Activate SST k-ω

After obtaining a stable mean-flow solution, the **SST k-ω turbulence model** was enabled.

The turbulent calculation then remained stable.

This demonstrated the importance of **initialisation and continuation strategies** in difficult high-speed CFD simulations.

---

## Current Results

The current project contains:

* Density contour
* Residual history
* Drag-monitor history
* Fluent simulation report

The density contour already shows strong density variations associated with the hypersonic flow around the aerospike and blunt body.

Additional visualisations such as:

* Mach number,
* static pressure,
* static temperature,
* Schlieren / density-gradient plots,
* and detailed shock structures

can be added in future post-processing.

---

## Current Status

The calculation is currently presented as a **benchmark reproduction and learning study**.

The solver has been stabilised successfully, but the current Fluent report does **not yet satisfy the specified residual convergence criteria**.

Further work will include:

* continuing convergence assessment,
* checking engineering monitors,
* producing Mach and pressure contours,
* generating Schlieren visualisation,
* examining AMR regions,
* checking mesh independence,
* and comparing the predicted flow structures with the published benchmark.

A drag coefficient is intentionally not reported at this stage because the aerodynamic reference values still require verification.

---

## Key Learning Outcomes

This study provided practical experience with:

* Hypersonic compressible CFD
* Density-based solvers
* 2D axisymmetric modelling
* Axis vs symmetry boundary conditions
* Pressure far-field boundaries
* Ideal-gas density
* Sutherland viscosity
* Operating-pressure selection
* Courant-number control
* Solver-divergence diagnosis
* Laminar-to-turbulent solution initialisation
* SST k-ω turbulence modelling
* Adaptive Mesh Refinement
* Shock-flow post-processing

---

## Acknowledgement

This study was carried out while following the **Flowthermolab – CFD of High-Speed Aerodynamics** course.

The course provided the learning framework for high-speed CFD concepts. The simulation setup, troubleshooting, post-processing and documentation shown here represent my implementation of the benchmark exercise.

---

## Reference

Roveda, R., *Benchmark CFD Study of Spiked Blunt Body Configurations*, AIAA 2009-367, 47th AIAA Aerospace Sciences Meeting, 2009.

---

## Tools

`ANSYS Fluent` · `Hypersonic CFD` · `Compressible Flow` · `Density-Based Solver` · `SST k-ω` · `AMR` · `Axisymmetric CFD`
