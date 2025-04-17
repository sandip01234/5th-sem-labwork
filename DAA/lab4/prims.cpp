#include <iostream>
#include <vector>
#include <climits>

using namespace std;

#define V 5

// Function to find the vertex with the minimum key value
int minKey(vector<int>& key, vector<bool>& mstSet, int &steps) {
    int min = INT_MAX, minIndex = -1;
    for (int v = 0; v < V; v++) {
        steps++;
        if (!mstSet[v] && key[v] < min) {
            min = key[v];
            minIndex = v;
        }
    }
    return minIndex;
}

// Prim's Algorithm for Minimum Spanning Tree (MST)
void primMST(int graph[V][V]) {
    vector<int> parent(V);  // Stores MST
    vector<int> key(V, INT_MAX); // Key values for picking min weight edge
    vector<bool> mstSet(V, false); // To check if vertex is included in MST
    key[0] = 0;
    parent[0] = -1; // First node is always the root of MST
    
    int steps = 0;

    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, mstSet, steps);
        mstSet[u] = true;

        for (int v = 0; v < V; v++) {
            steps++;
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    // Output the MST
    cout << "Minimum Spanning Tree Edges:\n";
    for (int i = 1; i < V; i++) {
        cout << parent[i] << " - " << i << " : " << graph[i][parent[i]] << endl;
    }
    cout << "Number of steps: " << steps << endl;
}

int main() {
    int graph[V][V] = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    primMST(graph);
    return 0;
}
