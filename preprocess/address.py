import pandas as pd
from geopy.geocoders import Nominatim

df_dong = pd.read_csv("../data/raw_data/KIKmix_20230701.csv")

# 법정동코드, 생성일자, 말소일자는 필요x
df_dong.drop(columns=['법정동코드', '생성일자', '말소일자'], inplace=True)
df_dong["주소"] = df_dong[["시군구명", "읍면동명", "동리명"]].fillna('').apply(lambda x: ' '.join(filter(None, x)), axis=1)

# 데이터프레임 주소값 추출
address= df_dong['주소']

# 주소 데이터 깔끔하게 다듬기
for i in range(len(address)):
    a = address[i].split(' ')
    address[i] = " ".join(a[0:4])

# 도로명주소 위도 경도 값으로 바꿔주기
geo_local = Nominatim(user_agent='South Korea')

# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y

    except:
        return [0,0]
    
# 주소를 위,경도 값으로 변환하기
latitude = []
longitude =[]

for i in address:
    latitude.append(geocoding(i)[0])
    longitude.append(geocoding(i)[1])

address_df = pd.DataFrame({'행정동코드': df_dong['행정동코드'],'시도명':df_dong['시도명'], '시군구명':df_dong['시군구명'], '읍면동명':df_dong['읍면동명'],'동리명':df_dong['동리명'], '위도':latitude,'경도':longitude})
address_df.to_csv('../data/hdong_with_lat_long.csv')