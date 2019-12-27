# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:04:23 2019

@author: igofed
"""

import tensorflow as tf

# Create graph with name graph1

graph1 = tf.Graph()
with graph1.as_default():
    # add two constant into the graph 
    # We add tf.Operation to the defaoult graph with value 2 and name constant_a
    a = tf.constant([2], name = 'constant_a')
    b = tf.constant([3], name = 'constant_b')
    c = tf.add(a, b) # adds two tensors (c = a + b)
    d = tf.subtract(b,a)
    # the summ of the tensors a and b
# initialize session to run the code
# We create a graph inside tf
sess = tf.Session(graph = graph1)
# run the session
result1 = sess.run([a,b,c])
result2 = sess.run(b)
result3 = sess.run(c)
print(result1,result2,result3)

#close the session to release resourses
#sess.close()

with tf.Session(graph = graph1) as sess:
    result = sess.run(c)
    print(result)
    result = sess.run(d)
    print(result)

graph2 = tf.Graph()
with graph2.as_default():
    Scalar = tf.constant(0)
    Vector = tf.constant([0,1,2])
    Matrix = tf.constant([[0,1,2], [3,4,5]])
    Tensor = tf.constant([[[0,1,2], [3,4,5]],[[0,1,2], [3,4,5]]])

with tf.Session(graph = graph2) as sess:
    result = sess.run(Scalar)
    print ("Scalar (1 entry):\n %s \n" % result)
    result = sess.run(Vector)
    print ("Vector (3 entries) :\n %s \n" % result)
    result = sess.run(Matrix)
    print ("Matrix (3x3 entries):\n %s \n" % result)
    result = sess.run(Tensor)
    print ("Tensor (3x3x3 entries) :\n %s \n" % result)
    
