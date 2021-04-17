import pickle
import networkx as nx
import numpy as np

dict_friends = {}
try:
    fh_data = open('friend_list.pickle', 'rb')
    dict_friends = pickle.load(fh_data)
    fh_data.close()
except Exception as e:
    print(e)

G = nx.Graph()

counter = 0
limit = 100  # number of main nodes
for k, v in dict_friends.items():
    counter += 1
    if counter < 2:
        continue
    if not counter <= limit:
        break
    print(counter)
    G.add_node(k)  # add main id
    for i in v:
        G.add_edge(k, i)  # add friends of id

# A = nx.adjacency_matrix(G)
# print(A.todense())

print(f"number of nodes: {len(G)}")
A = nx.to_numpy_array(G)
# print(A)
# print(f"Non-zero: {np.count_nonzero(A)}")

# A2 = np.linalg.matrix_power(A, 2)
# # print(A2)
# # print(f"Non-zero: {np.count_nonzero(A2)}")
#
# A3 = np.linalg.matrix_power(A, 3)
# # print(A3)
# # print(f"Non-zero: {np.count_nonzero(A3)}")
#
# A4 = np.linalg.matrix_power(A, 4)
# # print(A4)
# # print(f"Non-zero: {np.count_nonzero(A4)}")
#
# A5 = np.linalg.matrix_power(A, 5)
# # print(A5)
# # print(f"Non-zero: {np.count_nonzero(A5)}")
#
# A6 = np.linalg.matrix_power(A, 6)
# # print(A6)
# # print(f"Non-zero: {np.count_nonzero(A6)}")
#
# A7 = np.linalg.matrix_power(A, 7)
# print(A7)
# print(f"Non-zero: {np.count_nonzero(A7)}")

A8 = np.linalg.matrix_power(A, 8)
# print(A8)
# print(f"Non-zero: {np.count_nonzero(A8)}")

# S = A + A2 + A3 + A4 + A5 + A6 + A7 + A8
print(A8.sum())