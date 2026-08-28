################################################################################
## CHAPTER 1
## C1_01 : 새로운 반 (PART 1)
## 분위기 : 봄 / 청춘 / 힐링
################################################################################

label C1_01:

    $ current_scene = "C1_01"

    stop music fadeout 1.0

    scene black
    with Fade(1.0, 0.5, 1.0)

    "사람은 이상한 존재다."

    "처음 보는 풍경인데도."

    "가끔은 오래전부터 알고 있었던 것처럼 느껴질 때가 있다."

    "그 감각의 이름이 익숙함인지."

    "아니면 단순한 착각인지는."

    "나도 아직 잘 모르겠다."

    scene bg school_gate_day
    with fade

    play music BGM_SPRING fadein 2.5

    "따뜻한 바람이 셔츠 깃을 스쳐 지나갔다."

    "벚꽃잎 하나가 천천히 허공을 돌며 내려앉았다."

    play sound SE_BELL

    "딩동댕동—"

    "운동장 너머에서 울린 종소리가 학교 전체를 깨웠다."

    "학생들은 삼삼오오 웃으며 교문 안으로 들어갔다."

    "누군가는 친구를 부르고."

    "누군가는 숙제를 베끼느라 허둥댔다."

    "그리고."

    "나는 교문 앞에 멈춰 서 있었다."

    show seojin normal at center
    with dissolve

    s "(청운고...)"

    "가슴에 달린 새 이름표."

    "윤서진."

    "이름은 그대로인데."

    "모든 게 처음이었다."

    s "(심호흡.)"

    "후우..."

    "긴장하지 말자."

    "평범하게 지내면 된다."

    "친구도 사귀고."

    "수업도 듣고."

    "그냥, 평범하게."

    hide seojin
    with dissolve

    "나는 천천히 교문 안으로 걸음을 옮겼다."

    ########################################################################
    ## 등굣길
    ########################################################################

    scene bg school_path_day
    with dissolve

    "학교로 이어지는 벚꽃길."

    "양옆의 나무에서는 꽃잎이 비처럼 흩날리고 있었다."

    play sound SE_FOOTSTEP

    "사각."

    "운동화 밑창이 꽃잎을 밟는 소리가 유난히 선명했다."

    "앞에서는 두 여학생이 웃고 있었다."

    show student_girl smile at center_left
    show student_girl2 smile at center_right
    with dissolve

    sg1 "야, 오늘 급식 돈가스래!"

    sg2 "진짜? 그럼 매점 안 가도 되겠다."

    sg1 "아싸."

    hide student_girl
    hide student_girl2
    with dissolve

    "별것 아닌 대화."

    "그런데 이상하게."

    "그 평범함이 조금 부러웠다."

    "주머니 속 휴대폰이 짧게 진동했다."

    play sound SE_PHONE

    show phone mom at center
    with dissolve

    "『엄마』"

    "첫날이니까 너무 긴장하지 말고."

    "끝나면 전화해 :)"

    hide phone
    with dissolve

    s "(...응.)"

    "답장은 하지 않았다."

    "대신 휴대폰을 조용히 주머니에 넣었다."

    ########################################################################
    ## 복도
    ########################################################################

    scene bg hallway_day
    with dissolve

    "2학년 복도."

    "생각보다 훨씬 시끄러웠다."

    play sound SE_FOOTSTEP

    "체육복 차림으로 뛰어가는 학생."

    "창문을 열며 환기하는 반장."

    "복사물을 안고 달리는 선생님."

    "전부에게는 평범한 월요일."

    "나만 조금 다른 하루."

    "그때."

    show yuna smile at far_right
    with dissolve

    "복도 끝에서 누군가 이쪽을 발견했다."

    show yuna smile at center
    with move

    y "앗!"

    y "잠깐만요!"

    show yuna smile at center, double_hop
    "그녀는 작은 강아지처럼 폴짝폴짝 뛰어왔다."

    y "혹시 전학생 맞죠?"

    show seojin normal at center_left
    with dissolve

    s "응."

    y "우와!"

    y "진짜 전학생이다!"

    y "생각보다..."

    "그녀는 내 얼굴을 빤히 바라봤다."

    s "생각보다?"

    y "...엄청 평범하게 생겼어요."

    "잠깐의 정적."

    y "아."

    y "죄송해요!!"

    y "저 원래 생각나는 대로 말해서..."

    "양손으로 자기 입을 가린다."

    "얼굴이 순식간에 빨개졌다."

    s "...하하."

    s "괜찮아."

    y "진짜요?"

    s "응."

    y "휴..."

    y "다행이다."

    "그녀는 안도의 한숨을 내쉬더니 활짝 웃었다."

    y "아, 저는 유—"

    play sound SE_BELL

    "딩동댕동."

    "8시 20분입니다."

    y "......"

    y "......"

    y "꺄아아악!!"

    show yuna panic at center, shake
    with dissolve

    y "저 지각이에요!!"

    y "이따 봬요 전학생 선배!!"

    hide yuna
    with moveoutright

    "정말 바람처럼 사라졌다."

    show seojin normal at center
    with dissolve

    s "이름도 못 들었네..."

    "조금 전까지 시끄럽던 복도가."

    "갑자기 조용하게 느껴졌다."

    hide seojin
    with dissolve

    "복도 끝."

    "『2학년 2반』이라고 적힌 교실 문이 보였다."

    "나는 문 앞에서 교복을 한 번 정리했다."

    "그리고."

    "조심스럽게 문을 두드렸다."

    play sound SE_DOOR

    "똑."

    jump C1_01_PART2

label C1_01_PART2:
    "C1_01_PART2 씬 대기 중입니다."
    return
