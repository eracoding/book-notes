### Concepts
Shallow neural network - is neural network with multivariate inputs and outputs, and a single hidden layer.

### Universal Approximation Theorem !!! IMPORTANT
Consider the case with D hidden units where the $d^{th}$ hidden unit is:

$$h_d = a[\theta_{d0} + \theta_{d1} x]$$

and these are combined linearly to create the output:

$$y = \phi_0 + \sum^D_{d=1} \phi_d h_d$$

The number of hidden units in a shallow network is a measure of the *network capacity*. With *ReLU* activation functions, the output of a network with *D* hidden units has at most *D* joints and so is a piecewise linear function with at most *D+1* linear regions. As we add more hidden units, the model can approximate complex functions.

It means with enough capacity (hidden units), a shallow network can describe any continuous 1D function defined on a compact subset of the real line to arbitrary precision. To see this, consider that every time we add a hidden unit, we add another linear region to the function. As these regions become more numerous, they represent smaller sections of the function, which are increasingly well approximated by a line.

The **Universal Approximation Theorem** proves that for any continuous function, there exists a shallow network that can approximate this function to any specified precision.

