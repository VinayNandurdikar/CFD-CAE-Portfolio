# Flow past a cylinder: learning lift, pressure and FFT

**ANSYS Fluent learning project · Work in progress**

I ran a two-dimensional simulation of air flowing past a circular cylinder. I wanted to answer two questions: **Does the flow produce a repeating force on the cylinder? At what frequency does it repeat?** I recorded the cylinder's lift and the pressure at a point behind it, then looked at both signals over time and with an FFT.

The lift and pressure signals do repeat. In the windows I checked, the pressure signal repeats about twice as often as the lift signal. However, the lift frequency changed noticeably as I continued the simulation with different numerical settings. **I cannot yet present one validated shedding frequency or Strouhal number for this case.**

## What I did, step by step

1. **Set up the flow.** I used a 0.1 m diameter cylinder with air entering at 0.02 m/s. The flow was modelled as transient and laminar in Fluent. The original report records a mesh of 60,238 cells. These inputs give a Reynolds number of about 137.
2. **Recorded two signals every time step.** Lift is the force acting across the flow direction on the cylinder. The pressure monitor measures the changing pressure at one point in its wake.
3. **Looked at the signals against time.** A repeating rise and fall in lift suggested a repeating wake pattern. I used the time between similar lift peaks to estimate its period.
4. **Used FFT to check which frequencies were present.** FFT turns a time history into a plot of signal strength against frequency. I selected later parts of each run so that the initial flow development did not dominate the plots. Each selected part has one constant time-step size; I did not mix different time steps in one FFT.
5. **Compared lift with pressure.** The pressure peak was close to twice the lift frequency in each selected window. Comparing the two signals helped me interpret the pressure peak; the pressure plot alone would not establish its cause.
6. **Checked the numerical result.** Around flow time 1340 s, the inlet and outlet mass-flow rates were approximately equal in magnitude. I also compared results after changing the time step and later the time-integration scheme. Their frequencies did not agree closely enough to claim an independent numerical result.

## A simple example from the final run

Two similar lift peaks were about **44.2 seconds** apart. This is one period, so the estimated lift frequency is:

```text
frequency = 1 / period = 1 / 44.2 s ≈ 0.0226 Hz
```

That means roughly **one lift cycle every 44.2 seconds**. The pressure signal was around **0.0453 Hz**, approximately twice as frequent. This relationship belongs to the pressure probe used here; it should not be applied automatically to every pressure probe.

The FFT shows frequencies in discrete steps. A 200 s window has a spacing of about **1 / 200 = 0.005 Hz** between frequency bins. A plotted FFT peak at 0.025 Hz therefore does not prove that the physical frequency is exactly 0.025 Hz. This is why I also looked at peak spacing in the lift time history.

![Lift signals in the four analysis windows](figures/lift_histories.png)

![Frequency plots of lift and pressure](figures/frequency_spectra.png)

The figures above were made from the exported monitor data. The frequency plots use a Hann window, remove a linear trend, and are normalized for comparison. Their peak positions may differ slightly from the supplied Fluent screenshots. Their heights are **not** force or pressure amplitudes in physical units.

## What changed across the runs?

| Selected flow-time window | Time step | Time scheme | Approximate lift period | Approximate lift frequency |
| --- | ---: | --- | ---: | ---: |
| 621.1–890.2 s | 0.1 s | First Order Implicit | 27.0 s | 0.0371 Hz |
| 900–1090 s | 0.05 s | First Order Implicit | 32.0 s | 0.0312 Hz |
| 1140–1340 s | 0.025 s | First Order Implicit | 38.6 s | 0.0259 Hz |
| 1390–1590 s | 0.025 s | Second Order Implicit | 44.2 s | 0.0226 Hz |

These are **successive continuations of one simulation**. They do not isolate the effect of the time step: each window also occurs later in the flow history, and the final continuation changes the time scheme. The mesh has not been checked for its effect on frequency. The numbers in this table describe the observed windows, **not four validated answers**.

## What I learned and why it is useful

- A time plot shows *when* a signal changes; an FFT shows *which repeating frequencies* contribute to it.
- The duration of the selected data window limits how closely an FFT can separate nearby low frequencies.
- Lift and wake pressure can have different dominant frequencies. It helps to compare signals before naming an FFT peak as the shedding frequency.
- A numerically converged time step or good mass balance alone does not show that a predicted frequency is independent of the time step and mesh.

Frequency analysis is useful when unsteady flow produces repeating loads or pressure fluctuations, for example around tubes, bluff components, and parts in piping systems. The frequency can then be compared with a structure's natural frequencies as part of a **separate vibration assessment**. This cylinder exercise is a way to practise that analysis; it does not predict vibration or fatigue in an actual component.

## What I would do next

Save one common Fluent case-and-data checkpoint and start comparison runs from it. Keep the mesh, boundary conditions, time scheme, inner-iteration settings and analysis duration the same; change **only the time step**. After comparing settled lift periods, repeat with a different mesh. I would compare with a published cylinder benchmark only after these checks.

## Files in this project

- `data/`: lift and pressure CSV files for each constant-time-step window.
- `figures/`: the two comparison plots and renamed screenshots of the Fluent FFT displays.
- `raw/fluent_monitor_snapshots/`: the original Fluent lift and pressure monitor exports, renamed to distinguish the runs.
- `report/original_fluent_simulation_report.pdf`: the baseline Fluent report. It does not document all later continuations.

The original Fluent case-and-data files were not supplied with this repository.
