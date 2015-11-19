import tensorflow as tf

# Create constant op that creates a 1x2 matrix.
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output of the constant op.

matrix1 = tf.constant([[3., 3.]])

# Create another constant that creates a 2x1 matrix.
matrix2 = tf.constant([[2.],[2.]])

# Create a 'matmul' op that takes in 'matrix1' and 'matrix2' as inputs.
# The returned value, 'product', represents the result of the matrix multiplication.
product = tf.matmul(matrix1, matrix2)

# Launch the default graph
sess = tf.Session()

# To run the matmul operation wer call the session 'run()' method, passing 'product'
# which represents the output of the matmuul() op. This indicates to the call that we
# want to get the output of the matmul op back.
#
# All inputs needed by the op are automatically run by the session. They typically
# are run in parallel.
#
# The call 'run(product)' thus causes the execution of three ops in the graph:
# the two constants and matmul.
#
# The output of the op is returned in 'result' as a numpy 'ndarray' object.
result = sess.run(product)
print result

# Close the session when we're done
sess.close()

# Alternate code for same functionality:
# with tf.Session() as sess:
#	result = sess.run([product])
#	print result