import os
import math

dir_ = 'dataset'

os.chdir(dir_)


def folder_maker(folder_names):
    """
    this functions creates a new folder

    params: folders: foldername
    return: none
    """

    for x in folder_names:
        # check if folder exist
        if not os.path.isdir(x):
            os.mkdir(x)
        else: pass


folder_names = ['test','train', 'train/with_mask', 'train/without_mask', 'test/with_mask', 'test/without_mask']

#folder_maker(folder_names)

with_mask_dir = os.listdir('with_mask')
without_mask_dir = os.listdir('without_mask')

# 12% of the data will be for the test dataset
test_size_with = math.ceil(len(with_mask_dir) * 12/100)
test_size_without = math.ceil(len(without_mask_dir) * 12/100)

def move_withRange(items, range, from_, to):
    """
    this function will moe the data from one dir to other

    params: items: the images
    params: range: number of data to move
    params: from_: directory from where the data to be moved
    params:    to: desired directory to move in the data

    """

    for img_name in items[:range]:
        os.replace('%s/%s' % (from_, img_name), '%s/%s' % (to, img_name))


#move_withRange(without_mask_dir, test_size_without, 'without_mask', 'test/without_mask')
#move_withRange(with_mask_dir, test_size_with, 'with_mask', 'test/with_mask')


def move(items, from_, to):
    for img_name in items:
        os.replace('%s/%s'%(from_, img_name), '%s/%s'%(to,img_name))

move(with_mask_dir, 'with_mask', 'train/with_mask')
move(without_mask_dir, 'without_mask', 'train/without_mask')

