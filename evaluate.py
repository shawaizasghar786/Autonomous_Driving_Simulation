from stable_baselines3 import PPO
import gym
import cv2
import os

env = gym.make("CarRacing-v2", render_mode="rgb_array")

model = PPO.load("models/ppo_car_racing")

for _ in range(1000):
    action, _ =model.predict(obs)
    obs,reward,done,info=env.step(action)
    frame=env.render()
    frames.append(frame)
    if done:
        obs=env.reset()
    env.close()

    os.makedirs("videos",exist_ok=True)
    height,width,_=frame[0].shape
    out = cv2.VideoWriter("videos/drive.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()