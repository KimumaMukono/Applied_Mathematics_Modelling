# Double Pendulum Simulation

## Overview
This repository contains a Python script that simulates and animates the motion of a double pendulum using numerical integration and Matplotlib. The double pendulum is a classic example of a chaotic dynamical system, where small changes in initial conditions can lead to significantly different outcomes. The code is adapted from a C implementation available at [http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c](http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c).

The simulation uses Euler's method to solve the system of ordinary differential equations (ODEs) governing the double pendulum's motion and visualizes the results as an animation, including the pendulum's trajectory trace. The output is generated using `matplotlib.animation.Animation.to_jshtml`.

## Features
- Simulates the motion of a double pendulum with customizable parameters (masses, lengths, initial angles, and velocities).
- Animates the pendulum's motion, showing the positions of both pendulum masses and a trace of the second pendulum's path.
- Displays the simulation time in the animation.
- Uses Euler's method for numerical integration (with a note on using `scipy.integrate.solve_ivp` for more accuracy).

## Requirements
To run the simulation, install the following Python packages:
```bash
pip install numpy matplotlib
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/KimumaMukono/Applied_Mathematics_Modelling/double-pendulum.git
   cd double-pendulum
   ```
2. Ensure the required dependencies are installed (see above).
3. Run the Python script `double_pendulum.py`:
   ```bash
   python double_pendulum.py
   ```
4. The script will generate an animation of the double pendulum's motion.

## Code Structure
- `double_pendulum.py`: Main script containing the double pendulum simulation and animation logic.
- Key parameters:
  - `G = 9.8`: Acceleration due to gravity (m/s²).
  - `L1 = 1.0`, `L2 = 1.0`: Lengths of the first and second pendulums (m).
  - `M1 = 1.0`, `M2 = 1.0`: Masses of the first and second pendulums (kg).
  - `th1 = 120.0`, `th2 = -10.0`: Initial angles of the pendulums (degrees).
  - `w1 = 0.0`, `w2 = 0.0`: Initial angular velocities (degrees per second).
  - `t_stop = 2.5`: Simulation duration (seconds).
  - `history_len = 500`: Number of trajectory points to display.
- The script defines a `derivs` function to compute the ODEs and uses Matplotlib's `FuncAnimation` for visualization.

## Example Output
The script generates an animation showing:
- The motion of the double pendulum, with two masses connected by lines.
- A trace of the second pendulum's path over time.
- A time display in the top-left corner of the animation.

## Notes
- The current implementation uses Euler's method for simplicity. For more accurate results, consider using `scipy.integrate.solve_ivp` as noted in the code.
- The animation is rendered using Matplotlib and can be saved as a video or HTML file using `matplotlib.animation.Animation.to_jshtml`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for bug reports, feature requests, or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The double pendulum equations are based on the C code from [http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c](http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c).
- Thanks to the Matplotlib community for providing robust tools for visualization and animation.