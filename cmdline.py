import os
import sys
import atexit
import sqlite3_regist as reg
import dev_json as dev


def cmdline():
    topic = int(input('숫자를 입력해주세요 ( 1.디바이스정보 만들기  2.디바이스 등록  3.디바이스 조회  4.종료) \n:'))
    print(topic, '를 선택하셨습니다.')
    if topic == 1:
        print("디바이스 정보를 생성합니다.")
        a = dev.regist()
        a.make_json()
        while True:
            qq = input('json을 생성하시겠습니까? (Y/N) :')
            if qq == 'y' or qq == 'Y':
                a.write_json()
                break
            elif qq == 'n' or qq == 'N':
                break
        cmdline()
    elif topic == 2:
        print("디바이스 정보를 데이터베이스에 저장합니다.")
        reg.insert()
        cmdline()
    elif topic == 3:
        print("디바이스 정보를 조회합니다.")
        reg.search()
        cmdline()
    elif topic == 4:
        print("프로그램을 종료합니다.")
        sys.exit()
    else:
        print("다시 선택해주세요.")
        cmdline()
    # clear = lambda: os.system('cls')
    # clear()
    # os.system('cls')

def close():
    reg.con.close()
    print('db closed')

atexit.register(close)

if __name__ == "__main__":
    cmdline()
