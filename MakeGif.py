from PIL import Image
import glob
import os
from tqdm import tqdm

data_dir = 'data/imgs'
save_dir = 'results/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
img_list = sorted(glob.glob(data_dir + '/*.png'))  


def MakeGif(mode):
    try:
        img_0 = None
        imgs = []
        for i, path in tqdm(enumerate(img_list)):
            if i==0:
                img_0 = Image.open(path).convert(mode)
            else:
                img = Image.open(path).convert(mode)
                imgs.append(img)
        img_0.save('{}/{}.gif'.format(save_dir, mode), save_all=True, append_images=imgs, loop=0)
    except:
        print('ERROR: {} mode'.format(mode))


def main():
    MakeGif('L')
    MakeGif('P')
    MakeGif('RGB')
    MakeGif('RGBA')
    MakeGif('CMYK')
    MakeGif('YCbCr')
    MakeGif('HSV')
    MakeGif('I')
    MakeGif('F')


if __name__ == '__main__':
    main()