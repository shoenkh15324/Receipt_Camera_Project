import bleak

import asyncio # 비동기 모듈 가져오기
from bleak import BleakScanner # bleak의 Scanner가져오기

async def main(): # 비동기 함수 정의
     devices = await BleakScanner.discover() # 비동기 수행임을 알림
     for device in devices:
          print (device)
          
asyncio.run(main()) # main()함수가 비동기적으로 수행될 것임을 알림