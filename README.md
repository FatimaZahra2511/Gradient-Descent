# Gradient-Descent
Optimization Algorithm
##  Overview  
This project implements **Gradient Descent** to find the local minimum of mathematical functions. The optimization algorithm iteratively updates the function parameters by moving in the direction of the negative gradient until convergence.

##  Contents  
- **Question 1:** Basic Gradient Descent for a single-variable function.  
- **Question 2:** Enhanced version with a stopping condition based on precision.  
- **Question 3.1:** Visualization of the function `f(x,y) = g(x) ⋅ h(y)`.  
- **Question 3.2:** Sampling strategy and its effect on function behavior.  
- **Question 3.3:** Gradient Descent for a multi-dimensional function `f(x, y)`.  

---

## ** Implementation Details**
### ** Question 1: Basic Gradient Descent**
- The algorithm finds the local minimum of **y = (3x+5)²**.
- The update rule follows:
  ```python
  x_new = x_old - learning_rate * gradient
  ```
- The stopping criteria:  
  - Maximum number of iterations.  
  - Small change in `x` (below a precision threshold).  

### ** Question 2: Gradient Descent with Precision Control**
- Introduces a **precision-based stopping condition**.
- The algorithm stops when `|x_new - x_old| < precision`.  

### ** Question 3.1: 3D Visualization**
- Uses **Matplotlib** to plot the function `f(x, y) = g(x) ⋅ h(y)`.  
- Implements **mesh-grid** for 2D domain representation.

### ** Question 3.2: Sampling Strategy**
- Generates `x, y` values over the range **[-20, 20]**.
- Uses **160,000 points** to analyze function behavior.

### ** Question 3.3: Multi-Dimensional Gradient Descent**
- Adapts gradient descent for **two variables (x, y)**.
- Uses **partial derivatives** for function updates.

---

## ** Technologies Used**
- **Python** (Main Programming Language)
- **NumPy** (Array and Mathematical Operations)
- **Matplotlib** (Visualization)
- **SymPy** (Symbolic Differentiation)

---


## **Example Output**
```
Iteration 1: x = -4.2, y = 20.5, Gradient = 12.6
Iteration 2: x = -2.8, y = 7.9, Gradient = 8.4
...
Local minimum found at: x = -1.67, y = 0

