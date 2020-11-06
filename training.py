#Importing libraries
import torch
import torch.nn as nn
from torchvision.utils import make_grid
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, random_split
import numpy as np
import math

from DataPreprocessing import Preprocessing
from CNN import ResNet15, ResNet9

directory = 'dataset'

data = Preprocessing(path={ 'test':directory+'/test',
                            'train':directory+'/train'})

train_ds, test_ds = data.preprocessed_dataset()

# spiltting and creating batches of data
batch_size = 20
val_size = math.ceil(len(test_ds) * 20/100)
test_size = len(test_ds) - val_size

# splitting the data
val_ds, test_ds = random_split(test_ds, [val_size, test_size])

# creating data loader
train_dl = DataLoader(  train_ds, 
                        batch_size,
                        num_workers = 3,
                        shuffle = True,
                        pin_memory = True)

val_dl = DataLoader(    val_ds,
                        batch_size,
                        num_workers = 3,
                        pin_memory = True)


x, y = next(iter(train_dl))

# visualizing
fig, ax = plt.subplots(figsize = (12,12))
ax.imshow(make_grid(x[:10], nrow=10).permute(1,2,0))
x.shape

