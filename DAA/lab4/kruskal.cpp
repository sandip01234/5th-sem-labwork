#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int src, dest, weight;
};

// Comparator function to sort edges by weight
bool compare(Edge a, Edge b) {
    return a.weight < b.weight;
}

// Disjoint Set Union (DSU) functions
vector<int> parent, rankSet;  // Renamed `rank` to `rankSet`

int find(int v) {
    if (parent[v] == v) return v;
    return parent[v] = find(parent[v]);  // Path compression
}

void unionSets(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        if (rankSet[a] < rankSet[b]) swap(a, b);
        parent[b] = a;
        if (rankSet[a] == rankSet[b]) rankSet[a]++;
    }
}

void kruskal(vector<Edge> edges, int V) {
    sort(edges.begin(), edges.end(), compare);

    parent.resize(V);
    rankSet.resize(V, 0);  // Renamed from `rank`

    for (int i = 0; i < V; i++) parent[i] = i;

    int mstWeight = 0, steps = 0;

    for (int i = 0; i < edges.size(); i++) {
        steps++;
        if (find(edges[i].src) != find(edges[i].dest)) {
            cout << edges[i].src << " - " << edges[i].dest << " : " << edges[i].weight << endl;
            mstWeight += edges[i].weight;
            unionSets(edges[i].src, edges[i].dest);
        }
    }

    cout << "Minimum Cost of Spanning Tree: " << mstWeight << endl;
    cout << "Number of steps: " << steps << endl;
}

int main() {
    vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    int V = 4;  // Number of vertices
    kruskal(edges, V);
    return 0;
}
