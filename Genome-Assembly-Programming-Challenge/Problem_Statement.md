**Problem 1: 
Problem Description
Task. Given a network with lower bounds and capacities on edges, find a circulation if it exists.
Input Format. The first line contains integers 𝑛 and 𝑚 — the number of vertices and the number of edges, respectively. Each of the following 𝑚 lines specifies an edge in the format “u v l c”: the edge (𝑢, 𝑣) has a lower bound 𝑙 and a capacity 𝑐. (As usual, we assume that the vertices of the network are {1, 2, . . . , 𝑛}.) The network does not contain self-loops, but may contain parallel edges.
Constraints. 2 ≤ 𝑛 ≤ 40; 1 ≤ 𝑚 ≤ 1 600; 𝑢 ̸= 𝑣; 0 ≤ 𝑙 ≤ 𝑐 ≤ 50.
Output Format. If there exists a circulation, output YES in the first line. In each of the next 𝑚 lines output
the value of the flow along an edge (assuming the same order of edges as in the input). If there is no circulation, output NO.