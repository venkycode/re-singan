from operator import imatmul, imod
import math
import torch
from SinGAN import functions
from SinGAN.imresize import imresize
from skimage import io as img
import torch.nn as nn
from SinGAN.manipulate import SinGAN_generate
import matplotlib.pyplot as plt
from SinGAN.logger import *
from config import get_arguments

def saveUpScaledImage(imageName,deepFreeze=0):
    
    print('%f' % pow(in_scale, iter_num))
    print('Super Res by %f'%pow(in_scale, iter_num), imageName)
    Gs= torch.load("./TrainedModels/2_crop/scale_factor=0.793701,alpha=100/Gs.pth")
    NoiseAmp= torch.load("./TrainedModels/2_crop/scale_factor=0.793701,alpha=100/NoiseAmp.pth")
    reals= torch.load("./TrainedModels/2_crop/scale_factor=0.793701,alpha=100/reals.pth")
    Zs_sr = []
    reals_sr = []
    NoiseAmp_sr = []
    Gs_sr = []
    real = functions.np2torch( img.imread('./train_resized_clean/%s'%(imageName)),opt )    #reals[-1]  # read_image(opt)
    print("input size-> " , real.shape)
    real_ = real
    opt.scale_factor = 1 / in_scale
    opt.scale_factor_init = 1 / in_scale
    for j in range(1, iter_num + 1, 1):
        real_ = imresize(real_, pow(1 / opt.scale_factor, 1), opt)
        reals_sr.append(real_)
        Gs_sr.append(Gs[-1])
        NoiseAmp_sr.append(NoiseAmp[-1])
        z_opt = torch.full(real_.shape, 0, device=opt.device)
        m = nn.ZeroPad2d([3,2,3,2])
        z_opt = m(z_opt)
        Zs_sr.append(z_opt)
    out = SinGAN_generate(Gs_sr, Zs_sr, reals_sr, NoiseAmp_sr, opt, in_s=reals_sr[0], num_samples=1, imageName=imageName)
    out = out[:, :, 0:int(opt.sr_factor * real.shape[2]), 0:int(opt.sr_factor * real.shape[3])]
    print("output size-> " , out.shape)
    dir2save = functions.generate_dir2save(opt,deepFreeze)
    
    plt.imsave('%s/%s_HR_test.png' % (dir2save,imageName[:-4]), functions.convert_image_np(out.detach()), vmin=0, vmax=1)



if __name__ == '__main__':
    parser = get_arguments()
    parser.add_argument('--input_dir', help='input image dir', default='Input/Images')
    parser.add_argument('--input_name', help='training image name', default="33039_LR.png")#required=True)
    parser.add_argument('--noisy_input_name', help='training image name', default="33039_LR.png")
    parser.add_argument('--sr_factor', help='super resolution factor', type=float, default=4)
    parser.add_argument('--mode', help='task to be done', default='SR')
    parser.add_argument('--custom_sr_alpha',help='alpha for custom sr',type=int,default=100)
    parser.add_argument('--train_on_last_scale',help='train noisy image exclusively on last scale',type=int,default=0)
    parser.add_argument('--frozenWeight',help='weight for adverserial loss by frozen discriminator',type=float,default=1)
    parser.add_argument('--training_name',help='add name to the training',type=str,default='')
    parser.add_argument('--skip_training',help='skips training on clean image',type=int,default=0)
    parser.add_argument('--tx',help='timstamp',default='')
    opt = parser.parse_args()
    opt = functions.post_config(opt)
    print(type(opt.custom_sr_alpha),opt.custom_sr_alpha)
    opt.alpha=opt.custom_sr_alpha
    logger.initiate(opt)
    logger.log_('seed-> %d'%(opt.manualSeed))
    x=datetime.datetime.today()
    x= x.strftime("%b-%d-%Y-%H:%M:%S")
    x=x[-8:] #time of starting
    opt.tx=x

    logger.log_(opt.__repr__())
    Gs = []
    Zs = []
    Ds=[]
    reals = []
    NoiseAmp = []
    dir2save = functions.generate_dir2save(opt)
    
    if dir2save is None:
        print('task does not exist')
    #elif (os.path.exists(dir2save)):
    #    print("output already exist")
    else:
        try:
            os.makedirs(dir2save)
        except OSError:
            pass

        mode = opt.mode
        in_scale, iter_num = functions.calc_init_scale(opt)
        opt.scale_factor = 1 / in_scale
        opt.scale_factor_init = 1 / in_scale
        real = functions.read_image(opt)
        opt.min_size = 18
        real = functions.adjust_scales2image_SR(real, opt)

        Gs = []
        Ds = []
        Zs = []
        reals = []
        NoiseAmp = []
        saveUpScaledImage(opt.input_name)        