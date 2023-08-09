# FastCarRacing-v0 Gym Environment

## Click to play: 
[![Click to play](https://img.youtube.com/vi/ByztGknW5XE/0.jpg)](https://www.youtube.com/watch?v=ByztGknW5XE)

## Introduction

The original CarRacing-v2 environment in Gymnasium requires a long time to train due to the way its reward model is defined, especially for off policy continuous agents such as Soft-Actor Critic or TD3. The episode only terminates when the car is far from the track, which causes the car to spin around on the grass/not moving at all when the agent is exploring. Thus not very time efficient. Thus, I propose a modified environment fixing these problems, enabling faster and easier training/better performance for SAC/DDPG agents. 



## Features

-Immediate termination and a penalty of -100 reward when the nose of the car is off the road.

-Action space has been changed to 2 dimensional so that the throttle and brake are mutually exclusive. This way the car will not get jammed when throttle and brake are applied at the same time when the policy is exploring.

-Braking is only available when speed exceeds 70, maximizing the speed.

-Throttle is incentivized more than brake.

-State has been changed to a 96 x 96 Torch Tensor representing the grayscale image of the car's surrounding.

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

## Training

[Soft Actor-Critic](https://arxiv.org/abs/1801.01290) is being used to train the stochastic policy and the policy is evaluated deterministically(the mean of the distribution is used for the evaluation). Below is the code for the actor CNN policy:

'''python
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=8, stride=4)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=2)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        self.linear1 = nn.Linear(4096, 1024)
        self.linear2 = nn.Linear(1024, 1024)
        self.relu = nn.ReLU() # For each layer except the last.
        self.mu = nn.Linear(1024, env.action_space.shape[0])
        self.sigma = nn.Linear(1024, env.action_space.shape[0])
        self.device = device
        self.tanh = nn.Tanh() # Applied the the output action.


'''
