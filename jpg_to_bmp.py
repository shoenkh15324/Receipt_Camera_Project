import glob
from PIL import Image
import os
from tqdm import tqdm


def jpg_to_bmp_func(cap):
     # 현재 스크립트 파일이 위치한 디렉토리 경로
     script_dir = os.path.dirname(os.path.abspath(__file__))

     # jpg 이미지가 있는 상대경로
     src_path = os.path.join(script_dir, 'captured_img')

     # bmp 이미지를 저장할 상대경로
     dst_path = os.path.join(script_dir, 'changed_img')
     
     if not os.path.isdir(dst_path):  # 만약 존재하지 않는다면 디렉토리 생성
        os.mkdir(dst_path)

     # jpg 이미지를 변환하여 bmp로 저장
     for jpg_path in tqdm(list(set(glob.glob(src_path+"*/*.jpg", recursive=True)))):
          img = Image.open(jpg_path)
          jpg_name = os.path.basename(jpg_path)
          bmp_name = os.path.join(dst_path, jpg_name.replace("jpg", "bmp"))
          img.save(bmp_name)
          
          