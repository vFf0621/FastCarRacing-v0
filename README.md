# Fast Car Racing Gym Environment
[![Video](https://img.https:youtube.com/watch?v=ByztGknW5XE/default.jpg)](https://www.youtube.com/watch?v=ByztGknW5XE)

## Installation

```bash
git clone https://github.com/vFf0621/FastCarRacing-v0
cd FastCarRacing-v0
pip install -e .
```

## Usage

```python
import gymnasium
import gym_fast_car_racing

env = gym.make("FastCarRacing-v0")

obs = env.reset()[0]
done = False
episode_reward = 0

while not done:
  action = agent.policy(obs)
  obs_, reward, done, truncated, info = env.step(action)
  total_reward += reward
  env.render()

```
