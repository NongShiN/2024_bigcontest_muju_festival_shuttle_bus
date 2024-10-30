import pandas as pd
from tqdm import tqdm
import sys, os
import json
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from preprocess.dataload_preprocess import preprocess_od, preprocess_stay, preprocess_address, preprocess_visitor_city

# paths 파일 불러오기
with open('config.json', 'r', encoding='utf-8') as f:
    paths = json.load(f)

# 축제기간의 od 데이터 로드 함수
def load_od():
    df_od = pd.DataFrame()
    od_dir = paths['od_dir']

    address_df = load_address()
    # 무주군의 행정동코드 추출
    mooju = set(address_df[address_df['시군구명'] == '무주군']['행정동코드'])
    
    for dirpath, dirnames, filenames in os.walk(od_dir):
        for filename in tqdm(filenames, desc="load od data", unit="file"):
            if filename.endswith('.csv'):
                # 파일 이름에서 날짜 추출
                date_str = filename.split('_')[1]
                
                # 날짜가 20230902에서 20230910 사이인 파일만 처리
                if '20230902' <= date_str <= '20230910':
                    # 파일 경로 설정 및 CSV 읽기
                    file_path = os.path.join(dirpath, filename)
                    csv_data = pd.read_csv(file_path)
                    
                    # 전처리
                    filtered_data = preprocess_od(csv_data, mooju)

                    # 날짜에서 월일(MMDD) 부분 추출
                    mmdd_str = date_str[4:]  # 'YYYYMMDD'에서 마지막 네 자리 'MMDD' 추출
                    
                    # 동적으로 변수 생성 (예: df_0902)
                    globals()[f'df_{mmdd_str}'] = filtered_data
                    df_od = pd.concat([df_od, globals()[f'df_{mmdd_str}']])
    return df_od

# stay 데이터 로드 함수
def load_stay():
    df_stay = pd.DataFrame()
    stay_dir = paths['stay_dir']
    for dirpath, dirnames, filenames in os.walk(stay_dir):
        for filename in tqdm(filenames, desc="load stay data", unit="file"):
            if filename.endswith('.csv'):
                # 파일 이름에서 날짜 추출
                date_str = filename.split('_')[1]
                
                # 날짜가 20230902에서 20230910 사이인 파일만 처리
                if '20230902' <= date_str <= '20230910':
                    # 파일 경로 설정 및 CSV 읽기
                    file_path = os.path.join(dirpath, filename)
                    csv_data = pd.read_csv(file_path)
                    
                    # 전처리
                    filtered_data = preprocess_stay(csv_data)

                    # 날짜에서 월일(MMDD) 부분 추출
                    mmdd_str = date_str[4:]  # 'YYYYMMDD'에서 마지막 네 자리 'MMDD' 추출
                    
                    # 동적으로 변수 생성 (예: df_0902)
                    globals()[f'df_{mmdd_str}'] = filtered_data
                    df_stay = pd.concat([df_stay, globals()[f'df_{mmdd_str}']])
        return df_stay
    
# address 데이터 로드 함수
def load_address():
    address_path = os.path.join(paths['root_dir'], "address_with_lon_lat_final.csv")
    address_df = pd.read_csv(address_path)

    address_df = preprocess_address(address_df)
     
    return address_df



# visitor_city 데이터 로드 함수
def load_visitor_city():
    visitor_city_path = os.path.join(paths['root_dir'], "city_of_festival_visitors.csv")
    visitor_city_df = pd.read_csv(visitor_city_path)
    
    visitor_city_df = preprocess_visitor_city(visitor_city_df)
    
    return visitor_city_df