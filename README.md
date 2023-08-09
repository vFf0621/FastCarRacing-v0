# FastCarRacing-v0 Gym Environment
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ByztGknW5XE/0.jpg)](https://www.youtube.com/watch?v=ByztGknW5XE)
## Features

-Immediate termination and a penalty of -100 reward for going off the road.

-Action space has been changed to 2 dimensional so that the throttle and brake are mutually exclusive.

-

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
