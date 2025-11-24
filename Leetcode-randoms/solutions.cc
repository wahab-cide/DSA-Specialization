/*
LeetCode 2204. Distance to a Cycle in Undirected Graph
You are given a positive integer n representing the number of nodes in a connected undirected graph containing exactly one cycle. 
The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [node1i, node2i] denotes that there is a bidirectional edge connecting node1i and node2i in the graph.

The distance between two nodes a and b is defined to be the minimum number of edges that are needed to go from a to b.

Return an integer array answer of size n, where answer[i] is the minimum distance between the ith node and any node in the cycle.
*/

#include <vector>
#include <queue>
#include <unordered_set>
#include <functional>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        // Build graph
        vector<vector<int>> graph(n);
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        
        // Find cycle using DFS
        vector<bool> visited(n, false);
        vector<int> parent(n, -1);
        unordered_set<int> cycleNodes;
        
        function<bool(int, int)> findCycle = [&](int node, int par) -> bool {
            visited[node] = true;
            for (int nei : graph[node]) {
                if (nei == par) continue;
                
                if (visited[nei]) {
                    // Found a cycle - backtrack to build cycle nodes
                    int cur = node;
                    while (cur != nei) {
                        cycleNodes.insert(cur);
                        cur = parent[cur];
                    }
                    cycleNodes.insert(nei);
                    return true;
                } else {
                    parent[nei] = node;
                    if (findCycle(nei, node)) {
                        return true;
                    }
                }
            }
            return false;
        };
        
        findCycle(0, -1);
        
        // BFS from all cycle nodes
        vector<int> distances(n, -1);
        queue<int> q;
        
        for (int node : cycleNodes) {
            distances[node] = 0;
            q.push(node);
        }
        
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            
            for (int nei : graph[current]) {
                if (distances[nei] == -1) {
                    distances[nei] = distances[current] + 1;
                    q.push(nei);
                }
            }
        }
        
        return distances;
    }
};