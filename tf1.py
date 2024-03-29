%matplotlib inline               
import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt  
import tensorflow as tf


dataframe = pd.read_csv("data.csv") 
dataframe = dataframe.drop(["index", "price", "sq_price"], axis=1) 
dataframe = dataframe[0:10] 
dataframe 

dataframe.loc[:, ("y1")] = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1] 
                                                          
dataframe.loc[:, ("y2")] = dataframe["y1"] == 0           
dataframe.loc[:, ("y2")] = dataframe["y2"].astype(int) 
dataframe

inputX = dataframe.loc[:, ['area', 'bathrooms']].as_matrix()
inputY = dataframe.loc[:, ["y1", "y2"]].as_matrix()
inputX
inputY

# Parameters
learning_rate = 0.000001
training_epochs = 2000
display_step = 50
n_samples = inputY.size

x = tf.placeholder(tf.float32, [None, 2])
W = tf.Variable(tf.zeros([2, 2]))  
b = tf.Variable(tf.zeros([2]))              

y_values = tf.add(tf.matmul(x, W), b)   
y = tf.nn.softmax(y_values)                    
y_ = tf.placeholder(tf.float32, [None,2])  

#Let's specify our cost function and use Gradient Descent
# Cost function: Mean squared error
cost = tf.reduce_sum(tf.pow(y_ - y, 2))/(2*n_samples)
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
In [161]:
# Initialize variabls and tensorflow session
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)     
for i in range(training_epochs):  
    sess.run(optimizer, feed_dict={x: inputX, y_: inputY}) # Take a gradient descent step using our inputs and labels

    if (i) % display_step == 0:
        cc = sess.run(cost, feed_dict={x: inputX, y_:inputY})
        print "Training step:", '%04d' % (i), "cost=", "{:.9f}".format(cc) #, \"W=", sess.run(W), "b=", sess.run(b)

print "Optimization Finished!"
training_cost = sess.run(cost, feed_dict={x: inputX, y_: inputY})
print "Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n'

sess.run(y, feed_dict={x: inputX })
sess.run(tf.nn.softmax([1., 2.]))