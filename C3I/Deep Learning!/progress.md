# Progress so far! 16th June 2026! 

- Started with **_Kaggle's Deep Learning course_** alongside **_Andrew Ng's Deep Learning Course from Coursera_**. 
- Learnt about Neural Networks! 

### **_A Neural Network_** :
Its essentially made up of neurons , which are like basicc unit of a neural network. Now , to explain this you could relate this with you know , your very own nervous system . Just as how neuron is a basic unit there , same thing. 

Alright, so these neurons (in a neural network) , individually perform computations , and each of these computations then decide how complex a neural network is , somewhat like , more complex === more powerful a neural network is. 

So starting off....a normal linear neural network would look something like this 

"Insert cool image" 

Here as u can see , theres ```feature 1``` and ```feature 2``` , which is essentially you know inputs... these inputs , alongside some ```weight w``` and a ```bias b``` together forms your linear neural network.. assuming that : 

```

feature 1 = x (has weight)
feature 2 = a (has bias)
weight = w 
bias = b 
output = y 

then Y = xw + ab

``` 
This above is what people would call , ***A Single neuron Model or A Linear Model***..
Assuming theres multiple inputs , then your formula for output would look like (summ [{input_i}*{weight_i}] )

## Started with Keras!

- Keras.Sequential creates a neural network model , hold on lemme jus show u directly 

```

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential ([ #Building your first neural network model yay!
    layers.Dense(units = 1 , input_shape = [4]) #So units = 1 essentially means how many outputs , when its 1 ur essentially    
                                                 #saying 1 output only pls!
                                                 #And input shape is essentally your features or inputs as is!
])

```

## Deep Neural Networks! : 

When your neural network has something called ***"layers"*** , then its essentially called a deeeep neural network (coz its DEEP...and it has Layerss...and they go in DEEEEP...so DEEEEP Neural networks XD) , 

Each of these layers perform one simple transformation , hence through denser networks -> multiple computations -> each taking you closer to your output!. , it in essence looks like this! 

<img src = "neaternn.png"></img>

Yep , the image above if you noticed has ***One extra layers : an input then the middle layer***

## Activation Function : 

Yall know how yeast works? while baking cakes? same thing onli 

So essentially activation functions is simply some function that we apply to each layers output , for what? same reason. Taking it closer to your actual output . 

A nice example would be ```rectifierfunctionmax(0,x)``` (a graph whose negative positions are rectified to 0)...applying this function to a linear model output would bend-over the straight line (of the graph) . Its popularly called as ```Relu - Rectified Linear Unit``` 

## Building a sequential Model!: 

