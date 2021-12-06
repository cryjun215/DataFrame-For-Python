from save_weather_to_csv import save_weather_csv

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

saved_weather = save_weather_csv

def print_menu():
    print("1. 전체 지역 기온/습도 확인하기")
    print("2. 특별시/광역시 기온/습도 확인하기")
    print("3. 종료하기")
    get_num = input("메뉴 선택: ")
    return int(get_num)

def run():
    while 1:
        get_num = print_menu()
        if get_num == 1:
            df = pd.read_csv('weather.csv', index_col='point', encoding='UTF-8')
            font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
            mpl.rc('font', family=font_name)
            ax = df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
            ax.set_xlabel('도시', fontsize=12)
            ax.set_ylabel('기온/습도', fontsize=12)
            ax.legend(['기온', '습도'], fontsize=12)
            plt.show()
        elif get_num == 2:
            df = pd.read_csv('weather.csv', index_col='point', encoding='UTF-8')
            city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
            font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
            mpl.rc('font', family=font_name)
            ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
            ax.set_xlabel('도시', fontsize=12)
            ax.set_ylabel('기온/습도', fontsize=12)
            ax.legend(['기온', '습도'], fontsize=12)
            plt.show()
        elif get_num == 3:
            break
        else:
            print("잘못된 값이 입력되었습니다.")
run()
