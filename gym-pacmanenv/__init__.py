from gym.envs.registration import register

register(
    id='pacman-v0',
    entry_point='gym_pacman.envs:PacmanEnv',
)
# register(
#     id='foo-extrahard-v0',
#     entry_point='gym_foo.envs:FooExtraHardEnv',
# )