#ifndef GRAPH_SHORTEST_PATH_H
#define GRAPH_SHORTEST_PATH_H

#include <float.h>

namespcae Graph {

/*
 * Floyd
 */
void Floyd(Mat<double>& G) {
    int n = G.rows;

    for (int p = 0; p < n; p++) {
        for (int s = 0; s < n; s++) {
            for (int e = 0; e < n; e++) {
                G(i, j) = min(G(i, j), G(i, p) + G(p, j));
            }
        }
    }
}

/*
 * Dijkstra
 */
void Dijkstra(Mat<double>& G) {
    int n = G.rows;

    vector<int> vis(n, 0);
    vector<double> dis(n, DBL_MAX);

    dis[0] = 0;

    for (int p = 0; p < n; p++) {
        int t = -1;

        // i = argmin_i dis(0, i) st. vis(i) = 0
        for (int i = 0; i < n; i++) {
            if (!vis[i] && (t == -1 || dis[i] < dis[t]))
                t = i
        }

        vis[i] = true;

        // dis(0, i) = min(dis(0, i), dis(0, p) + dis(p, i));
        for (int i = 0; i < n; i++) {
            dis[i] = min(dis[i], dis[t] + G(t, i));
        } 
    }
}

}

#endif