def print_optimal_routes(optimal_routes, name):
    print(f"{name} 지역 최적의 셔틀 노선")
    if optimal_routes:
        # 최대 10개의 경로만 출력
        for i, (route, total_distance, total_time, total_weight, threshold) in enumerate(optimal_routes):
            if i == 10: 
                break
            
            # 순위 형식 고정 (5자리, 오른쪽 정렬)
            rank_formatted = f"{i+1}순위".rjust(5)

            # route가 리스트일 경우 문자열로 변환
            route_formatted = " -> ".join(route).ljust(50)  # 50자로 고정하여 왼쪽 정렬
            
            # 총 거리를 km로 변환하고 소수점 아래 두째 자리까지 포맷
            total_distance_km = total_distance / 1000  # 미터를 킬로미터로 변환
            total_distance_formatted = f"{total_distance_km:.2f} km".ljust(10)  # 10자로 고정

            # 총 시간을 시간과 분으로 변환 (반올림)
            total_time_hours = total_time // 60
            total_time_minutes = round(total_time % 60)
            total_time_formatted = f"{total_time_hours}시간 {total_time_minutes}분".ljust(10)  # 10자로 고정

            # 가중치와 threshold 형식 지정
            total_weight_formatted = f"{total_weight}".ljust(10)  # 10자로 고정
            threshold_formatted = f"{threshold:.2f}".ljust(10)    # 10자로 고정

            print(f"{rank_formatted} | 셔틀 노선: {route_formatted} | 총 거리: {total_distance_formatted} | 총 시간: {total_time_formatted} | 총 가중치: {total_weight_formatted} | threshold: {threshold_formatted}")
    else:
        print("유효한 경로가 없습니다.")
