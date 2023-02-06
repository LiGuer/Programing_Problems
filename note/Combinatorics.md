* Combinatorics
  * Counting

    - Property
      - Addition theorem  
        for $S = \cap_{i=1}^n S_i, S_i \cap S_j = \emptyset (i ≠ j)$
        $$\Rightarrow number(S) = \sum_{i=1}^n number(S_i)$$

      - Multiplication theorem  
        for sets $S_A, S_B$, and
        $$\begin{align*}
          S &= \{(a, b) | a \in S_A, b \in S_B\}  \\
            &= S_A × S_B  \tag{Cartesian积}  \\
        \end{align*}$$
        $$\Rightarrow number(S) = number(S_A) × number(S_B)$$

        - Proof
          $$\begin{align*}
            S 
            &= \{(a, b) | a \in S_A, b \in S_B\}  \\
            &= \cap_{a_i \in S_A} \{(a_i, b) | b \in S_B\}  \\
            \Rightarrow number(S) &= \sum_{i=1}^{number(S_A)} number(S_B)  \tag{Addition theorem}  \\
            &= number(S_A) × number(S_B)  \\
          \end{align*}$$

      - Principle of inclusion-exclusion  
        for $A_1,...,A_n \subseteq S$
        $$\begin{align*}
          number(\cup_{i=1}^n A_i) &= \sum_{k=1}^n ((-1)^{k-1} \sum_{\substack{i_1,...,i_k \in 1:n \\ i_1≠...≠i_k}} number(\cap_{i\in\{i_1,...,i_k\}} A_i))
        \end{align*}$$


      - Special Counting Sequence
        - Catalan Number
          $$\begin{align*}
            f_n 
            &= \frac{1}{n+1} C(2n, n)  \\
            &= C(2n, n) - C(2n, n-1)   \tag{通项式}\\
            &= \frac{(2n)!}{(n+1)!·n!}\\
          f_n &= \sum_{i=0}^{n-1} f_{i} · f_{n-1-i}  \quad; n ≥ 2  \tag{递推式}\\
            &= \frac{4n-2}{n+1} f_{n-1}
          \end{align*}$$

      - Pigeonhole Principle  
        for $A_1, ..., A_n \subseteq A, number(A) = n + 1$, $\Rightarrow \exists A_i, number(A_i) ≥ 2$.

  * Permutation & Conbination
    - Define  
      Conbination: n个元素的集合中, 任取r个元素形成无序子集合.  
      Permutation: n个元素的集合中, 任取r个元素形成有序序列. 

      The number of Conbination and Permutation Subsets
      $$\begin{align*}
        C(n, r) &= \frac{n!}{(n - m)!·m!}  \tag{Conbination}\\
        A(n, r) &= \frac{n!}{(n - m)!}  \tag{Permutation}
      \end{align*}$$

    - Property
      - $C(n,r) = C(n-1,r-1) + C(n-1,r)$
      - $C(n,r) = C(n,n-r)$
      - 
        $$\begin{align*}
          \sum_{i=0}^n C(n,i) &= 2^n  \\
          \sum_{i=0}^n C(n,i)^2 &= C(2n, n)  \\
          \sum_{i=0}^n C(k+i,k)^2 &= C(n+k+1, k+1) 
        \end{align*}$$

      - Full Permutation
        - Problem: Generate Full Permutation
          $$\begin{align*}
            f(\{a_i | i\in 1:n\}) 
            &= \{(a_1, a_2, ..., a_n), (a_2, a_1, ..., a_n), (a_n, a_{n-1}, ..., a_1)\}  \\
            &= \cup_{i=1}^n (\{(a_i)\} × f(\{a_j\ |\ j ≠ i, j\in 1:n\}))  \tag{$×$: 序列合并}  \\
            f(\{a_1\}) &= \{(a_1)\}  \tag{initial}  \\
          \end{align*}$$
