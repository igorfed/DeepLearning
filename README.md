
## Linear Regression

It is a function that depence from data of one vareables or data from another one. <br />
`Y = a X + b` <br />
**Y** - dependent variable <br />
**X** - independent variable  <br />
**a** is a scope of line, **b** is an intersept. Slope and intersept are possible to adjust.   

![alt tag](https://github.com/igorfed/DeepLearning/blob/master/img/YaXb.png)

## Linear Regression with TensorFlow
### Input Data.
MODELYEAR e.g. 2014<br />
MAKE e.g. Acura<br />
MODEL e.g. ILX<br />
VEHICLE CLASS e.g. SUV<br />
ENGINE SIZE e.g. 4.7<br />
CYLINDERS e.g 6<br />
TRANSMISSION e.g. A6<br />
FUEL CONSUMPTION in CITY(L/100 km) e.g. 9.9<br/>
FUEL CONSUMPTION in HWY (L/100 km) e.g. 8.9<br/>
FUEL CONSUMPTION COMB (L/100 km) e.g. 9.2<br/>
CO2 EMISSIONS (g/km) e.g. 182 --> low --> 0<br/>

### Gradient Descent Optimizer
Gradient Descent is a learning algorithm that attempt to minimize some error.<br/> 
Our error is define as the **square of error**.<br/>
`loss = tf.reduce_min(tf.square(Y - Y1))` <br/>
`optimizer =tf.train.GradientDescentOptimizer(0.5)` Here the training step is defined. <br/>
The aim is to minimise the value of the error **loss**. <br/>
`sess = tf.Session()` Connect session to execution <br/> 
`tf.global_variables_initializer()` **???Initialize global variables**.<br/>
`sess.run(init)` Run the graph with initialized variables <br/>
`for step in range(100):`
`   _, loss_val, a_val, b_val = sess.run([train, loss, a, b])` Train in 100 iterations
