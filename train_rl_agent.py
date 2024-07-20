# train_rl_agent.py
import gym
from stable_baselines3 import PPO
from custom_css_env import CustomCSS  


gym.envs.registration.register(
    id='CustomCSS-v0',
    entry_point='custom_css_env:CustomCSS',
)


env = gym.make('CustomCSS-v0')

# Create the RL model
model = PPO('MlpPolicy', env, verbose=1)

# Train the model
model.learn(total_timesteps=100000)

# Save the model
model.save("ppo_css")

# Load the model
model = PPO.load("ppo_css")

# Test the trained model
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
