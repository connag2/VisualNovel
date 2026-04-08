# Chapter 2 start file
# 기존 Scene 30 마지막 return 대신
#     jump chapter2_start
# 를 넣으면 바로 이어집니다.

label chapter2_start:

    # ---------------------------------------------------------
    # Scene 31
    scene black with fade
    centered "{size=40}Scene 31{/size}\n\n{size=30}축제 전야의 교실{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_group_fun.ogg" fadein 2.0

    "다음 날 아침 교실 문을 열자마자, 어제와는 다른 공기가 먼저 밀려왔다."
    "책상 배열은 그대로인데도 천장 가까이 매달린 장식과 창가에 세워 둔 안내판, 반쯤 완성된 꾸밈물들 때문에 교실 전체가 한층 더 빽빽하고 들뜬 공간처럼 보였다."
    play sound "audio/sfw_school_crowd.ogg" volume 0.6
    "복도에서도, 교실 안에서도 축제 이야기가 끊이질 않았다."
    "누가 어느 부스를 맡았는지, 어느 반 장식이 제일 화려한지, 오늘 안에 뭘 끝내야 하는지 같은 말들이 여기저기서 부딪히며 튀었다."
    stop sound fadeout 1.0

    th "축제가 정말 코앞까지 왔다."
    th "어제까지만 해도 그냥 같이 시간을 보내는 게 먼저였다면, 오늘은 그 시간이 조금 더 빠르게 흘러가는 느낌이다."

    show yuna grin at char_2 with dissolve
    show harin normal at left_mid with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    yn "좋아, 여러분!"
    yn "오늘의 목표는 깔끔합니다!"
    yn "하린 선배의 표정이 더 굳기 전에 미리미리 끝내기!"

    show harin annoyed at left_mid, react_tiny
    show gaeun laugh at right_mid, react_tiny
    show seola smile at char_4, react_tiny
    hr "내 표정을 작업 진척도 기준으로 쓰지 마."

    ge "근데 틀린 말은 아닌 것 같은데?"
    sa "응. 조금 전보다 이미 굳었어."

    show yuna laugh at char_2, excited_hop
    yn "보셨죠? 객관적 데이터입니다!"

    sj "아침부터 반장 놀리기 들어가네."

    "웃음이 퍼졌다."
    "그런데 웃는 와중에도 하린의 시선은 교실 뒤편 벽면과 책상 위 준비물 사이를 자꾸 오갔다."
    "마음이 다른 데 가 있는 사람처럼까지는 아니지만, 분명 평소보다 더 빠르게 확인하고 또 확인하는 눈이었다."

    hr "장난은 됐고, 일단 순서 다시 맞출게."
    hr "포스터 붙일 테이프, 가위, 색지, 마카, 예비 출력물까지 한 번에 빼 두자."

    play sound "audio/sfx_ui_click.ogg" volume 0.4
    "하린은 이미 적어 둔 체크리스트를 펼쳐 들었다."
    "반듯한 글씨와 깔끔하게 나뉜 항목들. 어제까지만 해도 그 정리벽이 조금 과한가 싶었는데, 오늘은 오히려 그 질서 덕분에 다들 덜 헤맸다."

    sj "이쯤 되면 네 체크리스트 없었으면 큰일 났겠다."

    show harin surprise at left_mid, react_tiny
    hr "…그 정도는 아니야."

    ge "아닌 척은."
    ge "너 없으면 우리 셋은 일단 떠들다가 십 분 보내고, 유나는 장식용 별 모양만 백 개 더 만들었을걸?"

    show yuna pout at char_2, react_tiny
    yn "왜요, 별 백 개면 엄청 예쁘잖아요."
    yn "그리고 서진 선배는 분명 옆에서 '적당히 해' 하면서도 같이 붙이고 있었을 거예요."

    sj "반박이 안 되네."

    show seola faint_smile at char_4 with dissolve
    sa "맞아."
    sa "이제는 다들 그렇게 움직일 것 같아."

    th "이제는."
    th "설아가 아무렇지 않게 붙인 그 두 글자가 이상하게 오래 남았다."
    th "처음엔 우연처럼 모였던 사람들이, 이제는 정말 각자 역할이 생긴 팀처럼 보인다."

    girl_a "와, 너네 반 진짜 준비 많이 했다."
    girl_b "특히 저 뒤쪽 진열 예쁘다. 누가 한 거야?"

    "잠깐 구경하러 들어온 다른 반 학생 둘이 교실 뒤편을 둘러보며 감탄했다."
    "별말 아닌 칭찬인데도, 하린의 어깨가 아주 미세하게 풀리는 게 보였다."

    ge "들었지? 칭찬이다."

    show harin smile with dissolve
    hr "…아직 다 안 끝났어."
    hr "그래도, 어제보단 나아졌네."

    show cg harin_small_smile with dissolve
    "그 말과 함께 스쳐 지나간 하린의 작은 미소는 아주 잠깐이었지만 분명했다."
    "억지로 만든 표정이 아니라, 애써 쌓아 온 게 조금은 형태를 갖췄다는 안도에서 나온 얼굴."

    scene bg classroom with dissolve
    show yuna smile at char_2 with dissolve
    show harin smile at left_mid with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    yn "좋아, 오늘은 진짜 잘될 것 같은 날이다!"
    yn "딱 느낌 왔어요!"

    sa "느낌이 너무 좋은 날은 가끔 빨리 지나가."

    "설아가 조용히 덧붙인 말에, 다들 순간만큼은 웃음을 멈췄다."
    "그 말 자체는 이상하지 않았다. 그냥 사소한 감상이었다."
    "그런데 축제가 가까워진 지금 듣고 나니, 괜히 하루가 더 빨라질 것만 같은 기분이 들었다."

    sj "그럼 더 아껴 써야겠네."
    sj "오늘 하루도."

    show yuna smile with dissolve
    yn "좋지."
    yn "그럼 시작하기 전에 약속!"
    yn "오늘도 끝나고 그냥 헤어지지 말기!"

    hr "아침부터 퇴근 후 계획 세우는 사람은 또 처음 보네."
    ge "근데 벌써 좋다."

    stop music fadeout 2.0

    # ---------------------------------------------------------
    # Scene 32
    scene black with fade
    centered "{size=40}Scene 32{/size}\n\n{size=30}손이 모자란 시간{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "점심시간이 가까워질수록 교실 뒤편은 점점 더 분주해졌다."
    "가위가 오가고, 마카 뚜껑이 열렸다 닫히고, 잘라 둔 종이 조각들이 책상 위에 차곡차곡 쌓였다."
    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "바스락, 사각."
    "손이 쉴 틈 없이 움직이는데도 이상하게 분위기는 나쁘지 않았다."

    show cg group_work_table with dissolve
    "한 책상에 자연스럽게 둘러앉은 다섯 사람의 손끝이 제각각 다른 일을 하고 있었다."
    "유나는 잘라 둔 장식을 넘겨주고, 하린은 순서를 확인하고, 설아는 가장 깔끔한 모서리를 골라 붙였고, 가은 선배는 전체 균형을 보며 색감을 맞췄다."
    "나는 그 사이를 메우듯 빈 곳을 채웠다."

    th "처음에는 누가 뭘 잘하는지 몰라서 우왕좌왕했는데."
    th "이제는 말하지 않아도 대충 손이 가는 방향이 같다."

    scene bg classroom with dissolve
    show yuna normal at char_2 with dissolve
    show harin normal at left_mid with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    play sound "audio/sfx_pen_click.ogg" volume 0.4
    hr "유나, 그 별 장식은 왼쪽이 아니라 가운데 쪽."
    hr "그리고 여긴 여백 조금 남겨야 해. 너무 꽉 차면 답답해 보여."

    show yuna pout at char_2, react_tiny
    yn "네에, 총감독님."
    yn "근데 이거 가운데도 예쁘고 왼쪽도 예쁜데요?"

    hr "둘 다 예쁜 것과, 지금 여기서 더 맞는 건 다른 문제야."

    ge "오, 나온다. 하린이 명언."
    sj "예쁨의 상대평가."

    show seola smile at char_4, react_tiny
    sa "조금 웃겨."

    "유나는 볼을 부풀린 채 장식을 다시 들었다 놓았다 하다가, 결국 하린이 말한 자리에 얌전히 붙였다."
    "그러고는 조금 떨어져서 고개를 갸웃하더니 곧바로 손바닥으로 책상을 짚었다."

    show yuna surprise at char_2, react_surprised
    yn "…어?"
    yn "잠깐, 진짜 이쪽이 더 낫네."

    show harin smile at left_mid with dissolve
    hr "그러니까."

    sj "방금 엄청 뿌듯해하는 표정이었어."

    show harin annoyed at left_mid, react_tiny
    show gaeun laugh at right_mid, react_tiny
    hr "안 했어."

    ge "했어. 아주 조용하게."

    "다들 웃었고, 하린은 부정하면서도 이번엔 굳이 더 말하지 않았다."
    "그 작은 승부욕조차 이제는 낯설지 않았다."

    play sound "audio/sfx_paper_cut.ogg" volume 0.5
    "그때, 가위질하던 설아의 손이 아주 잠깐 멈췄다."

    sj "왜 그래?"

    show seola surprise at char_4, react_tiny
    sa "아니."
    sa "밖이 조금 시끄러워서."

    play sound "audio/sfw_school_crowd.ogg" volume 0.35
    "열린 교실문 너머로 다른 반 학생들이 분주하게 오가는 소리가 들렸다."
    "웃는 소리, 누군가 뛰어가는 발소리, 멀리서 이름을 부르는 목소리."
    stop sound fadeout 0.8

    show yuna smile with dissolve
    yn "오늘 다들 들떠 있긴 해요."
    yn "축제 직전이면 원래 좀 붕 뜨잖아."

    sa "응. 알아."
    sa "그냥… 오늘은 조금 더 크게 들려."

    "설아는 그렇게 말하고 다시 종이에 시선을 내렸지만, 손끝은 전보다 아주 조금 더 신중해졌다."
    "하린도 그 변화를 느꼈는지, 체크하던 손을 멈추고 설아 쪽을 한 번 보았다."

    hr "잠깐 쉬었다 할래?"

    show seola normal with dissolve
    sa "아니. 괜찮아."
    sa "계속하면 괜찮아져."

    th "괜찮다고 말하는 목소리가 거짓처럼 들리진 않았다."
    th "다만, 정말 아무 일도 없다는 뜻으로 들리지도 않았다."

    ge "그럼 오 분만 템포 늦추자."
    ge "빨리 끝내는 것도 좋지만, 손 꼬이면 더 피곤해져."

    show yuna grin at char_2, react_tiny
    yn "좋아요. 잠깐 휴식 겸 오늘의 상태 체크!"
    yn "하린 선배는 긴장도 몇 점?"

    show harin sigh at left_mid, react_tiny
    hr "질문이 왜 그렇게 직설적이야."
    hr "…그래도 어제보단 덜해."

    ge "설아는?"

    show seola faint_smile at char_4 with dissolve
    sa "시끄럽긴 한데."
    sa "여기 안은 괜찮아."

    "설아가 '여기 안은'이라고 말하는 순간, 유나가 괜히 신난 얼굴로 나를 쳐다봤다."
    "안쪽 공기. 우리끼리. 준비실. 교실 뒤편."
    "그동안 몇 번이나 다른 말로 불렀던 감각이, 또 다른 이름 없이 그냥 공유되었다."

    show yuna smile with dissolve
    yn "좋다."
    yn "그 말."

    stop music fadeout 2.0

    # ---------------------------------------------------------
    # Scene 33
    scene black with fade
    centered "{size=40}Scene 33{/size}\n\n{size=30}복도 바깥의 말{/size}" with dissolve
    pause 1.5

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.5

    "점심이 끝나고 복도로 나가자, 축제 전날 특유의 열기가 그대로 밀려왔다."
    "평소보다 많은 포스터와 사인펜 냄새, 어디선가 테이프가 뜯기는 소리, 뛰어다니는 학생들."
    "복도는 그 자체로 들뜬 예고편 같았다."

    play sound "audio/sfw_school_crowd.ogg" volume 0.55
    "우리도 잠깐 필요한 걸 가지러 특별동 쪽으로 이동하고 있었는데, 앞서 걷던 유나가 갑자기 걸음을 늦췄다."
    stop sound fadeout 0.8

    show yuna normal at char_2 with dissolve
    show harin normal at left_mid with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    girl_a "저기 저 팀 또 같이 다닌다."
    girl_b "맨날 붙어 있지 않냐?"
    girl_a "근데 분위기 되게 묘해."
    girl_b "반장도 있고, 하얀 머리 걔도 있고… 좀 눈에 띄긴 해."

    "멀찍이 지나가던 다른 반 학생 둘의 목소리였다."
    "크게 악의적이지도, 그렇다고 완전히 무심하지도 않은 애매한 톤. 그래서 더 선명하게 들렸다."

    th "이제는 우리가 보기에도 자주 붙어 다닌다."
    th "그러니 남들이 그렇게 보는 것도 이상할 건 없다."
    th "그런데 막상 저 말이 바깥에서 들려오니, 이유 없이 마음이 한 번 걸렸다."

    show yuna pout at char_2, react_tiny
    yn "뭐야."
    yn "되게 이상하게 말하네."

    hr "신경 쓰지 마."
    hr "남이 뭘 보든 우리 할 일만 하면 돼."

    "하린은 단정하게 잘라 말했지만, 말끝이 평소보다 아주 조금 짧았다."

    show seola anxious at char_4, react_tiny with dissolve
    "설아는 아무 말도 하지 않았다."
    "다만 계단 난간 쪽으로 잠깐 시선을 피했다가, 다시 우리 쪽으로 돌아왔다."

    ge "그래도 너무 신경 쓰이면 재미없지."
    ge "그러니까 이렇게 생각하자."
    ge "요즘 우리가 좀 눈에 띄게 잘 지내긴 하나 보다, 하고."

    show yuna smile at char_2, react_tiny with dissolve
    yn "그건 맞긴 해요."
    yn "너무 보기 좋았나 보네."

    sj "회복 빠르네."

    show yuna grin with dissolve
    yn "저 원래 이런 쪽으로는 빨라요."
    yn "근데…"

    "유나는 설아를 한 번 보고 말을 고쳐 삼켰다."
    "늘 아무 생각 없이 툭툭 던지던 애가, 이번엔 아주 잠깐 멈춘 뒤 더 가벼운 표정을 골랐다."

    yn "다음엔 우리가 더 재밌는 얘기 해서 덮어버리면 되죠."

    show seola normal with dissolve
    sa "응."
    sa "그렇게 해 줘."

    "짧은 대답이었다."
    "그런데 설아가 그 말을 하는 동안, 오른손 손가락 끝이 교복 소매를 아주 약하게 움켜쥐었다 폈다."

    th "작은 반응이다."
    th "정말로 작아서, 모르는 척할 수도 있다."
    th "하지만 한 번 보인 이상, 이제는 전처럼 그냥 넘기기가 어렵다."

    play sound "audio/sfx_school_bell.ogg" volume 0.7
    "그때 다음 이동을 재촉하듯 예비종이 울렸다."
    stop sound fadeout 1.2

    hr "가자."
    hr "늦으면 또 복도 막혀."

    show gaeun smile at right_mid, react_tiny
    ge "응, 출발."

    show yuna smile at char_2, react_tiny
    show seola normal at char_4, react_tiny
    "다섯 사람의 걸음이 다시 맞춰졌다."
    "방금 스쳐 지나간 말은 뒤에 남았는데도, 이상하게 그 여운만은 우리 사이 어딘가에 따라붙는 기분이었다."

    stop music fadeout 2.0

    # ---------------------------------------------------------
    # Scene 34
    scene black with fade
    centered "{size=40}Scene 34{/size}\n\n{size=30}잠깐의 어긋남{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "방과 후, 다시 교실 뒤편에 모였을 때는 다들 아침보다 조금 더 지쳐 있었다."
    "그래도 손은 멈추지 않았다."
    "이쯤 되면 피곤함과 익숙함이 거의 같은 자리에 붙어 있었다."

    show harin normal at left_mid with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    th "유나만 아직 안 왔다."
    th "평소라면 제일 먼저 와서 오늘은 뭐부터 할 거냐고 떠들었을 텐데."

    hr "연락은?"

    sj "아까 이동수업 끝나고 잠깐 본 게 마지막이야."

    ge "곧 오겠지."
    ge "근데 확실히 유나 없으니까 시작 전 공기가 다르긴 하네."

    sa "조용해."
    sa "조금 너무."

    "설아의 말대로였다."
    "없어서 비는 자리라는 건 꼭 시끄러운 사람이 빠졌을 때만 느껴지는 건 아닌데, 유나는 이상하게 그 빈자리를 더 크게 만들었다."

    play sound "audio/sfw_running.ogg" volume 0.75
    "타닥, 타다닥—"
    stop sound

    show yuna flustered at char_2 with dissolve
    yn "죄송해요..! 늦었어요!"
    yn "선생님이 갑자기 심부름 시켜서— 아, 진짜 미치는 줄."

    show harin sigh at left_mid, react_tiny
    show gaeun laugh at right_mid, react_tiny
    show seola surprise at char_4, react_tiny
    hr "숨부터 고르고 말해."

    sj "드물게 정상적으로 늦네."

    show yuna pout at char_2, react_tiny
    yn "뭐예요, 평소엔 비정상적으로 늦는 사람처럼 말하네."

    ge "아예 늦는 일이 드물다는 뜻이지."
    ge "다들 너 기다리고 있었어."

    "가은 선배가 가볍게 말했지만, 그 순간 유나의 표정이 아주 잠깐 멈췄다."
    "장난으로 넘기려던 얼굴이 반 박자 늦게 다시 올라왔다."

    show yuna smile with dissolve
    yn "…헤헤. 그럼 제가 빨리 만회할게요."

    th "정말 잠깐이었다."
    th "하지만 그 짧은 틈이 괜히 눈에 남았다."

    hr "그럼 이거부터 부탁할게."
    hr "붙이는 순서만 맞추면 돼. 어렵진 않아."

    "하린은 평소보다 조금 더 부드러운 목소리로 말했다."
    "유나가 늦은 걸 탓하기보다, 다시 리듬 안으로 자연스럽게 들여놓으려는 말투였다."

    show yuna smile at char_2, react_tiny
    yn "오케이. 맡겨만 주세요."

    play sound "audio/sfx_paper_flutter.ogg" volume 0.45
    "다시 손이 움직이기 시작했다."
    "그리고 조금 전의 빈틈도, 표면적으로는 곧 메워졌다."

    "하지만 완전히 사라지진 않았다."
    "유나는 평소보다 더 밝게 굴었고, 하린은 평소보다 더 여러 번 순서를 확인했고, 나는 그런 둘을 평소보다 더 자주 보고 있었다."

    th "아주 작은 어긋남이다."
    th "별일 아닐 수도 있다."
    th "그런데 이상하게, 이제는 별일 아닌 것에도 먼저 시선이 간다."

    stop music fadeout 2.0

    # ---------------------------------------------------------
    # Scene 35
    scene black with fade
    centered "{size=40}Scene 35{/size}\n\n{size=30}끝나고 나면{/size}" with dissolve
    pause 1.5

    scene bg school_road_dusk with fade
    play music "audio/bgm_after_school_soft.ogg" fadein 2.0

    "오늘도 결국 끝까지 남았다."
    "해가 완전히 지기 직전의 길은 어제와 비슷했는데, 마음 한쪽만 조금 달랐다."
    "축제가 가까워진 만큼 기대도 커졌고, 동시에 그 이후를 떠올리는 순간도 늘어났다."

    play sound "audio/sfw_walking.ogg" volume 0.65
    "다섯 사람은 어제처럼 자연스럽게 같은 방향으로 걸었다."
    "누가 먼저 맞추지 않아도 발걸음이 비슷한 속도로 정리되는 게 이제는 너무 익숙했다."

    show yuna smile at char_2 with dissolve
    show harin normal at left_mid with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    ge "이제 진짜 얼마 안 남았네."
    ge "이상하다. 빨리 왔으면 좋겠다가도, 조금만 늦었으면 싶기도 하고."

    hr "준비하는 입장에선 빨리 오는 쪽이 더 편해."
    hr "이대로 계속 확인하다간 끝이 없을 것 같아서."

    yn "전 둘 다예요."
    yn "빨리 축제 왔으면 좋겠는데, 또 오면 너무 빨리 지나갈 것 같아."

    sa "응."
    sa "시작하면 끝도 같이 보이니까."

    "말이 끝나자, 잠깐 바람 소리만 들렸다."
    "누구도 일부러 분위기를 가라앉힌 건 아닌데, 다들 같은 지점을 한 번쯤 떠올린 얼굴이었다."

    sj "끝난 다음 얘기, 어제도 했잖아."
    sj "사소한 핑계 계속 만들기로."

    show yuna smile with dissolve
    yn "맞아요."
    yn "그러니까 끝 자체는 무서운 게 아닌데…"
    yn "이 좋은 시간이 그냥 한 번에 휙 지나가 버릴까 봐 그게 좀 아깝죠."

    show harin smile at left_mid, react_tiny
    hr "아까운 건 맞아."
    hr "요즘은 하루가 너무 빨라."

    show seola faint_smile at char_4 with dissolve
    sa "그래도 빨랐던 날이 더 오래 남을 때도 있어."
    sa "짧게 느껴졌다는 건, 그만큼 좋았다는 뜻이니까."

    th "설아는 가끔 이런 말을 너무 조용하게, 그런데도 정확하게 꺼낸다."
    th "그래서 듣고 나면 대답보다 여운이 먼저 남는다."

    ge "좋네."
    ge "그럼 축제 끝나도 기억에 남는 쪽으로 더 많이 만들자."

    show yuna grin at char_2, react_tiny
    yn "좋아, 그럼 내 목표 추가!"
    yn "축제 끝나고도 계속 모이기, 그리고 추억 더 만들기!"

    sj "목표가 점점 많아지는데."

    yn "많아야 재밌죠."

    "유나는 웃었지만, 웃는 얼굴 끝에 아주 얇은 조급함 같은 것이 스쳤다 사라졌다."
    "붙잡고 싶어서 더 크게 웃는 사람처럼."

    play sound "audio/sfw_cloth_moving.ogg" volume 0.45
    "바람이 스치며 설아의 머리카락을 가볍게 흔들었다."
    "하린은 손에 들고 있던 파일 가장자리를 괜히 한 번 더 맞췄고, 가은 선배는 그런 둘을 보고도 아무 말 없이 웃기만 했다."

    th "겉으로는 아무 문제도 없다."
    th "오늘도 같이 걸었고, 같이 웃었고, 내일도 같이 있을 거라고 자연스럽게 말한다."
    th "그런데 그래서 더 이상하다."
    th "이렇게 좋을수록, 언젠가 어긋나는 순간이 오면 더 크게 느껴질 것 같아서."

    show gaeun smile at right_mid, react_tiny
    ge "내일은 더 바쁠 거야."
    ge "그러니까 오늘은 다들 일찍 자. 진짜로."

    show harin normal at left_mid, react_tiny
    hr "그 말은 맞아."
    hr "축제 전날 컨디션 망치면 티 바로 나."

    show yuna pout at char_2, react_tiny
    yn "네에."
    yn "근데 단체방으로 한 번만 더 정리하고 자도 돼요?"

    sj "그 한 번이 보통 세 번쯤 되잖아."

    show yuna laugh at char_2, react_tiny
    yn "어떻게 알았지."

    "웃음이 났다."
    "방금 전까지의 얇은 침묵이 다시 조금 풀렸다."
    "그래도 완전히 없어지진 않았다."
    "마치 저녁 공기 속에 보이지 않게 섞여 있는 서늘함처럼, 가볍지만 분명하게 남아 있었다."

    stop sound fadeout 0.8
    stop music fadeout 2.0

    return
