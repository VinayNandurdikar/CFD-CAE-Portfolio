# Day 1 — Mesh Generation

**Workshop:** OpenFOAM: Academic Foundations to Industrial Applications  
**Organiser:** FOSSEE, IIT Bombay  
**Practice date:** 23 November 2026  
**Software used:** OpenFOAM v2412 and ParaView

## Objective

Practise mesh generation using blockMesh and snappyHexMesh,
and inspect the resulting meshes in ParaView.

## Exercise 1 — 2D Cavity

Reviewed and practised the blockMesh workflow using a
two-dimensional cavity case.

The supplied blockMeshDict defines:

- A single hexahedral block.
- 20 × 20 × 1 cells.
- Uniform mesh grading.
- movingWall and fixedWalls boundaries.
- empty front and back boundaries for a 2D case.

## Exercise 2 — 3D Particle Mixer

Generated a background mesh and a surface-conforming mesh
for a particle-mixer geometry.

The case contains:

- cold_inlet.stl
- hot_inlet.stl
- outlet.stl
- walls.stl

The meshing workflow covered background mesh generation,
feature extraction, castellation and snapping.

Layer addition is disabled in the current configuration.

## Screenshots

### Mixer background mesh

![Mixer background mesh](<Rectangular background mesh.png>)

### Mixer mesh after snappyHexMesh

![Mixer mesh](<Final mixer mesh.png>)

## What I Learned

- How vertices, blocks and cell counts define a blockMesh mesh.
- How a background mesh supports snappyHexMesh.
- How STL surfaces and feature edges are used during meshing.
- The purpose of castellation and snapping.
- How to inspect mesh edges in ParaView.

## Current Status

The practical meshing exercises have been completed.
Mesh screenshots are included.

Mesh-quality statistics will be added after recording
checkMesh output. Flow simulation results are outside the
current Day 1 submission.

## Files

The cases directory contains the workshop case files used
for these exercises.

## Reference and Credit

Completed by following the workshop organised by
FOSSEE, IIT Bombay. Credit for the original educational
material and tutorial cases belongs to the respective authors.

[Watch Day 1](https://www.youtube.com/watch?v=IXUax2Oc5C0)
