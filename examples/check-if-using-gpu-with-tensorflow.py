# If using GPU, it usually prints like
#           Default GPU Device: /device:GPU:0

import tensorflow as tf 

if tf.test.gpu_device_name(): 

    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))

else:

   print("Please install GPU version of TF")
   
   
