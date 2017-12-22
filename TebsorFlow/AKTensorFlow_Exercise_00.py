# import os
# import numpy as np
# import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
#
#
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# step = 5
# x = tf.placeholder(dtype=tf.float32, shape=[step])
# y = tf.placeholder(dtype=tf.float64, shape=[step])
# inx = [0.5, 1.5, 2.6, 3.7, 4.9]
#
# with tf.Session() as sess:
#     testx, testy = sess.run([x, y], feed_dict={x: inx, y: inx})
#     print("inx(tf.float32)：", testx)
#     print("iny(tf.float64)：", testy)
#
# x_data = np.float32(np.random.rand(2, 100))
# y_data = np.dot([0.100, 0.200], x_data) + 0.300
#
#
# b = tf.Variable(tf.zeros([1]))
# W = tf.Variable(tf.random_uniform([1,2], -1.0, 1.0))
# y = tf.matmul(W, x_data) + b99999999



# state = tf.Variable(0, name='counter')
#
# # 创建op
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# # 初始化
# init_op = tf.global_variables_initializer()
#
# # 运行op
# with tf.Session() as sess:
#
#     sess.run(init_op)
#
#     try:
#
#         for _ in range(2):
#
#             sess.run(update)
#             print('===', sess.run(state))
#     except Exception as error:
#
#         print(error)

# matrix1 = tf.constant([[3., 3.]])
# matrix2 = tf.constant([[2.], [2.]])
#
# product = tf.matmul(matrix1, matrix2)
#
# sess = tf.Session()
#
# result = sess.run(product)
#
# print(result)
#
# sess.close()






























