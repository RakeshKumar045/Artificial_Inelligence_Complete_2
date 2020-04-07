# Use-of-Dropout-and-Batch-Normalization-in-2D-CNN
Use of Dropout and Batch Normalization in 2D CNN


In this leeson, I am going to show you how you can use Dropout and Batch Normalization in increasing the accuracy and regularize your neural network.

What is Dropout
Dropout is a regularization technique patented by Google[1] for reducing overfitting in neural networks by preventing complex co-adaptations on training data. It is a very efficient way of performing model averaging with neural networks.[2] The term "dropout" refers to dropping out units (both hidden and visible) in a neural network

Dropout is a technique where randomly selected neurons are ignored during training. They are “dropped-out” randomly. This means that their contribution to the activation of downstream neurons is temporally removed on the forward pass and any weight updates are not applied to the neuron on the backward pass.

As a neural network learns, neuron weights settle into their context within the network. Weights of neurons are tuned for specific features providing some specialization. Neighboring neurons become to rely on this specialization, which if taken too far can result in a fragile model too specialized to the training data. This reliant on context for a neuron during training is referred to complex co-adaptations.

Batch Normalization

To reduce this problem of internal covariate shift, Batch Normalization adds Normalization “layer” between each layers. An important thing to note here is that normalization has to be done separately for each dimension (input neuron), over the ‘mini-batches’, and not altogether with all dimensions. Hence the name ‘batch’ normalization.

Due to this normalization “layers” between each fully connected layers, the range of input distribution of each layer stays the same, no matter the changes in the previous layer.

Normalization brings all the inputs centered around 0. This way, there is not much change in each layer input. So, layers in the network can learn from the back-propagation simultaneously, without waiting for the previous layer to learn. This fastens up the training of networks.


