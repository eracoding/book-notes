### Concepts
*Supervised Learning* - model defines a mapping from one or more inputs to one or more outputs. 

The model is just a mathematical equation; when the inputs are passed through this equation, it computes the output, and this is termed *inference*. The model equation also contains *parameters*. Different parameter values change the outcome of the computation; the model equation describes a family of possible relationships between inputs and outputs, and the parameters specify the particular relationship.

When we talk about learning or training a model, we mean that we attempt to find parameters *w* that make sensible output predictions from the input.

We quantify the degree of mismatch in this mapping with the *loss L*. **Loss function** is a scalar value that summarizes how poorly the model predicts the training outputs from their corresponding inputs for parameters ϕ.

### 1D Linear Regression Model
$$y=f[x, \phi] = \phi_0 + \phi_1 x$$

This model has two parameters $ϕ = [ϕ_0, ϕ_1]^T$ , where $ϕ_0$ is the y-intercept of the line and $ϕ_1$ is the slope. Different choices for the y-intercept and slope result in different relations between input and output (figure 2.1). Hence, equation defines a family of possible input-output relations (all possible lines), and the choice of parameters determines the member of this family (the particular line).


### Loss
The mismatch is captured by the deviation between the model predictions $f[x_i, ϕ]$ (height of the line at xi) and the ground truth outputs yi. We quantify the total mismatch, training error, or loss as the sum of the squares of these deviations for all I training pairs:
$$L[\phi] = \sum^I_{i=1} (f[x_i, \phi] - y_i)^2 = \sum^I_{i=1} (\phi_0 + \phi_1 x_i -y_i)^2$$
This loss function is called **least-squares loss (LSE)**. The squaring operation means that the direction of the deviation (i.e., whether the line is above or below the data) is unimportant.

The difference between loss function and cost function is in the number of data - loss function is per data, cost function is for banch (batch).

## Notes:
1. **Loss functions** vs **Cost functions**: Those terms are used interchangeably. However, more properly, loss function is the individual term associated with a data point, and the cost function is the overall quantity that is minimized. Cost function can contain additional terms that are not associated with individual data points. **Objective function** is any function that is to be maximized or minimized.

2. **Generative vs Disriminative models**: The models $y = f[x, \phi]$ are *discriminative models*. These make an output prediction *y* from real-world measurements *x*. Another approach is to build a *generative model* $x = g[y, \phi]$, in which the real-world measurements x are computed as a function of the output $y$.