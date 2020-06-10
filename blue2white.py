import PIL.Image as P
import os,sys
import numpy as np
import glob
import random
import time
class a_pic():
    def __init__(self,path):
        self.data=P.open(path)
        
        self.r, self.g, self.b = self.data.split() 
        #self.b = np.array(self.b).astype(np.uint8)
       # print(self.b)
       # exit()
        self.r = np.array(self.r).astype(np.uint8)
        self.g = np.array(self.g).astype(np.uint8)
        self.b = np.array(self.b).astype(np.uint8)
        self.data_x,self.data_y=self.r.shape
        self.data_copy_r=self.r
        self.data_copy_g=self.g
        self.data_copy_b=self.b
        self.start=time.time()
        self.get_blue()
    def get_blue(self):
        blue=np.where(self.b >200)
        self.ind=self.trans_idd(blue)
    def trans_idd(self,idd):
        ret=[]
        for x,y in zip(idd[0],idd[1]):
            ret.append([x,y])
        return np.array(ret)
    def run(self):
        for x,y in self.ind:
            self.data_copy_r[x][y]=255
            self.data_copy_g[x][y]=251
            self.data_copy_b[x][y]=240
    
    def save(self):
        self.data_copy=np.stack([self.data_copy_r,self.data_copy_g,self.data_copy_b])
        self.data_copy=np.transpose(self.data_copy,[1,2,0])
        print(self.data_copy.shape)
        img=P.fromarray(np.uint8(self.data_copy),mode='RGB')
        im_save=im.split(".jpg")[0]+"_rd.jpg"
        img.save(im_save)
        print("耗时%s 秒"%(time.time()-self.start))
if __name__=="__main__":
    im=sys.argv[1]
    A=a_pic(im)
    A.run()
    A.save()