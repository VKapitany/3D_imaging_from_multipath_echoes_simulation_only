# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:02:34 2020

@author: kapit
"""

import tensorflow as tf
import gc
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import matplotlib

# Define a function to clear the session and empty GPU memory, for when retraining models
def reset_keras(verbose=True):
    """Clears the GPU memory in the current session"""
    sess = tf.compat.v1.keras.backend.get_session()
    tf.compat.v1.keras.backend.clear_session()
    sess.close()
    tf.compat.v1.sess = tf.compat.v1.keras.backend.get_session()


    if verbose==True:
        print(gc.collect()) # if it's done something you should see a number being outputted
    else: 
        pass

    # use the same config as you used to create the session
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 1
    config.gpu_options.visible_device_list = "0"
    tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))
    
def fmse_iou(prediction,ground_truth,mask, k=0.5,acoustic=False,show=False):
    """
    Code to obtain the IOU/foreground MSE of 2 images given some binarising background mask

    Parameters
    ----------
    prediction : 2D array
        the predicted/reconstructed depth image
    ground_truth : 2D array
        the ground truth depth image
    mask : 2D array
        the background mask depth image
    k: float, binarising boundary; I used 0.5 for simulated data, 0.2 for radar and acoustic
    acoustic: boolean, used to present the acoustic data in a separate manner
    show : boolean, whether to plot an image of the 
        IOU. The default is False.

    Returns
    -------
    fmse : float, foreground MSE, basically:  mean squared error, 
        scaled according to the area of the union of the foregrounds.
    iou : float, intersection over union of prediction and ground
        truth, binarised using the mask.

    """

    pr = np.abs(mask-prediction)
    sorted_diff=sorted(pr.flatten())[-1] #find 95th percentile of the difference (should be a pixel in the silhuoette)
    epsilon=k*sorted_diff #binarising threshold = 1/2 of the 95th percentile difference
    pr[np.abs(pr)<=epsilon]=0
    pr[np.abs(pr)>epsilon]=1

    gt = np.abs(ground_truth-mask)
    sorted_diff=sorted(gt.flatten())[-1] #find 95th percentile of the difference (should be a pixel in the silhuoette)
    epsilon=k*sorted_diff #binarising threshold = 1/2 of the 95th percentile difference
    gt[np.abs(gt)<=epsilon]=0
    gt[np.abs(gt)>epsilon]=1

    union = pr+2*gt
    union_1 = union.copy()
    union_1[union>=1]=1

    select_pr = prediction.copy()
    select_pr[union_1==0]=0

    select_gt = ground_truth.copy()
    select_gt[union_1==0]=0

    number = len(np.where(union_1==1)[0])

    if show==True:
        if acoustic==False:
            plt.figure(figsize=(6,5),dpi=72)
            ax1 = plt.subplot(221)
            ax1.tick_params(direction='in')
            plt.imshow(prediction,vmin=0,cmap='viridis_r')
            plt.title('Reconstruction (R)')
            cbar=plt.colorbar()
            cbar.ax.tick_params(direction='in')
            cbar.set_label('Depth (m)',rotation=270,labelpad=12)
            ax1=plt.subplot(222)
            ax1.tick_params(direction='in')
            plt.title('Ground truth (G)')
            plt.imshow(ground_truth,cmap='viridis_r',vmin=0)
            cbar=plt.colorbar()
            cbar.ax.tick_params(direction='in')
            cbar.set_label('Depth (m)',rotation=270,labelpad=12)
            ax1=plt.subplot(223)
            ax1.tick_params(direction='in')
            plt.imshow(mask,vmin=0,cmap='viridis_r')
            plt.title('Background mask (M)')
            cbar=plt.colorbar()
            cbar.ax.tick_params(direction='in')
            cbar.set_label('Depth (m)',rotation=270,labelpad=12)
            ax1=plt.subplot(224)
            ax1.tick_params(direction='in')
            plt.imshow(union,cmap='binary',vmax=3)
            plt.title('IOU')
            cbar=plt.colorbar(ticks=[0,1,2,3])
            cbar.ax.tick_params(direction='in')
            cbar.ax.set_yticklabels([r'$\tilde{R}=\tilde{G}=0$', r'$\tilde{R}=1$', r'$\tilde{G}=1$', r'$\tilde{R}\tilde{G}=1$'])  # vertically oriented colorbar
            plt.show()
        elif acoustic==True:
            plt.figure(figsize=(6,5),dpi=72)
            ax1 = plt.subplot(221)
            ax1.tick_params(direction='in')
            plt.imshow(prediction,vmin=0,cmap='viridis')
            plt.title('Reconstruction (R)')
            cbar=plt.colorbar(orientation='vertical',mappable=plt.cm.ScalarMappable(cmap='viridis_r',norm=matplotlib.colors.Normalize(vmin=0, vmax=5)))
            cbar.set_label('Depth (m)')
            cbar.ax.tick_params(direction='in')
            ax1=plt.subplot(222)
            ax1.tick_params(direction='in')
            plt.title('Ground truth (G)')
            plt.imshow(ground_truth,cmap='viridis',vmin=0)
            cbar=plt.colorbar(orientation='vertical',mappable=plt.cm.ScalarMappable(cmap='viridis_r',norm=matplotlib.colors.Normalize(vmin=0, vmax=5)))
            cbar.set_label('Depth (m)')
            cbar.ax.tick_params(direction='in')
            ax1=plt.subplot(223)
            ax1.tick_params(direction='in')
            plt.imshow(mask,vmin=0,cmap='viridis')
            plt.title('Background mask (M)')
            cbar=plt.colorbar(orientation='vertical',mappable=plt.cm.ScalarMappable(cmap='viridis_r',norm=matplotlib.colors.Normalize(vmin=0, vmax=5)))
            cbar.set_label('Depth (m)')
            cbar.ax.tick_params(direction='in')
            ax1=plt.subplot(224)
            ax1.tick_params(direction='in')
            plt.imshow(union,cmap='binary',vmax=3)
            plt.title('IOU')
            cbar=plt.colorbar(ticks=[0,1,2,3])
            cbar.ax.tick_params(direction='in')
            cbar.ax.set_yticklabels([r'$\tilde{R}=\tilde{G}=0$', r'$\tilde{R}=1$', r'$\tilde{G}=1$', r'$\tilde{R}\tilde{G}=1$'])  # vertically oriented colorbar
            plt.show()

    fmse = (prediction.shape[0]*prediction.shape[1])/number*mean_squared_error(select_pr,select_gt)
    iou = len(np.where(union==3)[1])/len(np.where(union>0)[1])
    return fmse, iou
