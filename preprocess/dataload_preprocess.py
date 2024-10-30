def preprocess_od(df, mooju):
    # dest_hdong_cd 값이 축제가 열리는 곳인 무주군 데이터만 필터링
    filtered_df = df[df['dest_hdong_cd'].isin(mooju)]

    #filtered_df = df[df['dest_hdong_cd'] == 4573025000]
    """#filtered_df = df[df['dest_hdong_cd'] == 4573025000]
    df = pd.merge(df, address[['행정동코드', '시도명', '시군구명']], 
                     left_on='dest_hdong_cd', right_on='행정동코드', how='left')

    # 병합 후 불필요한 '행정동코드' 컬럼 제거 (필요에 따라)
    df = df.drop(columns=['행정동코드'])

    filtered_df = df[df['시군구명'] == '무주군']

    filtered_df = filtered_df.drop(columns=['시도명', '시군구명'])"""

    # 타 지역에서 온 데이터만 필터링
    #filtered_df = filtered_df[~filtered_df['origin_hdong_cd'].isin(mooju)]

    # 체류목적이 3(쇼핑여가), 4(기타), 5(여행) 인경우만 
    filtered_df = filtered_df[(filtered_df['dest_purpose'] == 3) | 
                          (filtered_df['dest_purpose'] == 4) | 
                          (filtered_df['dest_purpose'] == 5)]

    return filtered_df

def preprocess_stay(df):

    filtered_df = df[(df['purpose'] == 0)]
    grouped_residents = filtered_df.groupby(['hdong_cd', 'date', 'age'])['stay_cnts'].sum().reset_index()

    return grouped_residents