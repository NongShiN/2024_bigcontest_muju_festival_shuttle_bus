def print_optimal_routes(optimal_routes, name):
    print(f"{name}지역 최적의 셔틀 노선")
    if optimal_routes:
        for route, total_distance, total_time, total_weight, threshold in optimal_routes:
            # 총 거리를 km로 변환하고 소수점 아래 두째 자리까지 포맷
            total_distance_km = total_distance / 1000  # 미터를 킬로미터로 변환
            total_distance_formatted = f"{total_distance_km:.2f} km"

            # 총 시간을 시간과 분으로 변환 (반올림)
            total_time_hours = total_time // 60
            total_time_minutes = round(total_time % 60)

            print(f"최적의 셔틀 노선: {route} | 총 거리: {total_distance_formatted} | 총 시간: {total_time_hours}시간 {total_time_minutes}분 | 총 가중치: {total_weight} | threshold: {threshold:.2f}")
    else:
        print("유효한 경로가 없습니다.")