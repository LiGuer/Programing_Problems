* Interpolation
  - Define  
    求一个函数（曲线）$f(\.x, \.w) = 0$ (或 $y = f(\.x, \.w)$)，使得该函数（曲线）经过所有样本点$\{\.x_i\ |\ i = 1:N\}$ (或 $\{(\.x_i, y_i)\ |\  i = 1:N\}$).

  - Algorithm
    * Lagrange Interpolation
      $$
      \begin{align*}
        f\left(x\right) &= \sum_{i=1}^n  y_i · f_i\left(x\right)\\
        f_i\left(x\right) &= \prod_{j=1,i\neq j}^n  \frac{x - x_j}{x_i - x_j}
      \end{align*}
      $$
      第N点y = 基函数1 × 第1点y + 基函数2 × 第2点y + 基函数3 × 第3点y  
      基函数状态2 = (输入X-第1点x)(输入X-第3点x) / (第2点x-第1点x)(第2点x-第3点x)  

    * 样条 Interpolation  
      通过求解三弯矩方程组得出曲线函数组的过程

    * 反距离加权 Interpolation 

    * Kriging Interpolation 
