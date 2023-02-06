* Number Theory
  * Integer Ring
    - Define
      $$(\mathbb Z, +, ·)$$

  * Division with Remainder
    - Define    
      For $a,b,q,r \in \mathbb Z, 0 ≤ r < b$
      $$\begin{align*}
          a &= q \times b + r  \\
          a / b = q  \tag{Division}\\
          a \% b = r  \tag{Remainder}
      \end{align*}$$
      Division

      Remainder

    - Property
      - 
        $$\begin{align*}
          (a + b) \% c &= (a \% c + b \% c) \% c  \\
          (a - b) \% c &= (a \% c - b \% c + c) \% c  \\
          (a · b) \% c &= ((a \% c) · (b \% c)) \% c  \\
          (a / b) \% c &= (a · b^{-1}) \% c = ((a \% c) · (b^{-1} \% c)) \% c  \tag{$b^{-1}$:$b$的逆元}
        \end{align*}$$

      * Greatest Common Divisor & Least Common Multiple
        - Define

        - Property
          - 
            $$\begin{align*}
              gcd(a, b) &= gcd(b, a)  \\
              gcd(a, b) &= gcd(a - b, b) \quad;(a ≥ b)  \\
              gcd(a, b) &= gcd(a \% b, b)  \\
              gcd(k a, k b) &= gcd(k a, b)  \\
            \end{align*}$$

          $$lcm(a, b) = \frac{a · b}{gcd(a, b)}$$

        - Algorithm: Division algorithm
            $$\begin{align*}
              gcd(a, b) &= gcd(b, a \% b)  \\
              gcd(a, 0) &= a
            \end{align*}$$

      * Prime
        - Define  
          A number that can only be divided by $1$ and itself.

        - Property
          -  The Fundamental Theorem of Arithmetic  
            Any integer $n$ greater than $1$ can be uniquely expressed in the form of prime $p_i$ product.   
            $$n = \prod_i p_i^{α_i} \quad n \in \mathbb Z, n > 1$$

          - Resolving prime factor  
            Pollard Rho algorithm

      - Inverse element
        $(a · c) % b = 1$, 则$c$是$a$在$mod\ b$下的逆元$a^{-1}$

    - Problem
      * Congruence Equations
        - Purpose
          $$\begin{align*}
            \left\{\begin{matrix} x \% m_1 = a_1 \\ \vdots \\ x \% m_n = a_n \end{matrix}\right.
          \end{align*}$$

          $$x = k \prod_{i=1}^n m_i + \sum_{i=1}^n a_i \left(\prod_{j=1, j≠i}^n m_j\right) \left(\prod_{j=1, j≠i}^n m_j\right)^{-1}$$

  * Multiplicative Function
    - Define  
      A mapping $f: \mathbb Z \to R$, such that
      $$f(a · b) = f(a) f(b) \quad when\ a, b \in \mathbb Z, gcd(a, b) = 1$$

    - Property
      - $f(1) = 1$

    - Include
      * Eular Function
        - Define
          The number of coprimes with $n$ in positive integers less than $n$.
          $$\phi(n) = number({i\ |\ i \in 1:n, gcd(i, n) = 1})$$

        - Property
          $$\begin{align*}
            n &= \prod_i p_i^k_i  \\
            \phi(n) &= n \prod_{p|n} (1 - 1/p)  \\
          \end{align*}$$
