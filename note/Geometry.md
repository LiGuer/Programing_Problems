* Geometry
  - Concept 
    * Convex Set

    * Affine Set
      - Define  
        Affine Set is a set such that the lines drawn by any two points in the set are still in the set.  

      $$\forall \boldsymbol x_i \in C, θ_i \in R, \sum θ_i = 1 \quad \text{, then}\quad \sum θ_i x_i \in C$$

    * Affine Hull
      - Define  
        $$\text{aff}(C) = \left\{\sum θ_i x_i\ |\ x_i\in C,theta_i \in R, \sum θ_i = 1  \right\}$$
        Affine Hull is a set such that affine combinations of all points in the set constitutes an affine hull.

    * Cone
      - Define  
        $$\forall \boldsymbol x \in C, θ > 0, \quad \text{, then}\quad θ \boldsymbol x \in C$$
        以零点为起点的射线的集合.

      - Include
        * Convex Cone
          - Define  
            $$\forall \boldsymbol x_1, \boldsymbol x_2 \in C, θ_1,θ_2 ≥ 0 \quad \text{, then}\quad θ_1 \boldsymbol x_1 + θ_2 \boldsymbol x_2 \in C$$

  - Problem
    * Intersection Problem
      - Include
        * Intersection of segments  
