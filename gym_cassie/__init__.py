from .envs import CassieEnv
from gym.envs.registration import register

register(
    id='Cassie-v0',
    entry_point='gym_cassie.envs:CassieEnv',
)

register(
    id='Cassie-walking-v0',
    entry_point='gym_cassie.envs:CassieEnv',
    kwargs={'traj': 'walking'}
)