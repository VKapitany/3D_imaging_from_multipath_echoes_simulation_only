# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:10:49 2020

@author: kapit
"""
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Conv1D, UpSampling2D, Input



def simulation_nn(feats, kern_int_e, kern_int_d, kern_reg, kse, ksd, summary=True):
    """Returns the neural network architecture used in the simulations"""
    
    input_size=200

    inp=Input(shape=(input_size,1))
    
    ###################################################################################################################
            # Encoding
    ###################################################################################################################
    conv1 = Conv1D(feats * 2, kse, activation='relu', padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_e)(inp)
    
    conv2 = Conv1D(feats * 4, kse, activation='relu', padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_e, strides=2)(
        conv1)
    
    conv3 = Conv1D(feats * 8, kse, activation='relu', padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_e, strides=2)(
        conv2)
    
    #######################add extra strides to see if 8x8--64 size is suitable two more conv strides or 4
    ###################################################################################################################
        # Latent
    ###################################################################################################################
    conv4 = Conv1D(feats * 16, kse, activation='relu', padding='same', kernel_regularizer=kern_reg, strides=2,
                    kernel_initializer=kern_int_e)(conv3)
    
    shape = tf.keras.layers.Reshape((5, 5, feats * 16))(conv4)
    
    tconv1 = Conv2D(feats * 16, ksd, activation='relu', padding='same', kernel_regularizer=kern_reg,
                    kernel_initializer=kern_int_d)(shape)
    ###################################################################################################################
    ###################################################################################################################
    #         Decoding
    ###################################################################################################################
   
    tconv2 = UpSampling2D(size=(2, 2))(tconv1)    
    tconv2 = Conv2D(feats * 8, ksd, activation='relu', padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_d)(tconv2)
    
    tconv2 = UpSampling2D(size=(2, 2))(tconv2)    
    tconv3 = Conv2D(feats * 4, ksd, activation='relu', padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_d)(tconv2)
    
    tconv3 = UpSampling2D(size=(2, 2))(tconv3)    
    tconv4 = Conv2D(feats * 2, ksd, activation='relu', padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_d)(tconv3)
    
    tconv4 = UpSampling2D(size=(2, 2))(tconv4)    
    tconv5 = Conv2D(feats, ksd, activation='relu', padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_d)(tconv4)
   
    ###################################################################################################################
    ###################################################################################################################
    
    out = Conv2D(1, 1, padding='same', kernel_regularizer=kern_reg, kernel_initializer=kern_int_d)(tconv5)
    
    model = tf.keras.Model(inputs=inp, outputs=out)
    if summary==True:
        model.summary()
    return model
