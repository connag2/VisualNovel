################################################################################
## PROLOGUE 02
## 처음 스친 사람
################################################################################

label PROLOGUE_02:

    $ current_scene = "PROLOGUE_02"

    scene bg hallway_day
    with dissolve

    "복도는 생각보다 훨씬 활기찼다."

    play sound SE_FOOTSTEP

    "체육복 차림으로 뛰어가는 학생."

    "창문을 여는 반장."

    "숙제를 베끼는 친구들."

    "모두에게는 평범한 아침이었다."

    "나만 조금 다른 하루."

    show seojin normal at center
    with dissolve

    s "(2학년 2반...)"

    "교실을 찾으며 복도를 둘러봤다."

    "그때."

    hide seojin

    show yuna smile at far_right
    with dissolve

    "복도 끝에서 누군가 나를 발견했다."

    show yuna smile at center
    with move

    y "앗!"

    y "잠깐만요!"

    show seojin normal at center_left
    with dissolve

    s "응?"

    y "혹시 전학생 맞죠?"

    s "맞는데."

    y "우와!"

    y "진짜 전학생이다!"

    y "생각보다..."

    "그녀는 내 얼굴을 빤히 바라봤다."

    s "생각보다?"

    y "...엄청 평범하게 생겼어요."

    "순간 정적."

    y "아."

    show yuna awkward
    with dissolve

    y "죄송해요!!"

    y "저 원래 생각나는 대로 말해서..."

    s "...하하."

    s "괜찮아."

    show yuna smile
    with dissolve

    y "다행이다!"

    y "아, 저는 유—"

    play sound SE_BELL

    "딩동댕동."

    "8시 20분입니다."

    show yuna surprised
    with dissolve

    y "......"

    y "......"

    y "꺄아악!!"

    y "지각이다!!"

    hide yuna
    with moveoutright

    "그녀는 바람처럼 복도 끝으로 사라졌다."

    show seojin normal at center
    with dissolve

    s "이름도 못 들었네..."

    "나는 작게 웃으며 2학년 2반 문 앞에 섰다."

    play sound SE_DOOR

    "똑."

    "교실 안에서 '들어오세요.' 하는 목소리가 들렸다."

    jump C1_01