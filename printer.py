import os
import win32print

def list_printers():
     # 현재 시스템에 연결된 프린터 목록 출력
     printers = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)]
     print("Printers:", printers)
    
def print_file(printer_name):
     # 파일을 지정된 프린터로 인쇄
     try:
          # 현재 스크립트 파일이 위치한 디렉토리 경로
          script_dir = os.path.dirname(os.path.abspath(__file__))
          
          # bmp 이미지파일 상대경로
          file_path = os.path.join(script_dir, 'changed_img')
          
          print_job = win32print.OpenPrinter(printer_name)
          win32print.StartDocPrinter(print_job, 1, (file_path, None, "RAW"))
          win32print.StartPagePrinter(print_job)
          with open(file_path, "rb") as file:
               data = file.read()
               win32print.WritePrinter(print_job, data)
          win32print.EndPagePrinter(print_job)
          win32print.EndDocPrinter(print_job)
          win32print.ClosePrinter(print_job)
          print("Printing successful.")
          
     except Exception as e:
          print("Printing failed:", str(e))
