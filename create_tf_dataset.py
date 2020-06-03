from Segmentation.utils.data_loader import create_OAI_dataset
import os

if __name__ == "__main__":
    folder = 'valid'
    use_2d = False

    train = (folder == 'train')
    str_dim = "" if use_2d else "_3d"

    if not os.path.exists('./Data/tfrecords/'):
        os.makedirs('./Data/tfrecords/')
    if not os.path.exists(f'./Data/tfrecords/{folder}{str_dim}'):
        os.makedirs(f'./Data/tfrecords/{folder}{str_dim}')

    create_OAI_dataset(data_folder="./Data/" + folder,
                       tfrecord_directory="./Data/tfrecords/" + folder + str_dim,
                       get_train=train,
                       use_2d=use_2d)
