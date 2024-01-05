import glob
from PIL import Image
import os
from tqdm import tqdm


def jpg_to_bmp_func(cap):
     src_path = r"C:\Users\mok07\Desktop\Study\Project\vscode\Receipt_Camera\captured_img" # jpg images path
     dst_path = r"C:\Users\mok07\Desktop\Study\Project\vscode\Receipt_Camera\changed_img" # bmp images path

     if not os.path.isdir(dst_path): # make dst dir if it's not existed
          os.mkdir(dst_path)

     for jpg_path in tqdm(list(set(glob.glob(src_path+"*/*.jpg", recursive=True)))):
          img = Image.open(jpg_path)
          jpg_name = jpg_path.replace("\\", "/").split("/")[-1]
          bmp_name = os.path.join(dst_path, jpg_name.replace("jpg", "bmp"))
          img.save(bmp_name)
          
          