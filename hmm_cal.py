from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np
# matrices
initial_state = {"H":0.6, "C":0.4}
transition_matrix = {"HH": 0.7, "CH": 0.4, "HC":0.3, "CC":0.6} # a()
observation_matirx = {"SH":0.1, "SC":0.7, "MH":0.4, "MC":0.2, "LH":0.5, "LC":0.1} # b()
res16 = {}

# iter
# WHEN O = (S, S, S, M)

for str1 in "HC":
    prob1  = initial_state[str1] * observation_matirx["S"+str1]
    for str2 in "HC":
        prob2 = prob1 * observation_matirx["S"+str2] * transition_matrix[str1+str2]

        for str3 in "HC":
            prob3 = prob2 * observation_matirx["S"+str3] * transition_matrix[str2+str3]

            for str4 in "HC":
                prob4 = prob3 * observation_matirx["M"+str4]* transition_matrix[str3+str4]

                print(str1,str2,str3,str4, " is ", sep="", end ="")
                res16[str1+str2+str3+str4] = prob4
                print(f"{prob4:.6f}")


# to DataFrame

data = {
    'state': res16.keys(),
    'prob': res16.values()
}
df = pd.DataFrame.from_dict(data)
print("================ result before nolization ================ ")
print(df)


# Normalize the "prob" column
df['prob_normalized'] = normalize(df[['prob']], norm = 'l1', axis= 0)

# Print the normalized DataFrame
print(df)

# check maximum each state
# Filter rows and sum the 'prob' column
# Start from H
for i in range(1,5):
    prob_sum = dict()
    prob_sum['H'] = df.loc[df['state'].str[i-1] == 'H', 'prob'].sum()
    prob_sum['C'] = df.loc[df['state'].str[i-1] == 'C', 'prob'].sum()

    print(f"Probability: when {i}th position (H,C) {prob_sum}")
    print(f"And {max(prob_sum, key=prob_sum.get)} State has higher Prob.")


print(f"sum prob :{sum(df['prob'] )}")
print(f"sum of normalized_prob :{sum(df['prob_normalized'] )}")