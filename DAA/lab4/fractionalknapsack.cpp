#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int weight, value;
    double ratio;
};

// Function to sort items based on value/weight ratio
bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

void fractionalKnapsack(int capacity, vector<Item> items) {
    int i, steps = 0;
    double totalValue = 0.0;

    // Sorting items based on value/weight ratio
    sort(items.begin(), items.end(), compare);

    // Picking items for the knapsack
    for (i = 0; i < items.size(); i++) {
        steps++;
        if (capacity >= items[i].weight) {
            totalValue += items[i].value;
            capacity -= items[i].weight;
        } else {
            totalValue += items[i].ratio * capacity;
            break;
        }
    }

    cout << "Maximum value in Knapsack: " << totalValue << endl;
    cout << "Number of steps: " << steps << endl;
}

int main() {
    int i, capacity = 50;
    vector<Item> items = {{10, 60}, {20, 100}, {30, 120}};

    // Calculating value/weight ratio for each item
    for (i = 0; i < items.size(); i++) {
        items[i].ratio = (double)items[i].value / items[i].weight;
    }

    fractionalKnapsack(capacity, items);
    return 0;
}
