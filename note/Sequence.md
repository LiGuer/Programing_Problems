* Sequence 
  - Problem 
    * Sort

    * Longest Subsequence Problem
      - Include
        * Longest Common Subsequence
          - Purpose  
            input: sequence $a, b$
            $$\begin{align*}
              \max_{x}  \quad & \text{number}(x)  \\
              s.t. \quad & x \subseteq a  \\
                & x \subseteq b
            \end{align*}$$

          - Algorithm  
            Dynamic Programming  
            $$\begin{align*}
              f(a_{1:n}, b_{1:m}) &= \left\{\begin{matrix}
                f(a_{1:n-1}, b_{1:m-1}) + 1 \quad &;  a_n = b_m  \\
                \max(f(a_{1:n}, b_{1:m-1}), f(a_{1:n-1}, b_{1:m})) \quad &;  a_n ≠ b_m  \\
              \end{matrix}\right.  \\

              f(a_1, b_1) &= \left\{\begin{matrix}
                1    \quad ; a_1 = b_1  \\
                0   \quad ; a_1 ≠ b_1  \\
              \end{matrix}\right.  \tag{initial}
            \end{align*}$$

          - Include
            * Longest Continuous Common Subsequence
              - Algorithm  
                Dynamic Programming  
                $$\begin{align*}
                  f(a_{1:n}, b_{1:m}) &= \left\{\begin{matrix}
                    f(a_{1:n-1}, b_{1:m-1}) + 1 \quad &;  a_n = b_m  \\
                    0  \quad &;  a_n ≠ b_m
                  \end{matrix}\right.  \\

                  f(a_i, b_1) &= \left\{\begin{matrix}
                    1  \quad ; a_i = b_1  \\
                    0  \quad ; a_i ≠ b_1
                  \end{matrix}\right.  \tag{initial}  \\

                  f(a_1, b_i) &= \left\{\begin{matrix}
                    1  \quad ; a_1 = b_i  \\
                    0  \quad ; a_1 ≠ b_i
                  \end{matrix}\right.
                \end{align*}$$

        * Longest Ascending Subsequence
          - Purpose  
            (input) sequence $a$
            $$\begin{align*}
              \max_{x \subseteq a}  \quad &  number(x)  \\
              s.t. \quad & x_i < x_{i+1} \quad ; i \in 1:number(x)
            \end{align*}$$
            
          - Algorithm  
            $$\begin{align*}
              f(n) = max(f(i), max(f(j)) + 1) \quad ; j < i \ and\ a_j < a_i  \\
              f(1) = 1  \tag{initial}
            \end{align*}$$
            $f(n)$: 以$a_n$为结尾的最长上升子序列的长度.

        * Longest Public Prefix
          - Purpose  
            (input) sequence $a$
            $$\begin{align*}
              \max \quad & k  \\
              s.t. \quad & a_{1:k} = a_{n-k+1:n}
            \end{align*}$$

          - Algorithm  
            $$\begin{align*}
              f(n) = \left\{\begin{matrix}
                f(n-1) + 1  \quad &;  a_n = a_{f(n-1) + 1}  \\
                f(f(n-1)) + 1 \quad &; a_n = a_{f(f(n-1)) + 1}  \\
                \vdots & \vdots  \\
                0  \quad &; other
              \end{matrix}\right.
            \end{align*}$$

    * Sequence Palindrome
      - Include
        * Longest Palindrome Subsequence 
          - Purpose 
            $$\begin{align*}
              \max_{x \subseteq a} \quad & n_x = \text{number}(x)  \\
              s.t. \quad & x_i = x_{n_x - i + 1}  \quad ; i = 1:n_x  \tag{Palindrome}
            \end{align*}$$

          - Algorithm  
            Dynamic programming,
            $$\begin{align*}
              f(s,e) &= \left\{\begin{matrix}
                f(s-1,e+1) + 2 \quad & f(s,e) > 0 \ and\  a_{s-1} = a_{e+1}  \\
                0 \quad & other.
                \end{matrix}\right.  \\
              f(s,s) &= 1  \tag{initial}  \\
              f(s,s+1) &= 2 \quad ;a_s = a_{s+1}  \\
            \end{align*}$$
            $f()$: $a_{s:e}$的回文字数, 不是回文序列则为0.

        * Maximum Palindrome Prefix
          - Purpose  
            $$\begin{align*}
              \max_{x \in 1:n_a} \quad & x  \\
              s.t. \quad & a_i = x_{x - i + 1}  \quad ; i = 1:x  \tag{Palindrome}
            \end{align*}$$

    * Sequence Matching
      - Purpose  
        (input) $a, b \quad ; b \subseteq a$  
        find $\min\ k$, let $b = a_{k:k+n_b-1}$

      - Property  
        if $b_{1:i} = a_{k:k+i-1}$, and $l_i = \text{Maximum public prefix length}(b_{1:i})$
        $$\begin{align*}
          b_{1:l_i} &= a_{((k+i-1)-l_i+1):(k+i-1)}  \\
          b_{1:l'} &≠ a_{((k+i-1)-l'+1):(k+i-1)}  \quad ; l' > l        
        \end{align*}$$

      - Algorithm
        * Knuth-Morris-Pratt Algorithm
          $$\begin{matrix}
            b_{1:i} = a_{k:k+i-1} &\ and\ & b_{i+1} &= a_{k+i} & \Rightarrow & b_{1:i+1} &=& a_{k:k+i}  \\
            b_{1:i} = a_{k:k+i-1} &\ and\ & b_{g(i)+1} &= a_{k+i} & \Rightarrow  & b_{1:g(i)+1} &=& a_{(k+i)-g(i)+1:k+i}  \\
            b_{1:i} = a_{k:k+i-1} &\ and\ & b_{g(g(i))+1} &= a_{k+i} & \Rightarrow  & b_{1:g(g(i))+1} &=& a_{(k+i)-g(g(i))+1:k+i}  \\
            &&&... & \Rightarrow &...&&  \\
            & & b_{1} &= a_{k+1} & \Rightarrow  & b_{1:1} &=& a_{k+i:k+i}  \\
            & & b_{1} &≠ a_{k+1} & \Rightarrow  & b_{1:1} &≠& a_{k+i:k+i}  \\
          \end{matrix}$$