from stable_baselines3 import PPO
import gym
import os
env=gym.make("CarRacing-v0", render_mode="rgb_array")