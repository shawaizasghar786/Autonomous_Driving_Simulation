from stable_baselines3 import PPO
import gym
import cv2
import os

env = gym.make("CarRacing-v0", render_mode="rgb_array")
model = PPO.load("models/ppo_car_racing")

for _ in range(1000):
    action, _ =model.predict(obs)
    obs,reward,done,info=env.step(action)
    frame=env.render()
    frames.append(frame)
    if done:
        obs=env.reset()
    env.close()