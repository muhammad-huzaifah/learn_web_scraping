import pandas as pd

states = ["California", "Texas", "Florida", "New York"]
population = [39538223, 29145505, 21538187, 20201249]

dict_states = {'State': states, 'Population': population}

df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)
df_states.to_csv('states.csv', index=False)


# print(states[-4]) #output: New York

# for state in states:
#     print(state)

# for state in states:
#     if state == "Florida":
#         print(state)


# with open('test.txt', 'w') as file:
#     file.write("Data successfully scraped!")