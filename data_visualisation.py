import pickle
import networkx as nx
from pyvis.network import Network

dict_friends = {}
try:
    fh_data = open('friend_list.pickle', 'rb')
    dict_friends = pickle.load(fh_data)
    fh_data.close()
except Exception as e:
    print(e)

G = nx.Graph()

counter = 0
for k, v in dict_friends.items():
    counter += 1
    if counter < 2:
        continue
    if not counter <= 100:
        break
    print(counter)
    G.add_node(k)
    # nodes_list.append(k)  # add main id
    for i in v:
        G.add_edge(k, i)  # add friends of id

# print("adding nodes")
# G.add_nodes_from(nodes_list)
# print("nodes added")

# print(f"nodes = {G.nodes}")
# print(f"edges = {G.edges}")

net = Network(height='100%', width='100%', notebook=True, bgcolor='#F5F8FA')

print("importing graph to pyvis")
net.from_nx(G)
print("import complete")

net.set_options(''''
var options = {
  "nodes": {
    "color": {
      "border": "rgba(35,171,233,1)",
      "background": "rgba(17,146,196,1)",
      "highlight": {
        "border": "rgba(233,95,96,1)",
        "background": "rgba(255,121,137,1)"
      },
      "hover": {
        "border": "rgba(233,48,35,1)",
        "background": "rgba(255,159,178,1)"
      }
    },
    "font": {
      "color": "rgba(52,52,52,0)"
    },
    "scaling": {
      "min": 75,
      "max": 41
    },
    "shapeProperties": {
      "borderRadius": 11
    }
  },
  "edges": {
    "color": {
      "color": "rgba(86,86,86,1)",
      "inherit": false
    },
    "font": {
      "color": "rgba(52,52,52,0)"
    },
    "smooth": false
  },
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -12450
    },
    "minVelocity": 0.75
  }
}
''')

# net.show_buttons(filter_=['nodes', 'edges', 'physics'])
net.show("friend_list.html")
