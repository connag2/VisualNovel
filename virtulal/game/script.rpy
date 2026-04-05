# ---------------------------------------------------------
# 1. 게임에서 사용할 캐릭터 정의
# ---------------------------------------------------------

# 윤서진 (주인공 - 일반 대사용)
define sj = Character('서진', color="#c8c8c8")
# 윤서진 (주인공 - 독백/속마음용)
define th = Character('서진', color="#999999", what_prefix="(", what_suffix=")")

# 히로인들
define hr = Character('서하린', color="#a4c2f4")
define yn = Character('유나', color="#fce5cd")
define sa = Character('설아', color="#ffffff")
define ge = Character('민가은', color="#e6b8af")

# 엑스트라 학생들
define stu_a = Character('남학생 A', color="#999999")
define stu_b = Character('남학생 B', color="#999999")
define girl_a = Character('여학생 A', color="#999999")
define girl_b = Character('여학생 B', color="#999999")

# ---------------------------------------------------------
# 2. 게임 시작
# ---------------------------------------------------------
label start:

    # ---------------------------------------------------------
    # Scene 00. 프롤로그
    # ---------------------------------------------------------
    
    # play music "bgm_empty_piano.ogg" fadein 2.0
    scene black with fade

    # [프롤로그: 미지근한 온도]
scene bg morning_room with fade
play music "audio/bgm_spring_morning.ogg" fadein 2.0

th "(사람과 사람 사이에는 적당한 온도가 있다.)"
th "(너무 차갑지도, 그렇다고 데일만큼 뜨겁지도 않은 '미지근한 온도'.)"
th "(나는 그 적당한 거리를 유지하는 데 꽤 익숙한 편이다.)"
th "(괜히 나섰다가 피곤해지는 건 딱 질색이니까. {w=0.5}그게 내 평범한 고교 생활의 모토다.)"

scene bg classroom_ceiling with dissolve
play sound "audio/sfx_school_bell.ogg"

th "(새 학기가 시작된 지도 어느덧 한 달.)"
th "(오늘도 변함없이 맑고 평화로운, 완벽한 하루가 시작된다.)"

# ---------------------------------------------------------
# [Scene 1. 아침 등굣길 - 유나와의 첫 만남]
scene bg school_gate with fade
play music "audio/bgm_lazy_afternoon.ogg" fadein 1.0

"봄 햇살이 기분 좋게 내리쬐는 교문 앞. 누군가 내 등짝을 가볍게 툭 친다."

show yuna smile at center with dissolve

yuna "서진 선배! 안녕! 오늘 웬일로 지각을 다 하셨대?"

sj "어, 알람을 못 들어서. 오래 기다렸어?"

show yuna laugh with dissolve
yuna "에이, 한 10분? 선배 오는 길이니까 겸사겸사 기다려준 거죠!"

th "(유나는 1학년 후배다. 언제나 에너지가 넘치고 장난기가 많아서, 가만히 있어도 주변이 시끄러워지는 타입.)"

"그때, 뒤에서 같은 반 친구가 내 어깨를 치고 지나갔다."

mob_boy "야 윤서진! 너도 지각이냐? 나 먼저 뛰어간다!"

sj "어, 넘어지지나 마라."

"친구가 멀어지는 걸 보며 웃고 있는데, 내 교복 소매를 꾹 잡아당기는 손길이 느껴졌다."

show yuna pout with dissolve
yuna "선배! 지금 나랑 얘기하고 있었잖아요. 시선 집중!"

sj "알았어, 알았어. 미안."

"유나는 볼을 살짝 부풀리더니, 교복 주머니에서 딸기맛 사탕을 꺼내 입에 쏙 넣었다."

show yuna smile with dissolve
yuna "용서해 주는 대신 매점에서 바나나 우유 쏘기! 빨리 가요, 우리 진짜 지각하겠다!"

"유나가 밝게 웃으며 내 팔을 잡아끈다."
"아침부터 텐션이 높은 녀석이라 피곤하긴 해도, 뭐… 나쁘진 않다."

# ---------------------------------------------------------
# [Scene 2. 아침 조회 - 하린과의 교차]
scene bg classroom with fade
play music "audio/bgm_noisy_hallway.ogg" fadein 1.0

"조회 시간 직전, 왁자지껄한 교실."

show harin normal at center with dissolve

"반장인 하린이는 오늘도 완벽하다."
"단정하게 다려진 교복에, 먼지 하나 없이 깔끔하게 정돈된 책상. 그녀는 교탁 앞에서 칠판 당번 배정표를 작성하고 있었다."

sj "좋은 아침. 반장님은 아침부터 바쁘네."

harin "어, 안녕. 자리 앉아. 곧 선생님 들어오실 거야."

"하린이는 시선도 마주치지 않은 채, 자를 대고 반듯하게 선을 그으며 대답했다."

play sound "audio/sfx_pen_click.ogg"
"딸깍, 딸깍."

th "(버릇인 걸까? 무언가 집중할 때면 저렇게 볼펜을 까딱거리곤 한다.)"

"그때, 교실 뒷문을 열고 들어오던 남학생 둘이 장난을 치다 교탁을 살짝 건드렸다."
"하린이가 긋고 있던 선이 1mm 정도 삐끗하게 빗나갔다."

show harin sigh with dissolve
harin "아…."

"하린이는 아주 짧게 한숨을 쉬더니, 서랍에서 화이트를 꺼내 빗나간 선을 깔끔하게 지우기 시작했다."

menu:
    "어떻게 할까?"
    
    "그냥 둬도 괜찮지 않냐고 묻는다.":
        sj "그냥 둬도 아무도 모를 것 같은데."
        
        show harin normal with dissolve
        harin "내가 알아. {w=0.3}게시판에 한 달 내내 붙어있을 건데, 지저분하면 보기 안 좋잖아."
        
        th "(역시 깐깐한 반장님이다. 나는 가볍게 고개를 끄덕이고 돌아섰다.)"

    "내가 도와줄지 묻는다.":
        sj "종이 잡아줄까? 흔들리면 또 빗나갈라."
        
        show harin smile with dissolve
        harin "고맙지만 괜찮아. 거의 다 했어. 넌 얼른 네 자리에나 앉아."
        
        th "(하린이가 옅게 미소 지으며 대답했다. 완벽주의자답게 자기 일은 남에게 안 맡기는 성격이다.)"

hide harin with dissolve

"나는 내 자리에 가방을 내려놓았다."
"창밖으로 따뜻한 바람이 불어왔다. 아주 평범하고, 조금은 따분한 일상이다."