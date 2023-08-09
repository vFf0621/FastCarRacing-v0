# Fast Car Racing Gym Environment
[![Video](https://img.https:youtube.com/watch?v=ByztGknW5XE/default.jpg)](https://www.youtube.com/watch?v=ByztGknW5XE)

## Installation

```bash
git clone https://github.com/igilitschenski/multi_car_racing.git
cd multi_car_racing
pip install -e .
```

## Basic Usage
After installation, the environment can be tried out by running:

```bash
python -m gym_multi_car_racing.multi_car_racing
```

This will launch a two-player variant (each player in its own window) that can be controlled via the keyboard (player 1 via arrow keys and player 2 via `W`, `A`, `S`, `D`).

Let's quickly walk through how this environment can be used in your code:

```python
import gym
import gym_multi_car_racing

env = gym.make("MultiCarRacing-v0", num_agents=2, direction='CCW',
        use_random_direction=True, backwards_flag=True, h_ratio=0.25,
        use_ego_color=False)

obs = env.reset()
done = False
total_reward = 0

while not done:
  # The actions have to be of the format (num_agents,3)
  # The action format for each car is as in the CarRacing-v0 environment.
  action = my_policy(obs)

  # Similarly, the structure of this is the same as in CarRacing-v0 with an
  # additional dimension for the different agents, i.e.
  # obs is of shape (num_agents, 96, 96, 3)
  # reward is of shape (num_agents,)
  # done is a bool and info is not used (an empty dict).
  obs, reward, done, info = env.step(action)
  total_reward += reward
  env.render()

print("individual scores:", total_reward)
```

Overview of environment parameters:

| Parameter              | Type  | Description |
|------------------------| :---: |-------------|
| `num_agents`           |`int`  | Number of agents in environment (Default: `2`) |
| `direction`            |`str`  | Winding direction of the track. Can be `'CW'` or `'CCW'` (Default: `'CCW'`)|
| `use_random_direction` |`bool` | Randomize winding direction of the track. Disregards `direction` if enabled (Default: `True`). |
| `backwards_flag`       |`bool` | Shows a small flag if agent driving backwards (Default: `True`). |
| `h_ratio`              |`float`| Controls horizontal agent location in the state (Default: `0.25`) |
| `use_ego_color`        |`bool` | In each view the ego vehicle has the same color if  activated (Default: `False`). |

This environment contains the `CarRacing-v0` environment as a special case. It can be created via

```python
env = gym.make("MultiCarRacing-v0", num_agents=1, use_random_direction=False, 
        backwards_flag=False)
```

**Deprecation Warning:**  We might further simplify the environment in the future. Our current thoughts on deprecation concern the following functionalities.

* The direction related arguments (`use_random_direction` & `direction`) were initially aded to make driving fairer as the agents' spawning locations were fixed. We resolved this unfairnes by randomizing the start positions of the agents instead.
* The impact of `backwards_flag` seems very little in practice.
* Similarly, it was interesting to play around with placing the agent at different horizontal locations of the observation (via `h_ratio`) but the default from `CarRacing-v0` ended up working well.
* The environment also contains some (not active) code on allowing penalization of driving backwards. We were worried that agents might go backwards to have more tiles on which they are first but it turned out not to be necessary for successfull learning. 

We are interested in any feedback regarding these planned deprecations.

## Citation

If you find this environment useful, please cite our CoRL 2020 paper:

```bibtex
@inproceedings{SSG2020,
    title={Deep Latent Competition: Learning to Race Using Visual
      Control Policies in Latent Space},
    author={Wilko Schwarting and Tim Seyde and Igor Gilitschenski
      and Lucas Liebenwein and Ryan Sander and Sertac Karaman and Daniela Rus},
    booktitle={Conference on Robot Learning},
    year={2020}
}
```
