import os
from PIL import Image

def resize_image(new_width, new_height):
    try:
            # 현재 스크립트 파일이 위치한 디렉토리 경로
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            # bmp 이미지파일 상대경로
            input_path = os.path.join(script_dir, 'captured_img', 'captured_000.bmp')
            output_path = os.path.join(script_dir, 'captured_img', 'captured_000.bmp')
            
            # BMP 파일 열기
            img = Image.open(input_path)

            # 새로운 해상도로 리사이징
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # 새로운 파일로 저장
            resized_img.save(output_path)

            print(f"Resized successfully to {new_width}x{new_height}")
            
    except Exception as e:
            print(f"Error: {str(e)}")
          
          