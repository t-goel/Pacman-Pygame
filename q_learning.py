import pickle
import random



Q_table_file = "q_table.pkl"


try:
    with open(Q_table_file, "rb") as f:
        Q = pickle.load(f)
except FileNotFoundError:
    Q = {}


actions = ["U","D","L","R"]

def save_q_table():
    with open(Q_table_file, "wb") as f:
        pickle.dump(Q, f)

def get_state(ghost,pacman,tile_size):
    gx = ghost.rect.x // tile_size
    gy = ghost.rect.y // tile_size
    px = pacman.rect.x // tile_size
    py = pacman.rect.y // tile_size
    return (gx, gy, px, py)


def init_q(state):
    if state not in Q:
        Q[state] = {a: 0 for a in actions}


def epsilon_greedy(state, epsilon=0.2):
    init_q(state)
    if random.random() < epsilon:
        return random.choice(actions)
    else:
        return max(Q[state], key=Q[state].get)



def get_reward(ghost, pacman, valid_move, prev_distance=None):
    # Current Manhattan distance
    gx, gy = ghost.rect.x, ghost.rect.y
    px, py = pacman.rect.x, pacman.rect.y
    distance = abs(gx - px) + abs(gy - py)
    
    reward = 0

    # Caught Pac-Man
    if ghost.rect.colliderect(pacman.rect):
        print("learned")

        return 10, distance

    # Hit a wall
    if not valid_move:
        reward -= 5

    # Step penalty
    reward -= 1

    # Reward for getting closer to Pac-Man
    if prev_distance is not None:
        if distance < prev_distance:
            reward += 2  # moved closer
        elif distance > prev_distance:
            reward -= 2  # moved away

    return reward, distance


def update_q(state, action, reward, next_state, alpha=0.1, gamma=0.9):
    init_q(next_state)
    old_q = Q[state][action]
    Q[state][action] = old_q + alpha * (reward + gamma * max(Q[next_state].values()) - old_q)
    