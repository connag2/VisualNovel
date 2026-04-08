# Route Check Labels

label check_true_route:
    # 네 명 전원 구제 조건 점검
    if save_harin and save_yuna and save_seola and save_gaeun and true_route_key:
        jump ending_true_route
    else:
        jump check_bad_routes

label check_bad_routes:
    # 배드 엔딩 분기 처리
    jump ending_bad_total_collapse_01
