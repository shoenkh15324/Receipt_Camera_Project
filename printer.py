import subprocess
import cups
import os

def print_image():
     # 연결된 프린터 찾기
     printer_name=find_printer()
     
     if printer_name != None:
          # 현재 스크립트 파일이 위치한 디렉토리 경로
          script_dir = os.path.dirname(os.path.abspath(__file__))
          image_path=os.path.join(script_dir, 'captured_img')
     
          try:
               subprocess.run(['lp', '-d', printer_name, image_path], check=True)
               print("Print Success!")
          except subprocess.CalledProcessError as e:
               print("Error:", e)
     else:
          print("Error, No connected printer.")
        
def find_printer():
    try:
        conn = cups.Connection()
        printers = conn.getPrinters()

        if printers:
            printer_name = printers.keys()[0]  # 첫 번째 프린터의 이름을 가져옴
            print("Printer found:", printer_name)
            return printer_name
        else:
            print("No printer found.")
            return None
    except cups.IPPError as e:
        print("Error: Unable to connect to CUPS server:", e)
        return None
   