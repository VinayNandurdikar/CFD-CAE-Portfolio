# 1D Steady-State Heat Conduction using Python

## Objective

This project solves the 1D steady-state heat conduction equation using the finite difference method in Python.

## Governing Equation

d²T/dx² = 0

## Boundary Conditions

- T(0) = 0
- T(1) = 1

## Numerical Method

The domain is divided into 11 grid points.

Each interior point is updated using:

T_new[i] = 0.5 * (T[i-1] + T[i+1])

The solution is iterated until the numerical error is less than 1e-8.

## Tools Used

- Python
- NumPy
- Matplotlib

## Expected Result

The final temperature distribution is a straight line from 0 to 1.

## Key Learning

This project demonstrates:
- Grid generation
- Boundary conditions
- Finite difference discretization
- Iterative convergence
- Plotting

## Status

Completed as part of my CFD from Scratch using Python learning track.
