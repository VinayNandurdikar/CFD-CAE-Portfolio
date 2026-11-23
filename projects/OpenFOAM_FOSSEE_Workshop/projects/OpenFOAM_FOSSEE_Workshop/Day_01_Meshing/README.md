# Day 1 — Mesh Generation with blockMesh and snappyHexMesh

**Workshop:** OpenFOAM: Academic Foundations to Industrial Applications  
**Organiser:** FOSSEE, IIT Bombay  
**Practice date:** 23 November 2026  
**Software used:** OpenFOAM v2412 and ParaView  
**Project type:** Guided workshop exercise

## Objective

Practise two OpenFOAM meshing workflows:

- Structured mesh generation for a 2D cavity using blockMesh.
- Surface-conforming mesh generation for a 3D particle mixer
  using snappyHexMesh.

Inspect the resulting meshes in ParaView and develop an
understanding of the case files and meshing controls.

## Exercise 1 — 2D Cavity Using blockMesh

Practised the blockMesh workflow using the supplied
two-dimensional cavity case.

### Mesh Definition

| Parameter | Configuration |
|---|---|
| Block type | Single hexahedral block |
| Cell divisions | 20 × 20 × 1 |
| Number of cells defined | 400 |
| Mesh grading | Uniform: simpleGrading (1 1 1) |
| Domain dimensions after scaling | 0.1 × 0.1 × 0.01 m |
| Upper boundary | movingWall, type wall |
| Side and lower boundaries | fixedWalls, type wall |
| Front and back boundaries | frontAndBack, type empty |

The mesh uses one cell through its thickness. The front and
back patches are defined as empty for a two-dimensional case.

### Concepts Practised

- Defining geometry through vertex coordinates.
- Connecting vertices to form a hexahedral block.
- Specifying cell divisions in each direction.
- Understanding uniform mesh grading.
- Assigning block faces to boundary patches.
- Understanding the role of empty patches in a 2D case.

### Case Download

[Download the 2D cavity case](BlockMesh-2D-Cavity.zip)

## Exercise 2 — 3D Particle Mixer Using snappyHexMesh

Generated a background mesh and a surface-conforming mesh
for the supplied particle-mixer geometry.

### Geometry

The geometry is supplied through four STL files:

| Surface file | Region |
|---|---|
| cold_inlet.stl | Cold inlet |
| hot_inlet.stl | Hot inlet |
| outlet.stl | Outlet |
| walls.stl | Mixer walls |

These names identify the geometry regions. Boundary types
and flow conditions must be reviewed before any flow simulation.

### Background Mesh

The supplied blockMeshDict defines a rectangular background
domain enclosing the mixer geometry.

| Parameter | Configuration |
|---|---|
| Cell divisions | 152 × 116 × 84 |
| Background cell count defined | 1,481,088 |
| Mesh grading | Uniform |
| Purpose | Starting mesh for snappyHexMesh |

This is the background mesh count, not the final mixer mesh count.

### snappyHexMesh Configuration

| Stage | Setting |
|---|---|
| Castellation | Enabled |
| Snapping | Enabled |
| Layer addition | Disabled |
| Explicit feature snapping | Enabled |

The meshing process uses the background mesh, STL geometry
and extracted feature edges to produce a mesh that conforms
to the mixer surfaces.

### Workflow Practised

1. Generate the rectangular background mesh using blockMesh.
2. Extract surface feature edges.
3. Run snappyHexMesh with castellation and snapping enabled.
4. Open the generated mesh in ParaView.
5. Inspect the mesh using Surface With Edges.

### Case Download

[Download the 3D particle-mixer case](SnappyHexMesh-3D-ParticleMixer.zip)

## Mesh Screenshots

### Mixer Background Mesh — blockMesh

The rectangular mesh below is the background mesh used for
the particle-mixer exercise.

![Mixer background mesh](<Rectangular background mesh.png>)

### Mixer Mesh — snappyHexMesh

The image below shows the mesh following the mixer geometry
after castellation and snapping.

![Mixer mesh after snappyHexMesh](<Final mixer mesh.png>)

## What I Learned

Through these exercises, I practised:

- Reading and editing OpenFOAM meshing dictionaries.
- Understanding vertices, blocks and cell divisions.
- Defining boundary patches.
- Distinguishing a 2D cavity mesh from a 3D background mesh.
- Understanding why snappyHexMesh needs a background mesh.
- Using STL surfaces and feature edges during meshing.
- Understanding the purpose of castellation and snapping.
- Inspecting mesh edges and geometry conformity in ParaView.

## Verification and Current Limitations

The practical meshing exercises have been completed, and
screenshots and case archives are included.

The following items remain to be documented:

- checkMesh output for the generated meshes.
- Final mixer cell count.
- Mesh non-orthogonality and skewness.
- Any failed mesh-quality checks and their resolution.
- A separate screenshot of the 2D cavity mesh.

Visual inspection provides evidence of mesh generation.
Mesh quality has not yet been established in this documentation.

No flow, thermal-mixing or particle-tracking results are
presented in this Day 1 entry.

## Possible Further Practice

- Change the cavity mesh from 20 × 20 × 1 to 40 × 40 × 1.
- Compare the cell count and mesh appearance.
- Explore non-uniform grading in the cavity.
- Investigate how changing the mixer background cell size
  affects the final mesh and meshing time.

These are proposed extensions and have not yet been completed.

## Files Included

- [2D cavity case archive](BlockMesh-2D-Cavity.zip)
- [3D particle-mixer case archive](SnappyHexMesh-3D-ParticleMixer.zip)
- [Mixer background mesh screenshot](<Rectangular background mesh.png>)
- [Mixer mesh screenshot](<Final mixer mesh.png>)

## Reference and Acknowledgement

Completed by following the workshop
“OpenFOAM: Academic Foundations to Industrial Applications”,
organised by FOSSEE, IIT Bombay.

Credit for the original educational material, geometry and
tutorial cases belongs to the respective authors and instructors.
This page records my practical work and learning.

[Watch the Day 1 workshop recording](https://www.youtube.com/watch?v=IXUax2Oc5C0)

---

[Return to workshop overview](../../../README.md)

[Return to main portfolio](../../../../../README.md)
