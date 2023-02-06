  \Property
    - Representations of Graphs
      - Adjacency Matrix
      - Adjacency List

    - 同构

    - 连通性

    - 遍历
      \Problem
        从一个点出发, 通过图的边, 遍历图的所有点.

      \Algorithm
        - Depth-first Search

        - Breadth-first Search

    * Shortest Path
      \Problem

      \Property
        - 三角不等式
          $
            d(s, v) ≤ d(s, u) + 1  \yag{无边权的图} 
            d(s, v) ≤ d(s, u) + w(u, v)  \yag{有边权的图} 
          $

        - 最短路径的子路径, 也是最短路径.

        - 边权恒正的图, 任意两个结点之间的最短路, 不会经过重复的结点.

      \Algorithm
        - Dijkstra Algorithm
          - Greedy
          - 时间复杂度 $O(V^2)$
          - 要求: 图中不存在负边权

        - Floyd 算法
          - Dynamic Programming
          $d(i,j) = \min\{ d(i,k) + d(k,j) , d(i,j) \}  \tag{状态转移方程}$
          - 时间复杂度 $O(V^3)$
            空间复杂度 $O(V^2)$

    * Network Flow Problem
      \Problem
        设$G'$是$G$的子图, 
        $
          w'(u, v) ≤ w(u, v)  \tag{流量约束}
          \sum_i w'(u, v_i) = \sum_i w'(v_i, u)  \qu; u ≠ s, u ≠ e  \tag{非源、汇点进出流量相等}
        $

      \Include
        - Maximum Flow Problem
          \Problem
            $
              \max \qu& \sum_i w'(v_i, e) = w'(s, v_i)  \tag{源、汇点最大流量}
              s.t. \qu& w'(u, v) ≤ w(u, v)  \tag{流量约束}
                \sum_i w'(u, v_i) = \sum_i w'(v_i, u)  \qu; u ≠ s, u ≠ e  \tag{非源、汇点进出流量相等}
            $

          \Algorithm
            - Dinic Algorithm
              - Principle
                贪心 + "反悔"机制

        - Minimum Cut

        - 最小费用最大流

    * Travelling Salesman Problem
      \Problem
        求遍历所有给定点的最短闭合路径.

  \Include
    * Undirected Graph
      * Bipartite Graph
        \Define
          $(X, Y, E)$
          - $X, Y \subset V, X \cup Y = V$
            图的点集分为不相交的两个子集$X, Y$
          - $E = \{(x_i, y_j) \ |\ x_i \in X, y_j \in Y\}$
            边只存在于点集$X, Y$之间, 而不存在于其内部.

        \Property
          - 匹配: 二分图的一个子图, 且子图的边集中任意两条边都不依附于同一顶点;
            设$M$是二分图$G$的子图, 则
            $\forall e_i, e_j \in E_M, e_i≠e_j, then\ e_i(1) ≠e_j(1), e_i(2) ≠e_j(2)$

            - 最大匹配: 边数最多的匹配 $\arg\max_{M \subseteq G} \qu number(E_M)$
            - 完美匹配: 所有点都在匹配的边上.

            - 求最大匹配
              \Problem
                
              \Algorithm
                - Hungarian Algorithm

      * Tree

    * Directed Graph
      * Directed Acyclic Graph

