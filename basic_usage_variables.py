# DOES NOT WORK AT THE MOMENT

import tensorflow as tf

# Create a Variable, that will be initialized to the scalar value 0.
var = tf.Variable(0, name="counter")

# Create an Op to add one to `var`.

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# Variables must be initialized by running an `init` Op after having

# launched the graph.  We first have to add the `init` Op to the graph.
init_op = tf.initialize_all_variables()

# Launch the graph and run the ops.
with tf.Session() as sess:
    # Run the 'init' op
    sess.run(init_op)
    # Print the initial value of 'var'
    print sess.run(var)
    # Run the op that updates 'var' and print 'var'.
    for _ in range(3):
        sess.run(update)
        print sess.run(var)