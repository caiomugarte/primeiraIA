import gym

env = gym.make("Taxi-v3").env

state = env.encode(3, 1, 2, 0)
print("State:", state)
env.s = state

env.reset()
env.render()
print("Número de Ações Space {}".format(env.action_space))
#Encoding das posições do taxi do passageiro e do destino
print("State Space {}".format(env.observation_space))