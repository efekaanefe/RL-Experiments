import gymnasium as gym
import numpy as np


class PIDCartPoleAgent:
    def __init__(self, P, I, D):
        self.p = P
        self.i = I
        self.d = D
        self.prev_error = 0 # error for all the observations, shape -> (4,)
        self.integral = 0

    def choose_action(self, error):
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        pid = self.p * error + self.i * self.integral + self.d * derivative
        action = 0 if pid < 0 else 1
        # action = np.round(sigmoid(pid)).astype(np.int16)
        return action
    
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

if __name__=="__main__":
    env = gym.make("CartPole-v1", render_mode = "human")
    P, I, D = 20, 1, 80 # shifts a little from middle but works
    # P, I, D = 20, 1, 100

    agent = PIDCartPoleAgent(P, I, D)
    observation, info = env.reset()
    # original = observation[2]
    done = False
    while not done:
        env.render()
        observation_error = observation[0] + np.rad2deg(observation[2]) - 0 - observation[1] 
        action = agent.choose_action(observation_error)
        observation, reward, done, truncated, info = env.step(action)
        done = False
    env.close()

