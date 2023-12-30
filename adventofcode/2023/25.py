# seems like networkx is the "right" way to do this
import networkx as nx

G = nx.Graph()


with open('input/25.txt') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
    for line in lines:
        k, val = line.split(': ')
        for v in val.strip().split(' '):
            G.add_edge(k, v)

# algorithm for determining minimum edge cuts
# how does this know to only make 3 cuts? maybe inherent to the problem
edges_to_cut = nx.minimum_edge_cut(G)
G.remove_edges_from(edges_to_cut)

ans = 1
for i in nx.connected_components(G):
    ans *= len(i)

print(ans)
# print(prod([len(c) for c in nx.connected_components(G)]))