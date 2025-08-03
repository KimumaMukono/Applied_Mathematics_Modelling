##Tank Level Control Simulation

This Python script simulates a tank level control system using a P-only (proportional) controller. The system models the level of liquid in a tank based on the inflow controlled by a valve, using ordinary differential equations (ODEs) solved with scipy.integrate.odeint. The results are visualized with plots showing the tank level, valve position, and error over time.

Prerequisites

To run this simulation, you need the following Python libraries:


numpy
matplotlib
scipy

Install them using pip:

pip install numpy matplotlib scipy

Files

tank_level_control.py: The main Python script containing the tank level control simulation.

Usage



Clone or download the repository to your local machine.

Ensure the required libraries are installed (see Prerequisites).

Run the script:

python tank_level_control.py

The script can either:





Display animated plots in real-time if animate=True.



Generate static plots at the end of the simulation if animate=False.

Script Overview

Key Components





Tank Model: The tank function defines the dynamics of the tank level using the differential equation dLevel_dt = (c/(rho*A)) * valve, where:





rho = water density (1000 kg/m³)



A = tank area (1 m²)



c = valve coefficient (50 kg/s/%open)



valve = valve position (% open)



Simulation Setup:





Time span: 0 to 10 seconds with 0.1-second intervals.



Initial tank level: 0.



Initial valve position: 10% open.



Set point (SP): Desired tank level (default = 1).



P-only Controller: To be implemented by the user (currently a placeholder).





The controller should adjust the valve position based on the error (SP - Level0).



Tuning parameter Kc and bias ubias need to be defined.



Visualization:





Plots the tank level (process variable, PV), setpoint (SP), valve position, and error over time.



Supports both animated (real-time) and static plotting.

To-Do Tasks





Define the bias value (ubias) for the controller.



Select a tuning value for the proportional gain (Kc).



Implement the P-only controller logic to adjust the valve based on the error.



Set the desired tank level setpoint (SP).

Example Output

The script generates three subplots:





Tank Level: Compares the actual tank level (PV) with the setpoint (SP).



Valve Position: Shows the valve's % open over time.



Error: Displays the error (SP - PV) over time.

If animate=True, the plots update in real-time during the simulation. Otherwise, static plots are shown at the end.

Customization





Adjust c, rho, A, or SP to model different tank systems or desired levels.



Modify the time span (ts) or step size for different simulation durations or resolutions.



Implement the P-only controller by replacing the placeholder valve = 1 with proper control logic, e.g., valve = ubias + Kc * error.

Notes





The current script has placeholders for the P-only controller (ubias, Kc, and control logic). These must be defined to achieve meaningful control behavior.



Ensure matplotlib is configured to display plots correctly in your environment (e.g., a compatible backend for animations).



The simulation assumes a simple linear model for the tank dynamics, which may need adjustments for more complex systems.

License

This project is licensed under the MIT License. See the LICENSE file for details.