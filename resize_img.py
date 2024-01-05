import os
from PIL import Image

def resize_bmp(new_width, new_height):
    try:
            # 현재 스크립트 파일이 위치한 디렉토리 경로
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            # bmp 이미지파일 상대경로
            input_path = os.path.join(script_dir, 'changed_img')
            output_path = os.path.join(script_dir, 'resized_img')
            
            # 'changed_img' 디렉토리가 없으면 생성
            changed_img_dir = os.path.join(script_dir, 'changed_img')
            if not os.path.exists(changed_img_dir):
                  os.makedirs(changed_img_dir)
          
            # 디렉토리에 대한 쓰기 권한 부여
            os.chmod(input_path, 0o777)
            os.chmod(output_path, 0o777)
            
            # BMP 파일 열기
            img = Image.open(input_path)

            # 새로운 해상도로 리사이징
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # 새로운 파일로 저장
            resized_img.save(output_path)

            print(f"Resized successfully to {new_width}x{new_height}")
            
    except Exception as e:
            print(f"Error: {str(e)}")
          
resize_bmp(100, 100)