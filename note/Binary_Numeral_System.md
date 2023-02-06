* Binary Numeral System
  - Define  
  
  - Property
    - Addition
      $$\begin{align*}
        \text{ans}[i] &= (a[i] + b[i] + \text{carry}[i-1]) \% 10  \\
        \text{carry}[i] &= (a[i] + b[i] + \text{carry}[i-1]) / 10 \in \{0, 1\}  \\
        \text{carry}[1] &= 0
      \end{align*}$$
