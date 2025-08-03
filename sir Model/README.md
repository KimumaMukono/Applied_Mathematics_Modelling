# SIR Model for COVID-19 Analysis

## Overview
This repository contains a Python implementation of the SIR (Susceptible-Infected-Removed) model for analyzing the dynamics of infectious diseases, with a focus on the COVID-19 pandemic. The model is designed to introduce economists and researchers to quantitative modeling of disease spread, particularly to study the impact of suppression through social distancing.

The code is adapted from a Jupyter Notebook originally developed in Google Colab, available [here](https://colab.research.google.com/drive/17pAtBn8OYurXglxpibEiEcvyYyzd5NgK). It draws inspiration from:
- [NBER Working Paper No. 26867](https://www.nber.org/papers/w26867)
- [COVID-19 Working Papers and Code](https://sites.google.com/site/andyatkeson/home?authuser=0)

## Model Description
The SIR model divides a population into three compartments:
- **Susceptible (S)**: Individuals who can contract the disease.
- **Infected (I)**: Individuals who are currently infected and can spread the disease.
- **Recovered (R)**: Individuals who have recovered and gained immunity.

The dynamics are governed by the following ordinary differential equations:
```
dS/dt = -βSI
dI/dt = βSI - γI
dR/dt = γI
```
Where:
- `β` (beta) is the infection rate.
- `γ` (gamma) is the recovery rate.

The model is implemented using the `cpyment` library to simulate and analyze disease spread, including sensitivity analysis through gradient computations.

## Features
- Simulates SIR model dynamics with customizable parameters (`β`, `γ`).
- Visualizes population dynamics (Susceptible, Infected, Recovered) over time.
- Computes gradients to analyze the sensitivity of the model to changes in parameters like `β`.
- Generates plots with error bands to show the impact of parameter variations.

## Requirements
To run the code, install the following Python packages:
```bash
pip install numpy matplotlib cpyment
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/KimumaMukono/Applied_Mathematics_Modelling
   cd sir-Model
   ```
2. Open the Jupyter Notebook `The SIR model.ipynb` in a Jupyter environment.
3. Install the required dependencies (see above).
4. Run the notebook cells to simulate the SIR model and visualize results.

## Code Structure
- `The SIR model.ipynb`: Main Jupyter Notebook containing the SIR model implementation, simulations, and visualizations.
- Key parameters:
  - `beta = 3`: Infection rate.
  - `gamma = 1`: Recovery rate.
  - `I0 = 0.02`: Initial fraction of infected population.
- Outputs include plots of population dynamics and sensitivity analysis for the infected population.

## Example Output
The notebook generates:
- A plot showing the percentage of Susceptible, Infected, and Recovered populations over time.
- A sensitivity analysis plot with error bands illustrating how changes in `β` affect the infected population.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for bug reports, feature requests, or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The model is based on work from the [NBER Working Paper No. 26867](https://www.nber.org/papers/w26867).
- Thanks to Andrew Atkeson for providing foundational resources and code at [COVID-19 Working Papers and Code](https://sites.google.com/site/andyatkeson/home?authuser=0).