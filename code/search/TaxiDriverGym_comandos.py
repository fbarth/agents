import gym
env = gym.make("Taxi-v3").env

state = env.reset()
env.render()
print(env.desc)
taxi_row, taxi_col, pass_idx, dest_idx = env.decode(state)
print(taxi_row, taxi_col, pass_idx, dest_idx)

# The filled square represents the taxi, which is yellow without a passenger and green with a passenger.
# The pipe ("|") represents a wall which the taxi cannot cross.
# R, G, Y, B are the possible pickup and destination locations. The blue letter represents the current 
# passenger pick-up location, and the purple letter is the current destination.

# actions:
# 0 = south
# 1 = north
# 2 = east
# 3 = west
# 4 = pickup
# 5 = dropoff


