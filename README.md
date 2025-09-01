This is a Pacman clone created using pygame. The ghosts have randomized movement.

Core Features

Pac-Man Movement & Maze

Pac-Man moves in 4 directions.

Maze walls block movement.

Collectibles (dots/pellets) to increase score.

Collision detection with walls and ghosts.

Ghost AI

Each ghost is an RL agent using Q-learning:

State: Positions of the ghost and Pac-Man (and optionally walls around them).

Actions: Move up, down, left, right.

Reward: +1 for reducing distance to Pac-Man, -1 for moving away.

Ghosts learn a policy to chase Pac-Man efficiently over time.

Game Display

Render maze, Pac-Man, ghosts, and collectibles using Pygame.

Update ghost positions every tick based on learned Q-values.
