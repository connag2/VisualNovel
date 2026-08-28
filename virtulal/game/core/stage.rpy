################################################################################
## STAGE SYSTEM
################################################################################

# -----------------
# 1. 고정 위치 규격
# -----------------
transform far_left:
    xalign 0.08
    yalign 1.0
    zoom 0.92

transform left:
    xalign 0.22
    yalign 1.0
    zoom 0.96

transform center_left:
    xalign 0.36
    yalign 1.0
    zoom 1.0

transform center:
    xalign 0.50
    yalign 1.0
    zoom 1.03

transform center_right:
    xalign 0.64
    yalign 1.0
    zoom 1.0

transform right:
    xalign 0.78
    yalign 1.0
    zoom 0.96

transform far_right:
    xalign 0.92
    yalign 1.0
    zoom 0.92

# -----------------
# 2. 등장 및 퇴장 연출
# -----------------
transform enter_left:
    xalign -0.2
    yalign 1.0
    linear 0.35 xalign 0.22

transform enter_right:
    xalign 1.2
    yalign 1.0
    linear 0.35 xalign 0.78

transform enter_center:
    alpha 0.0
    zoom 0.95
    linear 0.25 alpha 1.0 zoom 1.03

transform exit_left:
    linear 0.25 xalign -0.2 alpha 0.0

transform exit_right:
    linear 0.25 xalign 1.2 alpha 0.0

# -----------------
# 3. 특수 애니메이션 (Animation)
# -----------------
transform hop:
    easein 0.15 yoffset -30
    easeout 0.15 yoffset 0

transform double_hop:
    easein 0.12 yoffset -40
    easeout 0.12 yoffset 0
    easein 0.12 yoffset -40
    easeout 0.12 yoffset 0

transform shake:
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset 0

transform nod:
    easein 0.15 yoffset 20
    easeout 0.15 yoffset 0
