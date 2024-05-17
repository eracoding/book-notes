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

Note that as the input dimensions grow, the number of linear regions increases rapidly. To get a feeling for how rapidly, consider that each hidden unit defines a hyperplane that delineates the part of space where this unit is active from the part where it is not. If we had the same number of hidden units as input dimensions $D_i$ , we could align each hyperplane with one of the coordinate axes. For two input dimensions, this would divide the space into four quadrants. For three dimensions, this would create eight octants, and for $D_i$ dimensions, this would create $2^{D_i}$ orthants. Shallow neural networks usually have more hidden units than input dimensions, so they typically create more than $2^{D_i}$ linear regions.

The activation function permits the model to describe nonlinear relations between input and the output, and as such, it must be nonlinear itself; with no activation function, or a linear activation function, the overall mapping from input to output would be restricted to be linear. Many different activation functions have been tried, but the most common choice is the ReLU, which has the merit of being easily interpretable. With ReLU activations, the network divides the input space into convex polytopes defined by the intersections of hyperplanes computed by the “joints” in the ReLU functions. Each convex polytope contains a different linear function. The polytopes are the same for each output, but the linear functions they
contain can differ.


### Terminology
For historical reasons, any neural network with at least one hidden layer is also called a **multi-layer perceptron**, or MLP for short.

Networks with one hidden layer are sometimes referred to as **shallow neural networks**.

Neural networks in which the connections form an acyclic graph (graph with no loops) are referred to as feed-forward networks.

If every element in one layer connects to every element in the next, the network is fully connected. These connections represent slope parameters in the underlying equations and are referred to as network weights. The offset parameters are called biases.

## Summary
Shallow neural networks have one hidden layer. They (i) compute several linear functions of the input, (ii) pass each result through an activation function, and then (iii) take a linear combination of these activations to form the outputs. Shallow neural networks make predictions y based on inputs x by dividing the input space into a continuous surface of piecewise linear regions. With enough hidden units (neurons), shallow neural networks can approximate any continuous function to arbitrary precision.

# Notes
## Neural Networks
“Neural” networks: If the models in this chapter are just functions, why are they called “neural networks”? The connection is, unfortunately, tenuous. Visualizations consist of nodes (inputs, hidden units, and outputs) that are densely connected to one another. This bears a superficial similarity to neurons in the mammalian brain, which also have dense connections. However, there is scant evidence that brain computation works in the same way as neural networks, and it is unhelpful to think about biology going forward.

## History of Neural Networks
McCulloch & Pitts (1943) first came up with the notion of an artificial neuron that combined inputs to produce an output, but this model did not have a practical learning algorithm.

Rosenblatt (1958) developed the perceptron, which linearly combined inputs and then thresholded them to make a yes/no decision. He also provided an algorithm to learn the weights from data. Minsky & Papert (1969) argued that the linear function was inadequate for general classification problems but that adding hidden layers with nonlinear activation functions (hence the term multi-layer perceptron) could allow the learning of more general input/output relations. However, they concluded that Rosenblatt’s algorithm could not learn the parameters of such models. It was not until the 1980s that a practical algorithm (backpropagation) was developed, and significant work on neural networks resumed. The history of neural networks is chronicled by Kurenkov (2020), Sejnowski (2018), and Schmidhuber (2022).

## Activation Functions
The ReLU function has been used as far back as Fukushima (1969). However, in the early days of neural networks, it was more common to use the logistic sigmoid or tanh activation functions

The ReLU was re-popularized by Jarrett et al. (2009), Nair & Hinton (2010), and Glorot et al. (2011) and is an important part of the success story of modern neural networks. It has the nice property that the derivative of the output with respect to the input is always one for inputs greater than zero. This contributes to the stability and eﬀiciency of training and contrasts with the derivatives of sigmoid activation functions, which **saturate** (become close to zero) for large positive and large negative inputs.

However, the ReLU function has the disadvantage that its derivative is zero for negative inputs. If all the training examples produce negative inputs to a given ReLU function, then we cannot improve the parameters feeding into this ReLU during training. The gradient with respect to the incoming weights is locally flat, so we cannot “walk downhill.” This is known as the **dying ReLU problem**.

Many variations on the ReLU have been proposed to resolve this problem, including (i) the leaky ReLU (Maas et al., 2013), which also has a linear output for negative values with a smaller slope of 0.1, (ii) the parametric ReLU (He et al., 2015), which treats the slope of the negative portion as an unknown parameter, and (iii) the concatenated ReLU (Shang et al., 2016), which produces two outputs, one of which clips below zero (i.e., like a typical ReLU) and one of which clips above zero.

A variety of smooth functions have also been investigated, including the softplus function (Glorot et al., 2011), Gaussian error linear unit (Hendrycks & Gimpel, 2016), sigmoid linear unit (Hendrycks & Gimpel, 2016), and exponential linear unit (Clevert et al., 2015). Most of these are attempts to avoid the dying ReLU problem while limiting the gradient for negative values. Klambauer et al. (2017) introduced the scaled exponential linear unit, which is particularly interesting as it helps stabilize the variance of the activations when the input variance has a limited range. Ramachandran et al. (2017) adopted an empirical approach to choosing an activation function. They searched the space of possible functions to find the one that performed best over a variety of supervised learning tasks.
**The optimal function** was found to be $$a[x] = x/(1 + exp[−βx])$$, where $β$ is a learned parameter. They termed this **function Swish**. Interestingly, this was a rediscovery of activation functions previously proposed by Hendrycks & Gimpel (2016) and Elfwing et al. (2018). Howard et al. (2019) approximated Swish by the HardSwish function, which has a very similar shape but is faster to compute:
$$HardSwish[z] = \bigg\{ 0, z < -3; z(z+3)/6, -3 \leq z \leq 3; z, z > 3$$
There is no definitive answer as to which of these activations functions is empirically superior.
However, the leaky ReLU, parameterized ReLU, and many of the continuous functions can be
shown to provide minor performance gains over the ReLU in particular situations. We restrict
attention to neural networks with the basic ReLU function for the rest of this book because it’s
easy to characterize the functions they create in terms of the number of linear regions.

## Universal approximation theorem: 
The width version of this theorem states that there exists a network with one hidden layer containing a finite number of hidden units that can approximate any specified continuous function on a compact subset of R n to arbitrary accuracy. This was proved by Cybenko (1989) for a class of sigmoid activations and was later shown to be true for a larger class of nonlinear activation functions (Hornik, 1991).

## Linear, affine, and nonlinear functions:
Technically, a linear transformation $f[•]$ is any function that obeys the principle of superposition, so $$f[a + b] = f[a] + f[b]$$ This definition implies that $f[2a] = 2f[a]$.The weighted sum $$f[h_1 , h_2 , h_3 ] = ϕ_1 h_1 + ϕ_2 h_2 + ϕ_3 h_3$$ is linear, but once the offset (bias) is added so $$f[h_1 , h_2 , h_3 ] = ϕ_0 + ϕ_1 h_1 + ϕ_2 h_2 + ϕ_3 h_3 $$ this is no longer true. To see this, consider that the output is doubled when we double the arguments of the former function. This is not the case for the latter function, which is more properly termed an aﬀine function. However, it is common in machine learning to conflate these terms. We follow this convention in this book and refer to both as linear. All other functions we will encounter are nonlinear.

