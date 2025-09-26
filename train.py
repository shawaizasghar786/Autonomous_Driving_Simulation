from stable_baselines3 import PPO
import os
import gymnasium as gym
env = gym.make("CarRacing-v3", render_mode="rgb_array")



model=PPO("CnnPolicy",env,verbose=1,device="cpu")
model.learn(total_timesteps=100_000)
os.makedirs("models",exist_ok=True)
model.save("models/ppo_car_racing")
env.close()