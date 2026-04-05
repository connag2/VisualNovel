# 캐릭터 정의 (script.rpy 파일의 최상단에 배치)
define sj = Character('서진', color="#c8c8c8")
define th = Character('서진', color="#999999", what_prefix="(", what_suffix=")")

define hr = Character('서하린', color="#a4c2f4")
define yn = Character('유나', color="#fce5cd")
define sa = Character('설아', color="#ffffff")
define ge = Character('민가은', color="#e6b8af")

define stu_a = Character('남학생 A', color="#999999")
define stu_b = Character('남학생 B', color="#999999")
define girl_a = Character('여학생 A', color="#999999")
define girl_b = Character('여학생 B', color="#999999")

# 여기서부터 본 게임 시작
label start:
    # ---------------------------------------------------------
    # [프롤로그 타이틀 띄우기]
    scene black with fade
    centered "{size=50}프롤로그{/size}\n\n{size=30}미지근한 온도{/size}" with dissolve
    pause 1.0

    scene bg morning_room with fade
    play music "audio/bgm_spring_morning.ogg" fadein 2.0

    th "사람과 사람 사이에는 적당한 온도가 있다."
    th "너무 차갑지도, 그렇다고 데일만큼 뜨겁지도 않은 '미지근한 온도'."
    th "나는 그 적당한 거리를 유지하는 데 꽤 익숙한 편이다."
    th "괜히 나섰다가 피곤해지는 건 딱 질색이니까. {w=0.5}그게 내 평범한 고교 생활의 모토다."

    scene bg classroom_ceiling with dissolve
    play sound "audio/sfx_school_bell.ogg"

    th "새 학기가 시작된 지도 어느덧 한 달."
    th "오늘도 변함없이 맑고 평화로운, 완벽한 하루가 시작된다."

    # ---------------------------------------------------------
    # [Scene 1 타이틀 띄우기]
    scene black with fade
    centered "{size=40}Scene 1{/size}\n\n{size=30}아침 등굣길{/size}" with dissolve
    pause 1.0

    scene bg school_gate with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.0

    "봄 햇살이 기분 좋게 내리쬐는 교문 앞. 누군가 내 등짝을 가볍게 툭 친다."

    show yuna smile at center with dissolve

    yn "서진 선배! 안녕! 오늘 웬일로 지각을 다 하셨대?"

    sj "어, 알람을 못 들어서. 오래 기다렸어?"

    show yuna laugh with dissolve
    yn "에이, 한 10분? 선배 오는 길이니까 겸사겸사 기다려준 거죠!"

    th "유나는 1학년 후배다. 언제나 에너지가 넘치고 장난기가 많아서, 가만히 있어도 주변이 시끄러워지는 타입."

    "그때, 뒤에서 같은 반 친구가 내 어깨를 치고 지나갔다."

    stu_a "야 윤서진! 너도 지각이냐? 나 먼저 뛰어간다!"

    sj "어, 넘어지지나 마라."

    "친구가 멀어지는 걸 보며 웃고 있는데, 내 교복 소매를 꾹 잡아당기는 손길이 느껴졌다."

    show yuna pout with dissolve
    yn "선배! 지금 나랑 얘기하고 있었잖아요. 시선 집중!"

    sj "알았어, 알았어. 미안."

    "유나는 볼을 살짝 부풀리더니, 교복 주머니에서 딸기맛 사탕을 꺼내 입에 쏙 넣었다."

    show yuna smile with dissolve
    yn "용서해 주는 대신 매점에서 바나나 우유 쏘기! 빨리 가요, 우리 진짜 지각하겠다!"

    "유나가 밝게 웃으며 내 팔을 잡아끈다."
    "아침부터 텐션이 높은 녀석이라 피곤하긴 해도, 뭐… 나쁘진 않다."

    # ---------------------------------------------------------
    # [Scene 2 타이틀 띄우기]
    scene black with fade
    centered "{size=40}Scene 2{/size}\n\n{size=30}아침 조회{/size}" with dissolve
    pause 1.0

    scene bg classroom with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.0

    "조회 시간 직전, 왁자지껄한 교실."

    show harin normal at center with dissolve

    "반장인 하린이는 오늘도 완벽하다."
    "단정하게 다려진 교복에, 먼지 하나 없이 깔끔하게 정돈된 책상. 그녀는 교탁 앞에서 칠판 당번 배정표를 작성하고 있었다."

    sj "좋은 아침. 반장님은 아침부터 바쁘네."

    hr "어, 안녕. 자리 앉아. 곧 선생님 들어오실 거야."

    "하린이는 시선도 마주치지 않은 채, 자를 대고 반듯하게 선을 그으며 대답했다."

    play sound "audio/sfx_pen_click.ogg"
    "딸깍, 딸깍."

    th "버릇인 걸까? 무언가 집중할 때면 저렇게 볼펜을 까딱거리곤 한다."

    "그때, 교실 뒷문을 열고 들어오던 남학생 둘이 장난을 치다 교탁을 살짝 건드렸다."
    "하린이가 긋고 있던 선이 1mm 정도 삐끗하게 빗나갔다."

    show harin sigh with dissolve
    hr "아…."

    "하린이는 아주 짧게 한숨을 쉬더니, 서랍에서 화이트를 꺼내 빗나간 선을 깔끔하게 지우기 시작했다."

    menu:
        "어떻게 할까?"
        
        "그냥 둬도 괜찮지 않냐고 묻는다.":
            sj "그냥 둬도 아무도 모를 것 같은데."
            
            show harin normal with dissolve
            hr "내가 알아. {w=0.3}게시판에 한 달 내내 붙어있을 건데, 지저분하면 보기 안 좋잖아."
            
            th "역시 깐깐한 반장님이다. 나는 가볍게 고개를 끄덕이고 돌아섰다."

        "내가 도와줄지 묻는다.":
            sj "종이 잡아줄까? 흔들리면 또 빗나갈라."
            
            show harin smile with dissolve
            hr "고맙지만 괜찮아. 거의 다 했어. 넌 얼른 네 자리에나 앉아."
            
            th "하린이가 옅게 미소 지으며 대답했다. 완벽주의자답게 자기 일은 남에게 안 맡기는 성격이다."

    hide harin with dissolve

    "나는 내 자리에 가방을 내려놓았다."
    "창밖으로 따뜻한 바람이 불어왔다. 아주 평범하고, 조금은 따분한 일상이다."

    # ---------------------------------------------------------
    # [Scene 3 타이틀 띄우기]
    scene black with fade
    centered "{size=40}Scene 3{/size}\n\n{size=30}쉬는 시간{/size}" with dissolve
    pause 1.0

    scene bg old_library with fade
    play music "audio/bgm_theme_seola.ogg" fadein 1.0

    "오후의 나른한 쉬는 시간. 나는 책을 반납하기 위해 인적이 드문 구관 도서관으로 향했다."
    "사람이 잘 오지 않는 이곳은 특유의 오래된 종이 냄새가 난다."

    show seola normal at center with dissolve

    "그리고 창가 쪽 구석 자리, 햇빛이 아스라히 떨어지는 곳에 설아가 앉아 있었다."
    "새하얀 머리카락과 묘한 붉은 눈동자. {w=0.3}언제 봐도 비현실적인 분위기를 풍기는 동급생이다."

    th "워낙 눈에 띄는 외모 탓에 주변에서 수군거리는 일이 잦지만, 본인은 별로 신경 쓰지 않는 것 같다."

    "복도를 지나가던 다른 반 학생들의 목소리가 열린 창문 틈으로 희미하게 들려왔다."

    stu_a "야, 저기 쟤 걔 아니야? 그 소문…"
    stu_b "쉿, 들리겠다. 가자 그냥."

    "설아는 읽고 있던 책에서 시선을 떼지 않았다."
    "다만, 목덜미로 내려앉은 햇살이 조금 따가웠는지 자신의 목 언저리를 가볍게 한두 번 긁적였을 뿐이다."

    menu:
        "어떻게 할까?"
        
        "조용히 목례만 하고 지나간다.":
            "나는 발소리를 죽여 걷다, 그녀와 우연히 시선이 마주쳤을 때 가볍게 고개만 끄덕였다."
            
            show seola smile with dissolve
            sa "……."
            
            "설아 역시 아주 희미하게 고개를 끄덕이더니 다시 책으로 시선을 돌렸다."
            th "침묵이 불편하지 않은, 이 적당한 거리가 나쁘지 않다."

        "창문을 조금 닫아준다.":
            "나는 밖에서 들려오는 소음이 거슬려, 설아의 자리 근처 창문을 반쯤 닫아주었다."
            
            show seola surprise with dissolve
            sa "…어?"
            
            sj "바람이 좀 불어서. 책 넘어가잖아."
            
            show seola normal with dissolve
            sa "…응. 고마워."
            
            th "설아가 나지막한 목소리로 대답했다. {w=0.3}여전히 말수는 적지만, 왠지 모르게 편안해 보인다."

    hide seola with dissolve
    "나는 도서관을 빠져나왔다. 고요하고 정적인, 아주 평화로운 시간이었다."

    # ---------------------------------------------------------
    # [Scene 4 타이틀 띄우기]
    scene black with fade
    centered "{size=40}Scene 4{/size}\n\n{size=30}방과 후{/size}" with dissolve
    pause 1.0

    scene bg rooftop_sunset with fade
    play music "audio/bgm_theme_gaeun.ogg" fadein 1.0

    "방과 후, 청소 당번을 적당히 끝내고 노을이 지는 옥상으로 올라왔다."
    "비밀스러운 나만의 아지트… 라고 생각했는데."

    show gaeun smile at center with dissolve

    ge "어라, 우리 후배님? 여기서 다 보네."

    "난간에 기대어 캔커피를 마시고 있던 가은 선배가 여유로운 미소로 나를 반겼다."
    "학교 최고 미인 중 한 명이자, 언제나 사람 좋은 웃음을 달고 다니는 다정한 선배."

    sj "선배, 또 청소 농땡이 치고 여기 올라와 계신 겁니까?"

    show gaeun laugh with dissolve
    ge "농땡이라니. 어른의 고독한 휴식 시간이라고 해둘래? {w=0.5}자, 여기 뇌물. 이거 마시고 나 본 건 비밀로 해줘."

    "선배가 주머니에서 온기가 남은 캔커피 하나를 꺼내 내 쪽으로 가볍게 던졌다."
    "가볍게 받아 든 커피를 만지작거리며 나도 난간 옆에 기대섰다."

    sj "매번 이렇게 여유로우시네요. 선배는 스트레스 같은 거 안 받으세요?"

    show gaeun smile with dissolve
    ge "에이, 내가 무슨 스트레스? 난 늘 행복한걸. 우리 후배님이 이렇게 귀엽게 챙겨주기도 하고."

    "선배가 장난스럽게 내 머리를 헝클어뜨리려 다가왔다."
    "내가 살짝 피하며 선배의 어깨를 가볍게 밀어내는 시늉을 하자—"

    show gaeun surprise with hpunch
    "콜록, 켁!"

    "선배가 갑자기 마시던 캔커피를 입에서 떼며 가볍게 기침을 했다."

    sj "어, 괜찮으세요? 사레들리셨어요?"

    show gaeun normal with dissolve
    ge "아… 응. 커피를 너무 급하게 마셨나 봐. 켁, 목에 뭐가 걸렸나?"

    "선배는 자신의 목을 가볍게 쓰다듬으며 아무렇지 않게 웃어 보였다."

    menu:
        "어떻게 할까?"
        
        "등을 두드려준다.":
            sj "조심 좀 하세요. 어른이 그것도 하나 제대로 못 마십니까."
            "내가 장난스럽게 타박하며 선배의 등을 가볍게 톡톡 두드려주었다."
            
            show gaeun smile with dissolve
            ge "앗, 아파라. 후배님 손맛 맵네. {w=0.3}진짜 괜찮다니까."
            th "선배는 여전히 사람 좋은 미소를 짓고 있었다."

        "그냥 농담으로 넘긴다.":
            sj "천천히 좀 드세요. 누가 안 뺏어 먹으니까."
            
            show gaeun laugh with dissolve
            ge "후배님이 내 거까지 뺏어 먹을까 봐 불안해서 그랬지! 얼른 마시기나 해."
            th "선배의 능청스러운 대답에 나도 픽 웃고 말았다."

    "노을이 길게 늘어지는 옥상."
    "선배와 주고받는 실없는 농담들이 공기 중으로 흩어졌다. 참으로 완벽한 방과 후의 풍경이다."
    
    return