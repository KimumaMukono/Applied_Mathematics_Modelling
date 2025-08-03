import matplotlib.pyplot as plt
import matplotlib.animation as anim

y = 5.0     # m
v = 0.0      # m/s
g = -9.81    # m/s^2
bounce = 0.8 # loss of 20% energy
dt  = 0.02

fig, ax = plt.subplots()  # Create figure and axis

ax.set_xlim(0, 2)
ax.set_ylim(0, 6)
ax.set_xlabel('Horizontal position (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Bouncing Ball Simulation')

# Set aspect ratio to be equal so the ball appears as a circle
ax.set_aspect('equal', 'box')

# Draw the ball
ball = plt.Circle((1, y), 0.1, color='red')  # Use plt.Circle instead of plt.circle
ax.add_patch(ball)

def animate(frame):
    global y, v
    a = g  # acceleration due to gravity
    v = v + a * dt  # update velocity
    y = y + v * dt  # update height
    
    if y <= 0:  # Bounce the ball if it hits the ground
        y = 0
        v = -bounce * v  # Invert velocity and apply bounce factor
    
    ball.center = (1, y)  # Update ball position
    return ball,

# Create the animation
ani = anim.FuncAnimation(fig, animate, frames=200, interval=int(dt*1000), blit=True)

plt.show()
