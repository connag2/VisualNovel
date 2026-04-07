# --- 1. 대화하는 사람을 추적 및 자동 포커스 파이썬 코드 ---
init python:
    speaking = None
    
    def speaker(name):
        def callback(event, **kwargs):
            global speaking
            if event == "begin":
                speaking = name
            elif event == "end":
                speaking = None
        return callback

    # 포커스(반투명화)를 부드럽게 적용해주는 클래스
    class FocusFunction:
        def __init__(self, char_tag):
            self.char_tag = char_tag
            
        def __call__(self, trans, st, at):
            # 아무도 말을 안 하거나 본인이 말할 땐 밝기 100%, 다른 사람이 말할 땐 40%
            target_alpha = 1.0 if (speaking == None or speaking == self.char_tag) else 0.4
            
            if trans.alpha is None:
                trans.alpha = 1.0
                
            # 부드러운 애니메이션 (서서히 어두워지고 서서히 밝아짐)
            if trans.alpha != target_alpha:
                diff = target_alpha - trans.alpha
                if abs(diff) < 0.05:
                    trans.alpha = target_alpha
                else:
                    trans.alpha += diff * 0.15
                    
            return 0.02 # 0.02초마다 부드럽게 갱신

# --- 2. 캐릭터 정의 (콜백 연결) ---
define sj = Character('서진', color="#c8c8c8")
define th = Character('서진', color="#999999", what_prefix="(", what_suffix=")")

# 각 캐릭터가 말할 때 작동하도록 speaker("태그")를 달아줍니다.
define hr = Character('서하린', color="#a4c2f4", callback=speaker("harin"))
define yn = Character('유나', color="#fce5cd", callback=speaker("yuna"))
define sa = Character('설아', color="#ffffff", callback=speaker("seola"))
define ge = Character('민가은', color="#e6b8af", callback=speaker("gaeun"))

define stu_a = Character('남학생 A', color="#999999")
define stu_b = Character('남학생 B', color="#999999")
define girl_a = Character('여학생 A', color="#999999")
define girl_b = Character('여학생 B', color="#999999")

default yuna_point = 0
default harin_point = 0
default seola_point = 0
default gaeun_point = 0

# --- 3. 대화 시 강조/반투명화 자동 트랜스폼 ---
transform auto_focus(char_tag):
    function FocusFunction(char_tag)


# --- 4. 화면 위치 조정을 위한 트랜스폼 정의 ---

# 1~2명 등장 시 사용할 기본 위치 (무릎을 가리기 위해 더 내리고(ypos 증가), 크기를 키움(zoom 증가))
transform left:
    xalign 0.18
    yalign 1.0
    zoom 1.16
    yoffset 28
transform center:
    xalign 0.5
    yalign 1.0
    zoom 1.16
    yoffset 28
transform right:
    xalign 0.82
    yalign 1.0
    zoom 1.16
    yoffset 28
transform center_lower:
    xalign 0.5
    yalign 1.0
    zoom 1.16
    yoffset 28

# 4명 동시 등장 시 사용할 위치
transform char_1:
    xalign 0.10
    yalign 1.0
    zoom 1.04
    yoffset 24
transform char_2:
    xalign 0.37
    yalign 1.0
    zoom 1.04
    yoffset 24
transform char_3:
    xalign 0.63
    yalign 1.0
    zoom 1.04
    yoffset 24
transform char_4:
    xalign 0.90
    yalign 1.0
    zoom 1.04
    yoffset 24

transform far_left:
    xalign 0.06
    yalign 1.0
    zoom 1.04
    yoffset 24

transform left2:
    xalign 0.24
    yalign 1.0
    zoom 1.08
    yoffset 26

transform center2:
    xalign 0.5
    yalign 1.0
    zoom 1.12
    yoffset 28

transform right2:
    xalign 0.76
    yalign 1.0
    zoom 1.08
    yoffset 26

transform far_right:
    xalign 0.94
    yalign 1.0
    zoom 1.04
    yoffset 24

transform idle_bounce:
    yoffset 0
    ease 0.28 yoffset -4
    ease 0.28 yoffset 0
    pause 0.18
    repeat

transform soft_bounce:
    yoffset 0
    ease 0.40 yoffset -3
    ease 0.40 yoffset 0
    pause 0.25
    repeat

transform tiny_bounce:
    yoffset 0
    ease 0.50 yoffset -2
    ease 0.50 yoffset 0
    pause 0.30
    repeat

transform excited_hop:
    yoffset 0
    ease 0.12 yoffset -12
    ease 0.12 yoffset 0
    ease 0.10 yoffset -6
    ease 0.10 yoffset 0

transform sway_soft:
    yoffset 0
    ease 1.2 yoffset -1
    ease 1.2 yoffset 0
    repeat


# --- 5. 이미지 정의 (크기 80% 축소 + 높이 보정 + 포커스 효과 모두 포함) ---

# [유나 이미지]
image yuna angry = At(Transform("images/yuna angry.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna pout = At(Transform("images/yuna pout.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna surprise = At(Transform("images/yuna surprise.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna vivid = At(Transform("images/yuna vivid.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna smile = At(Transform("images/yuna smile.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna laugh = At(Transform("images/yuna laugh.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna normal = At(Transform("images/yuna normal.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))

# [하린 이미지]
image harin normal = At(Transform("images/harin normal.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin sigh = At(Transform("images/harin sigh.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin faint_smile = At(Transform("images/harin faint_smile.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin surprise = At(Transform("images/harin surprise.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))

# [설아 이미지]
image seola normal = At(Transform("images/seola normal.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola surprise = At(Transform("images/seola surprise.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))

# [가은 이미지]
image gaeun normal = At(Transform("images/gaeun normal.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun smile = At(Transform("images/gaeun smile.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun laugh = At(Transform("images/gaeun laugh.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun surprise = At(Transform("images/gaeun surprise.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))

# 여기서부터 본 게임 시작
# [추가 이미지 별칭/호환 정의 - 실제 존재 리소스만 사용]
image yuna annoyed = At(Transform("images/yuna annoyed.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna anxious = At(Transform("images/yuna anxious.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna flustered = At(Transform("images/yuna flustered.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna grin = At(Transform("images/yuna grin.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna grip = At(Transform("images/yuna grip.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna happy = At(Transform("images/yuna happy.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna hollow = At(Transform("images/yuna hollow.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna sad = At(Transform("images/yuna sad.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna sigh = At(Transform("images/yuna sigh.webp", zoom=0.94, yoffset=-12), auto_focus("yuna"))
image yuna shock = "yuna surprise"
image yuna serious = "yuna normal"
image yuna soft = "yuna smile"
image yuna think = "yuna normal"
image yuna panic = "yuna surprise"

image harin angry = At(Transform("images/harin angry.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin annoyed = At(Transform("images/harin annoyed.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin anxious = At(Transform("images/harin anxious.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin flustered = At(Transform("images/harin flustered.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin happy = At(Transform("images/harin happy.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin hollow = At(Transform("images/harin hollow.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin sad = At(Transform("images/harin sad.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin smile = At(Transform("images/harin smile.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))
image harin vivid = At(Transform("images/harin vivid.webp", zoom=0.94, yoffset=-12), auto_focus("harin"))

image seola angry = At(Transform("images/seola angry.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola annoyed = At(Transform("images/seola annoyed.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola anxious = At(Transform("images/seola anxious.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola faint_smile = At(Transform("images/seola smile.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola flustered = At(Transform("images/seola flustered.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola happy = At(Transform("images/seola happy.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola hollow = At(Transform("images/seola hollow.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola sad = At(Transform("images/seola sad.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola sigh = At(Transform("images/seola sigh.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola smile = At(Transform("images/seola smile.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))
image seola vivid = At(Transform("images/seola vivid.webp", zoom=0.94, yoffset=-12), auto_focus("seola"))

image gaeun angry = At(Transform("images/gaeun angry.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun annoyed = At(Transform("images/gaeun annoyed.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun anxious = At(Transform("images/gaeun anxious.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun flustered = At(Transform("images/gaeun flustered.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun happy = At(Transform("images/gaeun happy.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun hollow = At(Transform("images/gaeun hollow.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun sad = At(Transform("images/gaeun sad.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun sigh = At(Transform("images/gaeun sigh.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))
image gaeun vivid = At(Transform("images/gaeun vivid.webp", zoom=0.94, yoffset=-12), auto_focus("gaeun"))

image bg classroom_day = "bg classroom"
image bg classroom_evening = "bg classroom"
image bg sunset_classroom = "bg classroom"
image bg hallway_day = "bg noisy_hallway"
image bg sunset_hallway = "bg noisy_hallway"
image bg sunset_stairs = "bg noisy_hallway"
image bg school_gate_evening = "bg school_gate"
image bg school_gate_sunset = "bg school_gate"
image bg road_evening = "bg school_road_dusk"
image bg crossroads_evening = "bg school_road_dusk"
image bg city_sidewalk_evening = "bg school_road_dusk"
image bg bus_stop_evening = "bg school_road_dusk"
image bg school_side_path_evening = "bg school_road_dusk"
image bg convenience_store_front = "bg store"
image bg convenience_store_front_evening = "bg store"
image bg convenience_store_inside = "bg store"
image bg school_backyard_evening = "bg school_gate"
image bg clubroom_afternoon = "bg old_library"

image cg seola_blueprint = "cg seola_design_discussion"

label start:
    # [프롤로그 타이틀]
    scene black with fade
    centered "{size=50}프롤로그{/size}\n\n{size=30}미지근한 온도{/size}" with dissolve
    pause 1.5

    scene bg dark_room with fade
    play music "audio/bgm_spring_morning.ogg" fadein 3.0

    "띠딕, 띠딕, 띠딕—"
    "규칙적이고 신경질적인 전자음이 고막을 찌른다."
    "나는 이불 밖으로 무거운 팔을 뻗어 휴대폰의 알람을 거칠게 껐다."
    play sound "audio/sfx_alarm_stop.ogg"
    
    "방 안은 다시 무거운 정적 속으로 가라앉았다. {w=0.5}암막 커튼 틈새로 얇고 날카로운 아침 햇살이 먼지와 함께 부유하고 있다."
    "침대에 가만히 누워, 천장의 무늬를 멍하니 맨눈으로 덧그렸다."
    
    th "사람과 사람 사이에는 적당한 온도가 있다."
    th "너무 차가우면 주위가 얼어붙어 고립되고, {w=0.3}너무 뜨거우면 결국 누군가는 화상을 입고 흉터가 남는 법이다."
    th "어릴 때는 그 뜨거움이 열정이나 진심인 줄 알았던 적도 있었다. 누군가의 삶에 깊게 관여하고, 내 속마음을 전부 털어놓고, 상처를 나누면 진정한 이해자가 될 수 있을 거라고 믿었던 멍청한 시절."
    th "하지만 결국 남는 건, 서로를 갉아먹다 파멸하는 결말뿐이었다."
    
    play sound "audio/sfw_walking.ogg"
    "나는 몸을 일으켜 느릿느릿 화장실로 향했다."
    "세면대의 차가운 물을 틀어 얼굴에 끼얹었다. {w=0.5}거울 속에는 살짝 피곤해 보이는, 어딜 가나 흔하게 볼 수 있는 평범한 남학생이 서 있다."
    
    th "그래서 나는, 그 누구와도 화상을 입지 않을 '미지근한 온도'를 유지하는 법을 배웠다."
    th "적당히 친절하고, 적당히 다정하게. {w=0.3}하지만 결정적인 순간에는 절대 선을 넘지 않는 것."
    th "괜히 타인의 진심이나 상처에 발을 들였다가 피곤해지는 건 딱 질색이니까. {w=0.5}그게 내 생존 방식이자, 이 평범한 고교 생활을 지탱하는 유일한 모토다."
    
    scene black with fade
    centered "{size=30}아침 등굣길{/size}" with dissolve
    scene bg school_road_morning with fade
    
    "집을 나서자 봄 특유의 훅 끼치는 따뜻한 공기가 뺨을 스쳤다."
    play sound "audio/sfw_walking.ogg"
    "거리에는 나와 같은 교복을 입은 학생들이 무리 지어 걸어가고 있었다."
    "어제 본 예능 프로그램 이야기, 새로 산 화장품 이야기, 피시방에서 올린 티어 이야기… {w=0.5}시시콜콜하고 가벼운 대화들이 벚꽃잎처럼 흩날린다."
    
    th "새 학기가 시작된 지도 어느덧 한 달이 지났다."
    th "서로 눈치를 보며 탐색하던 시기는 지나갔고, 교실 안의 무리는 어느 정도 견고하게 나뉘어 안정을 찾아가고 있다."
    
    "멀리, 언덕 위로 우리 학교인 사립 연화(蓮花) 고등학교의 깔끔한 신관 건물이 보이기 시작했다."
    "지역 최고 수준의 시설과 높은 명문대 진학률을 자랑하는, 겉보기엔 그야말로 흠잡을 데 없는 훌륭한 학교."
    
    th "물론, 그 완벽한 간판 이면에는 학생들 사이의 보이지 않는 숨 막히는 서열과 성적 압박, 그리고 잔인할 정도로 빠르게 도는 소문들이 폐쇄적인 생태계를 이루고 있지만."
    th "내가 그 압력 밥솥 같은 생태계의 중심에 설 일은 없다. 나는 그저 교실 뒷자리에 앉아 풍경처럼 존재하는 관찰자일 뿐이니까."
    
    scene black with dissolve
    centered "{size=30}연화 고등학교 교실{/size}" with dissolve
    scene bg classroom_ceiling with dissolve
    play sound "audio/sfx_school_bell.ogg"
    
    "학교 종이 울린다."
    "나는 내 자리에 앉아 창밖으로 시선을 돌렸다."
    "따뜻한 봄바람이 커튼을 둥글게 부풀렸다 가라앉힌다."
    
    th "오늘도 변함없이 맑고 평화로운 하루."
    th "누구와도 부딪히지 않고, 상처받지도, 상처 주지도 않을… {w=0.5}조금은 따분할 정도로 완벽하고 몽글몽글한 하루가 시작된다."
    th "적어도 나는, 이 일상이 영원할 거라고 믿고 싶었다."

    # ---------------------------------------------------------
    # Scene 1
    scene black with fade
    centered "{size=40}Scene 1{/size}\n\n{size=30}아침 등굣길{/size}" with dissolve
    pause 1.5

    scene bg school_gate with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "집에서 학교까지는 걸어서 대략 15분 남짓."
    "조금 이른 시간이라 그런지, 등교하는 학생들의 발걸음에는 아직 아침 특유의 나른한 여유가 묻어난다."
    play sound "audio/sfw_walking.ogg"
    "나 역시 밤공기의 서늘함이 채 가시지 않은 맑은 봄바람을 맞으며 천천히 걷고 있었다."
    "길가에 핀 벚꽃나무에서 연분홍빛 꽃잎들이 드문드문 떨어져 내리는, 꽤나 그림 같은 풍경이다."
    th "이맘때의 아침 공기는 사람을 묘하게 들뜨게 하는 구석이 있다."
    stop sound fadeout 1.0
    th "물론 나는 그런 분위기에 휩쓸려 오버하는 성격은 아니지만, 그래도 이런 쾌적한 아침이라면 학교 가는 길이 아주 끔찍하지만은 않다."
    "그렇게 학교 정문이 저만치 보일 무렵."

    play sound "audio/sfw_running.ogg" volume 0.8
    "타닥, 타다닥—!"
    "등 뒤에서부터 통통 튀는, 아주 가볍고 경쾌한 발소리가 빠르게 다가왔다."
    th "누군가 잰걸음으로 달려오는 소리. 굳이 뒤돌아보지 않아도 누군지 알 수 있다."
    th "내 좁고 평탄한 인간관계에서, 아침부터 이렇게 요란하고 에너지 넘치게 다가올 사람은 단 한 명뿐이니까."

    stop sound
    "탁!"
    play sound "audio/sfx_slap.ogg" volume 1.2
    with hpunch
    "아니나 다를까, 누군가 내 등짝을 제법 매운 손길로 찰싹 내려친다."
    show cg yuna_morning_surprise with dissolve
    yn "서진 선배! 안녕! 완전~ 좋은 아침!"
    "돌아보자, 햇살을 등지고 선 1학년 후배 유나가 특유의 반묶음 머리를 찰랑거리며 활짝 웃고 있었다."
    "달려오느라 살짝 상기된 두 뺨과 반짝거리는 눈동자. 그리고 언제나처럼 훅 풍겨오는 옅고 달콤한 딸기 샴푸 향기."
    sj "어, 안녕. 아침부터 기운도 넘치네. 등 뚫어지는 줄 알았다."
    
    # 캐릭터와 CG 겹침을 방지하기 위해 배경 초기화
    scene bg school_gate
    show yuna laugh at center_lower, idle_bounce with dissolve
    
    yn "에이, 선배가 아침부터 너무 흐물흐물하게, 영혼 가출한 좀비처럼 걷고 있으니까 후배로서 기합 좀 넣어준 거죠! 나 착하죠?"
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "유나는 내 앞으로 쏙 끼어들며 두 손으로 브이(V) 자를 그려 보였다."
    "조금 넉넉한 치수로 맞춘 탓에 손등을 반쯤 덮은 교복 소매가 그녀의 움직임에 맞춰 귀엽게 펄럭였다."
    th "유나는 언제나 에너지가 넘치고 장난기가 많아서, 가만히 옆에만 있어도 주변 공기마저 덩달아 밝아지게 만드는 타입이다."
    th "어쩌다 신학기 동아리 심부름으로 몇 번 엮인 이후부터, 녀석은 나를 자기 전담 장난감이라도 되는 양 쫄래쫄래 쫓아다니기 시작했다."
    th "처음엔 남의 영역에 거침없이 훅훅 들어오는 그 하이텐션이 좀 부담스러웠는데… 매일 아침 이렇게 강아지처럼 꼬리를 치며 나타나니 이젠 적응이 되어버렸다."
    sj "그래, 등짝 때려줘서 참 고맙다. 근데 너 방향 이쪽 아니지 않아? 1학년 건물은 반대쪽 언덕이잖아."
    show yuna pout at center_lower, sway_soft with dissolve
    yn "아, 진짜! 그게 뭐가 중요해요? 선배 오는 길목이니까 겸사겸사 마중 나온 거잖아요."
    yn "아침부터 이렇게 예쁘고 귀여운 후배 얼굴 짠! 하고 보면, 하루가 막 상쾌해지고 눈이 맑아지고 막 그러지 않아요?"
    "유나가 두 검지손가락으로 자기 볼을 콕 찌르며 과장되게 애교를 부린다."

    sj "상쾌하긴. 하도 옆에서 짹짹거려서 덜 깬 잠이 다 달아난다."
    show yuna smile at center_lower, tiny_bounce with dissolve
    yn "그거 칭찬이죠? 잠 깨워줬으니까 수고비로 매점에서 바나나 우유 쏘기! 약속!"
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "유나가 아주 자연스럽게 내 교복 마이 소매 끝자락을 꾹 잡아끌었다."
    "이런 스킨십에도 거침이 없다. 나는 체념한 듯 픽 웃으며 유나의 잰발걸음에 맞춰 걷는 속도를 올렸다."

    "그때였다."
    girl_a "어, 윤서진! 너도 이제 오냐?"

    "옆을 지나가던 같은 반 여학생 무리 중 한 명이 나를 향해 손을 흔들었다. 며칠 전 수행평가 프린트물을 빌려준 적이 있는 녀석이다."
    sj "어, 안녕. 먼저 들어가."

    "가볍게 손을 들어 인사를 받아주고 다시 고개를 돌린 순간."
    show yuna pout at center_lower, sway_soft with dissolve
    "내 소매를 쥐고 있던 유나가 갑자기 입술을 삐죽 내밀며 볼을 빵빵하게 부풀리고 있었다."
    sj "유나야? 갑자기 표정이 왜 그래."

    yn "…방금 저 선배 누구예요? 되게 친하게 인사하네."
    sj "친하긴. 그냥 짝꿍이라 숙제 몇 번 물어보고 프린트 빌려준 게 다야."
    yn "흐응~ 그냥 짝꿍? 선배는 참 발도 넓다니까. 나한테만 다정한 줄 알았더니 완전 만인의 연인이었어."
    sj "무슨 헛소리야. 너 아침 안 먹었지? 헛것이 보이나 본데."
    show yuna laugh at center_lower, idle_bounce with dissolve
    yn "아하하, 농담이에요 농담! 선배가 나 말고 다른 사람 챙기는 거 보니까 아주 조~금 질투 나서 그랬죠."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "유나는 금세 장난스러운 미소를 되찾더니, 교복 주머니를 뒤적거렸다."
    "그러고는 예의 그 투명한 비닐에 싸인 딸기맛 사탕을 두 개 꺼내어, 하나를 내 눈앞에 들이밀었다."
    yn "자, 아~ 하세요! 아침부터 당 떨어지면 안 되니까."

    sj "됐다, 아침부터 단 거 먹으면 입 텁텁해. 너나 먹어."
    show yuna pout at center_lower, sway_soft with dissolve
    yn "아, 진짜! 후배의 정성을 이렇게 무시하기예요? 까줄 테니까 진짜 하나만 먹어봐요. 이거 먹으면 기분 완전 좋아진다니까?"
    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "유나는 야무진 손놀림으로 사탕 껍질을 까더니, 내 입가로 사탕을 쑥 밀어 넣었다."
    "얼떨결에 사탕을 받아먹은 내 입안에 달콤하고 인공적인 딸기 향이 확 퍼졌다."

    sj "…어우, 달아."
    show yuna smile at center_lower, tiny_bounce with dissolve
    yn "그쵸? 완전 맛있죠! 자, 사탕도 먹여줬으니까 이따 쉬는 시간에 매점 가는 거 절대 잊지 마요!"
    play sound "audio/sfw_walking.ogg"
    "유나가 자신의 입에도 사탕을 쏙 넣고는 콧노래를 부르며 앞장서 걷기 시작했다."
    "녀석의 발걸음에 맞춰 찰랑거리는 머리카락에서 기분 좋은 샴푸 향이 났다."
    th "참 속도 편하고 투명한 녀석이다. 겉과 속이 저렇게 똑같으니 곁에 있어도 피곤하지 않은 거겠지."
    th "나의 평화롭고 미지근한 일상은, 이 녀석 덕분에 조금 더 소란스럽지만 따뜻하게 흘러가고 있다."
    th "이런 것도 꽤 나쁘지 않은 일상이다."
    stop sound fadeout 1.5

    # ---------------------------------------------------------
    # Scene 2
    scene black with fade
    centered "{size=40}Scene 2{/size}\n\n{size=30}아침 조회{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 2.0

    "조회 시간 10분 전."
    "아직 담임 선생님이 들어오지 않은 2학년 교실은 그야말로 통제 불능의 시장통이다."
    play sound "audio/sfw_school_crowd.ogg" volume 0.7
    "교실 뒤편에서는 어제저녁에 본 예능 프로그램을 재연하느라 책상을 치며 웃는 녀석들이 있고, 앞자리에서는 1교시 수학 숙제를 베끼느라 샤프심을 부러뜨려 가며 사투를 벌이는 녀석들이 있다."
    "창문 너머로 불어오는 따뜻한 봄바람마저 교실의 왁자지껄한 열기에 섞여 미지근해질 지경이다."
    stop sound fadeout 2.0
    "하지만, 그 아수라장 한가운데서 유독 이질적일 만큼 차갑고 정적인 공기를 유지하는 반경 1미터의 구역이 있다."
    show harin normal at center_lower, sway_soft with dissolve

    "우리 반 반장, 서하린."
    "다들 봄기운에 취해 춘추복 마이를 대충 벗어 던지거나 체육복 바지를 겹쳐 입고 있지만, 하린이만은 예외다."
    "목 끝까지 단정하게 채운 블라우스 단추, 먼지 하나 없이 빳빳하게 다려진 치마의 주름. 그녀의 책상 위에는 교과서와 필통마저 한 치의 오차도 없이 직각으로 정돈되어 있다."
    th "반장이라는 타이틀이 저렇게 사람을 숨 막히게 만드는 건지, 아니면 원래 저런 성격이라 반장이 된 건지는 모르겠다."
    th "분명한 건, 저렇게 매사를 각 잡고 살면 본인만 피곤할 텐데 대단하다는 거다."
    "하린이는 교탁 앞에 서서 주변의 소음 따위는 전혀 들리지 않는다는 듯 무언가에 열중하고 있었다."
    sj "좋은 아침. 반장님은 아침부터 무슨 집중을 그렇게 하십니까."

    "내 가벼운 인사에 하린이는 고개도 돌리지 않은 채 대답했다."
    hr "어, 안녕. 자리 앉아. 곧 선생님 들어오실 시간이야."

    "딱 부러지고 군더더기 없는 목소리."
    "차갑다기보다는, 굳이 필요 없는 감정을 섞지 않고 해야 할 말만 정확하게 전달하는 기계적인 깔끔함이다."
    "나는 내 자리로 가려다 말고, 무심코 교탁 위를 내려다보았다."
    "하린이는 자를 대고 검은색 볼펜으로 이번 달 칠판 당번 배정표를 그리고 있었다."
    show cg harin_perfectionist_focus with dissolve
    "단순히 줄을 긋는 수준이 아니라, 칸의 간격부터 이름의 자간까지 마치 인쇄소 폰트처럼 완벽하게 맞춰 넣는 중이었다."
    play sound "audio/sfx_pen_click.ogg"
    "딸깍. {w=0.3}딸깍."

    "하린이는 줄을 한 번 그을 때마다 습관처럼 볼펜 끄트머리를 까딱거렸다."
    th "버릇인 걸까? 무언가 집중할 때면 저렇게 볼펜을 누르곤 한다."
    th "그나저나 저 배정표, 그냥 대충 빈칸에 이름만 적어 넣으면 되는 거 아닌가?"
    th "누가 본다고 굳이 자까지 대가며 저렇게 공을 들이는지 모르겠지만… 뭐, 완벽하지 않으면 직성이 풀리지 않는 서하린 스타일이니까."
    play sound "audio/sfw_running.ogg"
    "그때였다. 뒷자리에서 체육복 겉옷을 던지며 쫓고 쫓기던 남학생 둘이 우당탕거리며 교탁 쪽으로 밀려들었다."
    stu_a "야! 내놔, 그거 오늘 체육 시간에 입어야 된다고!"
    stu_b "잡아보시지! 메롱!"
    stop sound

    "쿵-!"
    play sound "audio/sfx_Desk_thud.ogg"
    with vpunch
    "요란한 마찰음과 함께 녀석들의 엉덩이가 교탁 모서리에 세게 부딪혔다."
    "육중한 낡은 교탁이 기우뚱하며 크게 흔들렸다."
    
    scene bg classroom with dissolve
    show harin sigh at center_lower, sway_soft with dissolve
    
    "그 순간, 하린이가 자를 대고 숨을 참아가며 조심스럽게 긋고 있던 검은색 선이, 아주 미세하게… 한 1mm 정도 삐끗하게 빗나가버렸다."
    hr "하아……."

    "하린이는 눈을 질끈 감았다."
    "아주 짧고 작게 새어 나온 한숨이었지만, 그 안에는 깊은 짜증과 피로가 배어 있었다."
    "장난을 치던 녀석들도 순간적으로 얼어붙은 분위기를 파악했는지 멋쩍게 웃으며 슬금슬금 뒷자리로 도망쳤다."
    stu_a "아, 미안 미안 반장! 우리가 밀려다가 너무 세게 부딪혔다."
    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "하린이는 도망치는 녀석들의 등짝에 대고 소리를 지르거나 화를 내는 대신, 입술을 일자로 꾹 다문 채 서랍에서 수정테이프를 꺼냈다."
    "그러고는 빗나간 1mm의 선을 지우기 위해, 아예 그 주변의 완벽했던 두 줄 전체를 새하얗게 덮어 지우기 시작했다."
    "마치 그 작은 오점 하나가 종이 전체를 망쳐버렸다는 듯이."

    menu:
        "어떻게 할까?"
        "그냥 둬도 괜찮지 않냐고 묻는다.":
            sj "야, 그 정도는 그냥 둬도 아무도 모를 것 같은데. 굳이 다 지우고 처음부터 다시 긋게?"
            show harin normal at center_lower, sway_soft with dissolve
            "하린이가 수정테이프를 밀던 손을 멈추지 않고 건조하게 대답했다."
            hr "내가 알아."
            hr "교실 앞 게시판에 한 달 내내 붙어있을 건데, 삐뚤빼뚤하고 지저분하면 보기 안 좋잖아."
            hr "그리고 이런 거 하나 대충 해놓으면, 애들이 반장이 일 대충 한다고 뒤에서 말 나올지도 모르고. 할 거면 제대로 해야지."
            sj "피곤하게 사네. 애들이 그런 걸 신경이나 쓰냐? 지들 당번이 며칠인지나 겨우 확인하고 말지."
            hr "네가 신경 안 쓴다고 남들도 안 쓰는 건 아니야. 됐어, 넌 얼른 네 자리에 가서 앉기나 해."
            th "역시 깐깐하고 철저한 반장님이다. 타인의 시선과 책임감에 묶여 사는 전형적인 모범생."
            th "나는 더 말려봐야 내 입만 아프다는 걸 깨닫고 가볍게 고개를 끄덕이며 돌아섰다."
        "내가 도와줄지 묻는다.":
            sj "종이 끄트머리라도 좀 잡아줄까? 애들 또 뛰어다니면 흔들려서 아예 종이가 찢어질라."
            show harin smile at center_lower, tiny_bounce with dissolve
            "하린이가 지우던 손을 멈추고 나를 올려다보았다."
            "경계심이 살짝 누그러진, 아주 옅지만 분명한 미소가 그녀의 입가에 스쳐 지나갔다."
            hr "고맙지만 괜찮아. 거의 다 지웠고, 선만 다시 긋기만 하면 돼."
            hr "이런 건 남의 손 타는 것보다, 그냥 내 일은 내가 알아서 하는 게 속 편하거든."
            hr "대신 저기 뒤에서 떠드는 애들, 선생님 오기 전에 자리에 좀 앉혀줄래? 흙먼지 날린다."
            sj "알았어, 반장님 명 받들겠습니다. 천천히 다시 그려라."
            
            th "완벽주의자답게 자기 일은 절대 남에게 안 맡기는 성격이다."
            th "남의 손을 타서 오점이 남거나 폐를 끼치느니, 차라리 혼자 두 배로 고생하는 걸 택하는 타입."
            th "뭐, 그게 본인 마음이 편하다면 굳이 내가 더 참견할 이유는 없겠지."
    hide harin with dissolve

    play sound "audio/sfw_walking.ogg"
    "나는 하린이의 부탁대로(혹은 내 스스로 거슬려서) 교탁 주변을 얼쩡거리던 녀석들을 쫓아내고 내 자리에 가방을 내려놓았다."
    stop sound fadeout 1.0
    play sound "audio/sfx_Sliding_door.ogg"
    "얼마 지나지 않아 앞문이 열리고 담임 선생님이 출석부를 들고 들어오셨다."
    "하린이는 언제 선이 빗나갔냐는 듯 완벽하게 수정된 당번 표를 교탁 구석에 올려둔 채, 반듯한 자세로 일어나 차렷 구령을 붙였다."
    "창밖으로 따뜻한 봄바람이 커튼을 부풀렸다 가라앉힌다."
    "아주 평범하고, 흠잡을 데 없이 완벽한 아침 조회가 시작되고 있었다."

    # ---------------------------------------------------------
    # Scene 3
    scene black with fade
    centered "{size=40}Scene 3{/size}\n\n{size=30}오후의 정적{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_theme_seola.ogg" fadein 2.0

    "점심시간이 끝난 직후의 나른한 오후."
    "식곤증과 함께 교실 전체가 붕 뜬 것처럼 어수선해지는 이 시간대를, 나는 별로 좋아하지 않는다."
    play sound "audio/sfw_walking.ogg"
    "그래서 나는 대출 기한이 다 된 소설책을 핑계 삼아 교실을 빠져나와, 인적이 드문 구관 4층의 도서관으로 향했다."
    stop sound
    "드르륵—."
    play sound "audio/sfx_Sliding_door.ogg"
    "뻑뻑한 미닫이문을 열고 들어가자, 특유의 마른 먼지 냄새와 오래된 종이 냄새가 훅 끼쳐왔다."
    "신관에 크고 화려한 새 도서관이 지어진 이후로, 이곳 구관 도서관은 사실상 버려진 공간이나 다름없다."
    "하지만 나는 남들의 시선이 닿지 않는 이 고요하고 낡은 공간을 꽤 마음에 들어 하고 있다."
    "물론, 이 공간의 고요함을 즐기는 사람이 나 혼자만은 아니었다."

    show cg seola_library with dissolve

    "서가 맨 끝, 창문 틈새로 봄 햇살이 비스듬히 떨어지는 구석 자리."
    "그곳에 설아가 앉아 있었다."

    "새하얗게 색소가 빠진 긴 머리카락과 묘하게 붉은빛이 도는 눈동자, 그리고 햇빛을 받아 투명할 정도로 창백한 피부."
    "언제 봐도 현실감이 떨어지는, 마치 혼자만 채도가 낮은 세계에 살고 있는 듯한 이질적인 동급생."
    th "설아는 워낙 눈에 띄는 선천적 외모 탓에, 학기 초부터 다른 반 녀석들까지 구경을 오거나 등 뒤에서 수군거리는 일이 잦았다."
    th "하지만 본인은 주변의 시선 따위는 전혀 신경 쓰지 않는다는 듯, 항상 묵묵히 제 할 일만 하는 타입이다."
    th "쓸데없는 말은 하지 않고, 타인에게 먼저 다가가지도 않는 성격."
    th "그런 점에서 나는 그녀에게 묘한 동질감과 편안함을 느끼고 있었다."
    play sound "audio/sfw_walking.ogg"
    "나는 설아와 서너 칸 정도 떨어진, 적당히 거리가 있는 테이블에 조용히 의자를 빼고 앉았다."
    stop sound fadeout 1.0
    "우리는 서로 가벼운 목례조차 나누지 않았지만, 이 공간에서는 그 무심함이 오히려 당연하게 느껴졌다."
    play sound "audio/sfx_paper_flutter.ogg" volume 0.4
    "사락, 사락."
    "넓은 도서관 안에는 나와 설아가 책장을 넘기는 소리만이 규칙적으로 울려 퍼졌다."
    "완벽한 정적이었다."

    "하지만 그 평화는 그리 오래가지 못했다."
    girl_a "아, 진짜? 대박."
    girl_b "야, 쉿! 여기 도서관이야. 근데 걔 진짜 그 소문 맞대?"
    "창문 너머, 1층 화단 쪽을 걸어가는 다른 반 여학생들의 목소리가 열린 창문 틈을 타고 넘어왔다."
    girl_a "나도 들었어. 아침마다 아저씨 차 타고 등교한다며? 머리 하얀 애."
    girl_b "헐… 얼굴 믿고 그러는 건가? 겉보기엔 완전 조용해 보이던데."
    girl_a "원래 그런 애들이 뒤로 더 무서운 거라니까. 조심해, 엮이면 피곤해져."
    "여과 없이 쏟아지는 악의적인 수군거림이 봄날의 따뜻한 공기를 불쾌하게 오염시켰다."

    th "소문이란 건 참 잔인할 정도로 빠르다."
    th "특히나 설아처럼 남들과 조금 다르게 생긴, 튀는 표적에게는 더더욱 쉽고 가혹하게 달라붙기 마련이다."
    "나는 무심코 고개를 들어 설아 쪽을 바라보았다."
    "설아는 여전히 읽고 있던 책에서 시선을 떼지 않고 있었다."
    "표정 하나, 호흡 하나 변하지 않은 무심한 얼굴이었다. 마치 방금 들려온 이야기가 자신과는 아무 상관 없는 먼 나라의 언어라도 되는 것처럼."
    "다만—"

    play sound "audio/sfw_cloth_moving.ogg" volume 0.6
    "스윽, 슥."
    "설아는 시선을 책에 고정한 채, 무의식적으로 자신의 왼쪽 목덜미와 팔 안쪽을 아주 가볍게, 느릿느릿 긁적이고 있었다."
    th "햇살이 너무 정통으로 떨어져서 피부가 따가운 걸까?"
    th "아니면 도서관 구석에 날아다니는 날벌레라도 신경이 쓰이는 건지."
    th "무엇이 되었든, 그녀의 하얀 피부 위에 옅은 붉은 자국이 남는 것이 묘하게 거슬렸다."
    
    scene bg old_library with dissolve
    show seola normal at center_lower, sway_soft with dissolve

    menu:
        "어떻게 할까?"
        "조용히 자리에서 일어난다.":
            "소문이야 어찌 됐든, 내가 굳이 나서서 해명해 줄 의리나 오지랖은 없다."
            "서로 선을 넘지 않는 것이 우리 둘의 무언의 규칙이니까."
            
            play sound "audio/sfw_walking.ogg"
            "나는 읽던 책을 덮고, 바닥에 끌리는 소리가 나지 않게 조심하며 자리에서 일어났다."
            "내가 책을 반납하고 돌아서려던 찰나, 우연히 설아와 시선이 마주쳤다."
            stop sound fadeout 1.0
            "나는 가볍게 눈인사만 건넸다."
            show seola normal at center_lower, sway_soft with dissolve
            sa "……."
            "설아 역시 아주 희미하게, 그러나 분명하게 고개를 한 번 끄덕이더니 다시 책으로 시선을 돌렸다."
            th "서로에게 아무것도 묻지 않고, 무엇도 강요하지 않는 관계."
            th "침묵이 전혀 불편하지 않은 이 미지근한 거리가, 나는 아주 마음에 든다."
        "가서 창문을 조금 닫아준다.":
            play sound "audio/sfw_walking.ogg"
            "나는 가볍게 혀를 차며 자리에서 일어났다."
            "소문이 기분 나쁘다기보다는, 책을 읽는 데 방해가 되는 저 저급한 소음 자체가 거슬렸기 때문이다."
            "나는 설아의 자리 쪽으로 다가가, 반쯤 열려 있던 낡은 창문을 잡아당겼다."
            stop sound
            "드르륵- 탁!"
            play sound "audio/sfw_Window_close.ogg"
            "마찰음과 함께 창문이 닫히며, 밖의 수군거림도, 피부를 따갑게 데우던 햇살도 일순간 차단되었다."
            show seola surprise at center_lower, excited_hop with dissolve
            "설아가 놀란 듯 책에서 시선을 떼고 나를 올려다보았다."
            "그녀의 붉은 눈동자에 내 얼굴이 작게 비쳤다."
            
            sj "바람이 좀 많이 불어서. 책장 넘어가면 거슬리잖아."
            sj "답답하면 다시 열고."
            play sound "audio/sfw_walking.ogg"
            "나는 변명하듯 툭 한마디를 던지고 다시 내 자리로 돌아섰다."
            stop sound fadeout 1.0
            show seola normal at center_lower, sway_soft with dissolve
            sa "…아니."
            "등 뒤에서, 나지막하고 투명한 목소리가 들려왔다."
            
            sa "고마워. 안 답답해."
            
            th "설아가 다시 책으로 시선을 내렸다."
            th "여전히 말수는 적고 표정은 무심했지만, 어깨에 미세하게 들어가 있던 힘이 조금 풀린 것처럼 보였다."
            th "긁적거리던 손도 어느새 무릎 위로 얌전히 내려가 있었다."

    hide seola with dissolve
    
    play sound "audio/sfx_school_bell.ogg" volume 0.8
    "얼마 지나지 않아, 오후 수업을 알리는 예비종이 울렸다."
    stop sound fadeout 2.0
    play sound "audio/sfw_walking.ogg"
    "나는 책을 반납하고 도서관을 빠져나왔다."
    "말 한마디 제대로 나누지 않았지만, 여느 때와 다름없이 고요하고 평화로운 휴식 시간이었다."
    stop sound fadeout 1.0

    # ---------------------------------------------------------
    # Scene 4
    scene black with fade
    centered "{size=40}Scene 4{/size}\n\n{size=30}노을 지는 옥상{/size}" with dissolve
    pause 1.5

    scene bg rooftop_sunset with fade
    play music "audio/bgm_theme_gaeun.ogg" fadein 2.0

    "정규 수업이 모두 끝나고, 방과 후 청소 시간마저 대충 마무리된 시각."
    "학교 건물을 등지고 서쪽으로 기울어가는 태양이 온 세상을 짙은 오렌지빛으로 물들이고 있었다."
    "하루 중 가장 나른하고 부드러운 시간."
    play sound "audio/sfw_walking.ogg"
    "나는 빈 교실에 가방을 둔 채, 습관처럼 발걸음을 옥상으로 돌렸다."
    th "대부분의 학생들은 피시방을 가거나 학원으로 향하느라 바쁘게 교문을 빠져나갔을 테고."
    th "남아있는 녀석들은 운동장에서 땀을 빼거나, 자율학습실에 처박혀 있을 시간이다."
    th "그러니 이 시간의 옥상은 온전히 나만의 고요한 아지트… 라고 생각했는데."
    stop sound fadeout 1.0

    "끼이익—."
    play sound "audio/sfw_Creaky_metal_door.ogg"
    "무거운 철문을 열고 옥상으로 나서자, 뺨을 스치는 시원한 바람과 함께 예상치 못한 불청객의 모습이 눈에 들어왔다."
    show cg gaeun_rooftop with dissolve

    ge "어라? 우리 성실한 후배님 아니신가. 여기서 다 보네."
    "녹슨 철조망 난간에 삐딱하게 기대어 캔커피를 홀짝이던 사람이 여유로운 미소로 나를 반겼다."
    "바람에 부드럽게 흩날리는 긴 머리카락, 노을빛을 받아 더욱 뚜렷해진 이목구비."
    "학교 최고 미인 중 한 명이자, 특유의 사람 좋은 웃음과 친화력으로 누구와도 금방 친해지는 다정한 3학년 선배."
    "민가은 선배였다."
    sj "선배, 또 청소 농땡이 치고 여기 올라와 계신 겁니까? 3학년이 모범을 보이셔야지."
    
    scene bg rooftop_sunset with dissolve
    show gaeun laugh at center_lower, idle_bounce with dissolve
    
    ge "농땡이라니 섭섭하게. 수험생의 고독하고 우아한 휴식 시간이라고 해둘래?"
    ge "그리고 모범은 무슨, 원래 3학년쯤 되면 적당히 후배들한테 양보하고 뒤로 빠져주는 게 미덕이거든."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "가은 선배는 뻔뻔하게 어깨를 으쓱하더니, 주머니에서 온기가 남은 캔커피 하나를 꺼내 내 쪽으로 가볍게 휙 던졌다."
    "탁."
    play sound "audio/sfx_picking_up_can.ogg" volume 0.8
    ge "자, 여기 뇌물. 이거 마시고 나 본 건 쉿, 비밀로 해줘."
    "선배 특유의 윙크를 받으며, 나는 캔커피를 만지작거리며 난간 옆으로 다가가 나란히 기대섰다."
    "캔에서 전해지는 따뜻한 온기가 손바닥을 기분 좋게 데웠다."
    sj "매번 이렇게 태평하시네요. 3학년이면 입시 스트레스 같은 거 엄청 받을 때 아닌가요?"
    sj "선생님들이 하도 닦달해서 숨도 못 쉰다던데."
    show gaeun smile at center_lower, tiny_bounce with dissolve
    ge "에이, 내가 무슨 스트레스? 난 늘 긍정적이고 행복한걸."
    ge "게다가 이렇게 귀여운 후배님이 옥상까지 찾아와서 말동무도 해주고 말이야. 이보다 더 좋을 순 없지!"
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "선배가 꺄르르 웃으며, 장난스럽게 내 머리를 헝클어뜨리려 손을 뻗어왔다."
    "거리낌 없이 훅 다가오는 옅은 향수 냄새에 흠칫 놀란 내가 살짝 인상을 쓰며 뒤로 물러서자, 선배의 웃음소리가 더 커졌다."
    ge "아하하! 진짜 튕기기는."
    ge "나 좋다고 번호표 뽑고 기다리는 애들이 연병장 세 바퀴인데, 넌 참 복에 겨웠다니까. 한 번만 쓰다듬어 보자, 응?"
    sj "선배, 허풍이 갈수록 느시네요. 커피나 드세요, 식겠습니다."

    "내가 혀를 차며 다가오려는 선배의 어깨를 가볍게 툭, 밀어내는 시늉을 하자—"

    show gaeun surprise at center_lower, excited_hop with hpunch
    "욱, 콜록, 켁!"
    show cg gaeun_rooftop_fragile with dissolve
    "선배가 갑자기 마시던 캔커피를 황급히 입에서 떼며 격렬하게 기침을 했다."
    "어깨가 들썩일 정도로 큰 기침이었다. 순간적으로 얼굴이 창백해진 선배는 허리를 살짝 숙인 채 입을 틀어막았다."
    sj "어, 괜찮으세요? 갑자기 왜 그러세요, 사레들리셨어요?"

    "나는 놀라서 엉거주춤하게 손을 뻗었다."
    
    scene bg rooftop_sunset with dissolve
    show gaeun normal at center_lower, sway_soft with dissolve
    
    "선배는 한 손으로 입을 단단히 틀어막은 채 잠시 거칠게 숨을 고르더니, 곧바로 고개를 들며 다시 평소의 나른하고 여유로운 미소를 지어 보였다."
    ge "아… 응. 켁, 커피를 너무 급하게 넘겼나 봐. 목에 뭐가 콱 걸렸네."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "선배는 자신의 가슴을 가볍게 두드리며 아무렇지 않게 웃었다."
    "하지만 눈가에는 기침 탓인지 아주 옅게 눈물이 맺혀 있었다."
    
    th "아무리 장난치는 게 좋아도 그렇지, 음료수 마시면서 저렇게 무방비하게 떠드니까 사레가 들리지."
    th "어른스러운 척은 다 하면서 가끔 보면 참 덜렁댄단 말이야."

    menu:
        "어떻게 할까?"
        "등을 두드려준다.":
            sj "조심 좀 하세요. 어른이 음료수도 하나 제대로 못 마십니까."
            play sound "audio/sfw_cloth_moving.ogg" volume 0.7
            "나는 쯧쯧 혀를 차며 선배의 등을 가볍게 톡톡 두드려주었다."
            show gaeun smile at center_lower, tiny_bounce with dissolve
            ge "앗, 아파라. 후배님 손맛 한 번 맵네. 등 부서지겠다."
            ge "그래도 챙겨주는 건 너밖에 없다. 진짜 괜찮다니까. 감동해서 눈물 날 뻔."
            
            th "선배는 여전히 사람 좋은 미소를 짓고 있었다."
            th "아프다면서도 내 손길을 피하지 않는 걸 보면 정말 꽤나 감동한 눈치다. 가끔은 저 능청스러움을 당해낼 재간이 없다."
        "그냥 농담으로 넘긴다.":
            sj "천천히 좀 드세요. 뒤에서 누가 쫓아옵니까? 아니면 제가 뺏어 먹을까 봐 그래요?"
            show gaeun laugh at center_lower, idle_bounce with dissolve
            ge "콜록… 정곡 찔렸네."
            ge "우리 귀여운 후배님이 내 거까지 뺏어 먹을까 봐 불안해서 그랬지! 얼른 마시기나 해, 캔 구멍 뚫어지겠다."
            th "기침을 하면서도 받아치는 선배의 장난기 가득한 대답에 나도 결국 픽 웃고 말았다."
            th "참 대단한 성격이다."
            
    "노을이 길게 늘어지는 옥상."
    "선배와 주고받는 실없는 농담들이 오렌지빛 공기 중으로 기분 좋게 흩어졌다."
    th "유나, 하린, 설아, 그리고 가은 선배까지."
    th "개성 넘치는 녀석들 틈에 섞여 있지만, 결국 나의 하루는 어제와 크게 다르지 않은 평범하고 미지근한 궤도를 돌고 있다."
    th "이 학교에서 가장 마음 편하고, 완벽 방과 후의 풍경."
    th "나는 캔커피를 한 모금 삼키며, 이 몽글몽글하고 평화로운 일상이 내일도 똑같이 반복되기를 바랐다."
    scene black with fade
    "그렇게, 아주 완벽하게 위장된 나의 첫날이 저물어가고 있었다."

    # ---------------------------------------------------------
    # Scene 5
    scene black with fade
    centered "{size=40}Scene 5{/size}\n\n{size=30}소란스러운 매점 가는 길{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_spring_morning.ogg" fadein 2.0

    "다음 날, 2교시 수학 시간이 끝난 직후의 쉬는 시간."
    play sound "audio/sfw_school_crowd.ogg" volume 0.8
    "지루한 수식과 졸음과의 사투가 끝남을 알리는 종소리가 울리기가 무섭게, 교실은 그야말로 해방을 맞은 포로수용소처럼 돌변했다."
    "다들 아침을 부실하게 먹고 온 탓인지, 아니면 그저 갇혀 있던 에너지를 발산하고 싶은 건지. 복도에는 1층 매점을 향해 돌진하는 짐승 같은 발소리들이 요란하게 울려 퍼졌다."
    stop sound fadeout 2.0
    th "평소의 나라면 이 아비규환의 레이스에 굳이 끼어들지 않았을 거다."
    th "그냥 책상에 엎드려 부족한 잠을 보충하거나, 이어폰을 꽂고 외부의 소음을 차단하는 게 내 평소의 완벽한 쉬는 시간 루틴이니까."
    th "하지만 오늘은 불행히도 어제 아침에 잡힌 선약이 하나 있었다."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "나는 하품을 길게 내뱉으며 책상 서랍에서 지갑을 꺼냈다."
    play sound "audio/sfw_running.ogg"
    "자리에서 느릿느릿 일어나 기지개를 켜는데, 뒷문 쪽에서 유독 통통 튀는, 뾱뾱거리는 듯한 경쾌한 발소리가 들려왔다."
    stop sound
    show yuna smile at center_lower, tiny_bounce with dissolve

    yn "서진 선배! 나 왔어요!"
    "앞머리가 살짝 흐트러진 채, 숨을 할딱이며 교실 뒷문으로 불쑥 고개를 들이민 것은 1학년 후배 유나였다."
    "얼마나 급하게 뛰어왔는지 하얀 뺨이 복숭아처럼 붉게 상기되어 있었다."
    "1학년 교실은 아예 건물이 달라서 구름다리를 건너와야 하는데, 쉬는 시간 종이 친 지 1분도 안 돼서 여기까지 뛰어 올라온 모양이다."
    sj "야, 뭐 하러 여기까지 뛰어와. 내가 1층으로 내려가려고 했는데."
    show yuna laugh at center_lower, idle_bounce with dissolve
    yn "에이, 우리 귀차니즘 말기 선배가 언제 꾸물꾸물 내려오나 기다리다간 내 피 같은 쉬는 시간이 다 끝날걸요?"
    yn "그리고 내가 친히 모시러 와야 선배도 기분 좋게 지갑을 열 거 아니에요! 자, 빨리 가요! 늦으면 초코 소라빵 다 매진된단 말이에요!"
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "유나는 내 대답도 듣지 않고, 아주 자연스럽게 내 교복 마이 소매를 덥석 잡아끌었다."
    "어제 아침과 똑같은 패턴. 손끝에서 전해지는 녀석의 체온이 제법 따뜻했다."
    play sound "audio/sfw_walking.ogg"
    "나는 못 이기는 척, 살짝 끌려가는 시늉을 하며 유나와 함께 복도로 나섰다."
    stop sound fadeout 1.0
    
    scene black with dissolve
    centered "{size=30}시끌벅적한 복도{/size}" with dissolve
    scene bg noisy_hallway with wipeleft
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.0

    "예상대로 매점으로 향하는 중앙 계단은 이미 학생들로 꽉 차서 지옥의 출근길 전철을 방불케 했다."
    "다들 빨리 가겠다고 서로 밀치고, 장난치고, 소리를 지르는 통에 고막이 터질 지경이었다."

    stu_a "야! 밀지 마! 나 돈 떨어뜨렸다고!"
    girl_a "아, 진짜 좁아 죽겠네. 2학년 놈들 좀 비켜라!"

    play sound "audio/sfw_cloth_moving.ogg" volume 0.8
    "우당탕거리는 소음과 땀 냄새 섞인 열기 속에서, 내 앞을 걷고 있던 유나가 뒤에서 밀려드는 덩치 큰 남학생 무리에 치여 크게 휘청거렸다."
    show yuna surprise at center_lower, excited_hop with dissolve
    yn "앗, 엄…!"
    play sound "audio/sfx_arm_grap.ogg"
    "나는 반사적으로 유나의 어깨를 붙잡아 내 쪽으로 훅 끌어당겼다."
    show cg yuna_hallway with dissolve
    "내 팔 안쪽 공간으로 쏙 들어온 유나가 흠칫 놀라며 동그랗게 눈을 뜨고 나를 올려다보았다."
    "코끝에 어제 맡았던 그 달콤한 딸기 샴푸 향기가 확 끼쳤다."
    sj "조심해. 그렇게 급하게 가다 계단에서 구르면 약도 없다. 바나나 우유 도망 안 가니까 내 뒤에 딱 붙어서 천천히 와."
    "내가 가볍게 타박하며 그녀를 내 등 뒤로 세우자, 유나는 아주 잠깐 멍한 표정을 짓더니 이내 얼굴에 화색이 확 돌며 활짝 웃었다."
    
    scene bg noisy_hallway with dissolve
    show yuna smile at center_lower, tiny_bounce with dissolve
    
    yn "헤헤… 선배 완전 박력 넘치네. 나 방금 진짜, 아주 사아아알짝 설렜잖아요."
    sj "쓸데없는 소리. 발 밟히기 싫으면 헛소리 말고 옷자락이나 꽉 잡아."
    yn "네에~ 알겠습니다, 기사님!"
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "유나는 내 등 뒤로 쏙 숨어, 내 교복 마이 뒷자락을 양손으로 꼭 쥐었다."
    "등 뒤에서 나를 방패 삼아 종종걸음으로 따라오는 기척. 가끔씩 내 등에 녀석의 머리카락이 스칠 때마다 간질거리는 느낌이 들었다."
    th "정말 꼬리 흔드는 강아지 같다니까. 주인이 이끄는 대로 맹목적으로 따라오는 작고 시끄러운 강아지."
    th "뭐, 이렇게 무방비하게 기대오는 녀석을 굳이 쳐낼 만큼 내가 매정한 놈은 아니니까."

    # ---------------------------------------------------------
    scene black with fade
    pause 0.5
    centered "{size=30}매점{/size}" with dissolve
    scene bg store with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.0

    play sound "audio/sfw_school_crowd.ogg" volume 0.6
    "전쟁통 같은 인파를 뚫고 마침내 매점에 도착했다."
    "달착지근한 빵 냄새와 매콤한 컵라면 냄새가 뒤섞인 매점 안은 이미 발 디딜 틈이 없었다."
    "나는 유나를 한쪽 구석에 세워두고, 전투적으로 계산대 줄을 파고들어 녀석이 노래를 부르던 바나나 우유 하나와 내가 마실 시원한 이온 음료를 사서 빠져나왔다."
    stop sound fadeout 2.0
    sj "자, 어제 넥타이 똑바로 매준 값. 이거면 됐지?"

    "나는 차가운 냉장고 물방울이 맺힌 뚱뚱한 바나나 우유를 유나의 볼에 살짝 들이밀었다."
    show yuna surprise at center_lower, excited_hop with dissolve
    yn "앗, 차가!"
    "유나가 어깨를 움츠리며 두 손으로 우유를 소중하게 받아 들었다."
    "그런데 우유를 받아 든 그녀의 표정이 생각보다 훨씬 더 밝고 벅차 보였다."
    "단순히 공짜 간식을 얻어먹어서 기쁜 수준을 넘어, 마치 산타 할아버지에게 소원하던 선물을 받은 어린아이 같은 표정이었다."
    show yuna smile at center_lower, tiny_bounce with dissolve
    yn "……선배. 진짜 기억하고 있었네요?"
    sj "당연하지. 네가 어제부터 하루 종일 귀에 딱지가 앉도록 세뇌를 시켰는데 어떻게 잊냐."
    "내 가벼운 핀잔에도 유나는 전혀 개의치 않고 바나나 우유를 양손으로 감싸 쥐며 헤실헤실 웃었다."
    yn "아니, 보통 이런 가벼운 약속은 그냥 빈말로 하고 넘기거나 귀찮아서 까먹는 사람들도 엄청 많잖아요."
    yn "근데 선배는 나랑 한 약속 안 잊고 지켜줬어…."

    sj "우유 하나 사주는 게 뭐 대단한 약속이라고 그렇게 눈까지 반짝이면서 감동을 하냐. 오버하지 말고 얼른 빨대나 꽂아."
    play sound "audio/sfx_can_open.ogg" volume 1.5
    "내가 픽 웃으며 이온 음료 뚜껑을 따서 한 모금 마시자, 유나는 바나나 우유 뚜껑의 은박지를 조심스럽게 벗겨내며 나를 빤히 올려다보았다."
    show yuna laugh at center_lower, idle_bounce with dissolve
    yn "대단한 거예요! 나한테는 이 바나나 우유가 완전 다이아몬드보다 값진, 감동적인 약속의 증표라구요."
    yn "아, 나 진짜 이거 너무 아까워서 못 마실 것 같아요. 평생 내 방 책상 위에 가보로 장식해둘까?"
    sj "방구석에 우유 썩은 냄새 진동해서 파리 꼬이는 꼴 보고 싶으면 그렇게 하든가."
    yn "아하하! 농담이에요, 농담! 선배가 나 생각해서 사준 거니까 아주 맛있게, 바닥에 남은 한 방울까지 싹싹 다 먹을 거예요!"
    play sound "audio/sfx_eating.ogg"
    "유나는 우유에 빨대를 꽂더니 아주 힘차게 쭉 빨아들였다."
    "볼이 빵빵해지도록 달콤한 우유를 머금은 채, 두 눈을 반달로 접으며 나를 향해 환하게 웃는 얼굴."
    "그 햇살처럼 투명하고 티 없는 미소를 보고 있자니, 번잡한 매점까지 뚫고 오느라 쌓였던 피로가 조금은 가시는 듯했다."
    th "약속을 지켜줬다는 그 사소한 사실 하나에 저렇게까지 기뻐하다니."
    th "타인에게 바라는 기대치나 허들이 얼마나 낮으면 저러는 걸까 싶으면서도, 나를 맹목적으로 따르는 이 녀석이 밉지는 않다."
    th "오히려 누군가의 작은 호의를 의심 한 점 없이, 있는 그대로 기쁘게 받아들일 수 있는 유나가 조금 부럽기도 하다."
    th "어쩌면 쟤는, 내가 절대 가질 수 없는 평범하고 밝은 빛의 세계에 사는 애일지도 모른다."
    
    play sound "audio/sfx_school_bell.ogg" volume 0.8
    "그때, 3교시 시작을 알리는 예비종이 매점 복도 스피커를 타고 요란하게 울렸다."
    stop sound fadeout 2.0
    sj "벌써 종 치네. 천천히 마시면서 슬슬 올라가자. 너 또 지각해서 복도에 서 있지 말고."
    yn "네에! 아, 선배! 다음번에는 내가 선배한테 짱 맛있는 거 쏠 테니까 기대해요! 꼭이요!"
    play sound "audio/sfw_walking.ogg"
    "유나는 빈 손으로 내 소매를 다시 꼭 쥐고 콧노래를 흥얼거리며 앞장서 걷기 시작했다."
    "녀석의 발걸음에 맞춰 찰랑거리는 머리카락에서 또다시 기분 좋은 향기가 났다."
    th "나의 미지근하고 조용한, 조금은 회색빛이었던 일상에 난입한 가장 시끄럽고 달콤한 소음."
    th "오늘도, 그렇게 평화로운 궤도를 벗어나지 않고 아주 안전하게 흘러가고 있었다."
    stop sound fadeout 1.5

    # ---------------------------------------------------------
    # Scene 6
label scene_6:
    scene black with fade
    centered "{size=40}Scene 6{/size}\n\n{size=30}종례 끝의 지명{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "3교시 예비종 이후로도 수업은 평소처럼 흘러갔다."
    "칠판 위로 분필 가루가 부서지고, 창밖에서는 운동부의 구령 소리가 희미하게 들려왔다."
    "누군가는 졸았고, 누군가는 수업 중에 몰래 휴대폰을 만지다 걸렸고, 누군가는 수행평가 날짜가 밀렸다는 소식에 안도의 한숨을 내쉬었다."
    "아주 평범한 하루였다."
    
    th "그래야 했다."
    th "조금 시끄럽고, 조금 귀찮고, 조금 따분한 정도에서 끝나는 하루."
    th "나는 그 정도의 온도면 충분했다."
    
    play sound "audio/sfx_school_bell.ogg" volume 0.8
    "마지막 종이 울리고, 들뜬 교실 안 공기가 단번에 풀어졌다."
    stop sound fadeout 2.0
    "가방을 챙겨 교문을 향할 준비를 하던 우리들 앞에서, 담임 선생님이 출석부를 덮으며 학생들을 다시 붙잡았다."
    "다음 주부터 시작되는 봄 축제, 연화제 준비 때문에 각 반에서 운영 도우미를 몇 명씩 차출해야 한다는 이야기였다."
    "선생님은 교탁 앞에 붙은 명단을 내려다보며 아주 자연스럽게 반장 이름을 먼저 불렀다."
    
    show harin normal at center_lower, sway_soft with dissolve
    hr "네."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "하린이는 자리에서 반듯하게 일어나 짧게 대답했다."
    "선생님은 그 반응이 당연하다는 듯 고개를 끄덕이고는, 두 번째 이름을 불렀다."

    "윤서진."

    "교실 여기저기서 장난스러운 야유와 웃음소리가 튀어나왔다."
    stu_a "오, 웬일이래. 윤서진도 이제 학급을 위해 봉사하냐?"
    stu_b "야, 저 녀석 또 특유의 귀찮아 죽겠다는 표정 나왔다."
    th "왜 하필 나지."

    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "나는 작게 한숨을 삼키며 자리에서 일어났다."
    "선생님은 내 표정을 대충 읽었는지, 웃으며 덧붙였다."
    "특별활동도 안 하고, 방과 후에 바로 집 가는 학생이니 시간 비우기 제일 쉬울 것 같다고 했다."
    "거기에다 반장이 혼자 끌고 가기엔 잡무가 많을 테니, 적당히 손발 맞출 애 하나가 필요하다는 이유도 덧붙었다."
    th "아주 합리적이고, 그래서 더 반박하기 짜증나는 선정 기준이다."

    sj "…네."

    "나는 영혼 빠진 목소리로 대답했다."
    "곧바로 시선이 옆으로 옮겨졌다."
    hr "미안."
    hr "내가 일부러 고른 건 아닌데, 어쩌다 보니 같이 하게 됐네."

    sj "반장 탓은 아니지."
    sj "그래도 갑자기 방과 후가 통째로 날아가니까, 조금 억울하긴 하다."
    
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "일단 오늘은 첫 모임만 하면 돼."
    hr "학생회 쪽에서 전체 인원 배정 끝냈다던데, 준비실로 가보면 자세히 들을 수 있을 거야."

    th "첫 모임만."
    th "저 말은 대개 거짓말이다."
    th "이런 종류의 일은 늘 첫날이 가장 짧고, 그 다음부터 끝도 없이 늘어난다."
    
    show harin normal at center_lower, sway_soft with dissolve
    "종례가 끝나자마자 교실은 다시 부산스럽게 흔들리기 시작했다."
    "누군가는 바로 학원 가방을 메고 뛰쳐나갔고, 누군가는 교실 뒤에 남아 오늘 저녁 메뉴를 두고 시답잖은 논쟁을 벌였다."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "나는 느릿하게 가방을 들어 올렸다."
    play sound "audio/sfx_Sliding_door.ogg"
    "그때, 교실 뒷문이 벌컥 열렸다."
    
    show yuna smile at left, tiny_bounce with dissolve
    yn "서진 선배!"

    "익숙한 목소리와 함께 유나가 얼굴을 빼꼼 내밀었다."
    "숨을 약간 몰아쉬는 걸 보니, 이번에도 쉬는 시간 때처럼 건물을 가로질러 달려온 모양이다."

    sj "너는 또 왜 여기까지 와."
    sj "설마 1학년 건물에서 여기까지 뛰어온 거냐?"

    show yuna laugh at left, idle_bounce with dissolve
    yn "네! 정확히는 날아왔죠!"
    yn "아니, 방금 우리 반에서도 축제 도우미 얘기 나왔거든요? 나 지원했어요!"
    yn "근데 학생회 선배가, 2학년 쪽 도우미 명단에 선배 이름도 있다고 하더라구요."

    "유나는 눈을 반짝이며 두 손을 꼭 모았다."
    yn "우리 같이 하게 됐어요!"

    th "저렇게까지 기뻐할 일인가."

    sj "나는 방금 강제 징집 당한 기분인데, 너는 되게 신났네."
    show yuna smile at left, tiny_bounce with dissolve
    yn "당연하죠!"
    yn "선배랑 같이 있으면 재미있잖아요. 그리고 선배 혼자 보내면 분명 중간에 몰래 도망칠 것 같단 말이에요."
    sj "너 나를 대체 뭘로 보는 거냐."
    yn "도망 잘 치는 사람?"

    "나는 피식 웃으며 고개를 저었다."
    "그때 유나의 시선이 교탁 앞 하린이에게로 옮겨갔다."

    show harin normal at right, sway_soft with dissolve
    yn "…어?"
    yn "하린 선배도 같이예요?"

    hr "응. 우리 반 대표 맡았어."
    hr "학생회 준비실로 바로 오라고 하던데, 너도 거기 가는 거지?"
    "아주 잠깐."
    "정말 눈 깜빡할 정도로 짧은 순간이었지만, 유나의 웃는 얼굴이 아주 미세하게 굳었다."
    "금세 다시 원래의 밝은 표정으로 돌아왔지만, 이상하게도 그 짧은 틈이 눈에 걸렸다."
    
    show yuna smile at left, tiny_bounce with dissolve
    yn "네! 완전 열심히 할 거예요!"
    yn "선배들 방해 안 하고, 아니 오히려 엄청 도움이 될 자신도 있어요!"

    th "방해 안 하고, 라."
    th "저 말은 이미 방해할 준비가 끝난 사람의 대사처럼 들리는데."
    
    menu:
        "유나에게 뭐라고 할까?"
        "너라도 있어서 다행이라고 말한다.":
            sj "그래도 네가 같이 있으면 덜 심심하긴 하겠다."
            "내가 툭 내뱉자, 유나의 눈이 동그랗게 커졌다."

            show yuna surprise at left, excited_hop with dissolve
            yn "…진짜요?"
            sj "왜 그렇게 놀라."
            sj "혼자 하린이한테 끌려다니는 것보단 둘이 끌려다니는 게 낫다는 뜻이야."
            show harin sigh at right, sway_soft with dissolve
            hr "표현이 꼭 그래야 해?"
            show yuna laugh at left, idle_bounce with dissolve
            yn "헤헤… 그래도 좋아요."
            yn "방금 그 말, 나 오늘 집 가서 자기 전에 한 번 더 떠올릴래요."
        "너 때문에 더 시끄러워질 것 같다고 말한다.":
            sj "네가 있으면 덜 심심한 대신 두 배는 시끄러워질 것 같은데."
            show yuna pout at left, sway_soft with dissolve
            yn "아, 진짜!"
            yn "그렇게 말하면서 또 은근히 나 기다려줄 거잖아요."

            sj "자신감은 인정한다."
            show yuna smile at left, tiny_bounce with dissolve
            yn "선배가 맨날 그렇게 툴툴대도 결국 나 안 떼어내는 거, 나 다 안다니까요?"
            th "쓸데없이 정확하다."

    hide harin with dissolve
    hide yuna with dissolve

    play sound "audio/sfw_walking.ogg"
    "나는 가방끈을 다시 고쳐 잡고 교실 문을 나섰다."
    "복도 끝 창문에서는 노을이 아니라 아직 늦은 오후의 연한 햇빛이 길게 비스듬히 깔려 있었다."

    th "축제 준비."
    th "이런 말만 들으면 교실 안은 늘 들뜬다."
    th "장식, 공연, 야간 개방, 푸드 부스, 사진, 추억."
    th "누군가에게는 청춘이라는 이름으로 오래 남을 이벤트겠지."

    th "하지만 내게 그런 건 대체로 귀찮고 피곤한 소란일 뿐이다."
    th "그랬어야 했다."
    stop sound fadeout 1.0
    jump scene_7


    # ---------------------------------------------------------
    # Scene 7
label scene_7:
    scene black with fade
    centered "{size=40}Scene 7{/size}\n\n{size=30}특별동 준비실{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_theme_gaeun.ogg" fadein 2.0

    "학생회에서 임시 준비실로 쓰고 있다는 곳은, 구관 특별동 2층 끝에 있는 낡은 자료실이었다."
    "신관이 생긴 뒤로 사실상 방치된 공간이라 그런지, 문을 열자마자 오래된 종이 냄새와 먼지 냄새가 옅게 섞여 코끝을 간질였다."
    "탁자 위에는 색지, 가위, 테이프, 행사 배치도, 출력된 명단이 뒤섞여 널려 있었다."

    th "첫 모임부터 분위기가 벌써 피곤하다."
    "하지만 그 지저분한 풍경 한가운데, 혼자만 다른 화면처럼 여유로운 얼굴이 먼저 눈에 들어왔다."
    
    show gaeun smile at center_lower, tiny_bounce with dissolve
    ge "왔네, 우리 후배님들."
    "창가 쪽 책상에 걸터앉아 있던 민가은 선배가 손을 흔들었다."
    "학생회 완장을 느슨하게 찬 채 웃고 있는 얼굴은 오늘도 한없이 부드럽고 능청스러웠다."
    ge "내가 오늘 전체 도우미 명단 정리 맡았거든."
    ge "근데 이렇게 보니까 라인업이 제법 재미있네."
    sj "재미는 선배만 느끼시는 것 같습니다."

    show gaeun laugh at center_lower, idle_bounce with dissolve
    ge "차갑다, 차가워."
    ge "축제 준비는 원래 이런 우연한 조합에서 시작하는 거야. 그러다 친해지고, 추억 생기고, 나중엔 울고 웃고 난리도 나는 거지."
    th "마지막 말이 조금 걸렸지만, 굳이 짚고 넘어갈 정도는 아니었다."

    "가은 선배 옆쪽 자리에는 이미 하린이가 앉아 명단을 정리하고 있었다."
    "언제 가져왔는지 모를 자와 형광펜, 포스트잇이 정확한 각도로 정렬되어 있었다."
    show harin normal at right, sway_soft with dissolve
    hr "윤서진, 여기."
    hr "우리 반 배정표랑 진행 일정표야. 아직 확정본은 아니고 초안."
    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "나는 하린이가 내민 종이를 받아 들었다."
    "빽빽하게 적힌 체크 항목과 일정표가 눈에 들어오자, 벌써부터 피로가 몰려오는 기분이 들었다."

    sj "이걸 오늘 다 보자는 건 아니지?"
    hr "아직 아니야."
    hr "오늘은 담당 구역이랑 역할만 나누면 돼."
    play sound "audio/sfw_running.ogg"
    "그때 문 바깥에서 가벼운 발소리가 들렸다."
    
    stop sound
    show yuna smile at left, tiny_bounce with dissolve
    yn "죄송합니다아! 안 늦었죠?!"
    "유나가 두 손에 종이컵 음료가 든 비닐봉지를 달랑거리며 들어왔다."
    "헐레벌떡 뛰어왔는지 앞머리가 조금 흐트러져 있었지만, 표정만큼은 어김없이 환했다."
    ge "오, 막내도 왔네."
    ge "좋아, 이제 한 명만 더 오면 되겠다."
    
    play sound "audio/sfx_Sliding_door.ogg"
    "그 말이 끝나기 무섭게 문가에서 아주 조용한 인기척이 났다."
    show seola normal at char_2, sway_soft with dissolve
    "설아였다."
    "양손에는 말아 놓은 도화지 몇 장과 얇은 파일철이 들려 있었다."
    "창백한 손목 위로 연필 자국 같은 희미한 얼룩이 스쳐 지나갔다."
    th "설아까지?"

    play sound "audio/sfw_walking.ogg"
    "설아는 방 안에 들어서자마자 우리를 한 번씩 조용히 훑어보고, 말없이 가장 구석 자리에 섰다."
    stop sound fadeout 1.0
    ge "좋아, 인원 다 모였네."

    hide gaeun with dissolve
    hide harin with dissolve
    hide yuna with dissolve
    hide seola with dissolve

    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "가은 선배는 학생회 쪽에서 정리한 명단을 들어 보이며 하나씩 설명하기 시작했다."
    "하린이는 2학년 대표 겸 전체 일정 정리."
    "나는 물품 이동, 인원 체크, 행사 당일 현장 보조."
    "유나는 1학년 쪽 연락 담당과 간식, 소모품 심부름."
    "설아는 포스터 시안과 교내 전시 패널 디자인."
    "그리고 가은 선배는 학생회 측 총괄 보조."

    th "각자 따로 보면 별문제 없는 업무들이다."
    th "그런데 이상하게, 이 조합으로 한 공간에 모여 있다는 사실이 조금 낯설었다."
    
    show yuna smile at char_1, tiny_bounce
    show seola normal at char_2, sway_soft
    show harin normal at char_3, sway_soft
    show gaeun smile at char_4, tiny_bounce
    with dissolve

    yn "우와, 뭔가 진짜 팀 같아요!"
    yn "이름표라도 만들까요? 아니면 팀명 같은 거 정해도 재밌겠다."

    hr "그런 건 나중에."
    hr "먼저 해야 할 일부터 끝내자."
    show yuna pout at char_1, sway_soft with dissolve
    yn "하린 선배는 낭만이 없어요."
    hr "축제 준비에 낭만 찾다가 일정 밀리면 그게 더 큰 문제야."
    show gaeun laugh at char_4, idle_bounce with dissolve
    ge "둘이 벌써부터 잘 맞네."
    ge "한 명은 브레이크고 한 명은 엑셀이야. 차가 굴러가긴 하겠다."

    sj "그 차에 제가 왜 타고 있는지는 아직도 모르겠습니다."
    "내 말에 유나가 키득 웃고, 가은 선배도 어깨를 들썩였다."
    "반면 하린이는 손에 쥔 볼펜 끝을 딸깍, 딸깍 눌렀다."
    play sound "audio/sfx_pen_click.ogg"
    th "또 저 버릇이다."
    th "집중할 때마다, 혹은 신경이 곤두설 때마다 무의식적으로 반복하는 습관."
    
    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "그때 조용히 파일철을 펼치던 설아의 도화지 한 장이 바닥으로 미끄러져 내렸다."
    show seola surprise at char_2, excited_hop with dissolve
    "나는 가장 먼저 몸을 숙여 그것을 주웠다."
    "도화지 위에는 축제 메인 포스터 초안 같은 것이 연필선으로 그려져 있었다."
    "벚꽃과 교정 풍경, 그리고 어딘가 쓸쓸하게 비어 있는 중앙의 길."

    sj "이거 네가 그린 거야?"
    show seola normal at char_2, sway_soft with dissolve
    sa "…응."

    sj "잘 그렸네."
    sj "생각보다 훨씬."
    "말을 꺼낸 뒤에야, 표현이 어딘가 실례였다는 걸 깨달았다."
    "하지만 설아는 기분 나쁜 기색 없이 도화지를 받아 들었다."
    sa "생각보다, 라는 말은 빼도 돼."

    sj "미안."

    sa "괜찮아."
    sa "대충 들은 말은 아니니까."
    th "이상하게도 그 말이 오래 남았다."
    th "대충 들은 말은 아니라."
    
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "설아가 도화지를 정리하려 손을 뻗는 순간, 소매 끝이 살짝 밀려 올라갔다."
    "손목 안쪽에 붉은 긁힌 자국이 옅게 남아 있었다."
    "도서관에서 봤던 그것과 닮아 있었다."
    "내 시선이 닿은 걸 알아챘는지, 설아는 아주 자연스럽게 소매를 다시 끌어내렸다."
    
    sa "종이가 건조해서, 가끔 베여."
    th "나는 아무 말도 하지 않았다."
    th "거짓말이라고 단정할 수는 없었지만, 진실처럼 들리지도 않았다."
    
    show gaeun normal at char_4, sway_soft with dissolve
    ge "좋아, 그럼 역할 설명은 이 정도면 됐고."
    ge "오늘은 간단하게 자리 배치만 보고 끝내자. 다들 오래 붙잡아 두면 첫날부터 도망갈 테니까."
    sj "적어도 제 심리는 정확히 파악하고 계시네요."

    show gaeun smile at char_4, tiny_bounce with dissolve
    ge "후배님은 얼굴에 다 써 있거든."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "가은 선배가 웃으며 자리에서 일어나려던 순간이었다."
    
    show gaeun surprise at char_4, excited_hop with hpunch
    "켁, 콜록…!"
    
    "갑작스러운 기침 소리가 좁은 준비실 안에 번졌다."
    "어제 옥상에서 들었던 것보다 조금 더 거칠고, 조금 더 깊었다."

    sj "선배."
    "내가 반사적으로 부르자, 가은 선배는 손등으로 입가를 가린 채 고개를 살짝 저었다."
    show gaeun normal at char_4, sway_soft with dissolve
    ge "괜찮아."
    ge "요즘 교실이 좀 건조해서 그래. 먼지 먹었나 보다."

    "웃는 얼굴은 여전했지만, 이번에는 그 말이 전보다 덜 가볍게 들렸다."
    "하린이도 아주 잠깐 손을 멈췄고, 유나 역시 웃던 입꼬리를 조용히 내렸다."
    "준비실 안에 한순간 얇고 차가운 정적이 내려앉았다."
    
    show yuna smile at char_1, tiny_bounce with dissolve
    yn "그럼 제가 물 가져올까요?"
    yn "정수기 바로 아래층에 있어요. 금방 다녀올 수 있는데."

    ge "괜찮아, 막내야."
    ge "너까지 뛰어다니면 여기 바닥 무너질 것 같아."
    show yuna pout at char_1, sway_soft with dissolve
    yn "뭐예요, 그게."
    "유나가 볼을 부풀리며 투덜대자, 준비실 안 공기가 아주 조금 풀렸다."
    "정말 아주 조금."
    "하린이는 책상 위 일정표를 정리하며 낮게 입을 열었다."

    show harin normal at char_3, sway_soft with dissolve
    hr "그럼 오늘은 여기까지 하자."
    hr "내일 점심시간에 한 번 더 모여서 세부 배치 정리하면 돼."
    hr "윤서진, 너는 이거 가져가서 한 번 읽어봐. 빠진 물품 있으면 표시해두고."

    sj "알았어."
    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "나는 하린이가 건네는 종이 뭉치를 받아 들었다."
    "생각보다 무게감이 있었다."
    "서류의 무게인지, 앞으로의 귀찮음인지 분간이 안 갈 정도로."
    
    hide harin with dissolve
    hide gaeun with dissolve

    "짧은 모임은 그렇게 어수선하게 끝났다."
    "가은 선배는 학생회실로 다시 올라가겠다며 먼저 나갔고, 하린이는 남아서 테이블 위 물품을 한 번 더 정리하기 시작했다."
    "유나는 빈 종이컵 봉지를 들고 내 옆으로 쪼르르 붙었다."
    "설아는 조용히 도화지를 끌어안은 채 문가로 향했다."
    
    menu:
        "누구를 먼저 도울까?"
        "하린의 정리를 잠깐 도와준다.":
            sj "반장, 그거 나도 같이 정리할까?"
            show harin surprise at char_3, excited_hop with dissolve
            "하린이는 잠깐 의외라는 표정을 지었다."
            hr "…네가 먼저 말하는 건 좀 드문데."
            hr "그래도 고마워. 테이프랑 색지 종류별로만 나눠줘."

            "나는 말없이 손을 보탰다."
            "하린이는 나와 같은 책상 앞에 서서 물품을 정리하면서도, 흐트러진 모서리 하나까지 꼭 맞춰 세웠다."

            th "숨 막힐 정도로 꼼꼼하다."
            th "그런데 이상하게도, 저렇게까지 해야 겨우 버틸 수 있는 사람처럼 보일 때가 있다."
        "설아가 든 도화지를 대신 들어준다.":
            sj "그거 내가 좀 들어줄까?"
            show seola surprise at char_2, excited_hop with dissolve
            "설아는 내 손과 자신의 도화지를 번갈아 보더니, 잠깐 망설였다."
            sa "…괜찮아."
            sa "가볍거든."

            sj "가벼워 보여도 모서리 구겨지면 네가 더 싫어할 것 같은데."

            "잠시 정적이 흘렀다."
            "이윽고 설아는 말아 둔 도화지 절반을 내 쪽으로 내밀었다."

            show seola normal at char_2, sway_soft with dissolve
            sa "그럼, 잠깐만."
            th "거절과 허락의 중간 같은 대답."
            th "그래도 설아가 먼저 무언가를 건넨 건 처음이었다."
        "유나가 뛰어가지 못하게 옆에 붙잡아 둔다.":
            sj "너는 물 가지러 간다더니 벌써 나갈 자세네."
            show yuna laugh at char_1, idle_bounce with dissolve
            yn "왜요, 나 엄청 유능한 심부름 요정인데."
            sj "유능한 건 모르겠고."
            sj "복도에서 또 뛰다가 넘어질까 봐 일단 여기 있어."
            "내가 무심하게 말하자, 유나는 눈을 몇 번 깜빡였다."
            "그러더니 이상할 정도로 순순히 내 옆에 붙어 섰다."
            show yuna smile at char_1, tiny_bounce with dissolve
            yn "…네."
            yn "그럼 선배 옆에 있을래요."

            th "이런 식으로 말을 곧이곧대로 받는 건 반칙이다."
            
    hide yuna with dissolve
    hide seola with dissolve
    hide harin with dissolve

    "정리까지 얼추 끝났을 때쯤, 특별동 창문 밖으로 늦은 오후의 빛이 길게 기울어져 들어왔다."
    "먼지 떠다니는 공기 속에서 그 빛은 유난히도 옅고 희미했다."

    th "유나의 웃음은 지나치게 밝았고."
    th "하린의 손끝은 필요 이상으로 예민했고."
    th "설아의 소매 안쪽에는 설명되지 않는 자국이 남아 있었고."
    th "가은 선배의 기침은 그냥 넘기기엔 조금 깊었다."
    th "하지만 그때의 나는, 그 모든 걸 그저 사소한 이질감 정도로만 여겼다."
    th "누구에게나 말하지 않는 사정 하나쯤은 있다고."
    th "굳이 들여다보지 않아도 되는, 남의 체온 같은 거라고."

    scene black with dissolve
    centered "{size=30}저녁의 복도{/size}" with dissolve
    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.5

    play sound "audio/sfx_Sliding_door.ogg"
    "준비실 문을 나서자 학교는 여전히 평소처럼 시끄럽고 평화로웠다."
    "복도에서는 축제 얘기로 들뜬 학생들이 웃고 떠들었고, 창밖 운동장에서는 석양이 천천히 내려앉고 있었다."
    play sound "audio/sfw_walking.ogg"
    "나는 서류 뭉치를 옆구리에 끼고 천천히 계단을 내려갔다."

    th "그저 조금 더 귀찮아졌을 뿐이다."
    th "조금 더 얽히게 됐을 뿐이고, 조금 더 가까이서 보게 됐을 뿐이다."
    th "나는 아직도, 그 선을 넘지 않을 수 있다고 생각했다."
    stop sound fadeout 1.5
    scene black with fade
    "그날 이후, 나의 미지근했던 일상은 아주 천천히 방향을 틀기 시작했다."

    # ---------------------------------------------------------
    # Scene 8
label scene_8:
    scene black with fade
    centered "{size=40}Scene 8{/size}\n\n{size=30}첫 합동 작업{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "다음 날 방과 후."
    "축제 준비 첫날이라는 말이 무색하게, 우리 반 교실은 평소보다 더 어수선했다."
    "책상은 몇 개씩 밀려 한쪽으로 붙어 있었고, 창가 쪽에는 색지와 가위, 풀, 박스테이프 따위가 대충 쌓여 있었다."
    "평소 같으면 집으로 가는 발걸음을 재촉했을 시간인데, 나는 지금 잘 정리되지 않은 행사 물품들 한가운데 서 있었다."
    th "도망칠 기회는 분명 있었는데."
    th "하필 반장이 출석 체크를 너무 철저하게 하는 바람에, 적당히 빠질 틈도 사라졌다."
    
    show harin normal at right, sway_soft with dissolve
    show yuna smile at left, tiny_bounce with dissolve

    hr "윤서진, 거기 멍하니 서 있지 말고 색지부터 종류별로 나눠놔."
    hr "가로 현수막 문구도 오늘 안에 대충 초안 잡아야 해."

    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    yn "선배, 이거 보세요!"
    yn "나 아까 학생회실에서 스티커도 받아왔어요. 별 모양, 하트 모양, 반짝이 들어간 거까지!"

    sj "축제 장식이야, 유치원 미술시간이야."
    show yuna pout at left, sway_soft with dissolve
    yn "아, 진짜."
    yn "감성이 부족해, 감성이. 이런 디테일이 분위기를 사는 거라구요."

    "하린이는 그런 유나의 말을 흘려들으며 체크리스트를 훑고 있었다."
    "책상 위에는 이미 자와 펜이 직각으로 놓여 있었고, 체크 표시 하나까지 지나치게 반듯했다."

    th "저 정도면 준비가 아니라 의식이다."
    th "종교 수준의 정리정돈."

    play sound "audio/sfx_Sliding_door.ogg"
    "잠시 뒤, 교실 뒷문이 열리고 설아가 들어왔다."
    "품 안에 말아 든 도화지와 클립보드 몇 장."
    "그 뒤로 한 박자 늦게, 민가은 선배도 느긋한 얼굴로 모습을 드러냈다."
    hide yuna with dissolve
    hide harin with dissolve

    show seola normal at left, sway_soft with dissolve
    show gaeun smile at right, tiny_bounce with dissolve

    ge "다들 성실하네."
    ge "이 정도면 우리 팀, 생각보다 그럴듯하게 굴러가겠는데?"

    sj "지금은 시작 5분 차라 그렇죠."
    show gaeun laugh at right, idle_bounce with dissolve
    ge "후배님은 꼭 한마디씩 비틀어야 직성이 풀리더라."
    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    sa "…배치도 초안 가져왔어."

    "설아는 군더더기 없이 클립보드를 내밀었다."
    "축제 안내 패널과 교실 앞 장식 배치를 간단한 선으로 정리한 도안이었다."
    "불필요한 장식은 거의 없는데, 이상할 정도로 시선이 잘 모였다."
    
    sj "벌써 이만큼 했어?"

    sa "어제 대충 생각해뒀어."

    th "대충."
    th "설아가 말하는 대충은 보통 남들 기준의 꽤 열심히다."
    
    show harin normal at center_lower, sway_soft with dissolve
    hide gaeun with dissolve

    hr "좋아. 그럼 오늘은 세 가지부터 끝내자."
    hr "현수막 문구 정하기, 교실 앞 안내문 초안, 그리고 장식용 색지 재단."
    show yuna smile at right, tiny_bounce with dissolve
    yn "저는 뭐 하면 돼요?"
    hr "너는 우선 색지 자르는 쪽."

    show yuna pout at right, sway_soft with dissolve
    yn "엥, 제일 단순 노동이잖아요."
    hr "그래도 제일 손 많이 가."
    hr "그리고 네가 움직임 빠르잖아."
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "유나는 투덜거리면서도 결국 자리에 앉아 색지를 펼쳤다."
    "입으로는 불만을 말하지만 손은 제법 야무졌다."
    
    menu:
        "누구부터 도와줄까?"
        "유나 옆에 가서 색지를 같이 자른다.":
            sj "가위 혼자 쓰다 손 베지 말고, 반은 내가 할게."
            show yuna surprise at right, excited_hop with dissolve
            yn "…선배가 먼저 도와준다고 하네?"
            yn "오늘 해 뜨는 방향 바뀌었나?"

            sj "말 많다."

            show yuna smile at right, tiny_bounce with dissolve
            "내가 옆에 앉자 유나는 금세 헤실헤실 웃으며 잘린 색지를 가지런히 쌓았다."
            "손끝은 빨랐고, 기대 이상으로 꼼꼼했다."
            "가끔 내 팔꿈치에 제 팔이 닿을 때마다, 녀석은 괜히 더 기분 좋아 보였다."
            
            th "생각보다 익숙하다."
            th "누군가 옆에 딱 붙어 있는 거리감이."
        "하린 옆에서 현수막 문구를 같이 본다.":
            sj "문구는 뭐로 할 건데."
            sj "설마 '꿈과 낭만이 피어나는 연화제' 같은 건 아니지?"

            show harin sigh at center_lower, sway_soft with dissolve
            hr "…나도 그런 건 싫어."
            hr "너무 뻔하잖아."

            "하린이는 아주 잠깐 미간을 찌푸렸다."
            "그리고 내가 적당히 던진 농담을 의외로 진지하게 검토하기 시작했다."
            hr "차라리 간결한 쪽이 나아."
            hr "학생들이 멈춰서 읽게 하려면."

            sj "의외네. 반장은 되게 모범답안 좋아할 줄 알았는데."
            show harin normal at center_lower, sway_soft with dissolve
            hr "모범답안은 보기엔 깔끔해도, 기억에는 안 남으니까."
            th "그 말이 조금 의외였다."
            th "서하린은 늘 정답만 고를 것처럼 보여서."
        "설아가 가져온 배치도를 같이 본다.":
            sj "여기 비워둔 공간은 일부러?"
            show seola normal at left, sway_soft with dissolve
            sa "응."
            sa "다 채우면 답답해 보여."

            scene cg seola_blueprint with dissolve
            "설아는 손가락으로 도안의 중앙 빈칸을 조용히 짚었다."

            sa "비어 있는 데가 있어야, 나머지가 더 보여."
            sj "…디자인 쪽 사람 말 같네."

            sa "그런 거 아냐."
            sa "그냥, 꽉 차 있으면 숨 막혀서."

            th "무심코 흘린 말 같았는데, 어딘가 묘하게 걸렸다."
            th "꽉 차 있으면 숨 막힌다."
            th "그건 배치 이야기만은 아닌 것처럼 들렸다."
            
            scene bg classroom with dissolve
            show seola normal at left, sway_soft with dissolve

    hide yuna with dissolve
    hide harin with dissolve
    hide seola with dissolve

    "작업은 생각보다 빠르게 굴러갔다."
    "유나는 시끄럽지만 손이 빨랐고, 하린이는 숨 막힐 정도로 체계적이었고, 설아는 군더더기 없이 필요한 것만 정확히 골라냈다."
    "가은 선배는 그 셋 사이를 적당한 타이밍에 끼어들며 분위기를 풀었다."
    
    show gaeun smile at center_lower, tiny_bounce with dissolve
    ge "이야, 이 조합 꽤 재밌네."
    ge "한 명은 강아지고, 한 명은 자, 한 명은 칼날 같고."

    sj "그 비유에 저는 빠졌네요."

    ge "후배님은 미지근한 물."
    ge "어디든 무난하게 섞이는데, 가만 보면 제일 안 잡히는 타입."

    "나는 대꾸하지 않았다."
    "그 말이 농담처럼 들리면서도, 어쩐지 조금 지나치게 정확했다."

    show gaeun normal at center_lower, sway_soft with dissolve
    "그때, 가은 선배가 말을 멈추고 작게 기침했다."
    "전날보다 약하고 짧았지만, 나는 그 소리를 놓치지 못했다."

    sj "선배, 또 그러시네요."

    ge "먼지 때문이야."
    ge "구관은 공기까지 연식이 느껴져서 문제라니까."

    show gaeun smile at center_lower, tiny_bounce with dissolve
    "선배는 곧장 웃으며 넘겼다."
    "하지만 웃는 얼굴이 아주 잠깐 늦게 올라왔다."

    play sound "audio/sfx_school_bell.ogg" volume 0.8
    "어느새 창밖은 늦은 오후 빛으로 물들어 있었다."
    stop sound fadeout 2.0
    "첫날 작업은 예정한 것보다 조금 덜 끝났고, 그래서 하린이의 표정은 예정한 것보다 조금 더 굳어 있었다."
    scene black with fade
    "그리고 그 날, 아주 사소한 균열이 하나 더 생겼다."

    # ---------------------------------------------------------
    # Scene 9
label scene_9:
    scene black with fade
    centered "{size=40}Scene 9{/size}\n\n{size=30}흐트러진 순서{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 2.0

    "다음 날 점심시간."
    "학생회에서 내려온 수정 지시 하나로, 어제 만든 계획표 절반이 무용지물이 됐다."
    show harin normal at center_lower, sway_soft with dissolve
    hr "부스 배치가 바뀌었다고?"
    hr "어제 분명 최종안이라고 했는데."
    "하린이는 전달받은 출력물을 내려다보며 가만히 입술을 깨물었다."
    "목소리는 여전히 차분했지만, 볼펜을 누르는 손끝이 평소보다 빨랐다."
    play sound "audio/sfx_pen_click.ogg"
    "딸깍. 딸깍. 딸깍."

    yn "에이, 뭐 어때요!"
    yn "다시 하면 되죠. 어차피 축제 준비는 원래 이런 거라던데."
    show yuna smile at left, tiny_bounce with dissolve
    show harin sigh at center_lower, sway_soft with dissolve
    hr "그 '다시'가 문제야."
    hr "시간표 다시 짜야 하고, 인원 배치 다시 정리해야 하고, 포스터 문구도 바뀔 수 있어."

    yn "……."

    "유나는 입을 다물었다."
    "처음엔 분위기를 띄우려는 가벼운 말이었겠지만, 하린이의 반응은 생각보다 날카로웠다."

    th "반장은 지금 장난을 받을 상태가 아니다."
    th "그건 누가 봐도 티가 났다."

    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "설아는 말없이 바뀐 배치도를 넘겨받아 보고 있었다."
    "한참 동안 아무 말도 하지 않다가, 아주 담백하게 한 줄만 던졌다."
    show seola normal at right, sway_soft with dissolve
    sa "문구는 안 바꿔도 돼."
    sa "배치만 옮기면 돼."
    "하린이의 손이 잠깐 멈췄다."

    hr "…왜?"

    sa "사람 흐름은 바뀌어도, 시선이 머무는 위치는 비슷하니까."
    "설아는 수정할 부분과 놔둬도 되는 부분을 손가락으로 짚어 주었다."
    "짧고 단정한 설명."
    "쓸데없는 감정이 하나도 안 섞여 있어서 오히려 더 설득력이 있었다."
    
    show harin normal at center_lower, sway_soft with dissolve
    hr "알겠어."
    hr "그럼 수정 범위 줄일 수 있겠다."
    
    th "희한하네."
    th "설아는 말수가 적은데, 입을 열면 꼭 필요한 데만 정확히 꽂는다."

    "하지만 분위기가 완전히 풀린 건 아니었다."
    "유나는 아까 살짝 잘린 것 같은 표정으로 입꼬리를 애써 올리고 있었고, 하린이는 여전히 날 선 긴장을 손끝에 걸친 채였다."
    
    menu:
        "어떻게 할까?"
        "하린에게 잠깐 쉬라고 말한다.":
            sj "반장, 숨 좀 돌려."
            sj "네가 지금 표정으로 계속 보면 종이가 먼저 타겠다."

            show harin surprise at center_lower, excited_hop with dissolve
            "하린이는 의외라는 표정을 지었다."
            hr "…내 표정, 그렇게 안 좋아 보여?"

            sj "응."
            sj "적어도 지금은 완벽보다 속도가 먼저 같은데."

            "하린이는 한동안 말이 없었다."
            "그러다 아주 작게 한숨을 내쉬었다."

            show harin normal at center_lower, sway_soft with dissolve
            hr "알아."
            hr "근데 내가 놓치면 다 엉망이 될 것 같아서."

            th "그 말은 책임감처럼 들리면서도, 거의 강박에 가까웠다."
        "유나 쪽으로 붙어서 분위기를 풀어준다.":
            sj "너무 죽상 짓지 마."
            sj "아까 말 틀린 것도 아니었어. 결국 다시 하면 되긴 하지."
            show yuna surprise at left, excited_hop with dissolve
            yn "…선배가 내 편 들어주네?"
            sj "내 편, 네 편이 아니라."
            sj "반장이 예민한 건 이해하고, 네 말도 틀린 건 아니라는 뜻."
            "유나는 나를 한참 보다가, 조금 힘 빠진 웃음을 지었다."

            show yuna smile at left, tiny_bounce with dissolve
            yn "헤헤."
            yn "그 말, 이상하게 위로된다."

            th "늘 해맑은 줄만 알았는데."
            th "유나도 생각보다 쉽게 상처받는 쪽일지도 모른다."
        "설아가 표시한 수정 부분을 바로 정리한다.":
            sj "좋아, 그럼 말 나온 김에 수정할 부분부터 적자."
            sj "설아, 네가 짚은 데 내가 받아 적을게."

            show seola surprise at right, excited_hop with dissolve
            "설아는 아주 잠깐 눈을 깜빡였다."
            sa "…응."

            "우리는 나란히 배치도를 내려다봤다."
            "설아는 여전히 짧게 말했다."
            "하지만 이번엔 내가 말을 따라가는 쪽이 아니라, 설아의 호흡에 맞춰 움직이고 있었다."

            sa "여기 이동."
            sa "이 문구는 유지."
            sa "저쪽은 장식 줄여."

            th "신기하게도, 설아와는 말이 적을수록 오히려 더 편해진다."
            
    hide harin with dissolve
    hide yuna with dissolve
    hide seola with dissolve

    scene black with dissolve
    centered "{size=30}점심시간 복도{/size}" with dissolve
    scene bg noisy_hallway with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    play sound "audio/sfw_walking.ogg"
    "수정안을 얼추 정리한 뒤, 나는 프린트 몇 장을 들고 복도로 나왔다."
    "교무실 쪽 복도는 점심시간 특유의 소란이 조금 덜했다."
    "멀리서 웃음소리와 실내화 끄는 소리만 웅웅 울렸다."
    stop sound fadeout 1.0
    
    "그때, 복도 창문 앞에 서 있는 유나의 뒷모습이 눈에 들어왔다."
    show yuna normal at center_lower, sway_soft with dissolve
    "아까까지만 해도 시끄럽게 떠들던 녀석이, 지금은 조용히 휴대폰 화면만 내려다보고 있었다."
    "밝은 표정도, 장난스러운 몸짓도 없었다."
    "창밖으로 들어오는 빛이 옆얼굴을 비추자, 이상할 정도로 표정이 비어 보였다."

    sj "뭐 하냐."
    show yuna surprise at center_lower, excited_hop with dissolve
    "유나는 내 목소리에 화들짝 놀라 휴대폰을 급히 뒤집었다."

    yn "아, 깜짝이야!"
    yn "선배는 인기척이 왜 이렇게 없어요?"

    sj "네가 멍하니 있었던 거지."
    sj "무슨 일 있어?"
    
    show yuna smile at center_lower, tiny_bounce with dissolve
    yn "없는데요?"
    yn "그냥, 엄마한테 연락했는데 답장이 좀 늦어서."
    "말은 가볍게 했지만, 유나는 손에 쥔 휴대폰을 너무 세게 쥐고 있었다."
    
    menu:
        "뭐라고 할까?"
        "괜히 혼자 끙끙대지 말라고 한다.":
            sj "네가 그렇게 웃는 얼굴로 얼버무리면, 더 티 난다."
            "유나의 눈이 조금 크게 흔들렸다."

            sj "괜히 혼자 끙끙대지 마."
            sj "말할 거 있으면 하고."
            
            show yuna smile at center_lower, tiny_bounce with dissolve
            yn "……선배는 진짜."
            yn "맨날 무심한 척하면서, 이런 건 또 다 보네."

            "유나는 곧장 자세한 이야기를 하진 않았다."
            "그래도 아까보단 손에 들어간 힘이 조금 풀렸다."

        "굳이 캐묻지 않고 음료 하나를 건넨다.":
            play sound "audio/sfw_walking.ogg"
            "나는 자판기 쪽으로 걸어가 캔 음료 하나를 뽑아 유나에게 건넸다."
            stop sound
            sj "표정이 너무 죽었어."
            sj "당 보충이나 해."

            show yuna surprise at center_lower, excited_hop with dissolve
            yn "…이거, 저 주는 거예요?"
            sj "내가 마실 거면 내가 벌써 땄겠지."

            "유나는 캔을 받아 들고 한참 말이 없었다."
            "그리고 아주 작게 웃었다."
            
            show yuna smile at center_lower, tiny_bounce with dissolve
            yn "고마워요."
            yn "이런 거, 되게 오래 기억하는 성격인 거 알죠?"

        "아무것도 묻지 않고 같이 창밖만 본다.":
            "나는 유나 옆에 서서 창밖 운동장을 같이 내려다봤다."
            "한동안 누구도 먼저 입을 열지 않았다."

            "잠깐 뒤, 유나가 먼저 입을 열었다."

            yn "선배."
            yn "아무 말 안 하는 것도, 생각보다 위로되네요."

            sj "시끄러운 네가 그런 말 하니까 어색하다."
            show yuna laugh at center_lower, idle_bounce with dissolve
            yn "아하하, 뭐예요 그게."
            
            th "웃긴."
            th "근데 정말, 아까보다는 조금 나아 보였다."

    hide yuna with dissolve

    play sound "audio/sfw_walking.ogg"
    "교실로 돌아가는 길, 나는 괜히 뒤를 한 번 더 돌아봤다."
    "유나는 다시 평소처럼 웃고 있었다."
    "하지만 그 웃음이 전처럼 아무 걱정 없는 얼굴로만 보이지는 않았다."
    stop sound fadeout 1.5
    scene black with fade
    "누군가를 안다고 생각하는 것과, 실제로 아는 건 다른 문제였다."

    # ---------------------------------------------------------
    # Scene 10
label scene_10:
    scene black with fade
    centered "{size=40}Scene 10{/size}\n\n{size=30}선 밖의 저녁{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_theme_seola.ogg" fadein 2.0

    "그날 방과 후, 우리는 다시 특별동 준비실에 모였다."
    "낡은 창틀 사이로 늦은 햇빛이 길게 들어와, 공중의 먼지까지 또렷하게 보였다."
    "다들 어제보다 조금 피곤한 얼굴이었다."
    
    show seola normal at char_2, sway_soft
    show harin normal at char_3, sway_soft
    show gaeun smile at char_4, tiny_bounce
    with dissolve

    "하린이는 수정된 배치표를 다시 정리하고 있었고, 설아는 새 포스터 구도를 잡고 있었고, 가은 선배는 의자에 걸터앉아 학생회 쪽 전달사항을 확인하고 있었다."
    "유나는 한 박자 늦게 들어왔다."

    play sound "audio/sfx_Sliding_door.ogg"
    show yuna smile at char_1, tiny_bounce with dissolve

    yn "죄송합니다!"
    yn "오는 길에 학생회 선배 붙잡혀서 테이프 좀 나눠주고 왔어요."

    sj "네가 붙잡힌 건지, 네가 먼저 끼어든 건지 모르겠다."
    show yuna laugh at char_1, idle_bounce with dissolve
    yn "헤헤. 둘 다?"

    "겉보기엔 평소와 다르지 않았다."
    "하지만 전부 조금씩 달랐다."
    
    th "하린은 더 예민해졌고."
    th "유나는 더 밝게 웃으려고 했고."
    th "설아는 더 조용해졌고."
    th "가은 선배는 괜찮은 척이 점점 익숙해 보였다."

    "작업은 무난하게 진행되는 듯했다."
    "적어도, 사건이 벌어지기 전까지는."
    
    play sound "audio/sfx_Cardboard_box_drop.ogg"
    "준비실 한구석에 쌓아 둔 장식 상자를 옮기던 중, 맨 위 박스가 한쪽으로 기울어졌다."
    "그 안에 있던 종이 장식과 파일 뭉치가 바닥에 와르르 쏟아졌다."
    play sound "audio/sfx_pen_click.ogg"

    show harin surprise at char_3, excited_hop with dissolve
    hr "잠깐…!"
    
    play sound "audio/sfw_cloth_moving.ogg" volume 0.7
    "하린이가 급히 다가갔고, 유나도 동시에 몸을 숙였다."
    "설아는 떨어진 종이들이 밟히지 않도록 재빨리 발끝으로 밀어 빼냈다."
    "가은 선배는 웃으며 '다친 사람 없지?'부터 확인했다."
    "순식간에 네 사람이 동시에 움직였다."
    "그 장면이 이상하게 눈에 박혔다."
    
    th "다들 엉망이 되는 건 싫어한다."
    th "방법만 다를 뿐."
    
    menu:
        "누구를 먼저 챙길까?"
        "하린부터 본다.":
            sj "반장, 손 괜찮아?"
            sj "박스 모서리에 긁힌 것 같은데."

            show harin surprise at char_3, excited_hop with dissolve
            "하린이는 자기 손등을 보고서야 얕게 긁힌 자국을 알아챘다."
            hr "이 정도는 별거 아니야."

            sj "별거 아닌 걸 자꾸 누적시키는 게 문제지."

            "하린이는 대답하지 않았다."
            "대신 시선을 잠깐 내 쪽으로 들었다가, 다시 아래로 내렸다."

            show harin normal at char_3, sway_soft with dissolve
            hr "…고마워."
        "유나부터 본다.":
            sj "너는 또 무작정 몸부터 던졌냐."
            sj "안 다쳤어?"

            show yuna smile at char_1, tiny_bounce with dissolve
            yn "저 정도는 하나도 안 아픈데요?"
            sj "그 말 하는 애들이 꼭 나중에 정강이에 멍 들어 있다."

            "내가 팔목을 한 번 확인하듯 잡아 보자, 유나는 괜히 가만해졌다."
            "그리고 아주 잠깐, 웃는 걸 잊었다."

            yn "…선배."
            yn "그렇게 당연하게 챙기면 반칙이에요."
            
            show yuna laugh at char_1, idle_bounce with dissolve
            yn "아, 아무튼 전 멀쩡합니다!"
        "설아부터 본다.":
            sj "설아, 밟힐 뻔한 거 네가 먼저 뺐지."
            sj "괜찮아?"

            show seola normal at char_2, sway_soft with dissolve
            sa "응."
            sa "익숙해."

            sj "뭐가?"

            "설아는 대답 대신 바닥의 종이 몇 장을 주워 내 손에 올려두었다."

            sa "엉키기 전에 정리하는 거."
            
            th "짧은데 이상하게 오래 남는 말."
            th "설아는 늘 딱 필요한 만큼만 말하는데, 그래서 더 파고들 여백이 생긴다."
        "가은 선배부터 본다.":
            sj "선배는요."
            sj "안색이 더 안 좋아 보이는데."

            show gaeun normal at char_4, sway_soft with dissolve
            ge "와, 상처 입은 건 나 아닌데 제일 먼저 나 챙겨주네?"
            ge "후배님, 나 울겠다."

            sj "농담할 얼굴이 아닌데요."

            "가은 선배는 웃다가, 아주 잠깐 표정을 멈췄다."
            "숨을 들이마시는 호흡이 눈에 띄게 얕았다."

            ge "…진짜 괜찮아."
            ge "조금 피곤한 것뿐이야."

            th "그 말은 진짜 같지 않았다."
            
    hide harin with dissolve
    hide yuna with dissolve
    hide seola with dissolve
    hide gaeun with dissolve

    "정리를 끝내고 나니 어느새 학교는 거의 비어 있었다."
    "창밖은 이미 저녁빛으로 물들고, 복도 소음도 많이 가라앉아 있었다."

    scene black with dissolve
    centered "{size=30}해 질 녘 복도{/size}" with dissolve
    scene bg noisy_hallway with fade
    play music "audio/bgm_theme_gaeun.ogg" fadein 1.5

    play sound "audio/sfx_Sliding_door.ogg"
    "우리는 준비실 문을 잠그고 함께 복도로 나왔다."
    "평소보다 조용한 학교는 낯설 정도로 넓게 느껴졌다."

    "계단 앞에서 자연스럽게 발걸음이 갈렸다."
    
    show yuna smile at left, tiny_bounce with dissolve
    show seola normal at center_lower, sway_soft with dissolve
    show harin normal at right, sway_soft with dissolve
    
    yn "전 여기서 아래로 바로 갈게요!"
    yn "아, 선배. 내일 아침에 또 보러 갈 건데, 도망가면 안 돼요?"

    hr "난 교무실 들렀다가 갈 거야."
    hr "수정안 한 번 더 확인해야 해서."

    sa "난 잠깐 도서관."
    sa "빌린 책 반납하고."

    "각자의 목적지는 다 달랐다."
    "그런데도 이상하게, 아무도 먼저 완전히 떠나지는 않았다."

    th "조금만 더 가까워지면 곤란해질 것 같은데."
    th "조금만 더 멀어지면, 어쩐지 신경 쓰일 것 같기도 했다."
    "그리고 그 순간, 계단 위쪽에서 가은 선배의 기침 소리가 짧게 울렸다."
    
    hide seola
    hide harin
    hide yuna
    show gaeun normal at center_lower, sway_soft with dissolve

    "아주 짧았다."
    "하지만 다들 동시에 그쪽을 봤다."

    ge "왜, 다들 그런 표정이야."
    ge "진짜 괜찮다니까."
    "선배는 웃었고, 우리는 아무도 그 말을 곧이곧대로 받아들이지 못했다."
    
    menu:
        "마지막에 누구를 더 신경 쓸까?"
        "유나를 붙잡는다.":
            sj "야, 너."
            sj "내일 아침에 또 뛰어오지 말고 천천히 와."

            show yuna surprise at center_lower, excited_hop with dissolve
            yn "…그 말은, 기다려준다는 뜻이에요?"
            sj "왜 꼭 그런 식으로 해석하냐."

            show yuna smile at center_lower, tiny_bounce with dissolve
            yn "헤헤."
            yn "그럼 천천히 가도 결국 만날 수 있다는 뜻으로 받아들일게요."

            th "저런 식으로 기분 좋아하는 얼굴은, 보기보다 위험하다."
            th "괜히 한 발 더 들이게 만들잖아."

        "하린을 도와 교무실 쪽으로 같이 걷는다.":
            sj "반장, 서류 많아 보이는데."
            sj "교무실까지는 같이 가줄까."

            show harin surprise at center_lower, excited_hop with dissolve
            hr "…네가?"
            sj "나도 내가 왜 이런 말 하는지 잘 모르겠다."

            "하린이는 잠깐 입을 다물었다가, 아주 희미하게 고개를 끄덕였다."
            
            show harin normal at center_lower, sway_soft with dissolve
            hr "그럼, 잠깐만."
            th "서하린은 강한 척을 잘한다."
            th "그래서 오히려, 기대는 순간이 더 선명하게 보인다."
            
        "설아와 도서관 쪽으로 잠깐 같이 간다.":
            sj "나도 어차피 그쪽 지나가."
            sj "같이 갈래?"

            show seola surprise at center_lower, excited_hop with dissolve
            "설아는 내 얼굴을 잠깐 바라보다가, 조용히 고개를 끄덕였다."
            sa "…응."

            "짧은 대답."
            "그런데 이상하게도 거절보다 훨씬 크게 느껴졌다."

            th "설아와는 말이 적은데도 침묵이 불편하지 않다."
            th "오히려 그래서 더 위험한지도 모른다."

        "가은 선배를 끝까지 본다.":
            sj "선배."
            sj "집에 그냥 바로 가세요. 오늘은 진짜."

            show gaeun smile at center_lower, tiny_bounce with dissolve
            ge "명령이야, 부탁이야?"
            sj "둘 다요."

            "가은 선배는 웃었다."
            "하지만 이번에는 그 웃음 뒤에 아주 잠깐 피로가 그대로 드러났다."

            ge "…알았어."
            ge "오늘은 착한 후배 말 좀 들어줄게."

            th "처음이었다."
            th "민가은이 그렇게 순순히 물러나는 건."
            
    hide yuna with dissolve
    hide harin with dissolve
    hide seola with dissolve
    hide gaeun with dissolve

    scene black with fade

    "학교를 나서는 길."
    "봄밤의 공기는 낮보다 차가웠고, 그래서 더 또렷했다."

    th "유나는 생각보다 쉽게 흔들렸고."
    th "하린은 생각보다 위태로웠고."
    th "설아는 생각보다 많은 걸 숨기고 있었고."
    th "가은 선배는 생각보다 오래 버티고 있는 얼굴을 하고 있었다."
    
    th "나는 아직 아무것도 모른다."
    th "그저 가까이에서 봤을 뿐이고, 조금 더 신경 쓰이기 시작했을 뿐이다."

    th "그런데 이상하게."
    th "이제 와서 아무 일도 없는 척, 다시 예전 거리로 돌아가기는 어려울 것 같았다."

    "미지근했던 일상에, 아주 가느다란 금이 갔다."
    "그리고 그런 금은 대개, 소리도 없이 점점 깊어진다."
    
    th "정말 유치한데."
    th "왜 이렇게 마음에 남는 건지."
    scene black with fade

# ---------------------------------------------------------
# [Scene 11 타이틀]
label scene_11:

    scene black with fade
    centered "{size=40}Scene 11{/size}\n\n{size=30}반짝이와 형광펜{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "다음 날 방과 후, 특별동 준비실."
    "문을 열고 들어가자마자 내 시야를 가득 채운 건, 눈이 부실 정도로 번쩍거리는 정체불명의 물체였다."
    show yuna smile at left, tiny_bounce with dissolve

    yn "짠!! 서진 선배, 이거 어때요? 제가 점심시간에 매점 가는 길에 문방구 들러서 사 온 거예요!"
    sj "…그게 대체 뭔데."
    
    yn "모르겠어요? 벚꽃 장식에 달 반짝이 하트 몰딩이잖아요! 완전 예쁘죠?"
    "유나는 양손에 핫핑크색 반짝이가 잔뜩 묻은 거대한 하트 장식을 들고 해맑게 웃고 있었다."
    "장식이 흔들릴 때마다 바닥으로 반짝이 가루가 눈꽃처럼 후드득 떨어져 내렸다."
    show harin sigh at right, sway_soft with dissolve

    hr "유나야."
    "테이블 반대편에서, 자를 대고 예산안을 긋고 있던 하린이가 안경을 치켜올리며 아주 차분하게 불렀다."
    
    hr "그거, 예산 청구할 생각은 아니지?"
    hr "우리 부스 테마는 '모던'이랑 '깔끔함'이야. 그 핫핑크색 반짝이는 도저히 통과시켜 줄 수가 없는데."
    show yuna pout at left, sway_soft with dissolve
    yn "아, 반장 선배! 모던도 좋지만 축제는 무조건 눈에 띄어야 제맛이라구요!"
    yn "그리고 이거 제 사비로 산 거예요! 예산 청구 안 할 테니까 하나만 달게 해주세요, 네? 여기 딱 하나만!"
    hr "사비로 산 건 고맙지만, 바닥에 반짝이 떨어지잖아. 청소는 누가 할 건데."
    hr "그리고 그 장식, 안내 데스크 시야를 가려. 기각."
    
    "하린이는 단호하게 선을 그으며, 손에 쥔 형광펜으로 일정표에 체크 표시를 그었다."
    "유나가 입술을 삐죽이며 나를 향해 억울하다는 듯 구원의 눈빛을 보냈다."

    th "전형적인 학생회 에이스와 천방지축 1학년의 조합이다."
    th "이 시끄럽고 평화로운 소음이, 축제 준비라는 실감을 확 나게 만들었다."
    show gaeun laugh at center_lower, idle_bounce with dissolve
    ge "아하하! 우리 막내, 시작부터 기각당했네."
    "창가 쪽에 느긋하게 기대어 캔커피를 홀짝이던 가은 선배가 어깨를 들썩이며 웃었다."
    ge "하린아, 너무 팍팍하게 굴지 마. 애가 자기 돈까지 썼다잖아."
    ge "어디 구석에라도 하나 달게 해줘. 꽤 귀엽구만 뭐."
    show harin normal at right, sway_soft with dissolve
    hr "선배는 총괄 보조시면서 왜 유나 편만 드세요."
    hr "그렇게 귀여우시면 선배 학생회실 책상 위에 달아두시든가요."
    
    show gaeun smile at center_lower, tiny_bounce with dissolve
    ge "오, 그거 좋은데? 후배님, 그 반짝이 나한테 기부할래?"
    yn "진짜요?! 와, 역시 가은 선배가 최고예요! 하린 선배는 완전 냉혈한!"
    
    hr "들었어."
    "하린이는 가볍게 콧방귀를 뀌며 다시 서류로 시선을 돌렸다."
    "하지만 아까보다 입꼬리가 아주 미세하게 올라가 있는 걸 보면, 진짜 화가 난 건 아닌 모양이다."
    th "하린이는 매사 철저하고 깐깐하지만, 선을 넘지 않는 장난에는 생각보다 관대하다."
    th "다들 조금씩 이 기묘한 조합에 적응해가고 있는 것 같았다."
    hide yuna with dissolve
    hide harin with dissolve
    hide gaeun with dissolve

    "나는 가방을 내려놓고, 구석에서 조용히 도화지를 자르고 있는 설아 쪽으로 다가갔다."
    show seola normal at center_lower, sway_soft with dissolve
    
    "설아는 다른 사람들이 떠들든 말든, 자신의 세계에 빠져 안내 패널에 들어갈 글씨를 오리고 있었다."
    "그런데 그 모양이…."
    
    sj "설아, 너 지금 뭐 오려?"
    
    sa "별."
    
    sj "그치. 별이네. 아주 작고 반듯한 별."
    sj "근데 이거 패널 안내 문구 옆에 붙일 거 아니야? 너무 작아서 안 보일 것 같은데."
    
    sa "…알아."
    sa "그래도, 자세히 보면 보일 테니까."
    
    "설아는 하얀 손가락으로 좁쌀만 한 종이 별을 조심스럽게 밀어 모았다."
    "남들의 시선을 피하고 싶어 하면서도, 누군가 '자세히 봐주었으면' 하는 묘한 모순이 느껴졌다."
    "그때 복도 쪽에서 쿵쿵거리는 요란한 발소리와 함께 남자애들의 시끄러운 웃음소리가 스쳐 지나갔다."
    
    sa "……."
    "설아는 흠칫 놀라며 오리던 손을 멈추고 무의식적으로 목덜미를 한 번 쓰다듬었다."
    "하지만 금세 다시 평온한 얼굴로 돌아와 종이 별을 집어 들었다."

    th "이제 슬슬 나도 일손을 보태야 할 시간이다."
    th "이 평화롭고 소란스러운 난장판 속에서, 나는 누구 쪽으로 갈까."

    menu:
        "어디부터 도와줄까?"
        "유나의 반짝이 테러 현장을 수습한다.":
            # [수정 2] 설아가 이미 center에 있으므로, 겹치지 않게 자연스러운 퇴장 처리
            hide seola with dissolve
            $ yuna_point += 1
            
            sj "야, 유나. 너 여기 바닥에 반짝이 떨어진 거 안 보이냐."
            sj "하린이한테 혼나기 전에 내가 빗자루 가져올 테니까 같이 쓸자."
            show yuna smile at center_lower, tiny_bounce with dissolve
            yn "아, 넵! 죄송합니다 기사님!"
            yn "근데 선배, 빗자루질 같이 하니까 뭔가… 청소 당번 빙자한 데이트 같지 않아요?"
            
            sj "헛소리 말고 구석이나 꼼꼼히 쓸어."
            yn "치, 부끄러워하기는. 그래도 선배가 먼저 도와준다고 해서 나 지금 완전 기분 최고조예요!"
            "유나는 빗자루를 들고 콧노래를 부르며 내 옆에 딱 붙어 바닥을 쓸었다."
            "단순한 심부름조차 이렇게 즐거워하는 걸 보면, 참 신기한 에너지를 가진 녀석이다."
        "하린의 서류 작업을 보조한다.":
            # [수정 2] 겹침 방지
            hide seola with dissolve
            $ harin_point += 1
            
            sj "반장, 그거 색지별 예산 짠 거지. 영수증 내가 풀로 붙일까?"
            show harin surprise at center_lower, excited_hop with dissolve
            hr "…어? 아, 응. 여기."
            "하린이는 살짝 놀란 눈으로 영수증 더미와 딱풀을 내밀었다."
            
            hr "영수증 끝부분 선 맞춰서 반듯하게 붙여줘. 나중에 결재받을 때 지저분하면 다시 해야 하니까."
            sj "알았어, 아주 오와 열을 맞춰서 군대식으로 붙여드리지."
            
            show harin faint_smile at center_lower, tiny_bounce with dissolve
            hr "…뭐야 그게."
            "하린이가 작게 피식 웃으며 서류를 넘겼다."
            "여전히 볼펜을 손에 꼭 쥐고 있긴 했지만, 아까보다는 어깨에 힘이 많이 빠져 보였다."
        "설아의 종이 별 오리기를 돕는다.":
            $ seola_point += 1
            
            sj "나도 가위 줘. 그거 혼자 다 오리려면 날 새겠다."
            show seola surprise at center_lower, excited_hop with dissolve
            sa "…재미없을 텐데."
            sj "너 혼자 하는 것보단 덜 심심하겠지."
            
            "내가 가위를 집어 들고 서툴게 별 모양을 따라 자르기 시작하자, 설아가 가만히 내 손끝을 쳐다보았다."
            show seola normal at center_lower, sway_soft with dissolve
            sa "선, 삐뚤어졌어."
            sj "야, 나는 너처럼 정밀하게 못 오려."
            
            sa "…그래도, 괜찮아."
            sa "조금 삐뚤어진 별도… 나쁘지 않아."
            "설아의 옅은 칭찬에 우리는 말없이 종이 자르는 사각거리는 소리에 집중했다."
            "이 고요한 공간이 꽤 마음에 들었다."
        "가은 선배와 농땡이에 동참한다.":
            # [수정 2] 겹침 방지
            hide seola with dissolve
            $ gaeun_point += 1
            
            sj "선배, 혼자 커피 드시기 있습니까. 저도 좀 쉬어야겠습니다."
            show gaeun smile at center_lower, tiny_bounce with dissolve
            ge "어허, 2학년 젊은 피가 벌써부터 지치면 쓰나."
            ge "자, 이건 내 특별 하사품이야. 매점표 꿀물."
            
            "가은 선배가 주머니에서 따뜻한 캔 음료를 꺼내 내 볼에 가볍게 툭, 댔다."
            sj "선배는 진짜 도라에몽 주머니라도 달고 다니시나 봐요. 안 나오는 게 없네."
            ge "그치? 나 완전 유능한 선배지? 그러니까 가서 저기 삐약거리는 1학년이랑 깐깐한 반장 좀 말려봐."
            ge "이러다 오늘 안에 회의 안 끝날 것 같아."
            
            "가은 선배는 한 발짝 떨어져서 후배들을 관찰하며 즐거운 듯 웃었다."
            "하지만 내가 음료수를 받으려 선배 쪽으로 조금 가까이 다가가자, 선배는 아주 자연스럽게 한 걸음 뒤로 물러서며 거리를 유지했다."
            "정말 눈치채기 어려울 만큼 교묘한 회피였다."

    # 분기 종료
    scene black with fade
    play music "audio/bgm_spring_morning.ogg" fadein 2.0

    "우당탕거리는 소동 속에서도, 축제 준비는 아주 조금씩 앞으로 나아가고 있었다."
    "종이를 자르는 소리, 누군가 투덜거리는 소리, 그리고 가벼운 웃음소리."
    
    th "다들 각자의 방식으로 이 공간에 적응하고 있다."
    th "어쩌면 이 미지근하고 평화로운 시간이 생각보다 꽤 오래갈지도 모르겠다." 
    
    "창밖으로 봄꽃 냄새가 훅 끼쳐오는, 아주 완벽하게 몽글몽글한 오후였다."
# ---------------------------------------------------------
# [Scene 12 타이틀]
label scene_12:

    scene black with fade
    centered "{size=40}Scene 12{/size}\n\n{size=30}별이 뜨는 저녁의 피자 파티{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "어느새 창밖의 하늘이 오렌지빛에서 짙은 남색으로 넘어가고 있었다."
    "특별동 준비실의 형광등이 유난히 밝게 느껴질 즈음, 끝이 없을 것 같던 가위질과 풀칠도 어느 정도 마무리가 되어가고 있었다."
    "다들 말수는 줄어들었고, 책상 위에는 잘라낸 색지 쪼가리와 지우개 가루가 눈처럼 쌓여 있었다."
    play sound "audio/sfx_Stomach_growl.ogg"
    "꼬르륵—."
    "고요한 준비실의 정적을 깨는, 아주 크고 명확한 소리."
    "단순히 배가 고프다는 신호를 넘어, 거의 천둥소리에 가까운 우렁찬 울림이었다."

    sj "……누구냐."
    show yuna surprise at center_lower, excited_hop with dissolve
    "내 물음에, 가위질을 하던 유나가 헉, 하고 숨을 들이켜더니 얼굴을 붉게 물들였다."
    "녀석은 양손으로 자신의 배를 꽉 끌어안으며 내 눈치를 살폈다."

    yn "아, 아니에요! 저 아니에요! 방금 밖에서 오토바이 지나가는 소리 났는데?!"
    sj "오토바이가 네 뱃속에서 굴러가냐. 변명을 하려면 좀 성의 있게 해라."
    show yuna pout at center_lower, sway_soft with dissolve
    yn "아, 진짜 선배! 모른 척 좀 해주면 어디가 덧나요? 나 완전 수치스러워!"
    show gaeun laugh at right, idle_bounce with dissolve
    ge "아하하하! 우리 막내 배꼽시계 진짜 정확하네. 하긴, 점심 먹고 지금까지 내리 노동만 했으니 배고플 때도 됐지."
    "가은 선배가 박장대소하며 유나의 헝클어진 머리를 쓰다듬었다."
    "유나는 부끄러운지 가은 선배의 품으로 고개를 푹 숙이면서도, 힐끗힐끗 내 쪽을 쳐다보며 입술을 삐죽거렸다."
    show harin normal at left, sway_soft with dissolve
    hr "그러고 보니 벌써 시간이 이렇게 됐네."
    hr "오늘은 다들 고생했어. 일단 여기서 마무리하고 내일 마저 하자."

    "하린이가 책상 위의 서류들을 각 맞춰 정리하며 선언했다."
    "평소라면 당장 가방을 챙겨서 나갔을 테지만, 오늘은 어쩐지 다들 자리에서 선뜻 일어나지 않았다."
    "유나가 배를 문지르며 눈을 반짝였다."
    show yuna smile at center_lower, tiny_bounce with dissolve
    yn "저기요! 기왕 이렇게 늦은 거, 우리 다 같이 뭐 좀 시켜 먹고 가면 안 돼요?"
    yn "나 진짜 지금 이대로 집에 가다간 길바닥에서 아사할지도 몰라요! 네? 네에?"
    hr "학교에 외부 음식 반입하는 거, 원칙적으로는 금지야. 냄새도 배고."
    hr "게다가 뒷정리 제대로 안 하면 내일 아침에 벌레 꼬여서 안 돼."

    "하린이가 단호하게 고개를 저었다. 예상했던 반응이다."
    "완벽한 통제와 청결을 중시하는 반장님에게 교내 배달 음식이라니, 어불성설이지."

    show gaeun smile at right, tiny_bounce with dissolve
    ge "에이, 하린아. 원칙은 원래 가끔 깨라고 있는 거야."
    ge "그리고 오늘 진도도 많이 뺐는데, 이 정도 보상은 있어야 우리 도우미들이 내일도 도망 안 가고 일해주지 않겠어?"
    ge "오늘은 내가 쏜다! 법인 카드… 아니, 내 개인 카드 찬스!"
    show yuna surprise at center_lower, excited_hop with hpunch
    yn "헐! 가은 선배 완전 멋있어! 빛가은! 갓가은! 사랑해요!"
    "유나가 두 손을 번쩍 들며 환호했다."
    "하린이는 미간을 살짝 좁히며 가은 선배와 유나를 번갈아 보았다."
    
    hr "선배까지 그러시면…."
    ge "뒷정리는 쟤네 둘 시키면 되잖아. 그치, 서진아?"

    sj "거기서 제 이름이 왜 나옵니까."
    ge "네가 막내 오토바이 소리 놀렸으니까, 네가 청소 담당해. 어때, 합리적이지?"
    
    "가은 선배의 능청스러운 미소에 나는 짧게 한숨을 쉬었다."
    "반박하고 싶었지만, 사실 나도 아까부터 뱃속에서 요동을 치고 있던 참이었다."
    sj "…반장, 냄새 안 배게 창문 활짝 열어둘게. 뒷정리도 내가 완벽하게 할게."
    sj "오늘은 그냥 넘어가 주라. 나도 배고프다."
    show harin surprise at left, excited_hop with dissolve
    "내 말에 하린이의 눈이 아주 조금 커졌다."
    "자신을 밀어붙이는 게 유나나 선배가 아니라, 나라는 사실이 의외인 눈치였다."
    "하린이는 흠, 하고 헛기침을 하더니 시선을 슬쩍 피했다."
    show harin normal at left, sway_soft with dissolve
    hr "…네가 굳이 그렇게까지 말한다면."
    hr "대신 쓰레기는 무조건 학교 밖으로 가져가서 버리는 조건이야. 알겠지?"

    yn "아싸! 하린 선배도 최고! 우리 반장님 완전 천사!"
    "유나가 신이 나서 방방 뛰었고, 구석에서 조용히 짐을 챙기던 설아도 살짝 멈칫하더니 다시 자리에 앉았다."
    hide harin with dissolve
    hide yuna with dissolve
    hide gaeun with dissolve

    "메뉴 선정은 치열했다."
    "떡볶이를 주장하는 유나, 먹기 편한 치킨을 주장하는 하린, 그리고 둘 다 시키자는 호쾌한 가은 선배의 중재 끝에 결국 '피자와 치킨 세트'라는 가장 클래식한 합의에 도달했다."
    "약 30분 뒤."
    "배달 기사가 학교 철창 너머로 건네준 거대한 박스들을 들고 오자, 준비실은 순식간에 기름지고 고소한 냄새로 가득 찼다."
    scene black with dissolve
    centered "{size=30}피자 파티{/size}" with dissolve
    scene bg old_library with fade
    play music "audio/bgm_spring_morning.ogg" fadein 1.5

    show cg pizza_party with dissolve
    
    yn "와, 냄새 미쳤다! 잘 먹겠습니다!"
    "테이블 위에 신문지를 깔고 박스를 열자마자 유나가 환호성을 지르며 피자 한 조각을 집어 들었다."
    "치즈가 길게 늘어나는 걸 보며 세상을 다 가진 듯한 표정을 짓는 녀석을 보니, 덩달아 헛웃음이 나왔다."
    hr "유나야, 흘리지 않게 밑에 휴지 받치고 먹어."
    hr "치즈 바닥에 떨어지면 닦기 힘들어."
    "하린이는 자신이 먹을 치킨 한 조각을 접시에 조심스럽게 덜어내면서도, 유나에게 잔소리를 잊지 않았다."
    "녀석은 심지어 치킨을 먹을 때도 젓가락을 사용하고 있었다. 손에 기름을 묻히는 것조차 극도로 꺼리는 저 철저함."
    ge "아유, 우리 반장님은 밥 먹을 때도 깐깐하네."
    ge "자, 서진이랑 설아도 눈치 보지 말고 팍팍 먹어. 모자라면 더 시켜줄 테니까."
    "가은 선배는 콜라를 종이컵에 따라 모두에게 돌렸다."
    "나도 피자 한 조각을 집어 들고 한입 베어 물었다. 입안 가득 퍼지는 토마토소스와 페퍼로니의 짭짤한 맛에, 하루 종일 쌓였던 피로가 단번에 녹아내리는 기분이었다."
    th "축제 준비, 도우미, 강제 야근."
    th "이런 번잡한 일들은 딱 질색이라고 생각했는데."
    th "이렇게 다 같이 둘러앉아 밥을 먹고 있으니, 꽤 전형적이고 청춘스러운 학원물의 한 장면 같기도 하다."
    "시끌벅적하게 식사가 이어지는 가운데, 나는 문득 주변을 둘러보았다."
    "다들 각자의 방식으로 이 소란스러운 식사 자리를 즐기고 있었다."
    scene bg old_library with dissolve
    show yuna smile at char_1, tiny_bounce
    show seola normal at char_2, sway_soft
    show harin normal at char_3, sway_soft
    show gaeun smile at char_4, tiny_bounce
    with dissolve
    
    menu:
        "누구에게 말을 걸까?"
        "입가에 소스를 묻히고 먹는 유나를 챙긴다.":
            $ yuna_point += 1
            
            sj "야, 유나. 너 피자를 얼굴로 먹냐."
            show yuna surprise at char_1, excited_hop with dissolve
            yn "우물우물… 넹? 저 불렀어여?"
            "입안 가득 피자를 쑤셔 넣은 유나가 볼을 빵빵하게 부풀린 채 나를 쳐다보았다."
            "입가에는 토마토소스가 수염처럼 잔뜩 묻어 있었다."
            "나는 쯧쯧 혀를 차며, 테이블 위에 있던 물티슈를 한 장 뽑아 녀석의 입가를 거칠게 닦아주었다."
            sj "칠칠맞게. 하린이한테 또 혼나고 싶어서 그래?"
            
            "갑작스러운 내 손길에, 유나의 씹던 입이 딱 멈췄다."
            "녀석의 동그란 눈이 나를 빤히 쳐다보더니, 이내 얼굴이 홍당무처럼 확 달아올랐다."
            show yuna pout at char_1, sway_soft with dissolve
            yn "서, 선배! 갑자기 훅 들어오기 있어요?!"
            yn "이런 건, 막 순정만화에서 남주가 여주한테 해주는 그런 심쿵 포인트인데!"
            sj "순정만화 여주는 너처럼 피자 소스를 턱까지 묻히고 먹진 않아."
            show yuna smile at char_1, tiny_bounce with dissolve
            yn "아 진짜, 무드라곤 하나도 없다니까!"
            yn "그래도… 헤헤, 고마워요. 닦아준 김에 저 콜라도 한 잔만 따라주시면 안 될까요, 기사님?"
            
            "유나가 빈 컵을 들이밀며 헤실헤실 웃었다."
            "나는 어이가 없다는 듯 웃으며 녀석의 컵에 콜라를 가득 채워주었다."
            "유나의 과장된 밝음 이면에 숨겨진 인정 욕구가 조금 엿보였지만, 지금 이 순간만큼은 그저 사랑받고 싶어 하는 어린애 같아서 밉지 않았다."
        "불편해 보이는 하린에게 포크를 건넨다.":
            $ harin_point += 1
            
            "나는 젓가락으로 힘겹게 치킨 뼈를 발라내고 있는 하린이를 빤히 쳐다보았다."
            "손에 기름을 묻히기 싫어서 젓가락만 고집하고 있지만, 뼈 있는 치킨을 그렇게 먹기란 여간 불편한 게 아니다."
            "나는 배달 봉투 안에 들어있던 일회용 포크를 뜯어 하린이의 앞접시 곁에 조용히 놓아주었다."
            sj "젓가락 하나로 씨름하지 말고 포크랑 같이 써."
            sj "그렇게 긴장하고 먹으면 체한다."
            show harin surprise at char_3, excited_hop with dissolve
            "하린이는 내가 놓아준 포크와 내 얼굴을 번갈아 보았다."
            "그녀의 표정에 아주 미세한 당혹감이 스쳐 지나갔다."
            
            hr "…신경 쓰게 했어?"
            sj "너 혼자 고상하게 먹으려다 뼈 튀어서 내 옷에 묻을까 봐 그러지."
            "내가 일부러 퉁명스럽게 받아치자, 하린이는 아주 작게 피식 웃음을 터뜨렸다."
            "그녀가 그렇게 소리 내어 웃는 것은 처음 보는 것 같았다."
            show harin faint_smile at char_3, tiny_bounce with dissolve
            hr "핑계도 참."
            hr "고마워. 잘 쓸게."
            
            "하린이는 포크와 젓가락을 양손에 쥐고 한결 편안해진 얼굴로 치킨을 발라 먹기 시작했다."
            "그녀의 교복 소매 끝이 아주 미세하게 말려 올라가 있었지만, 지금은 그 안의 흉터를 굳이 찾아보려 하지 않았다."
            "오늘의 하린이는 완벽한 반장이 아니라, 그저 또래의 여학생처럼 보였다."

        "혼자 조용히 먹고 있는 설아에게 피자를 밀어준다.":
            $ seola_point += 1
            
            "모두가 시끌벅적하게 대화를 나누는 가운데, 설아는 테이블 가장자리에서 조용히 치킨 한 조각만을 베어 물고 있었다."
            "그녀의 앞접시는 텅 비어 있었고, 음식보다는 사람들의 온기를 관찰하는 데 집중하는 것 같았다."
            "나는 페퍼로니 피자 한 조각을 들어 설아의 앞접시에 조용히 올려놓았다."
            show seola surprise at char_2, excited_hop with dissolve
            sa "……?"
            "설아의 붉은 눈동자가 물음표를 띄우며 나를 향했다."
            
            sj "치킨만 먹으면 물리잖아. 피자도 좀 먹어."
            sj "다 식기 전에."
            show seola normal at char_2, sway_soft with dissolve
            "설아는 접시 위에 놓인 피자를 가만히 내려다보았다."
            "그리고 아주 조심스럽게, 두 손으로 피자 끝부분을 잡아 한입 작게 베어 물었다."
            
            sa "…따뜻해."
            
            sj "방금 막 왔으니까."
            sa "피자 말고."
            
            "설아는 나를 보며 아주 희미하게, 달빛처럼 은은한 미소를 지었다."
            
            sa "네가 챙겨주는 게."
            sa "따뜻하다고."
            "그 솔직하고 담백한 한마디에, 오히려 내 귀끝이 살짝 달아오르는 기분이었다."
            "설아는 사람의 시선을 두려워하지만, 거짓 없이 다가오는 다정함에는 누구보다 예민하게 반응하는 아이였다."
            "나는 헛기침을 하며 남은 콜라를 벌컥벌컥 들이마셨다."
        "적게 먹는 가은 선배의 상태를 살핀다.":
            $ gaeun_point += 1
            
            "가장 분위기를 주도하던 가은 선배는, 정작 본인은 피자 반 조각을 겨우 먹은 채 콜라만 만지작거리고 있었다."
            "음식을 삼키는 게 어딘가 불편해 보였다."
            
            sj "선배. 돈 내신 분이 제일 안 드시면 어떡합니까."
            sj "치킨 다리 하나 빼뒀는데 드실래요?"
            
            show gaeun smile at char_4, tiny_bounce with dissolve
            ge "어머, 후배님이 내 몫까지 챙겨주는 거야? 닭다리 양보하는 건 진짜 사랑인데."
            sj "사랑은 무슨. 돈 낸 사람에 대한 예의죠. 얼른 드세요."
            
            "내가 치킨을 밀어주자, 가은 선배는 고마워하는 척하며 받아 들었다."
            "하지만 그녀의 시선은 음식에 닿자마자 미세하게 흔들렸다."
            "선배는 아주 작게 목을 가다듬으며, 억지로 한입을 베어 물었다."
            ge "으음~ 맛있다. 역시 우리 후배님이 챙겨줘서 더 맛있네."
            
            "선배는 활짝 웃었지만, 나는 선배가 고기를 삼키며 아주 미세하게 미간을 찌푸리는 것을 놓치지 않았다."
            "마치 목구멍으로 무언가 넘어가는 것 자체를 본능적으로 거부하는 것 같은 몸짓."
            
            th "어제 옥상에서의 헛구역질."
            th "그리고 지금 음식을 잘 넘기지 못하는 모습."
            th "단순히 입맛이 없는 게 아니다. 무언가 심리적인 이유로 음식 넘기는 걸 힘들어하고 있다."
            "나는 더 이상 권하지 않고, 조용히 물컵을 선배 앞으로 밀어주었다."
            
            sj "체합니다. 천천히 드세요."
            show gaeun normal at char_4, sway_soft with dissolve
            "물컵을 받아 든 선배의 눈빛이 순간 아주 깊어졌다."
            "선배는 말없이 물을 한 모금 마시고는, 평소보다 훨씬 부드럽고 차분한 목소리로 속삭였다."
            
            ge "…고마워, 서진아."
            "장난기가 쫙 빠진, 진짜 가은 선배의 목소리였다."

    # 분기 종료 합류
    hide yuna with dissolve
    hide harin with dissolve
    hide seola with dissolve
    hide gaeun with dissolve

    scene black with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "식사가 끝나고, 내가 약속했던 대로 분리수거와 테이블 닦기를 완벽하게 끝냈을 때쯤엔 완전히 밤이 깊어 있었다."
    "창문을 열어 환기를 시키자, 서늘한 밤공기가 밀려 들어와 뺨을 식혀주었다."
    show harin normal at center_lower, sway_soft with dissolve
    hr "좋아. 냄새도 얼추 다 빠졌고, 쓰레기도 완벽해."
    hr "오늘은 정말 이만 해산하자. 내일은 점심시간에 다시 모이는 걸로."

    "하린이의 해산 선언에 다들 주섬주섬 가방을 챙겨 일어났다."
    "학교 건물을 빠져나와 텅 빈 운동장을 가로지르는 길."
    "가로등 불빛이 우리 다섯 명의 그림자를 길게 늘어뜨렸다."
    hide harin
    show yuna smile at left, tiny_bounce with dissolve
    show gaeun smile at right, tiny_bounce with dissolve
    
    yn "아~ 배부르니까 완전 행복해요! 가은 선배 진짜 잘 먹었습니다!"
    ge "우리 막내 잘 먹는 거 보니까 선배도 배부르다. 다음엔 더 맛있는 거 사줄게."
    "유나와 가은 선배가 앞서 걸으며 꺄르르 웃음을 터뜨렸다."
    "그 뒤를 하린과 설아가 나란히, 하지만 약간의 간격을 두고 걷고 있었다."
    "나는 무리의 맨 뒤에서 그들의 뒷모습을 가만히 응시했다."

    th "축제."
    th "이 뻔하고 귀찮은 행사가, 어쩌면 내 생각보다 훨씬 더 많은 것을 바꿔놓을지도 모르겠다."
    th "유나의 과장된 밝음 이면에 숨겨진 갈증."
    th "하린의 완벽함 뒤에 숨겨진 흉터."
    th "설아의 침묵 속에 담긴 상처."
    th "가은 선배의 웃음 뒤에 가려진 거부 반응."

    th "나는 이들의 미세한 균열들을 아주 조금씩, 가랑비에 옷 젖듯 알아가고 있다."
    th "이 몽글몽글하고 따뜻한 위장된 일상이 끝났을 때, 나는 어떤 선택을 하게 될까."
    "밤하늘에는 어느새 맑은 별 몇 개가 떠올라 있었다."
    "우리는 교문 앞에서 각자의 집 방향을 향해 손을 흔들며 헤어졌다."
    "내일 다시 시작될, 똑같지만 조금은 다를 평범한 하루를 기약하며."

    # ---------------------------------------------------------
# [Scene 13 타이틀]
label scene_13:

    scene black with fade
    centered "{size=40}Scene 13{/size}\n\n{size=30}약속의 답례{/size}" with dissolve
    pause 1.5

    scene bg school_gate with fade
    play music "audio/bgm_spring_morning.ogg" fadein 2.0

    "다음 날 아침."
    "전날 늦게까지 축제 준비를 했는데도, 이상하게 몸이 그렇게 무겁진 않았다."
    "잠은 부족했지만, 봄 아침 공기가 유난히 상쾌해서 그런 걸지도 모른다."
    th "평소 같으면 이 시간에 반쯤 혼이 빠진 얼굴로 걷고 있었겠지."
    th "그런데 오늘은, 괜히 정문 쪽을 한 번 더 보게 된다."

    "타닥, 타다닥—!"
    "기다렸다는 듯 익숙한 발소리가 등 뒤에서 튀어왔다."
    show yuna smile at center_lower, tiny_bounce with dissolve

    yn "서진 선배! 좋은 아침!"
    "유나는 양손을 등 뒤로 감춘 채 싱글벙글 웃고 있었다."
    "오늘은 숨도 많이 차지 않았고, 머리도 의외로 단정했다."
    "그런데 저 수상한 자세를 보면, 뭔가 숨기고 있는 건 분명했다."

    sj "너 또 뭐 숨기고 있냐."
    show yuna surprise at center_lower, excited_hop with dissolve
    yn "헉."
    yn "어떻게 알았지?"
    sj "네가 그렇게 티 나게 서 있으면 모르는 게 더 어렵겠다."
    show yuna laugh at center_lower, idle_bounce with dissolve
    yn "에헤헤. 역시 선배는 눈치가 빠르네."
    yn "그럼 짜잔~ 공개합니다!"
    "유나는 등 뒤에 숨기고 있던 작은 비닐봉지를 내밀었다."
    "안에는 딸기우유 하나와, 편의점에서 산 듯한 작은 크림빵이 들어 있었다."
    yn "전에 말했잖아요!"
    yn "다음엔 내가 선배한테 맛있는 거 사준다고!"

    th "…진짜 기억하고 있었냐."
    sj "아침부터 이걸 사 오려고 일찍 나온 거야?"

    yn "네!"
    yn "아, 물론 그냥 선배 생각나서 산 거지, 엄청 특별한 의미는 아니고요!"
    yn "진짜로요!"
    yn "조금 특별할 수도 있긴 한데 아무튼요!"

    "혼자서 말을 덧붙이느라 바쁜 유나를 보니 웃음이 나왔다."
    menu:
        "어떻게 받을까?"
        "순순히 받는다.":
            $ yuna_point += 1

            sj "그래. 고맙게 받지."
            sj "약속 지키는 건 너도네."

            "내가 비닐봉지를 받아 들자, 유나의 얼굴이 확 밝아졌다."
            show yuna smile at center_lower, tiny_bounce with dissolve
            yn "그쵸!"
            yn "저도 약속 엄청 잘 지키는 사람이거든요!"
            yn "그러니까 선배도 앞으로 저랑 한 약속 잘 지켜야 돼요."
            sj "은근슬쩍 조건을 붙이네."

            yn "협상은 타이밍이 중요하니까요."

        "너 먹으라고 도로 준다.":
            $ yuna_point += 1

            sj "이런 건 보통 네가 더 좋아하지 않냐."
            sj "반은 네가 먹어."

            show yuna surprise at center_lower, excited_hop with dissolve
            yn "어?"
            yn "진짜 같이 먹어요?"

            sj "그럼 뭐, 내가 혼자 크림빵 두 개라도 먹냐."

            "유나는 잠깐 멍하니 있다가 금세 배시시 웃었다."
            show yuna laugh at center_lower, idle_bounce with dissolve
            yn "…그럼 오늘 아침 공동 소유!"
            yn "선배랑 반띵이면 더 맛있을 것 같아요."

        "왜 갑자기 이렇게 잘해주냐고 묻는다.":
            $ yuna_point += 1

            sj "근데 너, 왜 이렇게까지 잘해주냐."
            sj "우유 하나 사준 걸 아직도 기억하고."

            "유나는 내 말을 듣고 눈을 두 번 깜빡였다."
            "그리고 장난기 어린 웃음을 조금 누그러뜨린 채 대답했다."

            show yuna smile at center_lower, tiny_bounce with dissolve
            yn "음…"
            yn "저한테 잘해준 사람은 오래 기억하는 편이라서요."
            "짧은 대답이었다."
            "그런데 이상하게도, 농담처럼만 들리진 않았다."

            yn "아, 너무 진지했나?"
            yn "아무튼 받으세요! 거절은 불가!"
    "우리는 나란히 정문을 지나 학교 안으로 걸어 들어갔다."
    "유나는 오늘도 평소처럼 재잘거렸고, 나는 오늘도 적당히 받아쳤다."
    "그런데 이상하게, 손에 들린 작은 딸기우유 하나가 생각보다 더 무겁게 느껴졌다."

    th "이 녀석은 사소한 걸 사소하게 안 넘긴다."
    th "그래서 더 피곤하고, 그래서 더 신경 쓰인다."

    scene black with fade
    "아주 평범한 답례였는데, 이상하게 하루 시작이 조금 더 달아졌다."
    jump scene_14

# ---------------------------------------------------------
# [Scene 14 타이틀]
label scene_14:

    scene black with fade
    centered "{size=40}Scene 14{/size}\n\n{size=30}팀명은 중요할까{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 2.0

    "점심시간."
    "축제 준비를 위해 잠깐 모인 교실은 여전히 어수선했지만, 며칠 전과는 결이 조금 달랐다."
    "낯선 사람들끼리 엮인 느낌은 희미해지고, 대신 애매하게 익숙해진 공기가 생겼다."
    
    # [수정 3] 3명일 때는 중앙으로 쏠리는 char_1,2,3 대신 넓게 분산되는 left, center, right 사용
    show yuna smile at left, tiny_bounce
    show seola normal at center, sway_soft
    show harin normal at right, sway_soft
    with dissolve

    hr "오늘은 교실 앞 안내판 문구랑 장식 위치만 최종으로 보자."
    hr "점심시간 안에 끝내야 하니까 딴 얘기 금지."

    yn "에이, 또 딴 얘기 금지래."
    yn "이런 회의에는 팀 이름 정하는 시간이 꼭 있어야 하는데."

    sj "그건 누가 정했는데."

    yn "제가요."
    show harin sigh at right, sway_soft with dissolve
    hr "기각."
    show yuna pout at left, sway_soft with dissolve
    yn "너무해."
    "유나는 의자 위에 턱을 괴고 한참 심통 난 얼굴을 하더니, 이내 포기하지 않고 다시 입을 열었다."
    yn "그럼 후보라도 들어봐 주세요!"
    yn "'봄빛 특공대'."
    yn "'연화제 정복단'."
    yn "아니면… '서진 선배와 즐거운 친구들'!"
    sj "마지막 건 지금 당장 폐기해라."

    show seola surprise at center, excited_hop with dissolve

    "설아의 어깨가 아주 조금 들썩였다."
    "웃은 건지 아닌지 애매할 만큼 작은 반응이었다."

    sj "설아, 방금 웃었냐."
    show seola normal at center, sway_soft with dissolve
    sa "…조금."

    yn "와."
    yn "선배, 설아도 웃겼대요."
    yn "그러니까 제가 맞는 거예요."

    hr "틀렸어."

    "하린이가 단호하게 끊었지만, 이번에는 목소리가 평소보다 덜 차가웠다."
    "오히려 아주 잠깐, 입꼬리가 흔들린 것 같기도 했다."

    menu:
        "뭐라고 거들까?"
        "유나 편을 든다.":
            $ yuna_point += 1

            sj "그래도 팀 이름 하나쯤 있으면 부르기 편하긴 하겠네."
            sj "적당히 덜 유치한 걸로."

            show yuna surprise at left, excited_hop with dissolve
            yn "헐."
            yn "선배가 제 편을 들어준다?"

            sj "너무 감동하지 마라."
            sj "방금 후보들이 너무 심각해서 오히려 더 낫다는 뜻이니까."
            show yuna laugh at left, idle_bounce with dissolve
            yn "아하하! 그래도 됐어요!"
            yn "이걸로 오늘 하루 버틸 에너지 충전 완료!"

        "하린 편을 든다.":
            $ harin_point += 1

            sj "반장 말이 맞아."
            sj "네가 이름 붙이는 순간 분위기가 급격히 유치해진다."

            show yuna pout at left, sway_soft with dissolve
            yn "너무해!"
            yn "둘이 지금 저 협공하는 거예요?"

            show harin faint_smile at right, tiny_bounce with dissolve
            hr "드물게 의견이 맞았네."
            "하린이가 작게 웃으며 펜 끝으로 표를 톡톡 두드렸다."

            th "서하린이 저런 식으로 장난을 받는 것도 조금 익숙해졌다."
        "설아한테 의견을 묻는다.":
            $ seola_point += 1

            sj "설아는."
            sj "이름 있는 게 좋아, 없는 게 좋아?"

            "설아는 잠시 생각하더니, 안내판 샘플 위에 적힌 글씨를 내려다봤다."
            sa "…없는 게 편한데."
            sa "근데 굳이 정하면, 너무 시끄럽지 않은 걸로."

            yn "오."
            yn "그럼 '조용한 봄' 어때요?"
            show seola normal at center, sway_soft with dissolve
            sa "…그건 괜찮아."
            th "유나 기준으로 꽤 얌전한 이름이다."

    hide yuna with dissolve
    hide harin with dissolve
    hide seola with dissolve

    "결국 팀 이름은 정식으로 정하진 않았지만, 유나는 회의가 끝날 때까지 우리를 멋대로 '조용한 봄 팀'이라고 불렀다."
    "하린이는 세 번 정정했고, 가은 선배는 네 번 웃었고, 설아는 두 번쯤 아주 작게 따라 읽었다."
    scene black with dissolve
    centered "{size=30}특별동 준비실{/size}" with dissolve
    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "방과 후 준비실에 모였을 때도 그 별명은 계속 이어졌다."
    show gaeun smile at center_lower, tiny_bounce with dissolve
    ge "왔네, 조용한 봄 팀."

    sj "선배까지 왜 그러십니까."
    show gaeun laugh at center_lower, idle_bounce with dissolve
    ge "좋잖아."
    ge "생각보다 청춘물 제목 같고."
    show gaeun smile at right, tiny_bounce
    show yuna smile at left, tiny_bounce with dissolve
    
    yn "그쵸, 그쵸!"
    yn "역시 가은 선배는 감성이 통한다니까."
    
    show harin sigh at center_lower, sway_soft with dissolve
    hr "아무도 정식 채택한 적 없거든."
    hide harin
    hide yuna
    hide gaeun
    show seola normal at center_lower, sway_soft with dissolve
    
    sa "…근데."
    sa "나쁘진 않아."
    "그 짧은 한마디에 준비실 안이 조용해졌다가, 곧 유나가 제일 먼저 환하게 웃었다."
    show yuna laugh at left, idle_bounce with dissolve
    yn "봐요!"
    yn "설아도 인정했어요!"

    th "이상한 팀이다."
    th "그런데 이상하게, 점점 진짜 팀처럼 느껴진다."

    scene black with fade
    "누군가 붙인 별명 하나만으로도, 사람들 사이의 거리가 조금 줄어들 때가 있다."
# ---------------------------------------------------------
# [Scene 15 타이틀]

    scene black with fade
    centered "{size=40}Scene 15{/size}\n\n{size=30}사진 한 장의 거리{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_spring_morning.ogg" fadein 2.0

    "축제 준비는 생각보다 순조롭게 흘렀다."
    "색지는 거의 다 잘렸고, 안내판 문구도 정리됐고, 설아의 배치도는 보기 좋게 정돈되어 가고 있었다."

    "문제는 마지막 장식 테스트였다."
    show yuna smile at left, tiny_bounce with dissolve
    yn "잠깐만요, 잠깐만."
    yn "이건 기록해야 돼요."
    yn "우리 지금 완전 열심히 청춘하고 있잖아요!"

    sj "청춘을 동사처럼 쓰지 마라."

    "유나는 어디서 꺼냈는지 모를 휴대폰을 번쩍 들었다."
    yn "사진 찍어요!"
    yn "준비실 첫 단체사진!"

    show harin surprise at right, excited_hop with dissolve
    hr "갑자기?"
    yn "갑자기가 아니고 필수예요!"
    yn "나중에 축제 끝나고 보면 완전 추억 된다니까."
    show gaeun smile at center_lower, tiny_bounce with dissolve
    ge "오, 좋은데."
    ge "후배님들 이런 건 남겨둬야지."
    hide gaeun
    show seola surprise at center_lower, excited_hop with dissolve
    sa "나는…"

    "설아가 말을 흐렸다."
    "유나는 금방 눈치를 챘는지 휴대폰을 내리며 살짝 고개를 갸웃했다."

    show yuna normal at left, sway_soft with dissolve
    yn "아."
    yn "설아, 사진 싫으면 안 찍어도 돼."
    yn "아니면 얼굴 안 나오게 손만 찍을 수도 있고."

    "설아는 유나를 가만히 바라봤다."
    "거절당할 걸 예상한 사람처럼 조심스러운 제안."
    "그 태도가 나름대로 다정했다."

    sa "…같이 찍는 건."
    sa "조금 괜찮아."
    show yuna smile at left, tiny_bounce with dissolve
    yn "진짜?"
    yn "오케이! 그럼 바로 진행!"
    th "유나는 저럴 때 사람을 재촉하지 않는다."
    th "마냥 들이대는 것 같아도, 아주 가끔은 묘하게 선을 잘 지킨다."

    "문제는 자리였다."
    "좁은 준비실 안에서 다섯 명이 한 프레임에 들어가려니, 생각보다 붙어 서야 했다."
    show harin normal at right, sway_soft with dissolve
    hr "삼각대 같은 건 없어?"

    yn "없죠!"
    yn "그래서 셀카예요!"
    sj "아주 계획적이다?"

    hide seola
    show gaeun laugh at center_lower, idle_bounce with dissolve
    ge "막내야, 네 팔 길이만 믿고 다섯 명을 넣겠다는 거야?"
    ge "그건 거의 모험인데."

    yn "가능해요!"
    yn "제가 또 셀카 장인이라."
    menu:
        "어디에 설까?"
        "유나 옆에 선다.":
            $ yuna_point += 1

            "내가 유나 쪽으로 한 걸음 붙자, 유나는 대놓고 눈을 반짝였다."
            show yuna smile at left, tiny_bounce with dissolve
            yn "헤헤."
            yn "역시 선배는 제 옆이 제일 편하죠?"

            sj "그런 말 하는 순간 불편해진다."

            yn "늦었어요."
            yn "이미 전 엄청 기분 좋아졌거든요."

        "하린 옆에 선다.":
            $ harin_point += 1

            "내가 하린이 쪽으로 자리를 옮기자, 하린이는 아주 잠깐 눈을 깜빡였다."
            hr "…왜 여기로 와."

            sj "네가 제일 안 움직일 것 같아서."
            sj "사진 찍을 때 한 명쯤 중심 잡아야 하잖아."
            show harin faint_smile at right, tiny_bounce with dissolve
            hr "무슨 기준이야, 그게."
        "설아 쪽에 선다.":
            $ seola_point += 1

            "설아가 가장 구석으로 빠지려는 걸 보고, 나는 그 옆자리를 먼저 차지했다."
            sj "너 거기로 가면 반밖에 안 나온다."

            hide gaeun
            show seola normal at center_lower, sway_soft with dissolve
            sa "…그럼."
            sa "조금만 안쪽으로 갈게."

            "설아는 내 쪽을 힐끗 보고 아주 조금 안으로 움직였다."
            "그 작은 양보가 생각보다 크게 느껴졌다."
        "가은 선배 옆에 선다.":
            # [수정 4] 겹침 방지 (설아 퇴장)
            hide seola with dissolve
            $ gaeun_point += 1

            "내가 가은 선배 옆에 서자, 선배는 능청스럽게 웃었다."
            show gaeun smile at center_lower, tiny_bounce with dissolve
            ge "왜, 후배님."
            ge "나랑 투샷 욕심나?"

            sj "단체사진이라면서요."

            ge "아쉽네."
            ge "난 또 드디어 후배님이 선배 미모의 가치를 알아본 줄."
    hide harin with dissolve
    hide seola with dissolve
    hide gaeun with dissolve
    hide yuna with dissolve

    "결국 유나가 팔을 한껏 뻗고, 우리는 어설프게 어깨를 맞댄 채 프레임 안으로 몸을 욱여넣었다."
    "하린이는 최대한 단정한 얼굴을 유지하려 했고."
    "설아는 어색한 표정으로 시선을 어딘가 두고 있었고."
    "가은 선배는 익숙하게 웃고 있었고."
    "유나는 세상에서 제일 신난 얼굴이었다."

    yn "하나, 둘, 셋!"

    play sound "audio/sfx_camera_click.ogg"

    show cg group_selfie with dissolve
    "찰칵."
    "사진이 찍히자마자 유나는 바로 화면을 확인했다."
    "그리고 1초 뒤, 준비실 안에 요란한 웃음이 터졌다."
    scene bg old_library with dissolve
    show yuna laugh at left, idle_bounce with dissolve
    yn "아하하하!"
    yn "선배 왜 혼자만 표정이 완전 장례식장이에요!"
    sj "누가 갑자기 그렇게 붙어서 찍으래."
    show gaeun laugh at center_lower, idle_bounce with dissolve
    ge "아니, 진짜네."
    ge "후배님만 유독 영혼이 빠져 있잖아."
    show harin faint_smile at right, tiny_bounce with dissolve
    hr "입꼬리가 1mm도 안 올라갔어."
    hide gaeun
    show seola normal at center_lower, sway_soft with dissolve
    sa "…그래도."
    sa "조금 웃기긴 해."
    "네 사람이 한꺼번에 웃는 바람에, 오히려 내가 제일 억울해졌다."

    sj "됐고."
    sj "다시 찍어."

    yn "오!"
    yn "선배가 먼저 재촬영 요청했어!"
    yn "이건 엄청 희귀한 이벤트다!"

    "두 번째 사진은 조금 나았다."
    "세 번째는 더 자연스러웠고, 네 번째쯤 되자 이미 장식 테스트는 핑계고 사진 놀이가 되어 있었다."
    "결국 제일 마지막에 찍힌 사진 속 우리는, 누구 하나 제대로 포즈를 맞추지도 못한 채 제각각 웃고 있었다."
    "그런데 이상하게도, 그 사진이 제일 그럴듯했다."

    hide seola
    show gaeun smile at center_lower, tiny_bounce with dissolve
    ge "좋네."
    ge "이건 나중에 축제 끝나고 꼭 다시 봐야겠다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "맞아요!"
    yn "제가 단체방 같은 거 만들어도 돼요?"

    show harin normal at right, sway_soft with dissolve
    hr "업무용으로만 쓰면."
    yn "업무용 반, 잡담용 반!"

    sj "그건 이미 잡담용이 더 많다는 뜻이잖아."
    hide gaeun
    show seola normal at center_lower, sway_soft with dissolve
    sa "…그래도."
    sa "있으면 편할 것 같아."
    "설아가 먼저 그렇게 말하자, 유나는 진심으로 놀란 얼굴을 했다가 곧장 웃었다."

    yn "오케이!"
    yn "그럼 오늘 저녁 안에 만들게요!"
    yn "이름은 당연히 '조용한 봄'이다!"

    hr "그건 아직 확정 아니라고 했지."
    hide seola
    show gaeun smile at center_lower, tiny_bounce
    ge "이쯤 되면 사실상 확정이네."
    th "정말 이상한 이름인데."
    th "이상하게 점점 익숙해진다."

    scene black with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    scene black with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5
    scene bg school_road_dusk with dissolve
    "그날 집에 돌아가는 길."
    "유독 눈이 부시던 평소의 노을과 다르게, 오늘은 차분하고 밝지 않은 아주 평범한 하굣길 풍경이 펼쳐져 있었다."
    "어쩐지 이 적당히 어둑하고 조용한 분위기가 마음을 더 편하게 만든다."
    "휴대폰에는 단체사진이 몇 장 도착해 있었다."

    "첫 번째는 내가 유독 무표정해서 웃긴 사진."
    "두 번째는 유나가 흔들린 사진."
    "세 번째는 하린이 드물게 웃는 사진."
    "네 번째는 설아가 아주 희미하게 웃고 있는 사진."
    "그리고 마지막은, 다 같이 어설프게 엉켜 있는데 이상하게 가장 자연스러운 사진."

    th "평범하다."
    th "정말 별일 없는 하루였다."
    th "그런데 이상하게."
    th "이런 평범한 날이, 생각보다 오래 기억에 남을 것 같은 기분이 든다."
# ---------------------------------------------------------
# [Scene 16 타이틀]

    scene black with fade
    centered "{size=40}Scene 16{/size}\n\n{size=30}점심시간 소동{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 2.0

    "다음 날 점심시간."
    "교실은 도시락 냄새와 매점 빵 봉지 뜯는 소리, 그리고 축제 이야기를 하는 학생들로 평소보다 더 들떠 있었다."
    "창밖으로는 봄 햇빛이 느슨하게 들어오고 있었고, 칠판 한쪽에 적힌 축제 준비 일정도 어제보다 조금 더 현실감 있게 느껴졌다."
    th "아직 축제까지는 시간이 남았다."
    th "그런데도 애들은 벌써 당일이 된 것처럼 들떠 있다."
    th "뭐, 이 학교에서 시험 말고 다 같이 같은 방향으로 신나는 일은 흔치 않으니까."
    th "이런 소란 정도는 나쁘지 않다."
    show harin normal at center_lower, sway_soft with dissolve

    "하린이는 내 자리 앞에 서서 클립보드 한 장을 내려놨다."
    "언제나처럼 반듯하게 정리된 체크표였다."

    hr "윤서진."
    hr "잠깐 시간 돼?"

    sj "반장이 '잠깐'이라고 하면 보통 안 잠깐이던데."
    hr "이번엔 진짜 잠깐이야."
    hr "축제 준비 물품 중에 직접 사 와야 하는 게 몇 개 있거든."
    hr "점심시간에 매점이랑 문구부에서 해결 가능한 것부터 체크하려고."

    sj "그걸 왜 나한테."

    hr "네가 제일 덜 바빠 보여서."
    sj "기분이 묘하게 나쁜데 맞는 말이라 반박을 못 하겠네."

    show harin faint_smile at center_lower, tiny_bounce with dissolve

    "하린이는 아주 잠깐 웃었다."
    "어제보다 확실히 표정이 부드러웠다."

    hr "좋게 말하면 여유 있어 보인다는 뜻이야."

    sj "반장 입에서 그런 미화가 나오는 건 드문데."
    hr "오늘은 기분이 조금 괜찮으니까."

    "그 말이 이상하게 귀에 남았다."
    "하린이는 좋은 상태일 때도 크게 티를 내는 타입이 아닌데, 오늘은 정말로 조금 편안해 보였다."

    "그때, 옆문이 벌컥 열렸다."
    show yuna smile at left, tiny_bounce with dissolve

    yn "선배들 뭐 해요?"
    yn "설마 둘만 몰래 재밌는 거 하려는 거 아니죠?"

    sj "축제 준비 심부름."

    yn "어?"
    yn "그럼 저도 갈래요."
    hr "유나는 밥 안 먹었어?"

    yn "먹었죠!"
    yn "근데 후식은 아직이잖아요."

    sj "결국 매점이 목적이네."
    show yuna laugh at left, idle_bounce with dissolve

    yn "선배, 사람을 너무 단순하게 보면 안 돼요."
    yn "저는 축제 준비를 위해 기꺼이 제 몸을 희생하는 헌신적인 인재라고요."
    sj "그 인재의 주 목적이 딸기우유와 빵인 것 같긴 하지만."

    yn "겸사겸사죠, 겸사겸사."
    "유나는 그렇게 말하며 내 책상에 턱 하고 기대섰다."
    "햇빛을 받은 머리카락 끝이 가볍게 흔들렸다."
    "교실 안에 떠다니는 소란까지 전부 자기 템포로 끌고 가는 애다."

    "뒤쪽 창가 쪽에서는 조용히 책을 읽고 있던 설아가 고개를 들었다."
    show seola normal at right, sway_soft with dissolve

    sa "문구부 가는 거면."
    sa "색지 두께도 같이 봐야 해."
    sa "어제 샘플, 너무 얇았어."

    "하린이는 설아를 돌아봤다."

    hr "맞아."
    hr "그 말 하려고 했어."
    hr "그럼 설아도 같이 갈래?"
    sa "응."

    "짧은 대답."
    "하지만 어제까지의 설아라면 굳이 먼저 입을 열지 않았을지도 모른다."
    "이 정도면 나름대로 먼저 발을 들인 셈이었다."
    "그리고 마지막으로, 교실 문틀에 기대어 이쪽을 보고 있는 사람이 하나 더 있었다."
    hide harin
    show gaeun smile at center_lower, tiny_bounce with dissolve

    ge "오."
    ge "벌써 원정대 결성했네."
    sj "선배는 왜 여기 계세요."

    ge "학생회 전달사항 주러 왔다가."
    ge "근데 재밌어 보여서 잠깐 구경."
    yn "가은 선배도 같이 가요!"

    ge "나까지 끼면 점심시간 끝나기 전에 못 돌아올걸?"
    ge "너희 넷이면 충분해."
    ge "대신 문구부 아저씨한테 학생회 이름 말하면 조금 깎아주실 수도 있으니까 그건 써먹어."
    show harin normal at center_lower, sway_soft
    hide gaeun
    hr "그런 중요한 걸 이제 말해요?"
    hide harin
    show gaeun smile at center_lower, tiny_bounce
    ge "이게 다 선배의 뒤늦은 사랑이지."
    sj "사랑치곤 실용적이네요."

    show gaeun laugh at center_lower, idle_bounce with dissolve

    ge "축제철 사랑은 원래 실용적인 법이야."
    hide gaeun with dissolve
    hide seola with dissolve
    hide yuna with dissolve

    "그렇게 해서 점심시간 짧은 심부름 원정대가 꾸려졌다."
    scene black with dissolve
    centered "{size=30}시끌벅적한 복도{/size}" with dissolve
    scene bg noisy_hallway with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "복도로 나오자 점심시간 특유의 소음이 사방에서 밀려왔다."
    "계단 쪽에서는 뛰어가는 발소리가 울렸고, 매점 쪽으로 향하는 복도는 이미 학생들로 반쯤 막혀 있었다."
    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "좋아, 오늘의 목표!"
    yn "색지, 양면테이프, 네임펜, 그리고 내 후식!"

    hr "마지막은 목표가 아니야."

    sj "쟤한텐 제일 중요한 목표 같은데."
    show yuna pout at left, sway_soft with dissolve

    yn "너무하네."
    yn "저도 엄연히 팀의 사기를 담당하고 있다고요."
    sa "그건 맞아."

    "유나는 설아 쪽을 홱 돌아봤다."

    show yuna surprise at left, excited_hop with dissolve

    yn "어?"
    sa "유나 없으면 조용해서."
    sa "조금 심심할 것 같아."

    "복도 한가운데서 유나가 그대로 굳었다."
    "그리고 몇 초 뒤, 귀까지 붉어졌다."
    show yuna laugh at left, idle_bounce with dissolve

    yn "뭐예요, 설아 선배."
    yn "갑자기 그렇게 말하면 제가 괜히 좋아하잖아요."

    sj "이미 좋아 보이는데."

    yn "들켰다."

    "하린이가 작게 한숨 섞인 웃음을 내뱉었다."
    show harin faint_smile at center_lower, tiny_bounce with dissolve

    hr "이러니까 분위기가 빠르게 풀리긴 하네."

    th "정말 그렇다."
    th "넷이 같이 걷는 것뿐인데도, 평소보다 복도가 덜 지루하게 느껴진다."
    scene black with dissolve
    centered "{size=30}교실{/size}" with dissolve
    scene bg classroom with dissolve

    "문구부 앞은 생각보다 한산했다."
    "우리는 필요한 물품 목록을 하나씩 확인하며 진열대를 둘러봤다."
    "하린이는 필요한 것과 필요 없는 것을 칼같이 구분했고, 설아는 색지와 마스킹테이프 색 조합을 눈으로 빠르게 골랐다."
    "유나는 옆에서 이것저것 들었다 놨다 하며 계속 말을 보탰다."

    # [수정 5] 3명일 때는 중앙으로 쏠리는 char_1,2,3 대신 넓게 분산되는 left, center, right 사용
    show yuna smile at left, tiny_bounce
    show seola normal at center, sway_soft
    show harin normal at right, sway_soft
    with dissolve

    hr "색지는 이 하늘색이랑 아이보리."
    hr "너무 진하면 글씨가 묻혀."

    sa "응."
    sa "그리고 장식용이면 이 분홍색 말고, 채도 낮은 쪽이 더 나아."

    yn "우와."
    yn "둘이 말하는 거 듣고 있으면 갑자기 엄청 전문가 같아요."

    sj "갑자기?"

    yn "원래도 전문가 같긴 했는데, 지금은 더."
    yn "하린 선배는 완전 체크리스트의 인간화 같고."
    yn "설아 선배는 색깔 보는 눈이 진짜 신기해요."

    hr "체크리스트의 인간화는 칭찬이야?"
    yn "네!"
    yn "엄청 신뢰된다는 뜻!"

    sa "그럼 나는?"

    yn "음……"
    yn "조용한데 정확해서 멋있어요."
    sa "애매하게 부끄럽네."

    sj "유나는?"

    show yuna grin at left, idle_bounce with dissolve

    yn "저는 귀여움 담당."
    sj "셀프 지정이네."

    hr "반박은 어렵네."

    "하린이의 입에서 자연스럽게 그런 말이 나오자, 유나는 두 손으로 입을 가리며 과장되게 감동한 척했다."
    show yuna laugh at left, idle_bounce with dissolve

    yn "세상에."
    yn "하린 선배가 방금 저를 인정했어요."
    hr "네가 너무 시끄러워서 부정할 틈이 없었던 거야."

    yn "그것도 인정이죠."

    "나는 양면테이프 묶음을 들고 둘의 대화를 지켜봤다."
    "보는 사람까지 괜히 웃게 되는 템포였다."

    menu:
        "누구 쪽에 맞춰 움직일까?"
        "하린이랑 같이 목록을 체크한다.":
            $ harin_point += 1

            sj "반장, 이거면 다 맞지?"
            sj "네임펜 두 개, 양면테이프 세 개, 색지 묶음 두 세트."

            "하린이는 내 쪽으로 체크리스트를 조금 기울였다."

            hr "응."
            hr "그리고 풀도 작은 걸로 두 개 더."
            hr "네가 확인해주니까 빠르네."

            sj "그 말, 은근히 고맙게 들리네."
            show harin faint_smile at right, tiny_bounce with dissolve

            hr "고마운 거 맞아."
            hr "혼자 보면 놓치는 것도 있거든."

            th "하린이는 뭐든 혼자 해낼 것처럼 보이는데."
            th "이렇게 자연스럽게 도움을 받는 것도, 생각보다 잘 어울렸다."

        "유나랑 같이 장식용 소품을 고른다.":
            $ yuna_point += 1

            sj "너는 왜 실용 물품 말고 별 모양 스티커만 보고 있냐."
            yn "축제는 낭만이 있어야죠."
            yn "이런 거 하나 붙이면 분위기 엄청 달라진다니까요?"

            "유나는 반짝이는 스티커 팩을 내 눈앞에 흔들었다."
            sj "네가 붙이면 교실 게시판이 아니라 네 폰케이스 될 것 같은데."

            yn "들켰네."
            yn "근데 진짜 예쁘지 않아요?"
            "나는 잠깐 고민하다가 별 스티커 하나를 장바구니에 넣었다."

            show yuna surprise at left, excited_hop with dissolve
            yn "어?"
            yn "선배가 이런 감성템을?"

            sj "축제용이야."
            sj "착각하지 마."

            show yuna smile at left, tiny_bounce with dissolve
            yn "헤헤."
            yn "그래도 잘 어울려요."

        "설아랑 같이 색 조합을 본다.":
            $ seola_point += 1

            sj "이쪽이 더 낫냐."
            sj "솔직히 나는 다 비슷해 보이는데."

            "설아는 색지 두 장을 나란히 놓고 잠깐 바라봤다."

            sa "이건 너무 밝고."
            sa "이건 너무 차가워."
            sa "이 정도가 제일 편해."

            sj "편해 보이는 색이 있다고?"

            sa "응."
            sa "보고 있으면 눈이 안 피곤한 색."

            "나는 설아가 고른 조합을 다시 바라봤다."
            "듣고 보니 정말 그랬다."
            "튀지는 않는데, 오래 봐도 질리지 않는 색."

            sj "신기하네."
            sj "네 말 듣고 보니까 알 것 같아."
            "설아는 아주 작게 고개를 끄덕였다."

            sa "그럼 됐어."

        "가은 선배 몫으로 장난감 같은 물건 하나 고른다.":
            $ gaeun_point += 1

            sj "가은 선배가 봤으면 괜히 재밌다고 샀을 법한 게 있네."
            yn "뭔데요?"

            "나는 진열대 한쪽에 걸린 작은 종 모양 장식을 집어 들었다."
            "움직일 때마다 맑은 소리가 났다."

            hr "실용성은 없네."
            sj "그래서 선배 취향 같잖아."

            sa "의외로 책상에 달아둘 수도 있어."

            yn "어, 진짜다."
            yn "가은 선배 이런 거 좋아할 것 같아요."

            "결국 우리는 그 작은 종 장식도 하나 같이 계산대에 올려두었다."
    hide harin with dissolve
    hide yuna with dissolve
    hide seola with dissolve

    scene black with dissolve
    centered "{size=30}점심시간 복도{/size}" with dissolve
    scene bg noisy_hallway with fade

    "필요한 물건을 다 산 뒤, 자연스럽게 매점 쪽으로 발길이 옮겨졌다."
    "이쯤 되면 축제 준비 심부름인지, 간식 원정인지 구분이 애매했다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "좋아!"
    yn "이제 진짜 중요한 일정!"

    hr "결국 그거였지."

    sj "반장도 이제 포기했네."

    hr "부정해봤자 이미 매점 앞이야."
    "유나는 빵 진열대 앞에서 진지한 얼굴로 한참을 고민하다가, 결국 딸기 크림빵과 초코우유를 집었다."
    "하린이는 가장 무난한 샌드위치를 골랐고."
    "설아는 의외로 작은 쿠키 한 봉지를 집어 들었다."

    sj "너는 그런 것도 먹는구나."

    sa "나는 어떤 이미지인 거야."
    sj "뭔가, 물이랑 샐러드만 먹을 것 같았어."

    sa "너무한데."

    show yuna laugh at left, idle_bounce with dissolve

    yn "설아 선배도 사람입니다~"

    "나는 캔커피를 하나 집었고, 계산을 마친 뒤 넷이 복도 창가 쪽에 나란히 섰다."
    "봄빛이 유리창에 반사되어 매끈하게 번졌다."

    "잠깐의 점심시간."
    "잠깐의 간식."
    "그런데 이상하게도, 교실에서 아무렇게나 먹는 것보다 훨씬 더 축제 같았다."
    yn "이렇게 보니까 진짜 동아리 같아요."

    sj "우린 동아리 아니고 임시 노동 인력인데."

    yn "말을 왜 그렇게 해요."
    yn "이런 순간엔 좀 청춘스럽게 말해도 되잖아요."

    hr "청춘스럽게가 대체 뭔데."
    yn "음……"
    yn "같이 심부름 갔다가, 간식 먹고, 축제 얘기하고."
    yn "그냥 그런 거요."
    "유나는 딸기우유 빨대를 꽂으며 활짝 웃었다."

    yn "저는 지금 꽤 좋아요."

    "그 말 뒤에 잠깐 조용한 공기가 내려앉았다."
    "부담스럽거나 어색한 침묵은 아니었다."
    "오히려 다들 비슷한 생각을 하고 있는 것 같은, 느슨하고 편한 정적."
    show harin faint_smile at center_lower, tiny_bounce with dissolve

    hr "……응."
    hr "나도."
    show seola normal at right, sway_soft with dissolve

    sa "복잡한 거 없이 이 정도면."
    sa "꽤 괜찮아."
    th "정말 별거 아닌 순간인데."
    th "이렇게 넷이 나란히 서서 간식이나 먹고 있으니까, 괜히 기분이 가벼워진다."
    th "굳이 특별한 사건이 없어도, 평화로운 하루는 생각보다 쉽게 사람을 들뜨게 만든다."
    play sound "audio/sfx_school_bell.ogg"

    "곧 점심시간 종료를 알리는 종이 울렸다."
    show yuna pout at left, sway_soft with dissolve

    yn "아아, 벌써요?"

    sj "네 후식 타임은 언제나 짧지."
    yn "축제 기간엔 점심시간 10분 연장해야 돼요."
    yn "이건 학생 복지를 위한 정당한 주장입니다."
    hr "학생회에 올리면 가은 선배가 제일 먼저 기각할걸."

    sj "아니, 의외로 진지하게 검토할지도."
    sa "대신 이유를 '딸기우유 안정적 섭취권 보장'으로 적어."

    "유나는 결국 참지 못하고 웃음을 터뜨렸다."
    show yuna laugh at left, idle_bounce with dissolve

    yn "설아 선배, 은근 웃겨요 진짜."
    "우리는 빈 봉지와 음료 캔을 정리한 뒤 다시 교실로 돌아가기 시작했다."
    "복도를 걷는 발걸음도 올 때보다 훨씬 가벼웠다."
    hide yuna with dissolve
    hide harin with dissolve
    hide seola with dissolve

    scene black with dissolve
    centered "{size=30}교실{/size}" with dissolve
    scene bg classroom with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.5

    "교실에 돌아오자 가은 선배가 문 앞에서 기다리고 있었다."
    "우리 손에 들린 봉투를 보더니 바로 상황을 파악한 얼굴이었다."

    show gaeun smile at center_lower, tiny_bounce with dissolve

    ge "오."
    ge "생각보다 빨리 왔네."
    ge "근데 왜 다들 표정이 좋아 보여?"

    sj "축제 준비 효율이 올라가서요."

    yn "그리고 후식도 챙겼어요!"
    ge "아하."
    ge "결국 핵심은 그거였구나."

    "하린이가 봉투를 건네며 필요한 물품을 설명했고, 가은 선배는 내용물을 하나씩 확인하며 고개를 끄덕였다."
    ge "완벽하네."
    ge "이 정도면 오늘 방과 후 작업도 금방 끝나겠다."

    hr "그렇게만 되면 좋겠네요."

    ge "좋게 생각해."
    ge "축제 준비는 원래 할 일이 많아도, 같이 움직이면 이상하게 덜 귀찮거든."
    "가은 선배는 내 손에 들린 작은 종 장식을 보고 눈을 가늘게 떴다."

    ge "근데 저건 뭐야?"
    sj "선배 취향 같아서 샀습니다."

    "가은 선배는 장식을 받아 들어 가볍게 흔들었다."
    "맑고 작은 소리가 교실 문 앞에 울렸다."
    show gaeun laugh at center_lower, idle_bounce with dissolve

    ge "와."
    ge "이건 진짜 내 취향인데?"
    ge "후배님들, 사람 보는 눈 있네."

    yn "역시 맞췄다!"

    sa "생각보다 쉬웠어."

    hr "학생회 총괄이 저런 취향이라는 건 조금 의외네요."
    ge "사람은 누구나 쓸데없이 귀여운 걸 하나쯤은 좋아하는 법이야."

    th "그 말이 괜히 웃겼다."
    th "쓸데없는 것."
    th "그런데도 기분은 좋아지는 것."
    th "어쩌면 오늘 점심시간 전체가 딱 그랬다."

    "종이 한 번 더 울리고, 다들 제자리로 흩어졌다."
    "나는 의자에 앉으며 창가 쪽으로 시선을 돌렸다."
    "봄 햇빛은 여전히 따뜻했고, 교실 안은 적당히 시끄러웠다."

    th "이 정도면 충분하다."
    th "누구 하나 크게 다치지도 않고, 분위기가 틀어지지도 않고."
    th "그냥 적당히 웃고, 같이 움직이고, 조금 가까워지는 정도."
    th "지금은 그런 평화가 좋았다."

    scene black with fade
    "축제는 아직 시작도 안 했지만, 이상하게 오늘 하루는 벌써 조금 특별했다."

    "그때였다."

    "복도 저편에서 누군가 급하게 뛰어오는 발소리가 들렸다."
    "한 학생이 우리 옆을 스쳐 지나가며 매점 봉지를 떨어뜨렸고, 안에 들어 있던 우유팩 하나가 바닥을 따라 데구르르 굴러왔다."

    show yuna surprise at left, excited_hop with dissolve
    yn "어어, 조심!"

    "유나가 반사적으로 몸을 숙여 우유팩을 붙잡았다."
    "거의 바닥에 닿기 직전이었다."
    "본인도 놀랐는지 유나는 우유팩을 든 채 눈을 동그랗게 떴다."

    show harin surprise at center_lower, excited_hop with dissolve
    hr "진짜 빠르네."

    show yuna laugh at left, idle_bounce with dissolve
    yn "후후."
    yn "이래 봬도 저는 매점 실전파라니까요."

    sj "그 실전 경험을 대체 어디에 쌓는 건데."

    "우유팩을 떨어뜨린 남학생은 연신 고개를 숙였다."

    stu_a "아, 감사합니다!"
    stu_a "진짜 죄송해요, 늦어서 뛰다가…"

    show seola normal at right, sway_soft with dissolve
    sa "괜찮아."
    sa "안 터졌으니까."

    "남학생은 다시 한 번 감사 인사를 하고 황급히 사라졌다."
    "유나는 제 손에 들린 우유팩을 멀뚱히 보다가, 피식 웃으며 원래 주인에게 돌려준 방향을 바라봤다."

    yn "왠지 오늘 저 되게 멋있지 않았어요?"
    sj "1초 정도는 인정."
    yn "와."
    yn "1초라도 인정받았다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "본인이 제일 뿌듯해 보이긴 해."

    "유나는 괜히 어깨를 으쓱이며 딸기우유를 한 모금 더 마셨다."
    "아무것도 아닌 해프닝인데, 그 짧은 소동 덕분에 네 사람 사이 공기가 한층 더 말랑해졌다."

    "바로 그때, 내 휴대폰이 짧게 진동했다."
    "이어 유나의 폰, 하린이 폰, 설아의 폰까지 거의 동시에 울렸다."

    show yuna surprise at left, excited_hop with dissolve
    yn "어?"
    yn "뭐지?"

    "유나가 화면을 켜더니, 곧장 활짝 웃었다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "왔다!"
    yn "제가 어제 말했던 단체방!"

    sj "벌써 만들었냐."

    yn "당연하죠."
    yn "일 잘하는 후배는 미루지 않습니다."

    hr "자기소개는 됐고."
    hr "이름 뭐로 했어."

    "유나는 아주 자랑스럽게 화면을 내밀었다."

    yn "'조용한 봄'."
    yn "완전 예쁘죠?"

    "하린이는 바로 미간을 아주 조금 좁혔다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "업무용이라며."

    yn "업무도 하고 감성도 챙길 수 있죠!"
    yn "요즘은 그런 시대예요."

    sj "어느 시대인데."

    show seola normal at right, sway_soft with dissolve
    sa "……괜찮은데."

    "하린이는 설아를 한 번 보고, 다시 휴대폰을 봤다."

    hr "……둘이 좋으면."
    hr "일단 두자."

    show yuna laugh at left, idle_bounce with dissolve
    yn "만장일치!"
    sj "방금 전까지 반대하던 사람 있었던 것 같은데."

    yn "중요한 건 결과예요."

    "우리는 창가에 선 채 자연스럽게 단체방을 확인했다."
    "첫 번째 메시지는 이미 올라와 있었다."

    "유나 : 사진file"
    "유나 : 어제의 역사적인 첫 단체사진!"
    "유나 : 다들 저장 필수!"

    sj "왜 첫 메시지가 업무 공지가 아니라 사진이냐."

    yn "팀워크 강화용 자료예요."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "말은 그럴듯하네."

    "하린이도 결국 사진을 저장했는지, 화면을 한 번 오래 보고 있었다."
    "설아 역시 말없이 내려다보다가 아주 미세하게 입꼬리를 올렸다."
    "나는 그 짧은 표정을 놓치지 않았다."

    sj "너도 저장했냐."

    sa "응."
    sa "…이상하게."
    sa "계속 보게 돼."

    th "나만 그런 게 아니었네."

    "유나는 신이 나서 단체방 설명까지 바꾸기 시작했다."

    yn "좋아."
    yn "공지 적는다."
    yn "'축제 준비 중. 간식 필수. 지각 금지.'"

    hr "간식 필수는 왜 들어가."

    yn "아주 중요한 운영 원칙이니까요."

    sj "누가 보면 먹으러 모이는 줄 알겠다."

    show yuna pout at left, sway_soft with dissolve
    yn "선배, 축제도 결국 당이 있어야 굴러가는 거예요."

    show seola normal at right, sway_soft with dissolve
    sa "그건 맞아."

    "이번에도 설아가 담담하게 유나 편을 들었다."
    "유나는 그 말을 듣자마자 또 눈을 반짝였다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "설아 선배는 이제 제 편이에요."
    hr "너는 왜 자꾸 편을 가르냐."

    yn "청춘에는 그런 게 필요하거든요."

    sj "또 청춘이냐."

    "그렇게 웃고 떠드는 사이, 어느새 복도 반대편에서 5교시 예비종이 울렸다."
    play sound "audio/sfx_school_bell.ogg"

    show harin normal at center_lower, sway_soft with dissolve
    hr "이제 진짜 들어가야 해."
    hr "물품은 내가 먼저 준비실에 가져다둘게."

    sj "혼자 들고 가려고?"
    hr "이 정도면 무겁진—"

    "말이 끝나기도 전에 유나가 재빨리 봉투 하나를 낚아챘다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "하나는 제가!"
    show seola normal at right, sway_soft with dissolve
    sa "그럼 나는 색지."
    sj "결국 다 나눠 드네."

    "하린이는 잠깐 우리 셋을 번갈아 보더니, 작은 숨을 내쉬었다."
    "그게 귀찮아서 나온 한숨은 아닌 것 같았다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "……그래."
    hr "그럼 부탁할게."

    th "이상하다."
    th "조금 전까지만 해도 그냥 점심시간 심부름이었는데."
    th "어느새 정말로 역할이 나눠진 팀 같았다."

    scene black with dissolve
    centered "{size=30}복도 끝 계단{/size}" with dissolve
    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.5

    "우리는 준비물을 나눠 들고 교실 쪽으로 천천히 걸었다."
    "오갈 데 없이 붐비는 점심시간 끝 무렵의 복도."
    "계단 쪽에서 올라오는 학생들과 부딪히지 않으려면 자연스럽게 일렬 비슷하게 줄이 맞춰졌다."

    show yuna normal at left, sway_soft with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "근데요."
    yn "우리 부스 이름도 진짜 정해야 하지 않아요?"
    yn "계속 '그거'라고 부르니까 좀 허전해."

    hr "후보는 있지."
    hr "문제는 정상적인 의견이 적다는 거고."

    sj "대체 누가 이상한 이름을 그렇게 많이 낸 건데."

    show yuna laugh at left, idle_bounce with dissolve
    yn "어…"
    yn "약간…"
    yn "제가 분위기를 주도했을 수도?"

    sj "역시 범인이었네."

    sa "난 조용한 봄도 괜찮다고 생각했어."

    show harin surprise at center_lower, excited_hop with dissolve
    hr "설아까지?"

    sa "이름만 들으면."
    sa "별거 없어 보여서 좋아."
    sa "부담 없어."

    "하린이는 잠깐 생각하는 눈치였다."
    "그러더니 클립보드 모서리를 손끝으로 톡톡 두드렸다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "……확실히."
    hr "너무 힘주지 않은 건 나쁘지 않네."

    yn "오!"
    yn "지금 거의 통과 분위기인데요?"

    sj "아직 회의도 안 했잖아."

    yn "회의 전에 여론전이라는 게 있거든요."

    "유나는 승리한 사람처럼 씩 웃었다."
    "그 표정이 어처구니없어서, 나도 모르게 웃음이 새어 나왔다."

    "계단 앞에서 잠깐 사람이 몰렸다."
    "우리는 걸음을 멈추고, 창문 옆 벽에 살짝 붙었다."
    "유나는 무료해졌는지 내 손에 들린 양면테이프를 힐끗 보더니, 장난기가 돈 얼굴로 말했다."

    yn "선배."
    yn "그거 왠지 되게 살림 잘하는 사람 같아요."

    sj "양면테이프 들고 있다고?"

    yn "네."
    yn "생활력 있어 보여요."

    sj "이상한 기준이다."

    hr "근데 조금 맞아."
    hr "아까도 목록 체크 제일 빨랐고."

    sj "반장까지 왜 그래."

    sa "부정은 안 하네."

    "세 사람의 시선이 한꺼번에 몰렸다."
    "별말 아닌데 괜히 궁지에 몰린 기분이었다."

    sj "그냥, 다들 너무 허술하니까 그렇지."

    show yuna grin at left, idle_bounce with dissolve
    yn "우와."
    yn "방금 은근하게 다 깠다."

    hr "허술한 사람 명단부터 정리해볼까?"
    sj "그건 미안하다."

    "하린이가 바로 받아치고, 유나가 웃고, 설아가 작게 웃음을 참는 얼굴을 했다."
    "짧은 몇 마디가 오가는 것만으로도 이상하게 템포가 딱 맞았다."

    scene black with dissolve
    centered "{size=30}준비실 앞{/size}" with dissolve
    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "준비실 문을 열자, 어제 정리해 둔 물건들이 그대로 우리를 맞았다."
    "오전보다 어수선했지만, 그래도 어제보다 확실히 사람 손이 탄 공간 같았다."
    "하린이는 바로 새로 사 온 물품을 책상 위에 가지런히 올려뒀고, 설아는 색지를 겹쳐 보며 어제 가져온 샘플과 비교했다."
    "유나는 종 장식을 봉투에서 꺼내자마자 반짝 눈을 빛냈다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "이거 생각보다 더 귀엽다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "그건 분명 안 사도 되는 물건이었는데."

    sj "학생회 선배 몫이라고 생각해."

    show seola normal at right, sway_soft with dissolve
    sa "책상 옆에 달아두면 괜찮을 것 같아."
    sa "바람 불면 소리도 날 것 같고."

    yn "오, 좋다!"
    yn "그럼 이건 분위기 담당!"

    hr "언제부터 준비실에 분위기 담당이 생겼어."

    yn "방금부터요."

    "유나는 의자를 끌고 와 벽 쪽 핀보드 옆에 종 장식을 조심스럽게 걸었다."
    "아주 작은 장식이라 티도 거의 안 났다."
    "그런데 정말로, 없을 때보다 있는 쪽이 조금 더 준비실답게 느껴졌다."

    "유나는 스스로도 그게 만족스러웠는지 뒤로 물러나 감상하듯 바라봤다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "좋아."
    yn "이 공간, 점점 우리 아지트 같다."

    sj "아지트라니."
    sj "말은 거창하네."

    yn "이런 데서 청춘이 시작되는 거예요."
    hr "또 청춘."

    sa "유나는 그 단어 좋아하네."

    yn "좋아하죠!"
    yn "왠지 말만 해도 반짝거리는 느낌이잖아요."

    "설아는 종 장식을 잠깐 바라보다가, 아주 미세하게 고개를 끄덕였다."

    sa "……조금은."
    sa "알 것 같아."

    "유나는 그 한마디에 또 기분이 좋아진 얼굴이 됐다."
    "정말 간단한 말에도 쉽게 들뜨는 애다."

    "하린이는 물건을 정리하다가 문득 벽시계를 올려다봤다."

    show harin surprise at center_lower, excited_hop with dissolve
    hr "잠깐."
    hr "5교시까지 3분 남았어."

    sj "그걸 이제 말하냐."

    show yuna surprise at left, excited_hop with dissolve
    yn "뭐?!"
    yn "왜 시간이 갑자기 그렇게 됐어요?"

    sa "원래 그랬어."

    "순간 준비실 안이 소란스러워졌다."
    "유나는 급하게 가방을 다시 둘러맸고, 하린이는 체크리스트를 챙겼고, 설아는 색지 견본을 가지런히 포개 놓았다."
    "나는 책상 위에 놓인 네임펜 뚜껑을 닫아 봉투에 밀어 넣었다."

    "그 와중에도 유나는 문 앞에서 한 번 뒤돌아보며 외쳤다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "방과 후에 또 오죠!"
    yn "오늘은 진짜 이름도 정하고 장식도 좀 더 하고!"

    show harin normal at center_lower, sway_soft with dissolve
    hr "수업 끝나고 바로 오면."
    hr "30분 정도는 가능할 거야."

    show seola normal at right, sway_soft with dissolve
    sa "나도 갈게."

    "세 사람의 시선이 자연스럽게 내 쪽으로 넘어왔다."

    sj "왜 다 나를 보냐."

    yn "당연하죠."
    yn "선배도 와야 팀이 완성되니까."

    hr "짐 옮길 사람도 필요하고."

    sa "……그리고."
    sa "없으면 좀 허전할 것 같아."

    "설아의 말은 아주 담백했는데, 이상하게 제일 크게 남았다."
    "유나는 이미 대놓고 고개를 끄덕이고 있었고, 하린이는 부정하지 않았다."

    th "이건 좀 반칙 아닌가."

    sj "알았어."
    sj "수업 끝나고 보자."

    show yuna laugh at left, idle_bounce with dissolve
    yn "좋았어!"
    yn "그럼 오늘 방과 후 준비실 집합!"
    yn "조용한 봄 2차 활동 개시!"

    hr "아직 공식 명칭 아니라고 했지."
    sa "근데 점점 굳어지는 것 같아."
    sj "이쯤 되면 돌이키기 힘들겠네."

    "우리는 거의 동시에 준비실을 빠져나왔다."
    "복도 끝에서 다시 종이 울렸고, 교실 쪽으로 뛰어가는 학생들 사이로 우리도 자연스럽게 섞였다."

    scene black with fade

    "점심시간의 짧은 소동."
    "별일이라면 별일도 아닌, 정말 사소한 심부름과 간식과 잡담뿐인 시간."

    "그런데 이상하게도."
    "이제는 준비실 문을 열고 들어가는 일이,"
    "혼자 남는 시간이 아니라 누군가와 이어지는 시간처럼 느껴지기 시작했다."

    th "여전히 시끄럽고, 가볍고, 딱히 특별할 건 없는데."
    th "그게 이상하게 좋다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 17 타이틀]

    scene black with fade
    centered "{size=40}Scene 17{/size}\n\n{size=30}방과 후의 아지트{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "수업이 끝난 뒤의 교실은 점심시간과는 다른 의미로 소란스러웠다."
    "의자를 밀어 넣는 소리, 가방 지퍼를 잠그는 소리, 오늘 약속이 있는 애들이 들뜬 목소리로 떠드는 소리."
    "창밖으로 기울어진 햇빛이 교실 바닥을 길게 쓸고 지나갔다."

    th "하루 중 제일 애매한 시간이다."
    th "집에 가기엔 아직 해가 남아 있고, 그렇다고 뭘 하기엔 피곤하고."
    th "원래라면 그냥 적당히 시간 때우다 귀가했을 시간인데."

    "내 휴대폰이 짧게 울렸다."

    "유나 : 다들 준비실로!!"
    "유나 : 도망가면 잡으러 갑니다"
    "유나 : 특히 윤서진 선배"

    th "왜 마지막이 특히냐."

    "나는 가방을 한쪽 어깨에 걸친 채 교실 문을 나섰다."
    "복도 창문으로 들어오는 노을빛이 생각보다 선명했다."
    "그 빛 때문에 학교 전체가 잠깐 다른 장소처럼 보였다."

    scene black with dissolve
    centered "{size=30}준비실 앞{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.5

    "준비실 문을 열자마자 가장 먼저 보인 건 사다리 위에 올라가 있는 유나였다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin surprise at center_lower, excited_hop with dissolve
    show seola normal at right, sway_soft with dissolve

    hr "민유나!"
    hr "위험하니까 내려와!"

    yn "조금만요, 조금만!"
    yn "이거 위에 달아야 예쁘단 말이에요!"

    sj "오자마자 왜 저런 광경이 펼쳐져 있는 거지."

    sa "3분 전부터 저러고 있었어."

    "유나는 의자도 아니고 작은 접이식 사다리를 끌어다 놓고, 어제 사 온 종 장식 하나를 핀보드 위쪽에 걸려고 낑낑대고 있었다."
    "하린이는 아래에서 사다리가 흔들릴까 봐 붙잡고 있었고, 설아는 한 발짝 떨어진 채 그 광경을 가만히 보고 있었다."

    sj "떨어지면 어떻게 하려고."
    yn "안 떨어져요!"
    yn "저 은근 균형감각 좋아요."

    "말이 끝나기 무섭게 사다리가 아주 조금 삐걱했다."

    show yuna surprise at left, excited_hop with dissolve
    yn "어."
    hr "봐봐!"
    sj "내려와."

    "결국 유나는 투덜거리면서 사다리에서 내려왔다."

    show yuna pout at left, sway_soft with dissolve
    yn "다들 너무 과보호야."
    yn "전 할 수 있었다고요."

    sj "방금 못 할 뻔했잖아."
    sa "조금 흔들렸어."

    yn "설아 선배까지…"

    "유나는 입술을 삐죽였지만 금방 다시 기운을 차렸다."
    "저런 표정도 오래 못 간다."
    "오히려 막힌 쪽에서 새 장난을 찾는 애였다."

    hr "좋아."
    hr "일단 오늘 해야 할 거 정리할게."
    hr "부스 이름 후보 다시 정리하고, 장식 배치 정하고, 가격표 시안도 대충 만들어야 해."

    sj "점점 진짜 일이 되네."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "원래 축제 준비는 다 그렇지."

    yn "그리고 간식도 있어요."

    sj "그건 업무 항목 아니지 않냐."

    show yuna laugh at left, idle_bounce with dissolve
    yn "아뇨, 중요한 사기 진작이에요."

    "유나는 책상 한쪽에 비닐봉지를 올려놨다."
    "안에는 매점에서 사 온 빵 두 개와 작은 과자 봉지 몇 개, 그리고 익숙한 딸기우유가 들어 있었다."

    sj "아까 점심에도 먹지 않았냐."
    yn "점심의 딸기우유와 방과 후의 딸기우유는 의미가 다르거든요."

    sa "무슨 의미인데."

    yn "음…"
    yn "방과 후 건 좀 더 낭만적이에요."

    sj "딸기우유에 낭만을 붙이는 사람은 처음 본다."

    "설아가 아주 작게 웃었다."
    "짧고 낮은 웃음이었다."
    "유나는 그걸 바로 잡아냈는지 괜히 더 신나 보였다."

    show yuna grin at left, idle_bounce with dissolve
    yn "방금 웃었죠?"
    sa "아니."
    yn "웃었는데."
    sa "조금."

    hr "둘 다 됐고."
    hr "일단 앉아."

    "결국 우리는 늘 그렇듯 준비실 가운데 긴 책상을 중심으로 둘러앉았다."
    "처음엔 임시로 모인 자리 같았는데, 이제는 묘하게 각자 자리가 정해진 기분이 들었다."
    "유나는 늘 내 왼쪽 근처로, 하린이는 서류나 체크리스트를 펼치기 편한 정면으로, 설아는 벽 쪽에 기대기 좋은 오른쪽으로."

    th "이상하네."
    th "불과 며칠 전까지만 해도 이렇게 같이 있는 게 어색했는데."

    show harin normal at center_lower, sway_soft with dissolve

    "하린이는 클립보드를 펴고 이름 후보가 적힌 종이를 꺼냈다."

    hr "후보는 총 다섯 개."
    hr "'봄의 작업실', '조용한 봄', '오후의 책갈피', '청춘 보관함', 그리고…"

    sj "마지막은 말 안 해도 될 것 같은데."
    hr "그래?"
    hr "'딸기처럼 달콤한 축제연구회'."

    show yuna laugh at left, idle_bounce with dissolve
    yn "좋죠?!"
    sj "최악이다."
    sa "길어."

    hr "나도 같은 생각이야."

    yn "다들 왜 이렇게 차가워요."
    yn "전 진심이었다고요."

    "유나는 진심으로 아쉬워하는 얼굴을 했다."
    "그 얼굴이 너무 멀쩡해서 오히려 더 웃겼다."

    sj "그 진심은 묻어두는 게 학교를 위해 좋아."
    yn "와."
    yn "말 되게 차갑게 하는데 상처는 안 주네요."
    sj "그것도 재능이지."

    show seola normal at right, sway_soft with dissolve
    sa "조용한 봄이 제일 나아."
    sa "별로 튀지 않고."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "나도 그쪽."
    sj "반장도?"
    hr "적어도 딸기보다 낫잖아."

    yn "그러면 거의 3 대 1이네…"
    yn "선배는요?"
    sj "나도 조용한 봄."

    "유나는 잠깐 충격받은 척 가슴을 부여잡더니, 이내 고개를 크게 끄덕였다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋아요."
    yn "민주주의는 존중해야죠."
    yn "그럼 오늘부터 정식으로 조용한 봄 확정!"

    hr "아직 학생회 제출 전이니까 정식은 아니야."
    yn "제 마음속 정식이에요."

    sa "그건 아무도 못 막지."

    "하린이도, 설아도, 나도 결국 조금씩 웃었다."
    "이상하게도 저 말이 완전히 허무맹랑하게 들리진 않았다."
    "준비실의 공기와, 늦은 오후의 노을빛과, 책상 위로 흩어진 색지들이 정말 그 이름이랑 어울렸다."

    scene bg old_library with dissolve

    "이름이 정해지고 나니 신기하게도 해야 할 일도 술술 굴러가기 시작했다."

    "하린이는 가격표에 들어갈 문구를 다시 정리했고,"
    "설아는 색지와 장식 재료를 실제로 대보며 어떤 조합이 가장 덜 촌스러운지 골랐다."
    "유나는 한 손에 네임펜을 들고 핀보드 여백에 작은 샘플 그림을 그리기 시작했다."

    sj "너 그림 은근 잘 그리네."

    show yuna surprise at left, excited_hop with dissolve
    yn "어?"
    yn "지금 칭찬했죠?"

    sj "사실만 말한 건데."

    yn "그게 칭찬이죠!"

    "유나는 금세 기분이 좋아져서, 꽃 모양인지 별 모양인지 애매한 낙서들을 더 빠르게 그리기 시작했다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "너무 많으면 복잡해 보여."
    yn "아…"
    yn "그럼 두 개만?"
    hr "세 개."
    yn "협상의 여지가 있네."

    "옆에서 듣고 있던 설아가 핀보드를 보다가 조용히 손을 뻗었다."

    show seola normal at right, sway_soft with dissolve
    sa "여기."
    sa "이 부분은 빈 게 더 나아."
    sa "대신 아래에 작게 넣으면 예쁠 것 같아."

    "설아가 손끝으로 짚어 준 위치는 의외로 정확했다."
    "유나도, 하린이도 동시에 그 자리를 봤다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "오."
    yn "진짜다."
    yn "설아 선배, 감각 있는데요?"

    sa "그냥…"
    sa "복잡한 건 별로라서."

    hr "아니, 맞아."
    hr "이쪽이 훨씬 깔끔해."

    "설아는 칭찬을 듣자 대답 대신 시선을 종이 쪽으로 내렸다."
    "하지만 아까보다 손끝 움직임이 조금 덜 망설여 보였다."

    th "정말 조금씩이네."
    th "말도, 표정도, 이런 자리도."

    "나는 무심코 책상 위를 둘러봤다."
    "가위, 풀, 색지, 과자 봉지, 딸기우유 빨대 껍질, 체크리스트."
    "정돈된 것과 어수선한 것이 이상할 만큼 자연스럽게 섞여 있었다."

    th "생각보다."
    th "이 분위기, 나쁘지 않다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "그럼 다음은 역할 정하기!"
    yn "각자 제일 잘하는 거 하나씩 말해봐요."

    sj "갑자기 면접이냐."

    yn "팀워크 강화 시간이에요."
    hr "쓸데없는 것 같지만…"
    hr "의외로 필요할 수도 있겠네."

    sj "반장이 동조하면 더 무섭거든."

    yn "좋아, 제가 먼저!"
    yn "저는 분위기 담당, 친화력 담당, 간식 담당, 그리고 귀여움 담당!"

    sj "마지막은 자가 평가잖아."

    yn "강점은 어필해야죠."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "나는 정리."
    hr "일정 관리, 기록, 확인 같은 거."

    sa "어울려."

    hr "그건 칭찬으로 들을게."

    "하린이는 짧게 답했지만, 이상하게 평소보다 목소리가 부드러웠다."
    "요 며칠 사이 가장 많이 달라진 건 의외로 하린이일지도 몰랐다."
    "처음엔 늘 긴장한 사람처럼 반듯했는데, 지금은 그 반듯함 사이로 조금씩 여유가 보였다."

    yn "그럼 설아 선배는요?"

    "설아는 잠깐 생각했다."

    sa "……잘 모르겠어."
    sa "근데."
    sa "보는 건 잘해."

    sj "보는 거?"

    sa "이상한 거."
    sa "어색한 거."
    sa "튀는 거."

    "책상 위 샘플들을 떠올리면 확실히 맞는 말이었다."

    hr "맞아."
    hr "설아가 제일 먼저 알아보는 편이긴 해."

    yn "오."
    yn "그럼 미감 탐지기 담당!"

    sa "이름이 이상해."

    sj "근데 뜻은 맞네."

    "유나는 그대로 메모지에 적어 넣었다."

    yn "'서설아 - 미감 탐지기 담당'."
    sa "진짜 적었어?"
    yn "응."

    "이번엔 나를 보며 눈을 반짝였다."

    yn "마지막으로 서진 선배."
    yn "선배는 뭐 잘해요?"

    sj "귀가."

    show yuna pout at left, sway_soft with dissolve
    yn "진지하게요."
    sj "몰라."
    sj "굳이 따지면… 잡일?"

    hr "겸손한 척하지 마."
    hr "체크 빠르고, 물건 옮길 때 빠릿하고, 애들 말 적당히 정리하는 것도 잘하고."

    sj "반장이 갑자기 왜 그렇게 후하게 평가하지."

    hr "사실이니까."

    sa "부정은 못 하겠네."

    yn "맞아요."
    yn "그리고 은근 다 챙겨요."
    yn "말은 툭툭하는데."

    sj "너희 셋이 왜 갑자기 사람을 몰아가냐."

    "세 사람의 시선이 한꺼번에 붙었다."
    "장난 같기도 하고, 진심 같기도 했다."
    "그게 괜히 낯간지러워서 나는 시선을 피했다."

    sj "됐고."
    sj "그럼 나는 적당히 수습 담당으로 해."

    show yuna laugh at left, idle_bounce with dissolve
    yn "좋아!"
    yn "'윤서진 - 수습 담당'."
    yn "뭔가 멋있어."

    hr "의외로 제일 필요하네."
    sa "응."

    th "별 말 아닌데."
    th "이상하게 조금 간지럽다."

    scene black with dissolve
    centered "{size=30}잠깐의 쉬는 시간{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.2

    "한참 집중하고 나니 준비실 안 공기가 조금 따뜻해졌다."
    "유나는 결국 과자 봉지를 뜯었고, 하린이는 처음엔 됐다고 하다가도 하나 집어 들었고, 설아는 말없이 초코과자 하나를 손에 쥐었다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "잠깐만."
    yn "이거 되게 중요한 주제인데."
    yn "다들 빵 먹을 때 어디부터 먹어요?"

    sj "또 시작이네."
    hr "그게 왜 중요해."

    yn "중요하죠!"
    yn "사람 성향이 다 보인단 말이에요."

    sa "안 보일 것 같은데."

    yn "보여요."
    yn "예를 들면 전 부드러운 부분부터 먹어요."
    yn "좋은 건 마지막에 남겨두는 타입."

    hr "나는 반대로 가운데부터."
    hr "정확히 반 나눠서 먹는 쪽."

    sj "진짜 반장답네."
    hr "왜."
    sj "빵에도 정렬감이 있네."

    "하린이는 어이없다는 듯 나를 봤다가도, 결국 작게 웃었다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "그럼 너는?"

    sj "아무 생각 없이 손에 잡히는 쪽."

    yn "와."
    yn "엄청 윤서진 선배답다."

    sj "그게 무슨 뜻인데."

    yn "겉보기엔 대충인데 은근 안정적인 타입?"

    sj "지금 해석 만들었지."

    yn "조금."

    "설아는 손에 든 과자를 내려다보다가 조용히 말했다."

    sa "나는 포장부터 예쁘게 뜯는 편."

    yn "오."
    yn "그것도 뭔가 설아 선배다."

    sj "그건 그냥 깔끔한 거 아냐."

    sa "아마."

    "대화의 내용은 정말 시시했다."
    "빵 먹는 순서, 과자 고르는 취향, 좋아하는 우유 맛."
    "그런데 이상하게 그런 쓸데없는 이야기일수록 사람을 금방 익숙하게 만들었다."

    yn "가은 선배는 아마 한 입 먹고 다른 사람 것도 뺏어 먹는 타입일걸요."
    hr "묘하게 맞을 것 같아서 반박이 안 되네."
    sa "응."
    sj "왜 다들 바로 납득하냐."

    "그 순간, 마치 이름이 불리기라도 한 것처럼 준비실 문이 열렸다."

    show gaeun smile at center_lower, tiny_bounce with dissolve
    hide harin
    ge "어라."
    ge "내 얘기 했어?"

    yn "와!"
    yn "진짜 소환됐다!"

    sj "타이밍 뭐예요."
    ge "학생회실 갔다가 그냥 들렀지."
    ge "너희 아직도 여기 있구나."

    "가은 선배는 문가에 기대어 준비실 안을 한 바퀴 둘러보더니, 핀보드에 달린 장식과 종이들을 보고 눈을 휘었다."

    ge "오."
    ge "제법인데?"
    ge "이제 진짜 아지트 같다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "그쵸!"
    yn "저도 아까 그렇게 말했어요!"

    ge "그럼 내가 늦었네."
    ge "이제 아지트 인정."

    "가은 선배는 우리 쪽으로 다가와 책상 위 과자 하나를 자연스럽게 집어 들었다."

    sj "진짜 뺏어 먹는 타입이네."
    ge "응?"
    yn "역시 맞았어!"
    ge "무슨 얘기 하고 있었는지 대충 알 것 같다."

    "선배는 과자를 한 입 베어 문 채, 우리가 정리한 시안과 이름 후보를 훑어봤다."

    ge "'조용한 봄'."
    ge "생각보다 좋네."
    ge "누가 밀었어?"

    yn "접니다!"
    sa "유나가 처음 말했어."
    hr "지금은 거의 다 동의했고."

    ge "오, 그럼 역사에 이름 남겼네."
    yn "역사라니."
    yn "갑자기 되게 뿌듯해졌어요."

    ge "축제 끝나고도 기억나는 건 의외로 이런 거야."
    ge "크게 멋진 사건보다, 같이 이름 짓고 과자 나눠 먹고 그런 거."

    "그 말은 가볍게 들렸지만, 묘하게 준비실 안에 오래 남았다."
    "유나는 그냥 활짝 웃었고, 하린이는 손에 든 펜을 한 번 굴렸고, 설아는 문득 핀보드를 올려다봤다."

    th "같이 이름 짓고."
    th "과자 나눠 먹고."
    th "정말 별거 아닌 것들인데."

    ge "아무튼."
    ge "너희 지금 분위기 좋다."
    ge "계속 이렇게만 가면 부스 망할 일은 없겠네."

    sj "선배 기준이 되게 느슨한데요."
    ge "아니야."
    ge "축제는 원래 분위기 좋은 팀이 제일 강해."

    "가은 선배는 그렇게 말하며 내 어깨를 툭 쳤다."

    ge "서진도 표정 많이 풀렸어."
    ge "처음보다 훨씬 사람 같아졌네."

    sj "그건 칭찬이에요?"

    ge "당연하지."

    show yuna grin at left, idle_bounce with dissolve
    yn "저도요!"
    yn "저도 그렇게 생각했어요!"
    yn "요즘 선배, 전보다 웃는 횟수 늘었어요."

    hr "맞아."
    sa "응."

    sj "오늘 왜 다들 단체로 사람 민망하게 만드는 쪽으로 합의라도 했냐."

    "네 사람의 시선이 동시에 모였다가, 결국 거의 같이 웃음으로 무너졌다."
    "준비실 안에 퍼진 웃음은 생각보다 오래 갔다."

    scene bg old_library with dissolve

    "해가 더 기울자 준비실 창문 틈으로 주황빛이 길게 들어왔다."
    "장식 끝이 그 빛에 반짝였고, 핀보드에 붙인 색지의 그림자도 조금 길어졌다."

    "우리는 결국 오늘 해야 할 일을 예상보다 많이 끝냈다."
    "이름도 사실상 정했고, 장식 배치도 대강 방향이 잡혔고, 가격표 시안도 반쯤 완성됐다."
    "하지만 이상하게 가장 기억에 남을 건 결과보다 그 과정 쪽일 것 같았다."

    show harin normal at center_lower, sway_soft with dissolve
    hide gaeun

    hr "오늘은 여기까지 하자."
    hr "생각보다 많이 했어."

    show yuna smile at left, tiny_bounce with dissolve
    yn "그럼 기념으로 사진!"
    sj "또냐."

    yn "이럴 때 남겨야죠."

    sa "어제도 찍었는데."

    yn "어제는 어제고 오늘은 오늘이에요."

    ge "맞아."
    ge "방과 후 준비실 버전은 또 다르지."

    "결국 반대하는 사람은 아무도 없었다."
    "유나는 준비실 구석 서랍 위에 휴대폰을 세워 두고 타이머를 맞췄다."

    yn "좋아!"
    yn "이번엔 다들 자연스럽게!"
    yn "너무 굳지 말고!"

    sj "그 주문이 제일 어렵거든."

    "우리는 핀보드 앞에 대충 모여 섰다."
    "유나는 제일 앞에서 브이를 들었고, 하린이는 또 웃지 않으려다 결국 웃는 쪽으로 졌고, 설아는 이번엔 처음보다 덜 망설였다."
    "가은 선배는 뒤에서 우리 넷을 보며 장난스럽게 손을 흔들었다."

    "찰칵."

    "작은 전자음과 함께 화면이 반짝였다."

    "그 순간은 정말 아무 일도 아니었다."
    "그런데 이상하게도, 준비실 안 공기와 함께 통째로 저장되는 기분이 들었다."

    th "……이런 장면이."
    th "나중에도 오래 기억에 남는 걸까."

    show yuna laugh at left, idle_bounce with dissolve
    yn "확인한다!"
    yn "와, 이거 괜찮은데요?"

    hr "벌써?"
    ge "보여줘 봐."

    "유나는 화면을 들이밀었고, 우리는 거의 동시에 그 작은 화면을 들여다봤다."
    "노을빛이 번진 준비실."
    "삐뚤게 매단 장식 하나."
    "정리 덜 된 책상."
    "그리고 어설프게 모여 선 다섯 사람."

    sa "……좋다."

    "설아가 아주 작게 중얼거렸다."
    "정말 작았는데도 다 들렸다."

    "유나는 괜히 더 환하게 웃었다."

    yn "그쵸."
    yn "우리 제법 잘 어울려요."

    sj "누가 들으면 원래부터 한 팀이었던 줄 알겠다."

    hr "며칠 안 됐는데도."
    hr "이상하게 그렇게 느껴지긴 해."

    ge "그게 팀이 되는 과정이지."

    "가은 선배의 말에, 잠깐 아무도 대꾸하지 않았다."
    "불편해서가 아니라, 다들 조금은 같은 생각을 했기 때문일 거다."

    scene black with fade

    "준비실 문을 닫고 복도로 나오니 학교 안은 한층 조용해져 있었다."
    "남아 있는 학생들의 목소리만 멀리서 띄엄띄엄 들려왔다."

    "우리는 자연스럽게 같이 계단 쪽으로 걸었다."
    "누가 먼저라고 할 것도 없이, 발걸음이 묘하게 맞았다."

    th "시끄럽고, 어수선하고, 별거 아닌 방과 후였다."
    th "그런데 오늘도 이상하게."
    th "혼자보다 같이였던 시간이 더 오래 남을 것 같은 기분이 든다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 18 타이틀]

    scene black with fade
    centered "{size=40}Scene 18{/size}\n\n{size=30}같이 걷는 하굣길{/size}" with dissolve
    pause 1.5

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 2.0

    "방과 후의 학교는 점심시간과는 또 다른 소음을 갖고 있었다."
    "체육관 쪽에서 들려오는 공 튀는 소리."
    "운동장 어딘가에서 누군가 이름을 부르는 소리."
    "교문 쪽으로 향하는 학생들의 가벼운 발걸음."
    "그리고 그 사이를, 우리 다섯도 자연스럽게 함께 걷고 있었다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "오늘 진짜 알찼다."
    yn "이 정도면 조용한 봄, 벌써 절반은 성공 아닌가요?"

    sj "절반까지는 너무 갔고."
    sj "한… 종 장식 하나 성공 정도?"

    show yuna pout at left, sway_soft with dissolve
    yn "너무 짜다."
    yn "평가가 너무 짜요, 윤서진 선배."

    hr "그래도 오늘 많이 한 건 맞아."
    hr "이름도 거의 정했고, 가격표도 방향 잡혔고."

    sa "장식도 하나 달았어."

    sj "그 하나를 이렇게 당당하게 말하는 것도 웃기네."

    "유나는 괜히 으쓱했다."
    "아무리 작은 성과라도 크게 만드는 데에는 저 애가 재능이 있었다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "원래 팀 분위기는 작은 성공을 부풀리면서 생기는 거예요."

    ge "그건 맞아."

    show gaeun smile at far_right, tiny_bounce with dissolve

    "가은 선배가 뒤에서 우리 속도에 맞춰 천천히 걸어오고 있었다."
    "언제 자연스럽게 합류했는지도 모를 만큼 익숙한 얼굴이었다."

    sj "선배 아직 안 가셨어요?"
    ge "응."
    ge "너희 구경하느라."

    yn "와, 저희 동아리도 아닌데 구경 대상이 됐어."

    ge "관찰 가치가 있거든."
    ge "보기 드물게 조합이 재밌잖아."

    hr "그게 무슨 뜻이에요."

    ge "겉보기엔 절대 안 섞일 것 같은 애들이,"
    ge "이상하게 제일 잘 섞이고 있다는 뜻?"

    "가은 선배는 그렇게 말하며 웃었다."
    "장난 같았지만, 이상하게 틀린 말은 아니었다."

    th "확실히."
    th "처음엔 나도 이렇게 될 줄은 몰랐다."

    scene bg noisy_hallway with dissolve

    "계단을 내려갈 땐 자연스럽게 두 줄이 됐다."
    "유나는 앞쪽 난간을 손끝으로 툭툭 두드리며 내려갔고,"
    "하린이는 혹시라도 발 헛디딜까 자꾸 주변을 살폈고,"
    "설아는 조용히 옆에 붙어 걸었고,"
    "가은 선배는 느긋하게 마지막을 따라왔다."

    show yuna grin at left, idle_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    hide gaeun

    yn "아 맞다."
    yn "우리 단체방 프로필 사진, 그냥 오늘 찍은 걸로 할까요?"

    hr "벌써?"

    yn "이럴 때 해야죠."
    yn "나중에 미루면 감정이 식는다고요."

    sj "단체방 프로필 사진에 왜 감정이 들어가."

    sa "조금은 들어갈 수도 있지."

    "설아가 담담하게 한마디 얹자 유나는 바로 눈을 반짝였다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "맞죠!"
    yn "역시 설아 선배는 알아."

    hr "그래서 어떤 사진으로 할 건데."

    yn "어제 찍은 거랑 오늘 찍은 거 둘 다 후보!"
    yn "투표로 정합시다."

    sj "너 왜 사소한 걸 전부 이벤트화하냐."

    yn "사는 재미가 있잖아요."

    "그렇게 말하는 얼굴이 너무 당연해서, 뭐라 반박할 기운도 안 났다."

    scene bg school_gate with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "교문 근처로 나오자 바깥 공기가 학교 안보다 훨씬 넓게 느껴졌다."
    "늦은 오후 특유의 부드러운 바람이 불었고, 벚나무 가지가 아주 조금 흔들렸다."
    "정문 바깥은 귀가하는 학생들로 적당히 붐볐지만, 이상하게 우리 주변만은 조금 느리게 흐르는 것 같았다."

    show yuna normal at left, sway_soft with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    show gaeun smile at far_right, tiny_bounce with dissolve

    yn "다들 집 방향 어디예요?"
    yn "생각해보니까 제대로 물어본 적 없네."

    hr "나는 학교에서 버스로 세 정거장 정도."
    sa "나는 반대쪽."

    ge "난 지하철 타야 돼."

    "셋의 시선이 자연스럽게 내게 왔다."

    sj "왜 또 다 나를 봐."
    yn "선배가 제일 안 말해줄 것 같아서."
    sj "무슨 이미지냐 그건."

    hr "조금 맞긴 해."
    sa "응."

    sj "상처받네."

    "별로 상처받지도 않았으면서 그렇게 말하자,"
    "유나가 바로 웃음을 터뜨렸다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "방금 표정 하나도 안 바뀌었거든요."

    sj "들켰네."

    "결국 나는 대충 집 방향을 말했다."
    "딱히 특별한 정보도 아니었는데, 이상하게 그 대화만으로도 서로가 조금 더 현실적인 사람처럼 느껴졌다."
    "교실이나 준비실에서만 보던 애들이 아니라, 학교 밖에서도 이어지는 생활을 가진 사람들."

    th "당연한 건데."
    th "왜 이제야 조금 실감나는 걸까."

    show yuna smile at left, tiny_bounce with dissolve
    yn "그럼 오늘은 어디까지 같이 가요?"
    sj "그건 또 무슨 질문이야."

    yn "그냥요."
    yn "같이 가면 좋잖아요."

    "아무렇지 않게 나온 말이었다."
    "그런데 그 말이 묘하게 자연스러워서, 아무도 바로 부정하지 못했다."

    hr "버스 정류장까진 같이 가도 되지."
    sa "응."
    ge "나도 그쪽이야."

    sj "이쯤 되면 선택권 없는 분위기네."

    yn "축하합니다."
    yn "강제 동행에 당첨되셨어요."

    scene bg school_road_dusk with dissolve

    "우리는 결국 학교 앞 길을 나란히 걸었다."
    "정문을 벗어나자 교복 차림 학생들이 여기저기 흩어졌고,"
    "문구점 앞에서 멈춰 서는 애들,"
    "편의점으로 들어가는 애들,"
    "이어폰을 끼고 혼자 걷는 애들 사이로 우리도 천천히 섞였다."

    "유나는 금세 길가의 작은 인형뽑기 기계를 발견했다."

    show yuna surprise at left, excited_hop with dissolve
    yn "우와."
    yn "저거 봐요."

    sj "설마 멈출 생각은 아니지."

    show yuna grin at left, idle_bounce with dissolve
    yn "…조금?"

    hr "안 돼."
    hr "너 분명 한 번으로 안 끝나."

    yn "반장님, 사람을 너무 잘 아시는데요."

    ge "난 구경은 가능."
    sa "나도."

    sj "전원 동조하네."

    "결국 우리는 인형뽑기 기계 앞에 잠깐 멈춰 섰다."
    "유리는 약간 뿌옇게 닦여 있었고, 안에는 토끼인지 곰인지 애매한 분홍 인형이 몇 개 들어 있었다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "저거 딱 제 취향이다."
    sj "전형적이네."
    yn "무슨 뜻이에요?"
    sj "딸기우유 좋아하고, 분홍색 좋아하고, 말 많고."
    yn "마지막은 왜 끼워 넣어요."

    sa "근데 어울려."

    "설아의 짧은 한마디에 유나는 또 만족한 표정을 지었다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "좋아, 설아 선배가 인정했으니 됐어."

    hr "넣을 거면 딱 한 번만 해."
    yn "진짜 한 번만!"
    sj "저 대사에서 이미 신뢰가 안 간다."

    "유나는 동전을 넣고, 진지한 얼굴로 버튼을 잡았다."
    "아까 준비실에서 사다리 타던 애랑 같은 사람이라고는 믿기지 않을 정도로 집중한 얼굴이었다."

    yn "…간다."

    "기계 팔이 천천히 내려갔다."
    "토끼 귀를 스치고, 인형 몸통을 아주 어설프게 집고, 그대로 미끄러졌다."

    show yuna surprise at left, excited_hop with dissolve
    yn "아악."
    yn "아깝다!"

    sj "역시."
    hr "끝."
    yn "한 번 더."
    hr "안 돼."

    ge "반응이 너무 예상 그대로라 웃기다."

    sa "거의 드라마 같아."

    "유나는 진심으로 아쉬워했지만, 하린이가 정말 단호하게 막아서자 결국 포기했다."
    "대신 유리창에 손을 대고 인형을 바라보며 중얼거렸다."

    show yuna pout at left, sway_soft with dissolve
    yn "다음에 꼭 데리러 올게…"

    sj "인형한테 약속까지 하네."

    scene bg store with dissolve

    "인형뽑기 소동이 끝난 뒤에도 이상하게 누구 하나 먼저 가자는 말을 하지 않았다."
    "그래서 우리는 자연스럽게 편의점 앞까지 걸어갔다."
    "교문에서 조금 떨어진 작은 편의점이었다."
    "통유리 너머로 형광등 불빛이 환하게 새어나오고 있었다."

    show yuna normal at left, sway_soft with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    hide gaeun

    yn "저 갑자기 아이스크림 먹고 싶어요."

    sj "너 오늘 먹는 얘기만 몇 번째냐."

    yn "사람은 원래 계절과 감정에 따라 먹고 싶은 게 바뀌는 거예요."

    hr "그럴듯하게 말하지 마."

    ge "근데 나도 좀 땡기긴 한다."

    sa "……나도."

    sj "여기서 설아까지?"
    sa "조금."

    "결국 또 다 같이 편의점 안으로 들어갔다."

    scene black with dissolve
    centered "{size=30}편의점{/size}" with dissolve

    scene bg store with fade
    play music "audio/bgm_daily_light.ogg" fadein 1.5

    "편의점 안은 바깥보다 조금 더 따뜻했다."
    "냉장고 모터 돌아가는 소리와 계산대에서 찍히는 바코드 소리가 잔잔하게 섞였다."
    "하린이는 처음엔 안 산다고 하더니 제일 먼저 탄산수를 집었고,"
    "유나는 아이스크림 냉동고 앞에서 심각한 표정으로 고민했고,"
    "설아는 음료 코너에서 한참 상표를 보고 있었다."
    "가은 선배는 그런 우리를 보며 웃기만 했다."

    sj "유나는 또 왜 그렇게 진지해."

    show yuna normal at left, sway_soft with dissolve
    yn "선택의 순간은 늘 엄숙한 법이거든요."
    yn "초코냐 딸기냐, 지금 이건 아주 중대한 문제예요."

    sj "이미 딸기 쪽으로 마음 기운 얼굴인데."

    yn "그건 편견입니다."
    yn "…근데 딸기가 더 예뻐 보이긴 하네요."

    hr "결국."

    "나는 대충 아무 아이스크림 하나를 집었고,"
    "하린이는 탄산수와 작은 과자,"
    "설아는 생각보다 오래 고민하다가 바닐라 아이스크림을 골랐다."

    show yuna surprise at left, excited_hop with dissolve
    yn "오."
    yn "설아 선배 바닐라 좋아해요?"

    sa "무난해서."
    yn "무난한데 맛있는 게 진짜 좋은 거죠."

    ge "그럼 난 초코."
    ge "균형 맞춰줄게."

    sj "그건 무슨 균형인데요."

    "계산을 마치고 편의점 앞 벤치 쪽으로 나오자, 바깥 하늘은 더 천천히 저물고 있었다."
    "아직 완전히 어두워지지도 않았고, 그렇다고 환하지도 않은 시간."
    "묘하게 모든 게 부드럽게 보이는 시간이었다."

    scene bg store with dissolve

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    show gaeun smile at far_right, tiny_bounce with dissolve

    "우리는 편의점 앞 좁은 벤치와 난간 근처에 적당히 흩어져 섰다."
    "누가 먼저라고 할 것도 없이 포장을 뜯는 소리들이 이어졌다."

    yn "좋아."
    yn "이건 비공식 뒤풀이예요."

    sj "부스 준비 두 시간 했다고 벌써 뒤풀이냐."

    yn "이럴 때 자주 해야 팀 결속이 생겨요."

    hr "그렇게까지 거창한 건 아니지만…"
    hr "뭐, 나쁘진 않네."

    "하린이가 탄산수 캔을 따는 소리가 맑게 울렸다."
    "설아는 바닐라 아이스크림 뚜껑을 아주 깔끔하게 벗겼고,"
    "가은 선배는 빨대도 안 쓰고 바로 음료를 마셨다."

    ge "근데 너희 진짜 재미있다."
    ge "준비실에서만 봤을 때도 그랬는데, 밖에서 보니까 더."

    sj "선배 자꾸 구경거리 보듯 말해요."

    ge "칭찬이야."
    ge "살아 있는 청춘 같다고."

    show yuna laugh at left, idle_bounce with dissolve
    yn "와, 오늘 두 번째 청춘."

    sj "이제 이 단어만 나오면 자동 반응하네."

    sa "유나한테 전염됐어."

    hr "조금씩 다들 전염되는 것 같긴 해."

    "하린이의 그 말에, 잠깐 다들 웃었다."
    "부정하려고 해도 이미 늦은 느낌이었다."

    "유나는 아이스크림을 한 입 먹더니 갑자기 휴대폰을 꺼냈다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "투표 간다."

    sj "아까 말한 단체방 사진?"

    yn "네."
    yn "오늘 사진이냐, 어제 사진이냐."

    "유나는 단체방에 바로 사진 두 장을 올렸다."
    "어제 처음 어색하게 모여 찍은 사진."
    "그리고 오늘 준비실 노을빛이 묻은 사진."

    "유나 : 자 지금부터 투표!"
    "유나 : 1번 어제 / 2번 오늘"

    hr "이걸 꼭 지금 해야 해?"
    yn "네."

    sa "난 2번."

    "설아가 제일 먼저 대답했다."
    "유나는 바로 환호했다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋았어!"
    yn "설아 선배 센스 있어."

    hr "…나도 2번."
    ge "나도 오늘."

    "셋이 너무 쉽게 넘어가자, 자연스럽게 시선이 내게 꽂혔다."

    sj "왜 또."
    yn "마지막 한 표."
    yn "중요합니다."

    "나는 휴대폰 화면을 내려다봤다."
    "어제 사진은 조금 더 어색했지만, 처음이란 느낌이 있었다."
    "오늘 사진은 준비실의 노을과 웃는 얼굴들 때문에 훨씬 편해 보였다."

    th "둘 다 나쁘지 않은데."

    sj "2번."

    show yuna laugh at left, idle_bounce with dissolve
    yn "만장일치!"
    yn "좋아, 그럼 프로필 사진 교체!"

    "유나는 바로 단체방 프로필을 바꿨다."
    "작은 원형 안에 다섯 사람이 다 들어가진 않았지만,"
    "그 잘려 있는 구도조차 이상하게 지금 우리 같았다."

    sa "잘렸다."
    yn "그게 포인트예요."
    sj "무슨 포인트냐."
    yn "완벽하지 않아서 더 좋은 느낌?"

    hr "어쩐지 조금 이해돼서 싫네."

    "하린이 말에 또 웃음이 번졌다."

    scene bg store with dissolve

    "아이스크림이 절반쯤 줄어들 무렵,"
    "대화는 또 사소한 쪽으로 흘렀다."

    "좋아하는 과자,"
    "수업 시간 졸릴 때 버티는 방법,"
    "교복 주머니에 늘 들어 있는 물건,"
    "시험기간 밤샘 가능 여부."

    yn "전 시험기간엔 꼭 젤리 있어야 돼요."

    hr "난 형광펜."
    sa "이어폰."

    sj "자는 거."
    yn "그건 준비물이 아니잖아요!"

    ge "서진은 너무 솔직해서 웃겨."

    sj "현실적인 거죠."

    "설아는 아이스크림 스푼을 내려다보다가 아주 작게 덧붙였다."

    sa "그래도."
    sa "같이 있으면 덜 졸릴 것 같아."

    "조용한 말이었는데, 다들 듣자마자 잠깐 멈췄다."
    "그 말이 웃기거나 이상해서가 아니라,"
    "너무 자연스럽고, 또 너무 예상 밖이라서."

    show yuna smile at left, tiny_bounce with dissolve
    yn "……그건 좀 좋다."

    hr "응."

    sj "맞네."

    ge "와."
    ge "이 팀, 생각보다 빨리 친해지는데?"

    "설아는 괜히 시선을 피하며 남은 아이스크림을 한 입 더 먹었다."
    "유나는 그런 설아를 괜히 건드리지 않고, 대신 혼자 흐뭇하게 웃었다."
    "하린이는 탄산수 캔 표면에 맺힌 물방울을 손끝으로 훑었다."
    "가은 선배는 우리를 번갈아 보다 작게 웃었다."

    th "같이 있으면 덜 졸릴 것 같아."
    th "정말 별거 아닌 말인데."

    th "오늘 하루를 설명하기엔."
    th "그 말 하나로 충분한 것 같기도 했다."

    scene bg school_road_dusk with dissolve

    "결국 아이스크림을 다 먹고 나서야 우리는 다시 길을 걸었다."
    "편의점 앞에서 조금만 더, 조금만 더 하다가,"
    "어느새 버스 정류장까지 같이 와 있었다."

    show yuna normal at left, sway_soft with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    show gaeun smile at far_right, tiny_bounce with dissolve

    hr "난 여기서 타."
    sa "나도 다음 버스."

    yn "아, 벌써 헤어질 타이밍인가…"

    sj "너 아까부터 같이 있었잖아."

    yn "그래도 아쉽단 말이에요."

    ge "그럼 내일 또 보면 되지."

    "가은 선배 말에 유나는 금방 살아났다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "맞다!"
    yn "내일 점심, 준비실 잠깐 들를래요?"
    yn "장식 배치 다시 보고 싶어요."

    hr "점심시간 다 쓰는 건 안 돼."
    hr "20분만."

    sa "20분이면 충분해."

    sj "벌써 일정 잡히네."

    yn "물 들어올 때 노 젓는 거예요."

    "버스 전광판의 숫자가 한 칸씩 바뀌었다."
    "하린이는 도착 시간을 보고 가방끈을 고쳐 잡았고,"
    "설아는 정류장 기둥 옆에 조용히 섰고,"
    "유나는 우리를 보다가 또 단체방을 열었다."

    yn "좋아."
    yn "오늘의 결론 정리."
    yn "1. 조용한 봄은 공식 분위기 확정"
    yn "2. 준비실은 아지트"
    yn "3. 설아 선배는 미감 탐지기"
    yn "4. 윤서진 선배는 수습 담당"

    sj "왜 그건 박제하냐."

    hr "난 반대 안 해."

    sa "나도."

    ge "아주 적절하네."

    sj "이 팀 위험하다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "이제 늦었어요."
    yn "선배는 이미 저희 팀이에요."

    "장난스럽게 말한 거였는데,"
    "그 말은 이상하게 장난으로만 들리지 않았다."

    th "이미 저희 팀."
    th "…뭐, 틀린 말도 아니네."

    "잠시 뒤 버스가 들어왔다."
    "하린이는 먼저 한 걸음 나섰고, 설아도 뒤를 따랐다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "내일 봐."

    show seola normal at right, sway_soft with dissolve
    sa "……내일."

    "둘은 짧게 손을 흔들고 버스에 올랐다."
    "문이 닫히고 버스가 떠난 뒤에도,"
    "유나는 한동안 그쪽을 보다가 천천히 몸을 돌렸다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "이상하네요."
    yn "며칠 전까지만 해도 그냥 같은 학교 사람들이었는데."

    sj "갑자기 감성 모드냐."

    yn "조금."
    yn "근데 진짜."
    yn "벌써 좀 아쉬워서."

    ge "좋은 거지."
    ge "그런 마음 드는 거."

    "가은 선배는 아주 당연하다는 듯 말했다."
    "그러곤 우리 둘을 번갈아 보더니, 짓궂게 웃었다."

    ge "남은 둘은 더 친해질 기회네."

    sj "왜 그렇게 되는데요."

    yn "오."

    show yuna grin at left, idle_bounce with dissolve
    yn "선배, 우리도 저쪽 편의점 다시 한 바퀴—"

    sj "안 돼."

    yn "거절 빠르다."

    ge "후후."
    ge "그 반응도 이제 좀 익숙해졌네."

    scene bg school_road_dusk with dissolve

    "가은 선배는 지하철역 쪽 갈림길에서 먼저 손을 흔들었다."

    ge "둘 다 조심히 가."
    ge "내일 또 봐."

    yn "네에!"
    sj "들어가세요."

    "선배가 멀어지고 나자, 길에는 나와 유나 둘만 남았다."
    "조금 전까진 다섯이었는데, 갑자기 조용해진 느낌이었다."
    "그런데 어색하진 않았다."
    "이상할 정도로."

    show yuna smile at left, tiny_bounce with dissolve

    yn "……선배."

    sj "왜."

    yn "오늘 재밌었어요."

    "유나는 앞을 보면서 말했다."
    "아주 가볍게 던진 말 같았는데, 목소리는 생각보다 조용했다."

    yn "준비실도 좋았고."
    yn "같이 걷는 것도 좋았고."
    yn "편의점도 좋았고."

    sj "먹는 게 제일 좋았던 거 아니냐."

    show yuna laugh at left, idle_bounce with dissolve
    yn "그건 부정 안 할게요."

    "유나는 금세 원래대로 돌아와 웃었다."
    "그리고 한 걸음 앞서 걷다가, 몸을 반쯤 돌려 나를 봤다."

    yn "근데 선배도 오늘 좀 즐거워 보였어요."

    sj "기분 탓."

    yn "아닌데."
    yn "전 이제 알아요."
    yn "선배가 진짜 귀찮은 거랑, 그냥 툭 말하는 거 차이."

    sj "그걸 벌써 구분한다고?"

    yn "네."
    yn "저 은근 눈치 빠르거든요."

    "나는 대꾸 대신 헛웃음만 흘렸다."
    "반박하고 싶은데, 정말로 완전히 틀린 말도 아니라서 더 그랬다."

    th "언제 이렇게까지 익숙해졌지."

    scene bg school_road_dusk with dissolve

    "조금 더 걷자, 결국 우리도 갈림길 앞에 섰다."
    "한쪽은 버스 정류장 쪽, 다른 한쪽은 주택가 쪽."
    "해는 더 내려가고 있었지만 아직 분위기가 어두워지진 않았다."
    "오히려 하루가 길게 남아 있는 것 같은, 그런 저녁이었다."

    show yuna normal at left, sway_soft with dissolve

    yn "그럼 여기서 진짜 빠이?"

    sj "그래야지."

    "유나는 잠깐 아쉬운 표정을 했다가, 이내 금방 웃었다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋아요."
    yn "대신 내일 점심 늦지 마요."
    yn "그리고 단체방 읽씹 금지."

    sj "조건 많네."

    yn "중요한 거예요."

    sj "알았어."

    "유나는 만족한 듯 고개를 끄덕였다."
    "그러고는 돌아서기 전에 한 번 더 말했다."

    yn "선배."

    sj "또 왜."

    yn "오늘 진짜."
    yn "같이 있어서 좋았어요."

    "그 말을 남기고, 유나는 가볍게 손을 흔든 뒤 제 쪽 길로 달려갔다."
    "짧게 펄럭이는 머리카락과 가방끈이 늦은 햇빛 아래에서 흔들렸다."

    "나는 멀어지는 뒷모습을 잠깐 바라보다가, 주머니 속 휴대폰이 진동하는 걸 느꼈다."

    "유나 : 오늘 수고했어요 다들!"
    "유나 : 조용한 봄 최고"
    "유나 : 내일도 잘 부탁합니다 ☺"

    "곧 이어서 메시지가 올라왔다."

    "하린 : 내일 점심 20분만."
    "설아 : 응."
    "가은 : 준비실 아지트화 축하"

    "나는 화면을 보다가, 잠시 멈췄다."

    th "원래라면 그냥 읽고 넘겼을 텐데."

    "손가락이 자연스럽게 키보드 위로 올라갔다."

    "서진 : 알겠어"
    "서진 : 내일 보자"

    "전송 버튼을 누르자마자,"
    "곧장 유나의 답장이 튀어 올라왔다."

    "유나 : 오"
    "유나 : 선배가 먼저 답장했다"
    "유나 : 역사적 사건"

    "나도 모르게 웃음이 샜다."

    scene black with fade

    "집으로 가는 길."
    "평소와 똑같은 거리, 똑같은 하늘, 똑같은 저녁일 텐데."

    "이상하게도 오늘은,"
    "교실도,"
    "준비실도,"
    "편의점도,"
    "버스 정류장도."

    "전부 조금씩 더 오래 기억에 남을 것 같았다."

    th "별일은 없었다."
    th "정말로, 하나도 특별한 사건은 없었다."

    th "그런데."
    th "아무 일도 없어서 좋았던 날도,"
    th "생각보다 꽤 오래 남는 법일지도 모른다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 19 타이틀]

    scene black with fade
    centered "{size=40}Scene 19{/size}\n\n{size=30}점심 20분의 약속{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "다음 날 점심시간."
    "수업이 끝나자마자 교실 안 공기가 순식간에 풀어졌다."
    "의자가 밀리는 소리, 급식실 갈 사람을 부르는 소리, 벌써 도시락 뚜껑을 여는 소리."
    "평소라면 그 소란 속에 적당히 섞여 있었을 텐데."
    "오늘은 이상하게, 머릿속 한구석에 먼저 떠오르는 장소가 있었다."

    th "준비실."
    th "딱 20분이라고 했지."

    "내 휴대폰이 짧게 울렸다."

    "유나 : 다들 출석 체크"
    "유나 : 준비실로 오는 사람 손"
    "유나 : 윤서진 선배 도망 금지"

    th "진짜 감시하네."

    "곧이어 메시지가 하나 더 올라왔다."

    "하린 : 나 먼저 가고 있어."
    "설아 : 곧."
    "가은 : 나는 학생회실 들렀다가 갈게"

    th "왜 다들 이렇게 성실한 거지."

    "나는 가방 대신 휴대폰만 챙긴 채 자리에서 일어났다."
    "점심시간의 햇빛이 창문을 타고 들어와 책상 위를 밝게 덮고 있었다."
    "그 빛이 이상하게 준비실의 핀보드와 색지들을 떠올리게 했다."

    scene black with dissolve
    centered "{size=30}준비실{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "문을 열자 익숙한 종 냄새와 풀 냄새가 먼저 느껴졌다."
    "그리고 이제는 꽤 자연스러운 풍경이 눈에 들어왔다."

    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    "하린이는 벌써 체크리스트를 들여다보고 있었고,"
    "설아는 어제 붙여 둔 장식을 올려다보며 위치를 다시 확인하는 중이었다."

    sj "진짜 먼저 와 있었네."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "20분뿐이잖아."
    hr "늦으면 아까워."

    sa "안 늦었어."
    sa "정각이야."

    sj "그걸 또 체크했냐."

    sa "조금."

    "설아는 아주 담담하게 대답했다."
    "그런데 그 말이 괜히 웃겨서 나는 피식 웃었다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "유나는 아직이야."

    sj "의외네."
    sj "제일 먼저 와서 떠들고 있을 줄 알았는데."

    "말이 끝나기 무섭게 복도 쪽에서 급한 발소리가 들렸다."
    "곧 문이 벌컥 열렸다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "세이프!"
    yn "아직 1분 남았죠?!"

    sj "본인이 늦을 뻔했네."

    show yuna pout at left, sway_soft with dissolve
    yn "매점 줄이 생각보다 길었단 말이에요."

    hr "또 갔어?"

    yn "오늘은 다 같이 먹을 거 사 왔어요."

    "유나는 자랑스럽게 비닐봉지를 흔들었다."
    "안에는 작은 초코과자와 사탕 몇 개, 그리고 우유 두 개가 들어 있었다."

    sj "점심 20분인데 준비실보다 간식 비중이 더 큰 거 아니냐."

    yn "기분 좋은 공간엔 기분 좋은 당이 필요합니다."

    sa "논리가 생긴 것 같으면서 없어."

    "설아가 그렇게 말하자 유나는 억울한 척했지만, 금방 웃었다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "설아 선배 요즘 말 되게 잘해요."
    sa "원래 했어."
    sj "근데 맞는 말이긴 해."

    "하린이는 결국 한숨 비슷한 숨을 내쉬면서도 비닐봉지를 받아 책상 위에 올려뒀다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "알았어."
    hr "대신 진짜 20분 안에 끝내."

    yn "네, 반장님!"

    scene bg old_library with dissolve

    "우리 넷은 어제보다 더 자연스럽게 책상 주변으로 모였다."
    "누가 어디에 서는지도 점점 정해지는 느낌이었다."
    "유나는 늘 가장 먼저 움직이고,"
    "하린이는 제일 먼저 정리하고,"
    "설아는 한 걸음 물러난 자리에서 전체를 보고,"
    "나는 그 사이에서 어중간하게 붙어 있다가 결국 다 같이 얽혔다."

    th "이제는 정말 어중간하지도 않네."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    hr "좋아."
    hr "오늘 할 건 간단해."
    hr "핀보드 왼쪽 여백 정리하고, 가격표 글씨체 대충 맞춰보고, 어제 말한 프로필 사진도 설명란이랑 같이 정리하자."

    yn "단체방 설명란도 꾸며요?"
    hr "꾸미는 건 아니고 정리."
    yn "그게 꾸미는 거죠."

    sj "너 기준에선 세상 모든 게 꾸미는 거지."

    yn "좋은 거잖아요."

    "유나는 말하면서 색지 한 장을 들어 빛에 비춰 봤다."
    "연노랑 종이가 햇빛을 받아 얇게 빛났다."
    "그걸 바라보는 얼굴이 괜히 진지해서, 나는 무심코 물었다."

    sj "넌 왜 그런 거 고를 때마다 표정이 그렇게 비장하냐."

    show yuna surprise at left, excited_hop with dissolve
    yn "네?"
    yn "전 늘 진심인데요."

    sa "맞아."
    sa "유나는 사소한 것도 전부 중요하게 생각해."

    "설아가 너무 자연스럽게 편을 들어 주는 바람에,"
    "유나는 순간 말문이 막힌 얼굴을 했다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "……설아 선배."
    yn "저 지금 약간 감동했어요."

    sa "왜."

    yn "방금 엄청 좋은 말 했잖아요."

    sa "그랬나."

    "설아는 진짜로 몰랐다는 표정이었다."
    "그래서 오히려 더 진심처럼 들렸다."

    th "이 둘 조합도 점점 재밌네."

    show harin normal at center_lower, sway_soft with dissolve
    hr "자, 감동은 나중에 하고."
    hr "이 부분."
    hr "왼쪽이 아직 좀 비어 보여."

    "하린이가 핀보드 모서리를 짚었다."
    "확실히 어제 붙인 종 장식 하나만으론, 왼쪽 위가 약간 휑해 보였다."

    sj "작은 거 하나 더 붙이면 되겠네."

    yn "맞아요!"
    yn "저 별 모양 잘라 둘까요?"

    hr "별은 조금 흔해."
    sa "작은 꽃."
    sa "아니면 잎사귀."

    "설아가 말하자 유나는 바로 색지를 뒤적였다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "그럼 오늘의 작업은 미니 잎사귀 생산."

    sj "이름 붙이는 속도는 진짜 빠르네."

    hr "쓸데없이."
    yn "쓸데없지 않아요."
    yn "이런 게 분위기를 만든다고요."

    scene bg old_library with dissolve

    "결국 우리는 정말로 작은 잎사귀 몇 개를 잘라 핀보드 여백에 대 보기 시작했다."
    "직접 해 보니 생각보다 미묘했다."
    "크기가 조금만 커도 튀고, 위치가 살짝만 어긋나도 이상했다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "오른쪽으로 1센티."
    sj "너 그런 걸 어떻게 바로 보냐."

    hr "보이는데."

    show seola normal at right, sway_soft with dissolve
    sa "조금만 아래."
    sa "지금은 위가 답답해."

    show yuna smile at left, tiny_bounce with dissolve
    yn "오케이, 미감 탐지기 선배 의견 반영!"

    sj "근데 진짜 둘 말 듣고 옮기니까 훨씬 낫네."

    "하린이와 설아는 잠깐 동시에 핀보드를 바라봤다."
    "서로 성격은 꽤 달라 보이는데, 이상하게 이런 쪽 감각은 잘 맞는 것 같았다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "의외로 통하네."

    sa "응."
    sa "하린도 잘 봐."

    "하린이는 별일 아니라는 척했지만,"
    "아주 조금 표정이 풀렸다."

    th "칭찬받으면 다들 똑같네."

    "유나는 그런 둘을 번갈아 보다가 갑자기 메모지에 뭔가 적기 시작했다."

    sj "또 뭔데."
    yn "별명 업데이트요."

    sj "왜 또."

    show yuna laugh at left, idle_bounce with dissolve
    yn "이미 다들 역할명이 있잖아요."
    yn "하린이는 체크리스트 반장."
    yn "설아 선배는 미감 탐지기."
    yn "서진 선배는 수습 담당."

    hr "난 언제 체크리스트 반장이 됐어."

    yn "방금."

    sa "직관적이긴 해."

    sj "설마 넌?"
    yn "전 당연히 분위기 담당."

    sj "그건 아무도 안 뺏어간다."

    "유나는 만족한 듯 고개를 끄덕였다."
    "이쯤 되면 진짜 별명 붙이는 걸 꽤 좋아하는 것 같았다."

    scene bg old_library with dissolve

    "작은 잎사귀 세 개를 더 붙이고,"
    "가격표용 종이에 글씨 샘플을 몇 번 써 보고,"
    "단체방 설명란을 '축제 준비 중 / 지각 금지 / 간식 권장'으로 정리했을 때쯤,"
    "준비실 문이 가볍게 두드려졌다."

    show gaeun smile at far_right, tiny_bounce with dissolve

    ge "실례합니다, 조용한 봄 여러분."

    yn "가은 선배 왔다!"

    "가은 선배는 문가에 기대 웃고 있었다."
    "점심시간이라 그런지 어제보다 더 가벼운 분위기였다."

    ge "다들 성실하네."
    ge "진짜 20분 쓰고 있었어?"

    hr "약속했으니까요."

    ge "좋다."
    ge "그런 거 의외로 오래 가."

    sj "선배는 꼭 그런 말 해요."

    ge "맞잖아."
    ge "이렇게 점심시간 쪼개서 같이 모이는 거."
    ge "나중엔 되게 별거 아닌데 오래 기억나는 쪽이거든."

    "가은 선배는 우리 쪽으로 다가와 핀보드를 한 번 보고,"
    "어제보다 조금 더 채워진 장식들을 보며 고개를 끄덕였다."

    ge "오."
    ge "진짜 점점 그럴듯해진다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "그쵸!"
    yn "오늘은 잎사귀까지 추가됐어요."

    ge "잎사귀?"
    sj "네이밍은 얘가 했어요."
    ge "그것도 유나답네."

    "가은 선배는 책상 위에 놓인 사탕 하나를 집어 들었다."

    ge "이건 회의비?"

    hr "아니요."
    sj "유나가 멋대로 사 온 간식."

    show yuna pout at left, sway_soft with dissolve
    yn "멋대로가 아니라 팀 복지예요."

    sa "지금은 거의 정식 명칭처럼 쓰네."

    ge "좋은데?"
    ge "복지 좋은 팀이 오래 가."

    "가은 선배는 사탕 포장을 뜯으며 자연스럽게 우리 사이에 섞였다."
    "정말 묘한 사람이다."
    "딱히 시끄럽게 끼어드는 것도 아닌데,"
    "어느 순간 보면 원래부터 그 자리에 있었던 사람처럼 편해 보인다."

    th "가은 선배는 그런 의미에서 제일 신기해."

    scene bg old_library with dissolve

    "점심시간은 생각보다 빨리 흘렀다."
    "아직 한참 남은 줄 알았는데, 시계를 보니 벌써 절반이 훌쩍 지나 있었다."

    show harin surprise at center_lower, excited_hop with dissolve
    hr "잠깐."
    hr "10분 남았어."

    show yuna surprise at left, excited_hop with dissolve
    yn "벌써요?!"
    yn "왜 준비실 시간은 이렇게 빨라."

    sj "어제도 똑같은 말하지 않았냐."

    sa "여기선 시간이 조금 빨라."

    "설아가 너무 아무렇지 않게 말해서,"
    "다들 잠깐 멈췄다가 작게 웃었다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "와."
    yn "그 말 되게 좋다."

    ge "오, 인정."
    hr "조금… 시 같은데."

    sa "그런가."

    "설아는 진심으로 모르겠다는 얼굴이었다."
    "그래서 더 웃겼다."
    "유나는 이미 휴대폰 메모장에 그 말을 적으려는 것처럼 화면을 켜고 있었다."

    sj "설마 적는 거냐."
    yn "당연하죠."
    yn "나중에 부스 소개 문구 같은 데 써도 좋을 것 같은데요?"

    hr "그건 조금 오버고."

    ge "근데 감성은 있다."

    sa "……그냥 생각난 건데."

    "그냥 생각난 말."
    "그런데 준비실 안에 있는 누구도 그 말을 가볍게 넘기지 않았다."
    "이 공간이 조금 특별해지고 있다는 걸,"
    "다들 비슷하게 느끼고 있었기 때문일지도 모른다."

    th "여기선 시간이 조금 빨라."
    th "묘하게 맞는 말이네."

    scene bg old_library with dissolve

    "남은 10분은 더 빨랐다."
    "하린이는 가격표 샘플을 두 장 골라 따로 모아 두었고,"
    "설아는 잎사귀 위치를 마지막으로 한 번 더 정리했고,"
    "유나는 단체방 설명란 뒤에 몰래 벚꽃 이모지를 하나 넣었다가 하린이에게 바로 걸렸고,"
    "나는 테이프와 네임펜을 다시 봉투 안에 정리했다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "민유나."
    hr "이모지 뺐어."

    show yuna pout at left, sway_soft with dissolve
    yn "왜요."
    yn "귀엽잖아요."

    hr "업무방이야."

    sj "근데 좀 귀엽긴 한데."

    "내가 무심코 그렇게 말하자,"
    "하린이와 유나가 동시에 나를 봤다."
    "설아도 따라 시선을 들었다."

    sj "왜."

    show yuna grin at left, idle_bounce with dissolve
    yn "선배가 귀엽다고 했다."

    sj "이모지가."
    yn "아무튼 귀엽다고 했잖아요."

    sj "이 팀 진짜 말 꼬투리 잘 잡네."

    sa "이미 늦었어."

    ge "응."
    ge "발언은 기록된다."

    "가은 선배까지 태연하게 얹자,"
    "결국 나는 그냥 한숨처럼 웃었다."

    th "이제 반박하는 것도 귀찮다."
    th "아니, 귀찮다기보다."
    th "그냥 이쪽이 더 편하다."

    scene bg old_library with dissolve

    "점심시간 종료 예비종이 울리기 직전,"
    "유나는 갑자기 책상 위를 한 번 둘러보더니 손뼉을 쳤다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "잠깐."
    yn "오늘도 기념 하나 남기죠."

    sj "또 사진?"

    yn "아뇨."
    yn "출석 도장."

    hr "그게 뭔데."

    "유나는 작은 메모지를 꺼내더니 동그라미 네 개를 그렸다."
    "그리고 각 동그라미 아래에 이름을 적었다."

    yn "오늘 점심 준비실 모임 참가자 표시!"
    yn "하루에 하나씩 체크해서 쌓는 거예요."

    sj "유치원 출석판 같거든."

    yn "그게 뭐 어때서요."
    yn "이런 거 귀엽잖아요."

    sa "귀엽긴 해."

    hr "…생각보다 괜찮은데."

    sj "둘 다 당하네."

    "결국 우리 넷은 각자 자기 이름 옆 동그라미 안에 표시를 남겼다."
    "하린이는 체크 표시,"
    "설아는 작은 점,"
    "유나는 하트를 그리려다가 하린이 눈치를 보고 그냥 동그라미,"
    "나는 대충 사선 하나."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "난?"
    yn "가은 선배는 특별 게스트!"
    ge "오, 좋다."

    "유나는 선배 이름 옆에 별표를 하나 그려 넣었다."
    "쓸데없는데 이상하게 웃겼다."

    th "진짜 별거 아닌데."
    th "이런 게 왜 이렇게 재밌지."

    scene bg old_library with dissolve

    "그리고 마침내 예비종이 울렸다."

    play sound "audio/sfx_school_bell.ogg"

    show harin surprise at center_lower, excited_hop with dissolve
    hr "이제 진짜 가야 해."

    show yuna surprise at left, excited_hop with dissolve
    yn "벌써?!"
    yn "진짜 너무 짧다…"

    sa "아까도 그랬잖아."
    ge "좋을 때 시간 빨리 가는 건 정상이야."

    "우리는 서둘러 책상 위를 정리했다."
    "이제는 누가 말하지 않아도 손이 먼저 움직였다."
    "누군가는 종이를 포개고,"
    "누군가는 펜 뚜껑을 닫고,"
    "누군가는 장식이 떨어지지 않았는지 마지막으로 확인했다."

    th "처음엔 어색해서 뭐부터 해야 할지 몰랐는데."
    th "지금은 그냥 움직이면 된다."
    th "그만큼 익숙해졌다는 뜻일까."

    show yuna smile at left, tiny_bounce with dissolve
    yn "내일도 올 거죠?"

    hr "상황 되면."
    sa "나는 갈 수 있어."
    ge "난 또 중간에 구경하러 올게."

    "그리고 유나는 마지막으로 내 쪽을 봤다."

    yn "선배는?"

    sj "왜 마지막 확인은 항상 나냐."

    yn "제일 대답 늦게 할 것 같아서."

    sj "……아마."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋아."
    yn "그 '아마'도 이제 해석할 수 있어요."

    sj "뭘 어떻게."

    yn "거의 온다는 뜻."

    "너무 자신만만하게 말해서,"
    "반박하려다 말았다."
    "솔직히 틀리지도 않았다."

    scene black with dissolve
    centered "{size=30}복도{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.5

    "준비실 문을 닫고 복도로 나오자,"
    "점심시간 끝 특유의 분주함이 우리를 한꺼번에 감쌌다."
    "서둘러 교실로 돌아가는 학생들 틈에서 우리는 잠깐 나란히 섰다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "오늘도 성공."
    hr "성공의 기준이 너무 낮아."
    yn "낮은 행복이 오래 가는 법이에요."
    sa "그건 맞아."

    sj "오늘 설아 말이 제일 많이 남는 날이네."

    sa "왜."

    sj "그냥."
    sj "은근 잘 꽂히는 말을 하잖아."

    "설아는 아주 잠깐 눈을 깜빡였다."
    "당황한 건지 아닌지 잘 모르겠는 표정."
    "하지만 아주 미세하게, 입꼬리가 올라갔다."

    show seola smile at right, tiny_bounce with dissolve
    sa "……그럼 다행."

    "그 짧은 변화 하나에,"
    "유나는 바로 만족한 얼굴을 했고,"
    "하린이도 뭔가 말할 듯하다가 그냥 작게 웃었다."

    th "정말 조금씩이지만."
    th "우리는 어제보다 오늘 더 편하다."

    play sound "audio/sfx_school_bell.ogg"

    "본종이 울렸다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "가자."
    yn "네에."
    sa "응."

    "우리는 각자 교실 쪽으로 흩어졌다."
    "멀어지는 와중에도 유나는 뒤돌아 손을 흔들었고,"
    "하린이는 그런 유나를 보며 어이없다는 듯 고개를 저었고,"
    "설아는 말없이 한 번 손을 들어 보였다."

    "나는 그 모습을 잠깐 바라보다가 걸음을 옮겼다."

    th "딱 20분."
    th "정말 짧은 시간이었는데."

    th "이상하게도."
    th "오늘 하루 전체보다,"
    th "그 20분이 더 선명하게 남을 것 같은 기분이 들었다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 20 타이틀]

    scene black with fade
    centered "{size=40}Scene 20{/size}\n\n{size=30}같이 만들면 빨라지는 것들{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "오후 수업은 평소보다 조금 더 빨리 지나간 기분이었다."
    "물론 실제로 빨랐을 리는 없고,"
    "아마 점심시간에 잠깐 다녀온 준비실이 자꾸 머릿속에 남아 있었기 때문일 거다."

    th "20분뿐이었는데."
    th "괜히 하루 중간에 이어지는 비밀 공간 같은 느낌이었지."

    "종이 울리자마자 교실 안이 와르르 풀어졌다."
    "어제와 비슷한 장면인데, 이상하게 오늘은 더 익숙했다."
    "누군가 날 먼저 부르지 않아도, 자연스럽게 가야 할 방향이 정해져 있는 느낌."

    "휴대폰이 진동했다."

    "유나 : 방과 후 2차 출석 체크!"
    "유나 : 조용한 봄 준비실 집합"
    "유나 : 지각자는 벌칙 있음"

    sj "벌칙은 또 뭐냐…"

    "나는 작게 중얼거리며 가방을 들었다."
    "화면을 내리자 바로 다음 메시지가 올라왔다."

    "하린 : 벌칙 같은 건 없어."
    "설아 : 유나가 방금 만든 거."
    "가은 : 난 오늘도 중간에 들를 예정"

    th "이 단체방도 점점 빠르게 굴러가네."

    scene black with dissolve
    centered "{size=30}준비실{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "준비실 문을 열자, 오늘은 어제보다도 더 먼저 와 있는 사람이 있었다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve

    "유나는 이미 의자에 반쯤 걸터앉아 네임펜을 돌리고 있었고,"
    "하린이는 핀보드 앞에 서서 어제 붙인 장식 위치를 다시 보고 있었다."

    sj "이번엔 안 늦었네."

    show yuna grin at left, idle_bounce with dissolve
    yn "흥."
    yn "저도 하면 합니다."

    hr "방금 온 지 30초도 안 됐어."

    show yuna pout at left, sway_soft with dissolve
    yn "하린아."
    yn "사람의 체면이라는 게 있거든."

    sj "반장이 제일 정확하네."

    "유나는 못마땅한 척했지만 금방 웃음을 터뜨렸다."
    "그때 복도 쪽에서 조심스러운 발소리가 들렸고,"
    "설아가 문틈으로 들어왔다."

    show seola normal at right, sway_soft with dissolve

    sa "다 왔네."

    yn "설아 선배!"
    yn "오늘도 정시네요."

    sa "유나도 오늘은 늦지 않았어."

    yn "와."
    yn "왠지 칭찬받은 기분."

    sj "기준 낮네."

    scene bg old_library with dissolve

    "준비실 안 공기는 하루 전보다 조금 더 편안했다."
    "문을 열자마자 느껴지는 낯섦이 거의 없었다."
    "풀 냄새, 색지 냄새, 햇빛이 기울어진 창문, 핀보드 앞에 대충 모여 있는 의자들."
    "이제는 이런 것들이 전부 '준비실'이라기보다 그냥 우리 쪽 풍경처럼 느껴졌다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "오늘은 가격표 마저 하고, 장식 끈 길이 맞추고, 부스 설명 문구 초안도 잡아 보자."

    show yuna smile at left, tiny_bounce with dissolve
    yn "문구!"
    yn "좋아, 이건 제가 활약할 타이밍이네요."

    sj "벌써 불안한데."

    sa "조금."

    yn "너무해."

    "유나는 억울한 표정을 지었지만,"
    "네임펜을 손에 쥔 얼굴은 이상하게도 진지했다."
    "정작 저런 애가 사소한 문구 하나에도 의외로 오래 고민한다는 걸 이제는 조금 알 것 같았다."

    th "사소한 것도 중요하게 생각하는 타입."
    th "설아 말이 맞았네."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "일단 부스 소개는 너무 과하면 안 돼."
    hr "짧고 깔끔하게."

    show yuna normal at left, sway_soft with dissolve
    yn "음…"
    yn "'작고 조용한 봄의 기록'?"
    yn "아니면 '잠깐 머물고 싶은 곳'?"

    sj "왜 벌써 시집 제목 같은데."

    show seola normal at right, sway_soft with dissolve
    sa "두 번째는 괜찮아."

    hr "응."
    hr "조금 손보면 쓸 수 있을 것 같아."

    "유나는 생각보다 긍정적인 반응이 돌아오자 바로 눈을 빛냈다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "봤죠!"
    yn "저도 감성 할 수 있어요!"

    sj "아무도 못 한다고는 안 했는데."

    yn "선배는 표정이 그랬어요."

    sj "내 표정 해석 그만해."

    "설아가 아주 작게 웃었다."
    "이제는 그런 짧은 웃음도 점점 익숙해지고 있었다."

    scene bg old_library with dissolve

    "우리는 책상 위에 가격표 종이를 펼쳐 놓고 글씨체를 맞춰 보기 시작했다."
    "하린이는 최대한 일정한 간격으로 단어를 배치했고,"
    "유나는 한 글자라도 밋밋하면 작은 장식을 붙이고 싶어 했고,"
    "설아는 둘의 중간에서 '여긴 괜찮고, 여긴 과하다'를 조용히 골라 냈다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "글씨 크기 통일해야 해."

    show yuna pout at left, sway_soft with dissolve
    yn "근데 조금 튀는 게 더 귀엽지 않아요?"

    sa "하나만 튀면 돼."
    sa "전부 튀면 눈이 피곤해."

    yn "…그건 인정."

    sj "오늘도 미감 탐지기 열일하네."

    "내가 무심코 그렇게 말하자,"
    "설아는 잠깐 손을 멈췄다."
    "그리곤 아주 살짝 시선을 내 쪽으로 돌렸다."

    show seola smile at right, tiny_bounce with dissolve
    sa "그 별명."
    sa "이제 진짜 굳어졌네."

    sj "싫냐."

    sa "아니."
    sa "나쁘지 않아."

    "유나는 그 말을 듣자마자 바로 끼어들었다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아!"
    yn "그럼 공식 인정입니다."

    hr "뭘 자꾸 공식 인정해."

    yn "중요하거든요."
    yn "별명도 팀 문화예요."

    sj "너는 진짜 뭐든 문화로 만든다."

    yn "좋죠?"
    sj "솔직히 조금."

    "내가 대수롭지 않게 대답하자,"
    "유나는 아주 만족스러운 표정을 지었다."

    th "저 표정."
    th "처음엔 너무 과한가 싶었는데."
    th "이제는 저런 식으로 기분 좋아하는 게 꽤 익숙하다."

    scene bg old_library with dissolve

    "가격표 두 장이 완성될 즈음,"
    "유나는 갑자기 종이 귀퉁이에 아주 작은 꽃 그림을 그리고 싶다고 주장했다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "진짜 조그맣게만요."
    yn "이 정도면 안 과해요."

    hr "음…"

    "하린이는 고민했고,"
    "설아는 그림이 그려질 빈자리를 한 번 봤고,"
    "나는 괜히 팔짱을 낀 채 지켜봤다."

    sa "하나만."
    sa "오른쪽 아래."

    hr "선 얇게."
    yn "좋아!"
    sj "결국 통과네."

    "유나는 금세 신이 나서 아주 작은 꽃 하나를 그렸다."
    "과하지도, 밋밋하지도 않게."
    "그리고 완성된 종이를 들고 혼자 만족스러운 표정을 지었다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "후후."
    yn "이런 걸 디테일의 승리라고 하는 거예요."

    sj "본인 입으로 말하네."
    hr "근데…"
    hr "생각보다 괜찮긴 하다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "진짜요?"
    hr "응."
    sa "예뻐."

    "유나는 순간 네임펜을 든 채 그대로 굳었다."
    "정말 예상 못 한 칭찬을 한 번에 받아 버린 얼굴이었다."

    yn "……잠깐만."
    yn "지금 둘 다 칭찬했어요."
    yn "저 오늘 좀 성공한 사람 같아."

    sj "꽃 하나 그려 놓고?"

    show yuna grin at left, idle_bounce with dissolve
    yn "네."
    yn "성공은 작고 소중한 데서 오는 겁니다."

    scene bg old_library with dissolve

    "이제는 누구도 그 말을 비웃지 않았다."
    "작고 소중한 것들."
    "장식 하나, 글씨 하나, 20분 모임, 단체방 프로필 사진."
    "이 며칠 사이 우리 사이를 붙들어 준 건, 어쩌면 늘 그런 것들이었으니까."

    th "정말 이상하지."
    th "큰 사건은 하나도 없는데."
    th "자꾸 여기로 오게 된다."

    "그 순간 문이 가볍게 열렸다."

    show gaeun smile at far_right, tiny_bounce with dissolve

    ge "실례."
    ge "오늘도 성실한 조용한 봄 여러분."

    yn "가은 선배!"
    yn "오늘도 타이밍 완벽하다."

    ge "그래?"
    ge "일부러 그런 건 아니고, 그냥 너희가 생각나서."

    "가은 선배는 아주 당연한 얼굴로 그렇게 말했다."
    "별거 아닌 말인데 묘하게 자연스러웠다."
    "이제는 선배도 이 공간에 들어오는 게 어색하지 않은 모양이었다."

    sj "이쯤 되면 선배도 멤버 아닌가요."
    ge "오."
    ge "정식 영입 제안?"
    yn "찬성!"
    sa "나도."
    hr "반대할 이유는 없고."

    "가은 선배는 우리를 한 번 둘러보더니 어이없다는 듯 웃었다."

    ge "뭐야."
    ge "너희 벌써 그렇게 친해졌어?"

    sj "저도 가끔 따라가기 벅찰 때 있어요."

    ge "좋네."
    ge "빠른 팀워크."

    "가은 선배는 책상 위 완성된 가격표를 집어 들고 훑어봤다."
    "그리고 작은 꽃 그림을 보더니 바로 말했다."

    ge "이거 유나지?"
    yn "티 나요?!"
    ge "응."
    ge "근데 딱 좋아."
    ge "있는 쪽이 훨씬 너희 같다."

    "유나는 또 한 번 기분 좋아하는 얼굴을 했다."
    "하린이는 그걸 보고 작게 한숨을 쉬면서도 말리진 않았고,"
    "설아는 조용히 완성된 종이를 다시 보았다."

    scene bg old_library with dissolve

    "가은 선배까지 합류하자 준비실 안은 더 북적였지만,"
    "신기하게도 산만하진 않았다."
    "누군가 떠들면 누군가가 정리해 주고,"
    "누군가 제안하면 다른 누군가가 다듬고,"
    "쓸데없는 말과 필요한 말이 이상할 만큼 자연스럽게 섞였다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    show gaeun smile at far_right, tiny_bounce with dissolve

    ge "근데 너희."
    ge "이쯤 되면 누가 제일 손 빠른지도 나와야 되는 거 아냐?"

    sj "갑자기 순위전입니까."

    ge "재밌잖아."
    ge "작업 속도 대결."

    yn "오!"
    yn "좋다!"

    hr "쓸데없어."

    ge "쓸데없는 게 제일 재밌는 법이지."

    "결국 반대한 사람은 하린이뿐이었고,"
    "그 하린이도 완전히 싫어 보이진 않았다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아, 그럼 종이 별 다섯 개 접기!"
    yn "누가 제일 빠른지 보는 거예요."

    sj "왜 하필 별이냐."

    yn "예쁘니까."

    sa "이유가 단순해."

    hr "기준도 없잖아."

    ge "그럼 내가 심판할게."
    ge "빠르고, 예쁘고, 덜 구겨진 사람 우승."

    sj "조건 세 개면 이미 복합 평가네."

    "유나는 벌써 색종이를 나눠 주고 있었다."
    "하린이는 이게 왜 이렇게 된 거냐는 표정으로도 결국 종이를 받았고,"
    "설아는 잠깐 보고 있다가 조용히 한 장 집어 들었고,"
    "나도 마지못한 척 받았다."

    scene bg old_library with dissolve

    "결과부터 말하자면,"
    "나는 두 번째로 빨랐고,"
    "유나는 제일 시끄러웠고,"
    "하린이는 가장 반듯했고,"
    "설아는 제일 깔끔했고,"
    "가은 선배는 심판인데도 중간에 끼어들어 하나 접었다."

    show yuna surprise at left, excited_hop with dissolve
    yn "잠깐만!"
    yn "왜 선배가 제일 예쁘게 접어요!"

    ge "경험치 차이?"

    hr "이건 반칙인데."

    sa "조용히 강해."

    sj "심판이 참가한 시점에서 이미 공정성은 끝났네요."

    "준비실 안에 웃음이 한 번 크게 번졌다."
    "유나는 자기 별을 들고 억울해했고,"
    "하린이는 반듯한 모서리를 다시 펴며 괜히 진지해졌고,"
    "설아는 완성된 별 다섯 개를 나란히 놓고 비교하다가 작게 웃었고,"
    "가은 선배는 그런 우리를 보며 너무 재밌다는 얼굴을 했다."

    show yuna pout at left, sway_soft with dissolve
    yn "다시 해요."
    yn "이번엔 선배 빠지고."

    ge "어라, 나 배제당했네."
    sj "공정성 회복을 위해 필요합니다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "그건 맞아."

    "하린이가 그렇게 단정하듯 말하자,"
    "또 한 번 웃음이 났다."

    th "정말 별거 아닌데."
    th "왜 이렇게 잘 웃게 되지."

    scene bg old_library with dissolve

    "두 번째 대결은 조금 더 진지했다."
    "유나는 혀까지 내밀고 집중했고,"
    "하린이는 모서리를 정확히 맞추는 데 집착했고,"
    "설아는 조용히 손끝만 움직였고,"
    "나는 어쩌다 보니 진짜 이기고 싶어져 있었다."

    "결과는 설아 승."

    show yuna surprise at left, excited_hop with dissolve
    yn "우와."
    yn "설아 선배 손 진짜 예뻐요."
    yn "아니, 손이 예쁜 게 아니라 접는 게 예쁜 건가."
    sj "둘 다 칭찬이긴 하네."

    show seola surprise at right, excited_hop with dissolve
    sa "……별 하나 접은 걸로 너무 과한데."

    ge "아니, 진짜 잘했어."
    hr "응."
    hr "모양 제일 일정해."

    "설아는 잠깐 말이 없었다."
    "그러더니 완성된 별을 가볍게 손끝으로 굴리며 아주 작게 말했다."

    show seola smile at right, tiny_bounce with dissolve
    sa "그럼."
    sa "오늘은 내가 이긴 걸로."

    "그 말투가 너무 담백해서,"
    "오히려 다 같이 웃어 버렸다."
    "유나는 바로 고개를 숙였다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "인정합니다, 챔피언."

    scene bg old_library with dissolve

    "별 다섯 개는 결국 버려지지 않았다."
    "유나가 '이렇게 된 거 장식으로 쓰자'고 우겼고,"
    "의외로 다들 반대하지 않았다."
    "하린이는 '정말 조그맣게만'이라는 조건을 붙였고,"
    "설아는 '창문 쪽 끈에 달면 괜찮다'고 했고,"
    "가은 선배는 '오늘 대결의 흔적이네'라며 웃었다."

    "우리는 결국 접은 별을 가는 실에 하나씩 묶어 창가 쪽에 매달았다."
    "아주 작은 장식이라 바람이 불 때마다 조금씩 흔들렸다."
    "노을이 비칠 땐 빛을 받아 반짝거릴 것 같았다."

    th "이제 진짜."
    th "준비실이 점점 준비실 같지 않아지고 있다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋다."

    "유나가 아주 작게 말했다."
    "평소처럼 호들갑도 아니고, 장난도 아니었다."
    "그저 눈앞 풍경이 마음에 드는 사람 같은 목소리."

    hr "응."
    hr "생각보다."

    sa "조금씩 채워지는 게 보여."

    ge "너희 취향 다 섞여 있어서 더 예쁜가 보다."

    "나는 창가에 달린 작은 별들을 잠깐 올려다봤다."
    "형태는 조금씩 다르고, 색도 크기도 미세하게 달랐다."
    "그런데 이상하게 한 줄에 같이 있으니 어색하지 않았다."

    th "꼭 누구 닮았네."

    scene bg old_library with dissolve

    "작업이 어느 정도 마무리되자,"
    "유나는 또 단체방에 사진을 올리기 시작했다."
    "가격표 사진 한 장."
    "창가에 달린 별 장식 사진 한 장."
    "그리고 준비실 책상 위에 널린 색지와 펜 사진 한 장."

    "유나 : 오늘의 성과!"
    "유나 : 별 챔피언은 설아 선배"
    "유나 : 근데 다들 잘했음"

    sj "왜 보고서가 실시간이냐."

    show yuna grin at left, idle_bounce with dissolve
    yn "기록은 중요하니까요."

    hr "근데…"
    hr "나중에 보면 재밌긴 하겠다."

    sa "응."
    ge "이래서 남기는 거지."

    "하린이까지 그렇게 말하자,"
    "유나는 뿌듯한 얼굴로 휴대폰을 흔들었다."

    scene bg old_library with dissolve

    "어느새 창밖 햇빛은 더 기울어 있었다."
    "준비실 안도 노을빛이 조금씩 번지고 있었다."
    "책상 가장자리와 핀보드 모서리가 주황빛으로 물들고,"
    "창가에 매단 별들이 아주 작게 반짝였다."

    "그 순간."
    "정말 별일도 아닌 지금 이 풍경이,"
    "이상할 만큼 오래 기억에 남을 것 같은 예감이 들었다."

    th "왜지."
    th "이렇게 사소한 장면인데."

    th "다 같이 웃고,"
    th "별 하나 접고,"
    th "장식 하나 거는 것뿐인데."

    th "그런데도."
    th "이런 시간이 자꾸 쌓이면,"
    th "정말로 뭔가가 되어 버릴지도 모르겠다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋아!"
    yn "그럼 오늘도 성공!"

    sj "너는 맨날 성공이네."

    yn "네."
    yn "왜냐면 오늘도 재밌었거든요."

    "아주 간단한 대답이었다."
    "그런데 준비실 안에 있는 누구도 그 말에 토를 달지 않았다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "…맞아."
    sa "응."
    ge "인정."

    "결국 나도 피식 웃었다."

    sj "그래."
    sj "오늘도 성공."

    "유나는 그 한마디를 듣자마자 활짝 웃었다."
    "정말 별말도 아닌데."
    "마치 기다렸던 답이라도 들은 것처럼."

    scene black with fade

    "학교 안 어딘가의 낡은 준비실."
    "가위와 테이프와 색지, 그리고 쓸데없는 내기와 장난."
    "처음엔 그냥 축제 준비 공간일 뿐이었는데."

    "이제는 조금씩,"
    "그 안에서 같이 웃고 있는 사람들이 먼저 떠오른다."

    th "아직 특별한 일은 없다."
    th "정말, 하나도."

    th "하지만."
    th "이런 평범한 날들이야말로,"
    th "나중에 가장 먼저 떠오를지도 모른다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 21 타이틀]

    scene black with fade
    centered "{size=40}Scene 21{/size}\n\n{size=30}조금만 더 같이{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    "작업이 끝났는데도, 이상하게 아무도 바로 가방을 들지 않았다."
    "언제나처럼 '이제 슬슬 가야지' 하는 분위기는 되었는데,"
    "정작 먼저 문 쪽으로 향하는 사람은 없었다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    show seola normal at right, sway_soft with dissolve
    show gaeun smile at far_right, tiny_bounce with dissolve

    yn "음."
    yn "오늘은 뭔가."
    yn "이대로 가면 아쉽지 않아요?"

    sj "또 시작이네."

    ge "근데 조금 이해돼."
    ge "오늘 작업 텐션 좋았잖아."

    hr "그래도 너무 늦어지면 안 돼."

    yn "알아요, 알아요."
    yn "그러니까 멀리는 아니고…"
    yn "정말 잠깐만!"

    sa "잠깐의 기준이 유나한테 제일 불안한데."

    yn "설아 선배."
    yn "절 너무 못 믿으시는 거 아니에요?"

    sa "조금."

    "설아가 아무렇지 않게 그렇게 말하자,"
    "유나는 또 진심으로 충격받은 척했다."
    "이제는 그 반응도 거의 익숙한 코미디처럼 느껴졌다."

    show yuna pout at left, sway_soft with dissolve
    yn "너무하네…"
    sj "근데 다들 같은 생각일걸."

    yn "와."
    yn "지금 팀 단합으로 저를 공격하네요."

    hr "공격까진 아니고."
    hr "예측 가능하다는 뜻."

    "하린이까지 그렇게 정리하자,"
    "결국 준비실 안이 한 번 더 웃음으로 무너졌다."

    th "이제는 이런 흐름이 정말 자연스럽다."
    th "누가 시작하면, 누군가 이어받고, 나머지가 받아친다."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "좋아."
    ge "그럼 학교 앞 자판기까지만?"
    ge "그 정도면 잠깐 맞지."

    yn "오, 찬성!"
    sa "그건 괜찮아."
    hr "자판기면… 뭐."

    "셋이 너무 빨리 넘어가 버리자,"
    "시선이 또 자연스럽게 내게 몰렸다."

    sj "왜 마지막은 항상 나냐."

    show yuna grin at left, idle_bounce with dissolve
    yn "클로징 멘트 담당이니까."

    sj "언제 그런 직책이 생겼어."

    yn "방금."

    scene black with dissolve
    centered "{size=30}학교 뒤편 복도{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.5

    "우리는 준비실 불을 끄고 복도로 나왔다."
    "방과 후의 학교는 점점 조용해지고 있었지만,"
    "아직 완전히 텅 빈 시간은 아니었다."
    "어딘가에서 청소 도구 끄는 소리가 들렸고,"
    "멀리 운동장 쪽에선 마지막까지 남아 있는 동아리 애들 목소리가 바람처럼 흘러왔다."

    "다섯이 같이 복도를 걷는 모습도 이제는 조금 익숙했다."
    "누가 앞서고 누가 뒤처지는지도 묘하게 일정했다."
    "유나는 늘 반 발짝쯤 앞서 있고,"
    "하린이는 그걸 눈으로 좇으며 속도를 맞추고,"
    "설아는 옆에서 조용히 따라오고,"
    "가은 선배는 뒤에서 느긋하게 흐름을 보고,"
    "나는 그 사이 어딘가에 섞인다."

    th "처음엔 어색했는데."
    th "이제는 그냥 이게 자연스럽다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    hide gaeun

    yn "근데요."
    yn "우리 다 같이 있을 때랑 둘셋씩 있을 때 느낌 되게 다른 거 알아요?"

    sj "갑자기 분위기 분석이냐."

    yn "중요하거든요."
    yn "예를 들면 다 같이 있으면 되게 북적북적한데,"
    yn "또 이상하게 둘씩 말할 때는 조용해져요."

    sa "맞아."
    sa "근데 어색하진 않고."

    hr "……그건 좀 알 것 같아."

    "하린이는 그렇게 말하며 창문 밖을 잠깐 봤다."
    "노을빛이 복도 유리에 옅게 번져 있었다."

    ge "그게 편해졌다는 거지."
    ge "사람 수 바뀌어도 분위기가 안 깨지는 거."

    sj "선배는 꼭 그런 걸 되게 쉽게 말하네요."

    ge "관찰자라서."

    show yuna laugh at left, idle_bounce with dissolve
    yn "와, 멋있다."
    yn "저도 그런 어른 되고 싶어요."

    sj "갑자기 어른이래."
    ge "난 아직 학생인데?"
    yn "그래도 선배는 어른 같단 말이에요."

    "가은 선배는 그냥 웃기만 했다."
    "부정도 긍정도 안 하는 저 표정도 이제는 조금 알 것 같았다."

    scene bg school_road_dusk with fade
    play music "audio/bgm_daily_light.ogg" fadein 1.5

    "학교 뒤편 자판기까지 오는 길은 정문 쪽보다 한산했다."
    "운동장 옆으로 난 좁은 길을 따라 몇 걸음만 더 가면,"
    "오래된 벤치 두 개와 자판기 세 대가 나란히 서 있는 작은 공간이 나왔다."

    "늦은 햇빛이 자판기 유리에 반사되어 반짝거렸다."
    "이 시간대 학교 뒤편은 묘하게 조용하고, 또 느긋했다."
    "유나는 자판기를 보자마자 괜히 들뜬 얼굴이 됐다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "오늘의 취향 조사 갑니다."

    sj "또 무슨 조사냐."

    yn "자판기 음료 취향!"
    yn "이건 사람을 파악하는 데 아주 중요해요."

    hr "너 기준에선 다 중요하잖아."

    sa "그래도 재밌긴 해."

    "설아가 그렇게 말하자 유나는 곧바로 활짝 웃었다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "역시 설아 선배!"
    yn "그럼 선배부터."

    sa "왜 나부터."

    yn "왠지 제일 의외일 것 같아서."

    "설아는 자판기 칸을 잠깐 훑어봤다."
    "그리고 아주 망설임 없이 버튼 하나를 눌렀다."
    "툭, 하고 떨어진 건 레몬 탄산수였다."

    sj "의외로 깔끔하네."

    sa "의외였어?"
    sj "조금."

    sa "왜."

    sj "왠지 달달한 거 안 고를 것 같긴 했는데."
    sj "그래도 탄산수는 더 담백해서."

    sa "그냥."
    sa "끝맛이 안 남아서 좋아."

    "그 말은 설아답다고 생각했다."
    "군더더기 없는 선택."
    "하지만 유나는 또 이상한 데서 감탄하고 있었다."

    yn "끝맛이 안 남아서 좋다…"
    yn "와, 말이 되게 설아 선배 같아요."

    sa "그게 무슨 뜻인데."

    yn "설명은 못 하겠는데 아무튼요."

    scene bg school_road_dusk with dissolve

    show harin normal at center_lower, sway_soft with dissolve

    "다음은 하린이 차례였다."
    "하린이는 한참 고민할 것 같더니 의외로 바로 버튼을 눌렀다."
    "나온 건 캔커피였다."

    show yuna surprise at left, excited_hop with dissolve
    yn "어?"
    yn "하린이 커피 마셔?"

    hr "가끔."
    hr "오늘은 조금 피곤해서."

    sj "은근 어른 취향이네."

    hr "그런 말 들으면 좀 이상한데."

    ge "근데 잘 어울려."
    ge "반장은 캔커피 쪽 이미지 있어."

    yn "맞아!"
    yn "왠지 정리 다 끝내고 혼자 창문 보면서 마실 것 같아."

    sj "그 상상은 좀 웃긴데."

    "하린이는 어이없다는 듯 나와 유나를 번갈아 봤다."
    "그런데 완전히 부정하진 않았다."
    "오히려 괜히 캔을 한 번 더 만지작거렸다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "…뭐."
    hr "가끔은 맞을지도."

    show yuna grin at left, idle_bounce with dissolve
    yn "우와."
    yn "인정했어."

    scene bg school_road_dusk with dissolve

    "유나는 말할 것도 없었다."
    "자판기 앞에 서자마자 주저 없이 딸기우유 버튼을 눌렀다."
    "심지어 누르기 전부터 결과를 다 알고 있는 사람 얼굴이었다."

    sj "예상 적중."

    show yuna laugh at left, idle_bounce with dissolve
    yn "이건 예상이 아니라 확신이죠."

    sa "이젠 놀랍지도 않아."

    hr "일관적이라 좋네."

    yn "좋은 거죠?"
    sj "적어도 이해는 쉽다."

    "유나는 자판기에서 나온 딸기우유 팩을 두 손으로 받아 들고,"
    "세상에서 제일 만족스러운 표정을 지었다."
    "진짜 저런 작은 걸로 저렇게 기분 좋아할 수 있다는 게,"
    "조금 부럽다고 생각했다."

    th "쟤는 좋아하는 걸 좋아한다고 숨기질 않는다."
    th "그래서 더 보기 편한 걸지도."

    scene bg school_road_dusk with dissolve

    show gaeun smile at far_right, tiny_bounce with dissolve

    ge "그럼 난…"

    "가은 선배는 잠시 고민하더니,"
    "사과주스를 골랐다."

    yn "오."
    yn "선배는 뭔가 탄산일 줄 알았어요."

    ge "왜?"
    yn "그냥 이미지가요."
    sj "저도 약간 그 생각했는데."

    ge "너희 나를 너무 화려하게 보는 거 아냐?"
    ge "의외로 무난한 것도 좋아해."

    sa "사과주스면 충분히 무난하네."

    hr "근데 잘 어울려."

    "가은 선배는 웃으며 빨대를 꽂았다."

    ge "좋아."
    ge "그럼 남은 건 서진."

    "나는 자판기 앞에 섰다."
    "대충 아무거나 고르면 될 것 같은데,"
    "이상하게 네 사람의 시선이 느껴져서 괜히 조금 신경 쓰였다."

    sj "왜 다들 집중하냐."

    show yuna grin at left, idle_bounce with dissolve
    yn "중요하니까."

    sj "네 기준에선 진짜 다 중요하네."

    "나는 잠깐 고민하다, 결국 포도 음료를 눌렀다."
    "캔이 아래로 굴러 떨어지는 소리가 작게 울렸다."

    show yuna surprise at left, excited_hop with dissolve
    yn "오."
    yn "포도?"

    hr "의외다."

    sa "조금."

    sj "그렇게 의외냐."

    ge "아니, 뭔가 깔끔한 거 고를 줄 알았어."

    sj "그냥 당겼는데."

    "유나는 포도 캔을 보더니 괜히 고개를 끄덕였다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "아니."
    yn "근데 이것도 선배 같아."

    sj "또 해석 시작이네."

    yn "뭔가요…"
    yn "겉보기엔 무난해 보이는데,"
    yn "은근 자기 취향 확실한 느낌?"

    sj "포도 음료 하나로 너무 멀리 갔다."

    sa "근데 아주 틀린 말은 아닌 것 같아."

    "설아까지 덧붙이자,"
    "나는 반박할 타이밍을 그냥 놓쳐 버렸다."

    scene bg school_road_dusk with dissolve

    "결국 우리는 자판기 앞 벤치에 적당히 기대거나 걸터앉은 채 음료를 마셨다."
    "말 그대로 정말 잠깐일 뿐인 시간."
    "그런데 방과 후 준비실에서 이어진 분위기가 그대로 따라와서,"
    "이 짧은 시간조차 자연스럽게 하나의 장면처럼 이어졌다."

    show yuna normal at left, sway_soft with dissolve
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    show seola normal at right, sway_soft with dissolve
    show gaeun smile at far_right, tiny_bounce with dissolve

    yn "좋아."
    yn "그럼 이제 음료 취향이 나왔으니 다른 것도 해 봅시다."

    sj "아직 더 있냐."

    yn "당연하죠."
    yn "빵 취향, 아이스크림 취향, 계절 취향, 색 취향…"

    hr "너 오늘 집 안 갈 생각이야?"

    yn "갈 거예요!"
    yn "근데 이런 거 알면 재밌잖아요."

    ge "맞아."
    ge "의외로 오래 기억에 남아."

    sa "음."
    sa "난 겨울보다 봄."

    yn "오!"
    yn "좋아, 계절 취향부터."

    sj "진짜 시작하네."

    "유나는 자판기 앞에서 아주 자연스럽게 즉석 설문을 열었다."
    "누가 봐도 쓸데없는 대화였지만,"
    "이상하게 한 마디도 버릴 게 없었다."

    scene bg school_road_dusk with dissolve

    yn "전 당연히 봄."
    yn "딸기 시즌이니까."

    sj "결국 거기로 귀결되네."

    hr "나는 가을."
    hr "덥지도 춥지도 않아서 좋아."

    sa "난 봄."
    sa "바람이 적당해서."

    ge "오, 난 여름."
    yn "선배 진짜요?"
    ge "응."
    ge "해 긴 거 좋아하거든."

    "유나는 놀란 얼굴로 고개를 돌렸다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "선배는요?"

    sj "겨울."

    "대답이 나오자마자 네 사람 반응이 조금씩 갈렸다."
    "유나는 '역시?' 하는 얼굴,"
    "하린이는 '그럴 것 같긴 했다'는 얼굴,"
    "설아는 납득,"
    "가은 선배는 흥미롭다는 얼굴."

    show yuna grin at left, idle_bounce with dissolve
    yn "와."
    yn "되게 윤서진 선배 같아."

    sj "그 말 오늘만 몇 번째냐."

    hr "근데 진짜 그래."
    hr "조용한 걸 좋아할 것 같아."

    sa "그리고 사람 적은 계절."

    sj "그건 맞네."

    ge "오, 인정 빠르다."

    "가은 선배가 웃자,"
    "나도 괜히 따라 웃었다."

    th "이젠 부정하는 게 더 이상하긴 하다."

    scene bg school_road_dusk with dissolve

    "대화는 계속 이어졌다."

    "좋아하는 색."
    "싫어하는 채소."
    "빵 먹을 때 먼저 뜯는 부분."
    "편의점 가면 꼭 한 번 보는 코너."

    "유나는 전부 빠짐없이 리액션을 했고,"
    "하린이는 하나하나 대답하면서도 왜 이걸 말하고 있는지 모르겠다는 얼굴을 했고,"
    "설아는 짧지만 정확한 대답을 했고,"
    "가은 선배는 묘하게 다 맞장구를 잘 쳤다."

    "그렇게 쓸데없는 얘기만 한참 한 것 같은데,"
    "신기하게도 지루하지 않았다."

    th "이런 시간이 제일 이상하다."
    th "정말 의미 없어 보이는데."
    th "끝나고 나면 이상하게 많이 남는다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "아."
    yn "근데 왠지 알 것 같아요."

    sj "뭘."

    yn "왜 준비실이 좋아졌는지."

    "유나는 딸기우유 팩을 손에 든 채,"
    "자판기 위쪽 하늘을 잠깐 올려다봤다."
    "붉게 물든 빛이 천천히 엷어지고 있었다."

    yn "그냥."
    yn "거기 가면 다들 있잖아요."

    "아주 쉬운 말이었다."
    "정말로 특별한 표현도 아니고, 꾸민 말도 아니었다."
    "그런데 그 짧은 한 문장이,"
    "오늘 자판기 앞에서 나눈 모든 대화보다 더 오래 남았다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "……맞아."

    show seola smile at right, tiny_bounce with dissolve
    sa "응."

    ge "그게 제일 크지."

    "가은 선배는 별일 아니라는 듯 가볍게 말했지만,"
    "나머지 셋은 조금 다른 표정이었다."
    "유나는 자기 말이 뭐가 그렇게 대단한지도 모르는 얼굴이었고,"
    "하린이는 캔커피를 손끝으로 굴리며 작게 웃었고,"
    "설아는 레몬 탄산수 캔 표면에 맺힌 물방울을 가만히 내려다봤다."

    th "그냥 거기 가면 다들 있다."
    th "정말 단순한데."
    th "그래서 더 정확한 말일지도."

    scene bg school_road_dusk with dissolve

    "잠깐만 더 있다 가자는 말은 정말로 잠깐으로 끝났다."
    "음료를 반쯤 비우고 나자,"
    "하린이가 먼저 시간을 확인했고,"
    "가은 선배도 슬슬 가야겠다고 했고,"
    "설아도 조용히 일어섰다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "이제 진짜 가자."
    yn "네에."
    yn "오늘은 얌전히 해산."

    sj "오늘은, 이라니."

    sa "본인도 알아."

    "유나는 들킨 사람처럼 웃었다."

    scene bg school_road_dusk with dissolve

    "우리는 자판기에서 나와 다시 학교 밖 방향으로 천천히 걸었다."
    "조금 전보다 하늘빛은 옅어졌지만,"
    "아직 분위기가 가라앉을 정도는 아니었다."
    "오히려 길게 이어진 하루의 끝이 부드럽게 정리되는 느낌이었다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    hide gaeun

    yn "오늘 알게 된 거 정리할게요."
    sj "또 정리냐."

    yn "네."
    yn "설아 선배는 레몬 탄산수."
    yn "하린이는 캔커피."
    yn "가은 선배는 사과주스."
    yn "윤서진 선배는 포도."

    hr "왜 마지막만 이름을 풀네임으로 부르는데."

    yn "중요 인물이니까요."

    sj "전부 중요 인물 아니었냐."

    yn "다 중요하지만,"
    yn "선배는 반응 보는 맛이 있거든요."

    sa "그건 맞아."

    sj "설아까지."

    "설아는 대답 대신 아주 조금 웃었다."
    "이제는 그런 사소한 표정 변화도 어렵지 않게 읽혔다."

    scene bg school_gate with dissolve

    "교문 근처에 다다르자,"
    "역시나 자연스럽게 발걸음이 조금 느려졌다."
    "누군가 먼저 헤어지자는 말을 해야 끝날 흐름."
    "그런데 또 아무도 바로 입을 열지 않았다."

    th "며칠 전엔 빨리 끝나길 바랐을지도 모르는데."
    th "지금은 오히려 조금 늦춰지고 있다."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "내일도 준비실?"
    yn "당연하죠!"
    hr "상황 보고."
    sa "나는 갈 수 있어."
    sj "이젠 자동으로 잡히네."

    ge "좋네."
    ge "그런 분위기."

    "가은 선배는 손을 흔들며 먼저 갈림길 쪽으로 빠졌다."

    ge "그럼 다들 조심히."
    ge "내일 또 봐."

    yn "네에!"
    hr "들어가세요."
    sa "안녕."

    "선배가 멀어지고,"
    "이번엔 하린이가 버스 정류장 방향으로 한 걸음 나섰다."

    hr "나도 여기서 갈게."
    hr "내일 점심엔 너무 늦지 마."

    yn "반장님."
    yn "이제 완전 관리 담당 같아요."

    hr "원래 그랬어."

    sj "맞는 말이네."

    "하린이는 나와 설아, 유나를 한 번씩 보고 작게 웃었다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "그래도…"
    hr "내일 보면 좋겠다."

    "짧은 말인데,"
    "묘하게 하린이답지 않게 솔직해서,"
    "유나가 바로 눈을 반짝였다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "와."
    yn "하린이 방금 엄청 좋은 말 했어."

    hr "그렇게 거창한 건 아닌데."
    sa "그래도 좋았어."

    "결국 하린이는 조금 민망한 얼굴로 먼저 몸을 돌렸다."

    scene bg school_gate with dissolve
    hide harin

    "남은 건 셋."
    "하지만 어색하진 않았다."
    "오히려 이런 식으로 사람이 하나씩 빠져도,"
    "대화의 온도가 그대로 이어지는 게 신기했다."

    show yuna smile at left, tiny_bounce with dissolve
    show seola normal at right, sway_soft with dissolve

    sa "유나는 내일도 딸기우유 마실 거야?"

    show yuna grin at left, idle_bounce with dissolve
    yn "아마도요."
    yn "이미 제 이미지가 그렇게 굳은 것 같긴 하지만."

    sj "네가 직접 굳혔잖아."

    sa "근데 어울려."

    "유나는 그 말에 또 만족한 얼굴로 웃었다."

    scene bg school_road_dusk with dissolve

    "곧 설아와도 갈림길이 가까워졌다."
    "설아는 늘 그랬듯 짧게 인사하고 갈 것 같았는데,"
    "오늘은 잠깐 멈춰 서서 우리 둘을 번갈아 봤다."

    show seola smile at right, tiny_bounce with dissolve
    sa "오늘 재밌었어."

    "짧고 담백한 한마디."
    "그런데 이상하게도 오늘 하루를 정리하는 데에는 그걸로 충분했다."

    yn "저도요."
    sj "나도."

    "설아는 고개를 한 번 작게 끄덕였다."

    sa "그럼 내일."

    "그리고 조용히 자기 쪽 길로 걸어갔다."
    "유나는 그 뒷모습을 잠깐 바라보다가, 괜히 작게 중얼거렸다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "설아 선배는 진짜."
    yn "말 하나하나가 오래 남아요."

    sj "맞네."

    "내가 바로 동의하자,"
    "유나는 의외라는 얼굴로 나를 봤다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "선배도 그렇게 생각해요?"
    sj "다들 생각할걸."

    yn "그럼 우리 진짜 많이 친해진 건가."

    sj "왜 갑자기 결론이 그렇게 되는데."

    yn "왜냐면요."
    yn "예전 같았으면 몰랐을 것까지 자꾸 보이잖아요."

    "나는 잠깐 대꾸하지 못했다."
    "그 말이 이상하게 정확했기 때문이다."

    th "예전 같았으면 몰랐을 것들."
    th "좋아하는 음료, 계절, 말버릇, 웃는 타이밍."
    th "정말 사소한 건데."
    th "이제는 이상할 만큼 선명하다."

    scene bg school_road_dusk with dissolve

    "결국 남은 건 또 나와 유나 둘이었다."
    "이제는 이 상황도 낯설지 않았다."
    "같이 걷는 속도도, 중간중간 비는 침묵도."

    show yuna normal at left, sway_soft with dissolve

    yn "선배."
    sj "왜."

    yn "우리 진짜 좀 팀 같죠?"

    sj "조금이 아니라 꽤."

    "생각보다 빨리 대답이 튀어나왔다."
    "유나는 눈을 동그랗게 떴다가,"
    "곧장 환하게 웃었다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "우와."
    yn "지금 그거 엄청난 인정이에요."

    sj "그렇게까지?"

    yn "네."
    yn "윤서진 선배가 그런 말 하면 무게가 있거든요."

    sj "그럼 앞으로 조심해야겠네."

    yn "아뇨."
    yn "앞으로도 자주 해주세요."

    "유나는 아무렇지 않게 그렇게 말했다."
    "그 말이 이상하게 장난처럼만 들리진 않았다."

    scene bg school_road_dusk with dissolve

    "조금 더 걷자, 우리도 결국 갈라지는 길 앞에 섰다."
    "오늘도 여기까지였다."
    "그런데 이제는 이 헤어짐조차 묘하게 익숙한 루틴 같았다."

    show yuna smile at left, tiny_bounce with dissolve

    yn "그럼 내일 진짜 봐요."
    yn "읽씹 금지, 지각 금지, 빠지기 금지."

    sj "규칙 계속 늘어나네."

    yn "좋은 건 꽉 잡아야 하거든요."

    sj "그건 또 무슨 말이야."

    yn "그냥요."

    "유나는 웃으며 대답을 넘겼다."
    "그리고 익숙하게 손을 흔들었다."

    yn "잘 가요, 선배."

    sj "너도."

    "유나는 몇 걸음 먼저 가다가,"
    "갑자기 뒤돌아보더니 한마디를 더 던졌다."

    show yuna grin at left, idle_bounce with dissolve
    yn "아."
    yn "포도 음료, 진짜 의외였어요."

    sj "아직도 그 얘기냐."

    yn "네."
    yn "그래서 더 기억날 것 같아요."

    "그 말만 남기고,"
    "유나는 가볍게 달려가듯 자기 길로 멀어졌다."

    "나는 그 뒷모습을 잠깐 바라보다가,"
    "휴대폰을 꺼내 단체방을 확인했다."

    "유나 : 오늘 자판기 모임도 성공"
    "유나 : 음료 취향 정보 획득 완료"
    "유나 : 내일도 잘 부탁합니다 조용한 봄 ☺"

    "곧이어 하린의 답장이 올라왔고,"
    "설아도 짧게 '응'이라고 남겼고,"
    "가은 선배는 사과 이모지를 하나 보냈다."

    "나는 잠깐 망설이다가,"
    "결국 짧게 답장을 남겼다."

    "서진 : 포도는 놀랄 일이 아니거든"
    "서진 : 내일 보자"

    "메시지를 보내자마자,"
    "유나의 답장이 거의 동시에 튀어 올랐다."

    "유나 : ㅋㅋㅋㅋ"
    "유나 : 네 포도 선배"

    "…헛웃음이 났다."

    scene black with fade

    "오늘도 큰일은 없었다."
    "정말로 자판기에서 음료를 고르고,"
    "서로의 취향을 조금 더 알고,"
    "같이 걷다가 헤어진 것뿐이다."

    "그런데 이상하게도."
    "이런 사소한 장면 하나하나가,"
    "이제는 그냥 지나가는 시간이 아니라"
    "조금씩 모여 쌓이는 무언가처럼 느껴지기 시작했다."

    th "아직은 아무 일도 없다."
    th "그래서 좋다."

    th "지금은 그냥,"
    th "이렇게 계속."
    th "조금씩 더 익숙해지면 되는 거다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 22 타이틀]

    scene black with fade
    centered "{size=40}Scene 22{/size}\n\n{size=30}우리끼리만 아는 말{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "다음 날 점심시간이 다가오자,"
    "이제는 수업 끝 종이 울리기 전부터 이상하게 마음 한구석이 먼저 준비실 쪽으로 기울었다."

    th "겨우 며칠인데."
    th "사람은 생각보다 금방 익숙해지는구나."

    "앞줄 누군가가 의자를 끄는 소리와 함께 종이 울렸다."
    "교실 안이 금세 느슨해졌다."
    "나는 반쯤 습관처럼 휴대폰을 확인했다."

    "유나 : 오늘은 간식 있습니다"
    "유나 : 중요한 공지니까 빨리 와요"
    "유나 : 특히 포도 선배"

    sj "이젠 진짜 그걸로 부르네…"

    "곧바로 메시지가 이어졌다."

    "하린 : 이상한 별명 고정하지 마."
    "설아 : 이미 고정된 것 같은데."
    "가은 : 포도 선배 조금 웃기네"

    th "다들 너무 빨리 받아들이는 거 아니냐."

    "결국 나는 작게 헛웃음을 흘리며 자리에서 일어났다."
    "교실 문을 나서는 발걸음이 생각보다 자연스러웠다."

    scene black with dissolve
    centered "{size=30}준비실{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "준비실 문을 열자마자,"
    "평소보다 먼저 달큰한 냄새가 났다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    "유나는 책상 위 비닐봉지를 펴 두고 있었고,"
    "하린이는 이미 그 봉지 안 내용물을 보고 한숨 쉴 준비가 된 얼굴이었고,"
    "설아는 그 옆에 서서 아주 미세하게 웃고 있었다."

    sj "뭐냐."
    sj "냄새부터 수상한데."

    show yuna laugh at left, idle_bounce with dissolve
    yn "오늘의 간식 테마는 봄!"
    yn "벚꽃 모양 젤리랑 딸기크림 쿠키입니다!"

    sj "또 테마까지 붙였냐."

    hr "나도 아까 똑같은 말 했어."

    sa "근데 좀 귀엽긴 해."

    "설아가 그렇게 말하자,"
    "유나는 또 세상 다 얻은 표정이 됐다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "설아 선배가 귀엽다고 했다."
    sj "오늘도 그거 오래 우려먹겠네."

    yn "당연하죠."
    yn "좋은 말은 오래 가야 해요."

    "하린이는 봉지 안을 다시 들여다보더니,"
    "결국 포기한 듯 작은 숨을 내쉬었다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "알았어."
    hr "대신 부스 물품 위에 과자 부스러기 흘리면 안 돼."

    yn "네, 체크리스트 반장님."

    hr "그 별명도 언제까지 쓰는 거야."

    sa "이미 굳은 것 같아."

    sj "이 팀 별명 고정 속도 진짜 빠르다."

    scene bg old_library with dissolve

    "책상 위에는 오늘도 작업할 것들이 놓여 있었다."
    "가격표 초안."
    "장식용 끈."
    "어제 접어 둔 별들."
    "그리고 그 옆에 너무 당당하게 놓인 벚꽃 젤리 봉지."

    "정리된 것과 어수선한 것."
    "일과 장난."
    "이제는 그 둘이 함께 있어야 오히려 준비실답게 느껴졌다."

    th "이상하네."
    th "처음엔 그냥 어수선하다고만 생각했는데."

    show harin normal at center_lower, sway_soft with dissolve
    hr "오늘은 부스 설명 문구 마저 정하고,"
    hr "배치 다시 한 번 확인하고,"
    hr "장식 끈 길이 맞춰서 정리하면 될 것 같아."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋아."
    yn "작업 전에 당 충전부터."

    sj "순서가 왜 그러냐."

    yn "집중력 향상을 위해서요."

    sa "명분이 점점 그럴듯해져."

    "결국 우리는 작업 전에 벚꽃 젤리 봉지를 뜯었다."
    "젤리는 진짜로 벚꽃 모양이었고,"
    "쿠키는 지나치게 분홍색이었다."
    "하린이는 분명 안 먹겠다더니 가장 먼저 젤리 하나를 집었고,"
    "설아는 말없이 분홍 쿠키를 반으로 나눠 들었다."

    sj "하린 너 아까 한숨 쉬지 않았냐."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "별개야."
    hr "이건 이거고, 간식은 간식."

    show yuna grin at left, idle_bounce with dissolve
    yn "우와."
    yn "완전 명언."
    sa "적어 둘까."
    sj "왜 다 기록하려고 하냐."

    yn "이제 우리 팀엔 쌓인 문장들이 많거든요."

    th "쌓인 문장."
    th "그 표현도 묘하게 맞다."

    scene bg old_library with dissolve

    "준비실 안에는 어느새 작은 말들이 조금씩 쌓여 있었다."
    "'여기선 시간이 조금 빨라.'"
    "'좋은 건 꽉 잡아야 하거든요.'"
    "'그냥 거기 가면 다들 있잖아요.'"
    "별거 아닌데, 이상하게 자꾸 남는 말들."

    "그리고 그 사이에 포도 선배 같은 이상한 말도 섞여 있다."

    th "그건 좀 빼고 싶은데."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "좋아."
    yn "오늘은 문구를 진짜 정합시다."

    hr "응."
    hr "너무 길지 않게."

    sa "딱 봤을 때 편했으면 좋겠어."

    sj "결국 방향은 다 비슷하네."

    "우리는 책상 위에 종이를 펼쳐 놓고,"
    "각자 생각나는 문구를 하나씩 적어 보기로 했다."
    "유나는 당연히 제일 먼저 펜을 잡았고,"
    "하린이는 최대한 단정한 글씨로 짧게 적었고,"
    "설아는 잠깐 생각하다 천천히 적었다."
    "나도 대충 빈칸 하나를 차지했다."

    scene bg old_library with dissolve

    "잠시 뒤,"
    "네 장의 종이가 책상 위에 나란히 놓였다."

    show yuna normal at left, sway_soft with dissolve
    yn "전."
    yn "'잠깐 머물고 싶은 봄'."

    show harin normal at center_lower, sway_soft with dissolve
    hr "'작고 편한 기록 공간'."

    show seola normal at right, sway_soft with dissolve
    sa "'잠깐 쉬어가기 좋은 곳'."

    sj "'그냥 편하게 보고 가는 곳'."

    "잠깐 정적이 흘렀다."
    "그리고 그다음 순간, 유나가 먼저 웃음을 터뜨렸다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "와."
    yn "마지막 너무 윤서진 선배다."

    sj "또 그 소리냐."

    hr "근데 진짜 그래."

    sa "꾸미지 않은데."
    sa "제일 정확할 수도."

    "설아가 그렇게 말하자,"
    "나는 괜히 시선을 피했다."
    "별로 대단한 말을 쓴 것도 아닌데,"
    "셋이 진지하게 읽는 게 이상하게 민망했다."

    ge "오, 다 좋아 보이는데?"

    show gaeun smile at far_right, tiny_bounce with dissolve

    "언제 왔는지 모르게,"
    "가은 선배가 문가에 기대 우리 종이를 내려다보고 있었다."

    yn "가은 선배!"
    yn "지금 문구 심사 중이에요."

    ge "음."
    ge "개인적으로는 설아 거랑 서진 거 사이 어딘가가 좋다."
    ge "딱딱하지 않고, 또 너무 힘주지도 않고."

    hr "나도 그 생각 했어."

    sa "그럼 섞을까."

    sj "어떻게."

    sa "……"
    sa "'그냥 편하게 쉬어갈 수 있는 곳'."

    "그 말이 나오자,"
    "이상하게 아무도 바로 말을 잇지 않았다."
    "과한 것도 아니고, 밋밋한 것도 아니었다."
    "딱 지금 준비실 분위기랑 비슷했다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "응."
    hr "이걸로 가자."

    ge "채택."

    sj "내 문장이 조금 들어갔네."

    yn "축하합니다."
    yn "포도 선배 문구 당선."

    sj "그 호칭은 빼고 축하하면 안 되냐."

    scene bg old_library with dissolve

    "결국 부스 소개 문구는"
    "'그냥 편하게 쉬어갈 수 있는 곳'"
    "으로 정리됐다."

    "하린이는 그 문장을 가장 단정한 글씨로 다시 옮겨 적었고,"
    "유나는 그 옆에 아주 작은 벚꽃 두 장만 그려 넣었다."
    "설아는 위치가 과하지 않은지 확인했고,"
    "가은 선배는 멀찍이서 전체 균형을 봐 줬다."
    "나는 테이프를 잘라 하린이 옆에 조용히 놓았다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "이제 진짜 그럴듯하다."
    hr "응."
    sa "조금씩 완성돼 가네."
    ge "너희 취향이 다 들어간 느낌이야."

    th "다 들어간 느낌."
    th "확실히 그렇다."

    "문구 하나 정했을 뿐인데,"
    "묘하게 다 같이 만든 것 같은 기분이 들었다."
    "누구 하나만의 결과물이 아니라,"
    "조금씩 섞이고 다듬어져서 나온 말."

    th "준비실도, 우리도."
    th "요즘은 그런 식으로 모양 잡히는 것 같다."

    scene bg old_library with dissolve

    "문구 정리가 끝나자,"
    "유나는 갑자기 벚꽃 젤리 하나를 집어 들고 진지한 얼굴로 말했다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "그럼 오늘부터 새로운 내부 규칙 추가."

    sj "왜 자꾸 규칙이 늘어나."

    yn "준비실에서 좋은 말 나오면 저장."
    yn "이건 진짜 필요해요."

    hr "또?"
    sa "근데 조금 재밌을 것 같아."

    "설아가 동조하자,"
    "하린이도 완전히 반대하진 못했다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "정리만 잘하면."

    yn "좋아!"
    yn "그럼 이름은…"

    sj "설마 이것도 이름 붙이냐."

    show yuna laugh at left, idle_bounce with dissolve
    yn "당연하죠."
    yn "'조용한 봄 어록'!"

    sj "촌스러운데."
    ge "조금 웃기긴 해."

    sa "그래도 기억은 잘 날 것 같아."

    "결국 준비실 책상 맨 구석에 작은 메모지가 한 장 놓였다."
    "맨 위에는 정말로 유나 글씨로"
    "'조용한 봄 어록'"
    "이라고 적혀 있었다."

    "그 아래엔 지금까지 나온 문장들이 아주 짧게 적혔다."

    "여기선 시간이 조금 빨라."
    "그냥 거기 가면 다들 있잖아요."
    "좋은 건 꽉 잡아야 하거든요."
    "오늘도 성공."

    sj "마지막은 너무 유나 개인 슬로건 아니냐."

    show yuna smile at left, tiny_bounce with dissolve
    yn "중요하거든요."
    hr "그건 인정."
    sa "응."

    sj "왜 셋 다 그건 바로 인정해."

    scene bg old_library with dissolve

    "점심시간 20분은 역시 빨랐다."
    "아무리 짧다고 생각해도,"
    "준비실 안으로 들어오면 더 빨리 흘렀다."

    "간식 한 봉지 뜯고,"
    "문구 하나 정하고,"
    "별명 하나 더 굳히고,"
    "이상한 규칙 하나 추가했을 뿐인데,"
    "벌써 절반이 넘었다."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "너희 진짜 내부 밈 생기기 시작했네."

    sj "그건 또 뭔가요."

    ge "우리끼리만 웃긴 말."
    ge "나중엔 다른 애들이 들으면 무슨 말인지 모르는 거."

    yn "오."
    yn "그거 좋다."

    hr "좋아하면 안 될 것 같은데."

    sa "근데 이미 생긴 것 같아."

    "설아가 벽 쪽에 붙은 작은 메모지를 봤다."
    "정말 그랬다."
    "포도 선배."
    "미감 탐지기."
    "체크리스트 반장."
    "오늘도 성공."
    "그냥 들으면 별 의미 없을 텐데,"
    "이 안에선 다 통한다."

    th "우리끼리만 아는 말."
    th "그게 생긴다는 건."
    th "생각보다 큰 변화일지도."

    scene bg old_library with dissolve

    "하린이는 마지막으로 장식 끈 길이를 재정리했고,"
    "설아는 창가에 매단 별들이 한쪽으로 쏠리지 않게 살짝 만졌고,"
    "유나는 메모지 아래에 아주 작은 벚꽃 낙서를 추가했다."
    "가은 선배는 그걸 보며 결국 웃음을 참지 못했다."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "너 진짜 벚꽃에 진심이다."

    show yuna grin at left, idle_bounce with dissolve
    yn "봄이잖아요."
    yn "그리고 우리 이름도 조용한 봄이잖아요."

    sj "네가 제일 그 이름 좋아하는 것 같긴 하다."

    yn "당연하죠."
    yn "제가 제일 먼저 꽂혔으니까."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "근데 이제 진짜 어울려."

    "하린이가 무심하게 그렇게 말하자,"
    "유나는 아주 잠깐 조용해졌다."
    "그리고 이번엔 호들갑 대신,"
    "조금 작게 웃었다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "……응."
    yn "그러네."

    "그 짧은 대답이 이상하게 오래 남았다."
    "장난스럽던 이름이,"
    "이제는 정말 우리 쪽 이름처럼 들렸기 때문일 거다."

    scene bg old_library with dissolve

    "곧 예비종이 울릴 시간이 가까워졌다."
    "하린이는 자동으로 시계를 봤고,"
    "설아는 비닐봉지 안 쓰레기를 접어 정리했고,"
    "유나는 남은 젤리를 억울한 얼굴로 바라봤고,"
    "나는 테이프와 가위를 원래 자리로 돌려놨다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "3분 남았어."

    show yuna surprise at left, excited_hop with dissolve
    yn "왜 또 이렇게 빨라!"

    sa "여기선 시간이 조금 빨라."

    "설아가 아주 자연스럽게 그 말을 꺼내자,"
    "이번엔 모두가 거의 동시에 웃었다."

    sj "이젠 완전 공식 문장이네."

    ge "어록 첫 줄다운 위엄인데."

    yn "좋아."
    yn "이건 진짜 조용한 봄 대표 문장이다."

    hr "대표 문장을 정하는 팀은 또 처음 보네."

    sj "우리 팀이 원래 좀 그렇지."

    "내가 무심코 그렇게 말하자,"
    "순간 다들 잠깐 나를 봤다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "선배."
    yn "방금 '우리 팀'이라고 했어요."

    sj "…그랬나."

    sa "응."
    hr "맞아."

    "정말 별생각 없이 나온 말이었다."
    "그런데 네 사람은 그 한마디를 이상할 만큼 곧게 받아냈다."
    "유나는 대놓고 기분 좋아 보였고,"
    "하린이는 작게 웃었고,"
    "설아는 아무 말 없이도 조금 부드러운 표정이었고,"
    "가은 선배는 그저 재미있다는 얼굴로 보고 있었다."

    th "아."
    th "진짜 그렇게 생각하고 있었나 보네."

    scene black with dissolve
    centered "{size=30}복도{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.2

    "준비실 문을 닫고 복도로 나오자,"
    "점심시간 끝의 소란이 다시 우리를 감쌌다."
    "학생들이 교실 쪽으로 흩어지는 흐름 사이에서,"
    "우리는 잠깐 나란히 섰다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    show seola smile at right, tiny_bounce with dissolve

    yn "오늘도 성공."

    hr "또 그 말이네."

    sa "근데 맞아."

    sj "이제 반박하기도 어렵다."

    ge "좋네."
    ge "짧아도 계속 쌓이는 팀."

    "가은 선배는 그렇게 말하고 먼저 손을 흔들었다."

    ge "난 먼저 갈게."
    ge "다들 오후 수업도 잘 버텨."

    yn "네에!"
    hr "다녀와요."
    sa "응."

    "선배가 멀어지고,"
    "우리는 다시 각자 교실 쪽으로 걸음을 옮겼다."

    "유나는 내 옆에서 걷다가 작게 웃으며 중얼거렸다."

    show yuna grin at left, idle_bounce with dissolve
    yn "포도 선배."

    sj "또 왜."

    yn "아니."
    yn "그냥 불러 보고 싶었어요."

    sj "그게 더 이상하거든."

    yn "근데 이젠 좀 어울리잖아요."

    sj "전혀."

    sa "조금."

    hr "조금."

    sj "왜 다들 한 편이냐."

    "셋의 타이밍이 너무 절묘해서,"
    "결국 나도 웃고 말았다."

    play sound "audio/sfx_school_bell.ogg"

    "본종이 울렸다."

    "우리는 각자 다른 방향으로 흩어졌다."
    "하지만 멀어지기 직전까지도,"
    "준비실 안에 남겨 둔 작은 말들과 웃음이"
    "어딘가에 이어져 있는 것 같은 기분이 들었다."

    th "우리끼리만 아는 말."
    th "우리 팀."
    th "여기선 시간이 조금 빨라."

    th "정말 별거 아닌데."
    th "이상하게 자꾸 좋은 쪽으로 마음에 남는다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 23 타이틀]

    scene black with fade
    centered "{size=40}Scene 23{/size}\n\n{size=30}작은 실수는 더 오래 웃긴다{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "오후 수업이 끝나갈 무렵,"
    "나는 오늘도 별생각 없이 필기를 하고 있었는데,"
    "머릿속 어딘가에서는 이미 준비실 문을 여는 장면이 먼저 떠오르고 있었다."

    th "이젠 진짜 습관이 됐네."
    th "방과 후면 자연스럽게 그쪽을 생각하게 된다."

    "종이 울리자 교실 안이 금세 느슨해졌다."
    "가방을 챙기는 소리, 친구를 부르는 소리, 창가 쪽으로 몰리는 발걸음."
    "그 속에서 나는 익숙하게 휴대폰부터 확인했다."

    "유나 : 오늘은 진짜 작업 많이 해야 해요"
    "유나 : 다들 늦지 마"
    "유나 : 그리고 오늘 포도 선배 금지"

    sj "갑자기 왜."

    "곧장 답장이 달렸다."

    "유나 : 왜냐면 제가 먼저 말하려고 했거든요"
    "하린 : 그게 더 이상해."
    "설아 : 이미 말했잖아."
    "가은 : 시작부터 시끄럽네"

    th "이 단체방은 점점 숨 돌릴 틈이 없어."

    scene black with dissolve
    centered "{size=30}준비실{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "준비실 문을 열자,"
    "오늘은 다들 거의 비슷하게 도착한 모양이었다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    "유나는 책상 위에 색지를 꺼내 놓고 있었고,"
    "하린이는 벽 쪽 장식 끈 상태를 보고 있었고,"
    "설아는 창가 별 장식이 꼬이지 않았는지 조용히 살펴보는 중이었다."

    sj "오늘은 다들 빠르네."

    show yuna grin at left, idle_bounce with dissolve
    yn "네."
    yn "왜냐면 오늘은 우리 부스의 얼굴이 될 안내판 초안까지 만져야 하거든요."

    sj "또 갑자기 말이 거창해졌네."

    show harin normal at center_lower, sway_soft with dissolve
    hr "그래도 오늘 할 건 조금 많긴 해."
    hr "배치도랑 설명란도 같이 봐야 하고."

    sa "장식 끈도 하나 더 자르면 좋을 것 같아."
    sa "창가 쪽이 조금 비어 보여."

    "설아가 그렇게 말하며 창문 위쪽을 가볍게 가리켰다."
    "이제는 이런 식으로 먼저 의견을 내는 것도 조금씩 자연스러워졌다."

    th "처음엔 한마디 꺼내는 것도 조심스러워 보였는데."
    th "정말 조금씩이지만, 다 변하고 있네."

    scene bg old_library with dissolve

    "우리는 늘 그렇듯 책상 주위로 모였다."
    "이제는 누가 어디쯤 서는지도 거의 정해져 있었다."
    "유나는 펜과 가위를 제일 빨리 잡는 자리,"
    "하린이는 전체를 보기 쉬운 정면,"
    "설아는 창가 쪽,"
    "나는 어쩌다 보니 늘 그 사이를 채우는 자리."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "좋아."
    yn "그럼 오늘 목표!"
    yn "첫째, 안내판 문구 다듬기."
    yn "둘째, 장식 위치 최종 확인."
    yn "셋째, 다들 저녁 전에 해산."

    sj "마지막이 제일 지켜질 것 같지가 않다."

    show yuna pout at left, sway_soft with dissolve
    yn "왜요."
    yn "저도 시간 개념 있거든요."

    sa "조금 불안하긴 해."

    hr "다들 같은 생각일걸."

    "유나는 억울한 얼굴을 했지만,"
    "딱히 반박은 못 했다."
    "그 반응이 웃겨서 나도 모르게 피식 웃었다."

    scene bg old_library with dissolve

    "오늘의 작업은 생각보다 순조로웠다."
    "하린이는 안내판에 들어갈 문장 간격을 맞추고,"
    "설아는 어느 색이 가장 눈에 덜 피로한지 고르고,"
    "유나는 종이 모서리에 아주 작게 넣을 포인트 장식을 고민하고,"
    "나는 잘린 끈 끝을 정리했다."

    "그렇게 10분쯤 지났을까."

    show yuna normal at left, sway_soft with dissolve
    yn "음."
    yn "이거 오른쪽 아래가 조금 심심하지 않아요?"

    hr "또 뭘 넣으려고."

    yn "아니, 진짜 조금만."
    yn "아주 쪼끄맣게."

    sa "작은 꽃?"
    sj "아니면 별."

    show yuna smile at left, tiny_bounce with dissolve
    yn "오."
    yn "좋다."
    yn "그럼 꽃이랑 별을 하나씩 해볼까요?"

    hr "둘 다는 많아."

    "하린이는 여전히 단호했지만,"
    "이젠 유나도 그 선을 아는지 바로 물러났다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "좋아요."
    yn "그럼 하나만."

    "그리고 바로 그때였다."

    "유나가 네임펜 뚜껑을 열다가,"
    "그 옆에 세워 둔 젤리 통을 팔꿈치로 건드렸다."

    "톡."

    "아주 가벼운 소리와 함께,"
    "작은 벚꽃 젤리 몇 개가 책상 위를 데구르르 굴렀다."

    show yuna surprise at left, excited_hop with dissolve
    yn "어."

    "그중 두 개는 가격표 종이 위로,"
    "하나는 하린이 체크리스트 쪽으로,"
    "그리고 하나는 정말 절묘하게 내가 정리해 둔 장식 끈 사이로 파고들었다."

    "정적이 딱 1초."

    show harin surprise at center_lower, excited_hop with dissolve
    hr "민유나."

    show seola surprise at right, excited_hop with dissolve
    sa "……정확하다."

    sj "이걸 이렇게 흘린다고?"

    "유나는 그대로 굳은 채 젤리 통을 들고 있었다."
    "스스로도 너무 완벽하게 사고를 쳐 버렸다는 걸 알아버린 얼굴이었다."

    show yuna surprise at left, excited_hop with dissolve
    yn "잠깐만요."
    yn "이건."
    yn "진짜 일부러 그런 게 아니라…"

    "그 말이 끝나기도 전에,"
    "설아가 먼저 책상 위를 굴러다니는 젤리 하나를 집었다."
    "하린이도 체크리스트 위에 올라간 젤리를 떼어 들었고,"
    "나는 장식 끈 사이로 들어간 하나를 꺼냈다."

    "그리고 문제는,"
    "그 장면이 너무 진지할 이유가 없을 만큼 웃겼다는 거다."

    show seola smile at right, tiny_bounce with dissolve
    sa "벚꽃 습격."

    "설아가 아주 담담하게 그렇게 말한 순간,"
    "유나가 먼저 빵 터졌고,"
    "그 다음은 나였고,"
    "결국 하린이까지 웃음을 참지 못했다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "벚꽃 습격이 뭐예요!"
    sj "아니 근데 너무 정확하잖아."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "진짜 딱 그거네."

    "유나는 웃으면서도 책상 위 젤리를 황급히 주워 담기 시작했다."
    "하린이는 그런 유나를 보며 한숨을 쉬었지만,"
    "이번엔 정말 하나도 화난 얼굴이 아니었다."

    hr "그래도 문서 위에 흘리는 건 금지."
    yn "죄송합니다, 체크리스트 반장님…"

    sa "오늘의 교훈."
    sa "간식은 안전거리 유지."

    sj "어록 추가다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아!"
    yn "방금 그거 진짜 좋았어."
    yn "'간식은 안전거리 유지'."

    hr "그걸 왜 또 좋아해."

    "유나는 젤리 통을 다시 안전한 구석으로 치워 놓더니,"
    "정말로 메모지 한쪽에"
    "'간식은 안전거리 유지'"
    "라고 적어 넣었다."

    scene bg old_library with dissolve

    "그 짧은 소동 이후,"
    "준비실 안 분위기는 오히려 더 풀어졌다."

    "유나는 무언가를 건드릴 때마다 일부러 양손을 번쩍 들며"
    "'이번엔 안 흘림!'"
    "같은 소리를 했고,"
    "설아는 그럴 때마다 작게 웃었고,"
    "하린이는 결국 '이제 됐으니까 집중해'라고 말하면서도 웃고 있었고,"
    "나는 장식 끈을 정리하다가도 자꾸 그 장면이 떠올라 피식거리게 됐다."

    th "정말 별일 아닌데."
    th "이런 게 더 오래 남는 걸지도."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "좋아."
    yn "그럼 사고 수습도 끝났고, 다시 안내판!"

    sj "사고 수습이라는 표현이 너무 정확하네."

    hr "수습 담당이 있잖아."

    sj "왜 그게 또 나한테 돌아오냐."

    sa "어울리니까."

    "이젠 셋 다 너무 자연스럽게 말한다."
    "그만큼 이 별명도 완전히 굳은 모양이었다."

    scene bg old_library with dissolve

    "우리는 다시 안내판 쪽으로 집중했다."
    "유나는 이번엔 정말 조심해서 종이 오른쪽 아래에 아주 작은 포인트 하나만 넣었고,"
    "하린이는 글씨 간격을 다시 맞췄고,"
    "설아는 전체 균형을 본 뒤 살짝 고개를 끄덕였다."

    show seola normal at right, sway_soft with dissolve
    sa "이제 괜찮아."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "응."
    hr "이 정도면 딱 좋다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "진짜요?"

    sj "어."
    sj "이번엔 인정."

    "유나는 순간 아주 조용해졌다가,"
    "이내 조금 작은 목소리로 웃었다."

    yn "오늘 저."
    yn "젤리도 흘리고, 장식도 통과되고."
    yn "감정 기복 크다."

    sj "하루 알차네."

    sa "낙폭이 큰 편."

    hr "근데 결과는 좋으니까 됐어."

    "하린이가 그렇게 말하자,"
    "유나는 대놓고 뿌듯한 얼굴을 했다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "그럼 오늘도 성공."

    sj "또 나왔다."

    sa "그래도 맞아."

    scene bg old_library with dissolve

    "가은 선배는 오늘 조금 늦게 왔다."
    "준비실 문을 열고 들어오자마자,"
    "책상 구석에 안전하게 놓인 젤리 통과,"
    "그 옆에 적혀 있는 새 문장을 먼저 발견했다."

    show gaeun smile at far_right, tiny_bounce with dissolve

    ge "어라."
    ge "'간식은 안전거리 유지'?"
    ge "이건 또 뭐야."

    show yuna laugh at left, idle_bounce with dissolve
    yn "오늘 새로 생긴 조용한 봄 어록이에요."

    ge "벌써?"
    ge "무슨 일이 있었길래."

    sj "벚꽃 습격."

    "내가 아무렇지 않게 말하자,"
    "가은 선배는 잠깐 멈췄다가 바로 웃음을 터뜨렸다."

    ge "잠깐."
    ge "그 말 너무 웃긴데?"

    sa "정확했어."

    hr "유나가 젤리 통 엎을 뻔했거든."

    ge "아하."

    "가은 선배는 상황을 머릿속으로 그려 본 듯,"
    "바로 납득한 얼굴로 고개를 끄덕였다."

    ge "좋네."
    ge "이제 진짜 내부 밈이 많아지네."

    yn "그쵸!"
    yn "우리끼리만 알아듣는 말 생기는 거 되게 좋지 않아요?"

    ge "좋지."
    ge "그게 친해졌다는 뜻이기도 하니까."

    "선배의 말은 언제나처럼 가벼웠지만,"
    "묘하게 맞는 말이었다."

    th "우리끼리만 알아듣는 말."
    th "확실히, 며칠 전엔 없던 거다."

    scene bg old_library with dissolve

    "가은 선배가 온 뒤로 준비실 안은 더 시끄러워졌지만,"
    "이상하게 작업은 더 잘 굴러갔다."
    "누군가 말하면 누군가 웃고,"
    "누군가 실수해도 누군가 자연스럽게 받았고,"
    "작업은 그 사이에서 느슨하게 이어졌다."

    "결국 안내판 초안은 생각보다 빠르게 완성됐다."
    "문구도 정돈됐고,"
    "장식도 과하지 않았고,"
    "전체 배치도 이제야 정말 하나의 분위기로 묶인 느낌이었다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "이 정도면 오늘 목표는 거의 끝."

    show yuna smile at left, tiny_bounce with dissolve
    yn "우와."
    yn "우리 진짜 잘한다."

    sj "갑자기 팀 자화자찬이네."

    yn "아니."
    yn "진짜 그렇잖아요."

    sa "응."
    sa "처음보다 훨씬 빨라졌어."

    ge "맞아."
    ge "호흡이 생겼네."

    "그 말이 나오자,"
    "잠깐 아무도 바로 장난을 치지 않았다."
    "왜냐하면 다들 비슷하게 느끼고 있었기 때문일 거다."

    th "호흡."
    th "그 단어가 제일 정확할지도."

    scene bg old_library with dissolve

    "예비종이 울리기 전,"
    "유나는 오늘도 어김없이 단체방에 사진을 올렸다."

    "유나 : 오늘의 성과!"
    "유나 : 안내판 초안 완성"
    "유나 : 그리고 벚꽃 습격 발생"

    sj "왜 그걸 같이 올리냐."

    show yuna grin at left, idle_bounce with dissolve
    yn "기록은 솔직해야 하니까요."

    hr "그건 굳이 안 적어도 됐는데."

    sa "근데 안 적으면 아쉬워."

    ge "응."
    ge "오히려 그쪽이 더 기억에 남을 듯."

    "그럴지도 모른다."
    "안내판 완성도 물론 좋았지만,"
    "오늘을 떠올릴 때 먼저 생각나는 건 아마"
    "체크리스트 위에 얌전히 올라가 있던 벚꽃 젤리 한 개와,"
    "그걸 보며 다 같이 웃던 순간일 거다."

    scene bg old_library with dissolve

    "예비종이 울렸다."

    play sound "audio/sfx_school_bell.ogg"

    show harin surprise at center_lower, excited_hop with dissolve
    hr "정리하자."

    show yuna smile at left, tiny_bounce with dissolve
    yn "네, 반장님."
    yn "오늘은 간식 안전거리도 지켰고."
    sj "후반부에나."

    sa "그래도 지켰으면 된 거지."

    "우리는 서둘러 책상 위를 정리했다."
    "이제는 말하지 않아도 손이 먼저 움직였다."
    "펜 뚜껑을 닫고,"
    "가위를 한쪽에 모으고,"
    "젤리 통을 제대로 닫고,"
    "안내판 초안을 구겨지지 않게 벽 쪽에 세워 두었다."

    th "이런 것도 익숙해졌네."
    th "정리하는 속도까지 맞아 가는 걸 보면."

    scene black with dissolve
    centered "{size=30}복도{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.2

    "준비실 문을 닫고 복도로 나오자,"
    "점심이든 방과 후든 늘 비슷한 감각이 들었다."
    "짧았고, 웃겼고, 또 금방 지나갔다."
    "그런데 그래서 더 선명했다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    show seola smile at right, tiny_bounce with dissolve

    yn "좋아."
    yn "오늘의 결론."

    sj "또 정리냐."

    yn "네."
    yn "벚꽃 젤리는 위험하다."

    hr "그건 네 주변에서만."

    sa "간식은 안전거리 유지."

    sj "수습 담당은 오늘도 고생했다."
    ge "그리고 벚꽃 습격은 오래 남는다."

    show gaeun smile at far_right, tiny_bounce with dissolve

    "다섯 사람의 말이 거의 동시에 엉켰고,"
    "결국 또 웃음이 터졌다."

    th "정말 별것 아닌 날."
    th "정말 별것 아닌 실수."

    th "그런데."
    th "이상할 정도로 오래 기억될 것 같다."

    play sound "audio/sfx_school_bell.ogg"

    "본종이 울렸다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "내일 또 봐요!"
    hr "수업 늦겠다, 빨리 가."
    sa "응."
    ge "다들 해산."

    "우리는 각자 흩어졌지만,"
    "오늘 생긴 말 하나는 분명 오래 남을 것 같았다."

    th "벚꽃 습격."
    th "정말 유치한데."

    th "왜 이렇게 마음에 남는 건지."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 24 타이틀]

    scene black with fade
    centered "{size=40}Scene 24{/size}\n\n{size=30}문을 열면 있는 사람들{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "다음 날 점심시간 직전."
    "수업 내용은 분명 칠판 위에 있었는데,"
    "이상하게도 머릿속 한구석엔 자꾸 다른 장면이 먼저 떠올랐다."

    th "오늘은 누가 먼저 와 있으려나."

    "생각이 거기까지 닿고 나서야,"
    "나는 조금 늦게 그게 이상하다는 걸 깨달았다."

    th "준비실에 가는 게 아니라."
    th "누가 있는지를 먼저 떠올렸네."

    "종이 울리자 교실 안이 풀어졌다."
    "나는 평소보다 빨리 휴대폰을 켰다."

    "유나 : 오늘 점심 준비실 정상 운영"
    "유나 : 출석 체크할 거예요"
    "유나 : 빠지면 포도 압수"

    sj "왜 내 포도를 압수해."

    "곧바로 메시지가 이어졌다."

    "하린 : 네 것도 아닌데."
    "설아 : 포도는 원래 네 거 아니었어."
    "가은 : 포도 선배 자산권 침해"

    th "이젠 선배까지 너무 자연스럽네."

    "나는 결국 웃음을 참지 못한 채 자리에서 일어났다."
    "교실 밖으로 나서는 발걸음이, 생각보다 가볍다."

    scene black with dissolve
    centered "{size=30}준비실 앞{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.2

    "준비실 앞에 도착했을 때,"
    "문은 닫혀 있었지만 안쪽에서 희미하게 목소리가 들렸다."

    "작게 웃는 소리."
    "무언가 종이를 넘기는 소리."
    "그리고 익숙한 누군가의 한숨 섞인 반응."

    th "아, 벌써 와 있구나."

    "나는 별생각 없이 문고리를 잡았다."
    "그런데 이상하게, 열기 직전의 순간이 조금 좋았다."
    "문을 열면 누가 있을지 알고 있는데도,"
    "그래서 더 반가운 기분."

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "문을 열자,"
    "익숙한 풍경이 한 번에 들어왔다."

    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    "하린이는 책상 위에 놓인 종이를 정리하고 있었고,"
    "설아는 창가 쪽 별 장식 하나가 돌아간 걸 손끝으로 바로잡고 있었다."

    "둘 다 동시에 문 쪽을 돌아봤다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "왔네."

    show seola smile at right, tiny_bounce with dissolve
    sa "안 늦었어."

    "정말 짧은 말이었다."
    "그런데 그 한마디가 생각보다 훨씬 반갑게 들렸다."

    sj "뭐야."
    sj "둘만 있으니까 되게 조용하네."

    sa "유나 아직 안 왔어."

    hr "그래서 더 조용한 걸지도."

    "하린이 말에 설아가 아주 작게 웃었다."
    "그 미세한 웃음이 괜히 눈에 남았다."

    th "정말 이상하네."
    th "며칠 전까지만 해도 어색했을 텐데."
    th "지금은 이렇게 둘만 먼저 와 있는 풍경도 편하다."

    scene bg old_library with dissolve

    "준비실 안은 이제 정말 낯설지 않았다."
    "벽에 붙은 안내판 초안,"
    "창가에 매단 작은 별들,"
    "구석의 '조용한 봄 어록' 메모지,"
    "테이프와 가위가 놓인 위치까지."

    "그리고 그 안에 서 있는 사람들."

    "하린이는 자연스럽게 내 몫처럼 빈자리를 하나 비워 두었고,"
    "설아는 아무 말 없이 책상 위에 남은 펜을 내 쪽으로 밀어 두었다."

    sj "내 자리도 있었냐."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "이제는 있는 편이지."

    sa "원래 늘 여기쯤 서잖아."

    "설아는 아주 아무렇지 않게 말했다."
    "그 말이 더 이상하게 느껴졌다."
    "아무렇지 않아서."
    "정말로 내가 늘 그 자리에 있었던 사람처럼 들려서."

    th "늘 여기쯤."
    th "그 정도로 익숙해졌나."

    scene bg old_library with dissolve

    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    "나는 가방도 없이 빈손으로 책상 쪽에 다가갔다."
    "하린이가 정리 중이던 종이엔 어제 다듬어 둔 안내판 문구가 다시 적혀 있었고,"
    "설아 쪽 창가엔 별 장식이 햇빛에 아주 약하게 흔들리고 있었다."

    sj "뭐 하고 있었어."

    hr "안내판 글씨 위치 다시 보는 중."
    hr "아까 와서 보니까 아래쪽 여백이 조금 신경 쓰이더라."

    sa "별도 하나 돌아가 있었어."
    sa "바람 때문에."

    sj "둘 다 오자마자 바로 일했네."

    "내가 그렇게 말하자,"
    "하린이는 종이를 한 번 내려다보다가 조금 어색하게 대답했다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "…그냥."
    hr "조금 일찍 오면 뭐라도 하게 되니까."

    sa "여기 있으면 손이 먼저 가."

    "설아의 말도 비슷했다."
    "둘 다 거창한 말을 하는 건 아닌데,"
    "그 안에 이미 준비실이 '그냥 오는 곳'이 아니라는 뜻이 들어 있었다."

    th "다 똑같구나."
    th "나만 그런 게 아니었네."

    scene bg old_library with dissolve

    "그때였다."
    "복도에서 익숙한 발소리가 빠르게 다가왔다."
    "다음 순간, 문이 벌컥 열렸다."

    show yuna smile at left, tiny_bounce with dissolve

    yn "세이프!"
    yn "좋아, 오늘도 다들 있—"

    "유나는 말을 하다 말고 잠깐 멈췄다."
    "우리 셋이 이미 너무 자연스럽게 준비실 안에 서 있는 걸 보고,"
    "괜히 웃음이 번진 얼굴이었다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "…어."
    yn "뭔가 좋다."

    sj "뭐가."

    yn "아니."
    yn "그냥 문 열었는데 다들 있잖아요."

    "이번엔 그 말이 아주 가볍게 들리진 않았다."
    "어제 자판기 앞에서 유나가 했던 말이,"
    "이번엔 준비실 한복판에서 조금 다른 모양으로 다시 놓인 기분이었다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "너도 지금 왔으니까 다 있는 거지."

    show seola smile at right, tiny_bounce with dissolve
    sa "응."
    sa "이제 다 있네."

    "설아의 말에 유나는 대놓고 기분 좋아하는 얼굴이 됐다."

    show yuna laugh at left, idle_bounce with dissolve
    yn "좋아요!"
    yn "오늘 출석률 100퍼!"
    sj "그걸 그렇게 기뻐할 일이냐."

    yn "엄청 중요하죠."
    yn "이런 거 하나하나가 다 분위기라고요."

    scene bg old_library with dissolve

    "결국 오늘도 유나는 작은 메모지 하나를 꺼냈다."
    "며칠 전부터 생긴 출석 체크용 종이였다."
    "이름 네 개와, 특별 게스트용 별표 칸."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "조용한 봄 점심 모임, 전원 출석."

    hr "가은 선배는 아직이야."
    yn "특별 게스트는 예외 적용."

    sa "규칙이 늘 유나한테 유리해."

    sj "진짜 그러네."

    "유나는 억울한 척했지만,"
    "이미 체크 표시를 그리는 손은 멈추지 않았다."
    "하린이는 자기 이름 칸에 반듯한 체크를,"
    "설아는 오늘도 작은 점을,"
    "나는 대충 사선을,"
    "유나는 또 하트를 그리려다 하린 눈치를 보고 결국 동그라미를 쳤다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "매번 왜 같은 패턴이야."

    show yuna pout at left, sway_soft with dissolve
    yn "제 안의 귀여움 본능이…"
    sj "또 시작이다."

    scene bg old_library with dissolve

    "출석 체크까지 끝나자,"
    "준비실 안 공기는 더 말랑해졌다."
    "이제는 정말 작업을 시작하기 전 잠깐 모여 있는 시간조차 따로 의미가 생긴 느낌이었다."

    "유나는 책상에 양팔을 기대고 우리를 한 번씩 보더니,"
    "갑자기 장난기 섞인 얼굴로 말했다."

    show yuna grin at left, idle_bounce with dissolve
    yn "근데요."
    yn "이제 누가 먼저 와 있는지도 좀 캐릭터 같지 않아요?"

    sj "또 무슨 이상한 분석이냐."

    yn "아니, 진짜."
    yn "하린이는 먼저 와 있으면 이미 정리하고 있을 것 같고,"
    yn "설아 선배는 조용히 장식 보고 있을 것 같고,"
    yn "선배는 문 열고 들어오자마자 '다 와 있었네' 할 것 같고."

    sa "방금 그대로였어."

    hr "맞네."

    "셋의 시선이 동시에 내게 왔다."
    "반박하고 싶은데,"
    "이상할 정도로 정확해서 말이 안 나왔다."

    sj "…너 진짜 별 걸 다 본다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋은 건 잘 보이거든요."

    "그 말이 너무 아무렇지 않게 나와서,"
    "오히려 내가 잠깐 말문이 막혔다."
    "설아는 유나를 가만히 보다가 아주 조금 고개를 끄덕였고,"
    "하린이는 괜히 종이 한 장을 다시 정리하는 척했다."

    scene bg old_library with dissolve

    "잠시 뒤, 가은 선배도 준비실에 얼굴을 비쳤다."
    "문을 열자마자 선배는 우리 넷을 한 번 보고,"
    "익숙하게 웃었다."

    show gaeun smile at far_right, tiny_bounce with dissolve

    ge "다들 벌써 모였네."
    ge "이제 여기 들어오면 매번 같은 풍경이라 좋다."

    yn "그쵸!"
    yn "이제 완전 정착됐죠?"

    ge "응."
    ge "문 열었는데 너희 있으면 괜히 안심돼."

    "가은 선배의 말은 아주 가볍게 떨어졌는데,"
    "그 말 뒤로 준비실 안이 잠깐 조용해졌다."
    "누구도 특별히 티 내진 않았지만,"
    "다들 조금은 비슷한 감각을 느낀 듯했다."

    th "문 열었는데 있으면 안심된다."
    th "…그것도 맞는 말이네."

    scene bg old_library with dissolve

    "오늘 작업 자체는 아주 크지 않았다."
    "안내판 초안을 벽에 대 보고,"
    "장식 간격을 조금 조정하고,"
    "별 장식 아래에 작은 종이 택을 달아 볼지 고민하고."

    "그런데 이상하게 작업보다 중간중간의 짧은 대화가 더 오래 남았다."

    show harin normal at center_lower, sway_soft with dissolve
    hr "이쪽은 조금 더 올릴까."

    show seola normal at right, sway_soft with dissolve
    sa "아니."
    sa "지금이 더 편해 보여."

    show yuna smile at left, tiny_bounce with dissolve
    yn "저도 설아 선배 쪽!"
    sj "그럼 2 대 1이네."

    hr "너는?"

    sj "나도 지금 쪽."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "…알겠어."

    "하린이는 군말 없이 위치를 다시 맞췄다."
    "예전 같으면 자기 기준을 더 밀었을지도 모르는데,"
    "지금은 의견이 오가고, 섞이고, 자연스럽게 정리됐다."

    th "하린도 많이 편해졌네."

    show yuna normal at left, sway_soft with dissolve
    yn "근데 진짜 신기하다."
    yn "우리 다 취향 조금씩 다른데 결과물은 잘 섞여요."

    sa "그래서 좋은 걸지도."

    ge "응."
    ge "누구 하나만 했으면 안 나왔을 느낌."

    sj "그건 맞네."

    "괜히 그렇게 대답한 뒤,"
    "나는 벽에 기대 선 안내판을 다시 봤다."
    "누구 하나의 색만 진하지 않았다."
    "대신 조금씩 섞여 있었다."
    "그게 이상하게 준비실 전체 분위기랑 닮아 보였다."

    scene bg old_library with dissolve

    "작업 도중, 유나는 또 뭔가 떠오른 얼굴로 메모지를 들었다."

    show yuna grin at left, idle_bounce with dissolve
    yn "좋아."
    yn "오늘의 질문."

    sj "왜 매일 있어."

    yn "있어야죠."
    yn "문 열었을 때 제일 먼저 반가운 건 뭐예요?"
    yn "장식? 사람? 간식?"

    sj "질문이 너무 유나식이다."

    sa "근데 궁금하긴 해."

    hr "…하나만 고르라는 거지?"

    yn "네."

    "유나는 정말 진지한 얼굴이었다."
    "하린이는 잠깐 생각했고,"
    "설아는 창가를 한 번 봤고,"
    "가은 선배는 팔짱을 낀 채 우리를 구경했다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "나는."
    hr "사람."

    show seola smile at right, tiny_bounce with dissolve
    sa "나도."

    "둘이 거의 겹치듯 대답했다."
    "유나는 바로 기분 좋아진 얼굴이 됐다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "…저도."

    "이젠 셋의 시선이 자연스럽게 내게 왔다."
    "나는 잠깐 말없이 준비실 안을 둘러봤다."
    "창가의 별 장식."
    "어록 메모지."
    "책상 위 종이들."
    "그리고 그 사이에 서 있는 네 사람."

    sj "…사람."

    "말은 짧았는데,"
    "이상하게 그 뒤는 더 조용했다."
    "유나는 바로 웃어 버릴 것 같더니,"
    "이번엔 그러지 않았다."
    "하린이는 손에 들고 있던 종이를 괜히 반듯하게 맞췄고,"
    "설아는 아주 조용히 웃었고,"
    "가은 선배는 그저 아는 얼굴로 우리를 봤다."

    ge "그럼 정답 나왔네."

    scene bg old_library with dissolve

    "그 뒤로는 누가 먼저랄 것도 없이 분위기가 조금 더 느슨해졌다."
    "유나는 괜히 '좋아, 그럼 오늘도 사람 출석 완료' 같은 말을 했고,"
    "하린이는 '그 말은 좀 이상해'라고 하면서도 웃었고,"
    "설아는 출석 체크 메모지 옆에 아주 작게 사람 모양 낙서를 하나 그렸다가 유나에게 들켰다."

    show yuna surprise at left, excited_hop with dissolve
    yn "어?"
    yn "설아 선배 이거 뭐예요?"

    show seola surprise at right, excited_hop with dissolve
    sa "…아무것도 아냐."

    show yuna laugh at left, idle_bounce with dissolve
    yn "아닌데."
    yn "완전 귀엽잖아."

    sj "설아도 이런 거 하네."
    sa "실수."

    hr "실수치곤 정성인데."

    "설아는 괜히 메모지를 뒤집으려 했지만,"
    "이미 다 들킨 뒤였다."
    "유나는 그 조그만 사람 낙서를 보며 혼자 한참 즐거워했다."

    th "이제는 이런 작은 것도 전부 웃기다."

    scene bg old_library with dissolve

    "예비종이 울리기 직전,"
    "가은 선배가 준비실 문쪽으로 한 걸음 물러서며 웃었다."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "좋다."
    ge "이제 여기 오면 진짜 준비실보다 '너희 있는 곳' 같아."

    show yuna smile at left, tiny_bounce with dissolve
    yn "와."
    yn "그 말도 어록."

    hr "또 늘어나네."

    sa "근데 좋다."

    sj "인정."

    "유나는 진짜로 어록 메모지에 한 줄을 더 적었다."

    "'여기 오면 준비실보다 너희 있는 곳 같아.'"

    "그 문장을 보고 있자니,"
    "그 말 자체보다도,"
    "아무도 그걸 과하다고 생각하지 않는다는 사실이 더 크게 느껴졌다."

    th "정말 그렇구나."
    th "이제는 장소보다 사람이다."

    scene black with dissolve
    centered "{size=30}복도{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.2

    "준비실 문을 닫고 복도로 나오자,"
    "본종 전의 분주한 소리가 다시 우리를 감쌌다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    show seola smile at right, tiny_bounce with dissolve

    yn "좋아."
    yn "오늘의 결론."

    sj "또 나온다."

    yn "문 열었을 때 반가운 건 사람."

    hr "간단하네."

    sa "근데 맞아."

    ge "이제 진짜 팀 같다."

    "그 말에 누가 특별히 반응한 건 아니었다."
    "그럴 필요도 없었다."
    "이미 다들 알고 있었으니까."

    play sound "audio/sfx_school_bell.ogg"

    "본종이 울렸다."
    "우리는 다시 각자 교실 쪽으로 흩어졌다."

    "멀어지는 와중에도,"
    "오늘 준비실 문을 열던 순간이 자꾸 떠올랐다."

    th "문을 열면 있는 사람들."

    th "정말 별거 아닌데."
    th "그게 이렇게까지 반가워질 줄은,"
    th "조금 전까지만 해도 몰랐다."

    scene black with fade

    # ---------------------------------------------------------
    # [Scene 25 타이틀]

    scene black with fade
    centered "{size=40}Scene 25{/size}\n\n{size=30}처음으로 들은 바깥의 말{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_daily_light.ogg" fadein 2.0

    "오후 수업이 끝날 무렵,"
    "나는 괜히 창밖을 한 번 더 봤다."
    "날씨가 특별히 좋은 것도 아닌데,"
    "요즘은 이 시간이 되면 이상하게 마음이 먼저 가벼워졌다."

    th "오늘은 뭐 했더라."
    th "안내판 정리 거의 끝났고."
    th "창가 별 장식도 맞췄고."
    th "어록은 또 늘었고."

    th "……이젠 진짜 준비실 생각부터 하네."

    "종이 울리자마자 교실 안이 느슨하게 풀어졌다."
    "나는 늘 하던 대로 휴대폰부터 확인했다."

    "유나 : 오늘 목표 있음"
    "유나 : 외부 공개 가능한 수준 만들기"
    "유나 : 다들 준비실 집합!"

    sj "외부 공개는 또 뭐야…"

    "곧바로 이어서 메시지가 떴다."

    "하린 : 말만 거창하게 하지 마."
    "설아 : 근데 뭔지 조금 궁금해."
    "가은 : 오, 드디어 바깥 반응 받는 날인가?"

    th "선배가 제일 빨리 이해했네."

    scene black with dissolve
    centered "{size=30}준비실{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.5

    "준비실 문을 열자,"
    "오늘은 유난히 안쪽이 밝아 보였다."
    "창문으로 들어오는 햇빛 때문인지,"
    "아니면 벽이 조금씩 채워져서 그런 건지 잘 모르겠다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    "유나는 책상 위에 안내판 초안을 세워 두고 있었고,"
    "하린이는 그걸 조금 떨어져서 전체로 보고 있었고,"
    "설아는 창가에서 별 장식 흔들림을 확인하고 있었다."

    show yuna grin at left, idle_bounce with dissolve
    yn "왔네요, 포도 선배."

    sj "이젠 인사 대신 그거냐."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "포기해."
    hr "이미 다들 익숙해졌어."

    show seola smile at right, tiny_bounce with dissolve
    sa "조금 어울리기도 하고."

    sj "설아까지 그러면 진짜 반박할 힘이 없거든."

    "셋이 동시에 웃었다."
    "이제는 이런 대화도 거의 준비운동 같았다."
    "본격적으로 뭘 하기 전, 먼저 한 번 분위기가 풀리는 과정."

    scene bg old_library with dissolve

    show harin normal at center_lower, sway_soft with dissolve

    hr "오늘은 일단 이 안내판."
    hr "최종으로 벽에 대 보고, 괜찮으면 복도 쪽에도 한 번 보여줄까 생각 중이야."

    sj "복도?"

    show yuna smile at left, tiny_bounce with dissolve
    yn "네."
    yn "지나가던 애들이 보기라도 하면 좋잖아요."
    yn "우리가 만든 게 어떤 느낌인지."

    sa "반응 보는 거네."

    ge "그거 중요하지."

    show gaeun smile at far_right, tiny_bounce with dissolve

    "가은 선배는 언제나처럼 타이밍 좋게 문가에서 말을 받았다."
    "이제는 진짜 문 열리고 선배 목소리 들리는 것도 익숙하다."

    sj "선배 오늘도 자연스럽게 들어오네요."

    ge "응."
    ge "이쯤 되면 나도 조용한 봄 준멤버 아니야?"

    yn "준멤버가 아니라 거의 고정 특별 게스트예요."

    ge "오, 직함 생겼네."

    scene bg old_library with dissolve

    "우리는 안내판 초안을 들고 벽 쪽으로 갔다."
    "하린이가 양쪽 모서리를 맞췄고,"
    "나는 테이프를 잘라 건넸고,"
    "설아는 조금 떨어져서 전체 균형을 봤고,"
    "유나는 두 손을 모은 채 너무 진지한 얼굴로 결과를 기다렸다."

    show seola normal at right, sway_soft with dissolve
    sa "조금만 위."

    show harin normal at center_lower, sway_soft with dissolve
    hr "이 정도?"

    show yuna normal at left, sway_soft with dissolve
    yn "아니, 잠깐."
    yn "왼쪽이 아주 조금 내려간 것 같기도…"

    sj "너 방금까지 너무 감성 담당이더니 이런 것도 보냐."

    yn "그럼요."
    yn "전 섬세한 사람입니다."

    ge "유나는 의외로 디테일 집착 있어."

    sj "그건 인정."

    "결국 안내판은 하린이와 설아의 눈, 유나의 감, 내 손, 가은 선배의 구경이 합쳐져 벽에 잘 붙었다."

    "그리고."
    "이상하게도."
    "정말 괜찮았다."

    "지금까지 책상 위에 눕혀져 있을 땐 몰랐는데,"
    "실제로 벽에 붙어 있으니 그럴듯함이 갑자기 훅 올라왔다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "…오."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "생각보다 더 괜찮네."

    show seola smile at right, tiny_bounce with dissolve
    sa "응."
    sa "진짜 부스 같아졌어."

    th "조금 전까진 종이였는데."
    th "붙는 순간 분위기가 생기네."

    scene bg old_library with dissolve

    "우리는 잠깐 아무 말 없이 안내판을 올려다봤다."
    "'그냥 편하게 쉬어갈 수 있는 곳.'"
    "단정한 글씨."
    "과하지 않은 작은 벚꽃."
    "여백 사이에 남겨진 숨 쉴 자리."

    "정말 누구 하나만의 취향은 아니었다."
    "대신 다 같이 만든 느낌이 분명히 있었다."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "좋다."
    ge "딱 너희 같아."

    sj "너희 같다는 말 자주 하네요."

    ge "왜냐면 진짜 그렇거든."
    ge "시끄러운 애 하나 있고."
    ge "반듯한 애 하나 있고."
    ge "조용한데 감각 좋은 애 하나 있고."
    ge "겉으론 덤덤한데 은근 계속 붙어 있는 애 하나 있고."

    "마지막 말에서 선배 시선이 내 쪽으로 잠깐 머물렀다."
    "유나는 바로 웃었고,"
    "하린이는 괜히 펜을 만지작거렸고,"
    "설아는 아주 조금 고개를 숙였다."

    sj "선배는 사람 분석을 너무 쉽게 해요."

    ge "관찰하는 거 좋아하니까."

    scene bg old_library with dissolve

    "유나는 안내판 앞에 서서 한참을 바라보다가,"
    "갑자기 몸을 홱 돌렸다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋아."
    yn "이건 진짜 다른 사람 반응 받아도 안 부끄러울 것 같아요."

    hr "그럼 복도 앞쪽 게시판에 잠깐 대 볼까?"
    hr "완전히 붙이진 말고."

    sa "응."
    sa "지나가면서 보기 좋을 것 같아."

    sj "진짜 공개하네."

    yn "왜요."
    yn "긴장돼요?"

    sj "조금은."

    "내가 별생각 없이 그렇게 말하자,"
    "유나가 의외라는 얼굴로 나를 봤다."

    show yuna grin at left, idle_bounce with dissolve
    yn "우와."
    yn "선배도 긴장해요?"

    sj "사람이니까 하겠지."

    sa "그것도 맞네."

    hr "다 같이 만든 거니까 더 그렇지."

    "하린이 말이 괜히 맞았다."
    "혼자 만든 게 아니니까."
    "그래서 더 별거 아닌 반응 하나에도 신경이 쓰일 것 같았다."

    scene black with dissolve
    centered "{size=30}준비실 앞 복도{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.2

    "우리는 안내판 초안을 조심히 들고 복도 쪽으로 나왔다."
    "점심시간만큼 북적이진 않지만,"
    "방과 후 복도에도 아직 학생들이 조금씩 오갔다."

    "하린이는 복도 벽 게시판 한쪽에 안내판을 가볍게 대 보았고,"
    "설아는 두 걸음 뒤로 물러서서 봤고,"
    "유나는 아예 반대편까지 가서 거리감까지 확인했다."
    "가은 선배는 팔짱을 낀 채 그 광경을 구경했고,"
    "나는 왠지 모르게 주변 사람 눈치를 한 번 보게 됐다."

    show yuna normal at left, sway_soft with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve

    yn "좋은데."
    yn "멀리서도 꽤 보여요."

    hr "글씨 크기는 괜찮은 것 같아."

    sa "색도 안 튀고."

    sj "진짜 다듬긴 많이 다듬었네."

    "그때."
    "복도를 지나가던 다른 반 여학생 둘이,"
    "우리 쪽을 흘끗 보더니 속도를 조금 늦췄다."

    stu_b "어?"
    stu_b "저거 이번 축제 거야?"
    stu_c "예쁘다."

    "정말 짧은 말이었다."
    "그리고 아마 그 애들은 대수롭지 않게 지나가며 한 말이었을 거다."
    "그런데 그 한마디가 묘하게 또렷하게 남았다."

    "예쁘다."

    "유나는 눈을 동그랗게 떴고,"
    "하린이는 움직이던 손을 멈췄고,"
    "설아는 아주 조용히 시선을 들어 그 애들 뒷모습을 봤다."

    show yuna surprise at left, excited_hop with dissolve
    yn "방금…"

    show harin surprise at center_lower, excited_hop with dissolve
    hr "들었지."

    show seola smile at right, tiny_bounce with dissolve
    sa "응."

    sj "첫 외부 평가네."

    ge "좋네."
    ge "엄청 좋은데?"

    scene bg noisy_hallway with dissolve

    "유나는 바로 웃을 줄 알았는데,"
    "이번엔 잠깐 멍한 얼굴이었다."
    "정말 예상 못 한 곳에서 칭찬을 받아 버린 사람 같은 표정."

    show yuna smile at left, tiny_bounce with dissolve
    yn "……와."
    yn "저 지금 조금 감동."

    sj "너 아까도 그 말 했잖아."

    yn "아니, 이번 건 진짜예요."
    yn "우리끼리 좋다고 한 거 말고,"
    yn "다른 사람이 보고 예쁘다고 한 거잖아요."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "그러네."

    "하린이도 아주 작게 웃었다."
    "평소보다 조금 더 힘 빠진, 편한 웃음이었다."

    sa "괜히 기분 좋다."

    "설아가 그렇게 말했고,"
    "그 말에 아무도 토를 달지 않았다."
    "정말로 다 같은 기분이었으니까."

    th "별거 아닌 한마디."
    th "근데 왜 이렇게 뿌듯하지."

    scene bg noisy_hallway with dissolve

    "그 뒤로도 몇 분 정도 더 대강 위치를 바꿔 보며 확인했다."
    "그런데 이미 분위기는 정해져 있었다."
    "첫 칭찬 한 번으로 다들 기분이 눈에 띄게 부드러워졌다."

    show yuna smile at left, tiny_bounce with dissolve
    yn "좋아."
    yn "그럼 오늘의 목표 달성."

    sj "외부 공개 성공?"

    yn "네."
    yn "그리고 외부 반응 획득 성공."

    hr "말은 거창했는데 결과도 나쁘지 않네."

    sa "처음으로 바깥 말 들은 날."

    ge "그것도 어록감인데."

    sj "또 늘리냐."

    show yuna grin at left, idle_bounce with dissolve
    yn "당연하죠."
    yn "'예쁘다' 추가."
    sj "그건 어록이라기보다 그냥 평가잖아."

    sa "그래도 남기고 싶어."

    "설아가 그렇게 말하자,"
    "유나는 진짜로 휴대폰 메모장에"
    "'예쁘다 - 지나가던 학생 2명'"
    "이라고 적어 넣었다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "너무 구체적이네."

    yn "중요하니까요."

    scene bg noisy_hallway with dissolve

    "가은 선배는 그런 우리를 가만히 보다가,"
    "아주 만족스러운 얼굴로 웃었다."

    show gaeun smile at far_right, tiny_bounce with dissolve
    ge "좋다."
    ge "너희 지금 엄청 팀 같다."

    sj "요즘 맨날 그 소리 하네요."

    ge "왜냐면 매번 더 그래지니까."

    "그 말에 유나는 괜히 어깨를 폈고,"
    "하린이는 괜히 아닌 척 안내판 모서리를 다시 만졌고,"
    "설아는 게시판 유리창에 희미하게 비친 우리를 잠깐 봤다."

    "나도 무심코 그쪽을 따라 봤다."
    "안내판 하나를 사이에 두고,"
    "자연스럽게 모여 선 다섯 사람."
    "누가 봐도 같은 일 하다가 나온 얼굴들."

    th "진짜 그렇게 보이나."

    th "…보이겠지."
    th "이 정도면."

    scene black with dissolve
    centered "{size=30}다시 준비실{/size}" with dissolve

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 1.0

    "우리는 안내판을 다시 준비실 안으로 가져왔다."
    "아직 완전히 밖에 붙일 단계는 아니었지만,"
    "이제 정말 곧이라는 생각이 들었다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin normal at center_lower, sway_soft with dissolve
    show seola normal at right, sway_soft with dissolve
    show gaeun smile at far_right, tiny_bounce with dissolve

    yn "좋아."
    yn "기념으로 오늘 간식 먹어도 되죠?"

    sj "결국 또 그거냐."

    hr "뭐 가져왔는데."

    show yuna laugh at left, idle_bounce with dissolve
    yn "오늘은 초코볼입니다."
    yn "외부 평가 성공 기념."

    sa "명분이 점점 늘어나."

    ge "근데 오늘은 인정."

    "유나는 가방에서 작은 초코볼 봉지를 꺼냈다."
    "이번엔 정말 안전거리를 지키는 듯"
    "책상 한쪽 제일 구석에 조심히 올려놨다."

    sj "벚꽃 습격 이후로 배운 건 있네."

    show yuna grin at left, idle_bounce with dissolve
    yn "당연하죠."
    yn "저도 성장하는 사람입니다."

    hr "그건 맞네."
    sa "오늘은 사고 없을 듯."

    "결국 우리는 초코볼 몇 알씩 나눠 먹으며,"
    "방금 들었던 짧은 칭찬 이야기를 또 한 번 꺼냈다."

    scene bg old_library with dissolve

    "누가 먼저랄 것도 없이,"
    "'예쁘다'라는 단어를 각자 한 번쯤 되짚었다."

    show harin faint_smile at center_lower, tiny_bounce with dissolve
    hr "솔직히."
    hr "조금 더 다듬어야 한다고 생각했는데,"
    hr "지나가다 보기엔 충분한가 봐."

    show seola smile at right, tiny_bounce with dissolve
    sa "응."
    sa "우리가 너무 가까이서만 봤나 봐."

    show yuna smile at left, tiny_bounce with dissolve
    yn "근데 전."
    yn "그냥 우리끼리 좋다고 했던 것도 좋았어요."
    yn "오늘은 거기에 하나 더 생긴 느낌."

    sj "외부 검증 완료?"

    yn "네."
    yn "조용한 봄 공식 인증."

    ge "누가 인증했는데?"
    yn "지나가던 학생 2명."

    "가은 선배가 웃음을 터뜨렸고,"
    "나도 결국 따라 웃었다."

    scene bg old_library with dissolve

    "그날 준비실 안의 공기는,"
    "평소보다 조금 더 가벼웠다."
    "작업이 엄청 진척된 것도 아니고,"
    "큰 사건이 생긴 것도 아닌데,"
    "바깥에서 들은 짧은 칭찬 하나가"
    "이상할 정도로 오래 기분을 띄워 놓았다."

    th "정말 단순하네."
    th "근데 이런 걸로 충분한 날도 있지."

    "창가 쪽 별 장식이 아주 약하게 흔들렸다."
    "어록 메모지 한쪽엔 유나가 적은 새 줄이 추가돼 있었다."

    "'예쁘다' - 지나가던 학생 2명"

    "정말 유치한 기록인데,"
    "이상하게 지우고 싶진 않았다."

    scene black with dissolve
    centered "{size=30}복도{/size}" with dissolve

    scene bg noisy_hallway with fade
    play music "audio/bgm_noisy_hallway.ogg" fadein 1.2

    "예비종이 울리기 전,"
    "우리는 준비실 문 앞에 잠깐 모여 섰다."

    show yuna smile at left, tiny_bounce with dissolve
    show harin faint_smile at center_lower, tiny_bounce with dissolve
    show seola smile at right, tiny_bounce with dissolve

    yn "좋아."
    yn "오늘의 결론."

    sj "또 나온다."

    yn "외부 반응도 성공."
    hr "인정."
    sa "예쁘다도 얻었고."
    ge "초코볼도 무사했고."

    sj "마지막은 왜 들어가."

    show yuna laugh at left, idle_bounce with dissolve
    yn "중요하잖아요."

    "또 웃음이 번졌다."
    "복도엔 여전히 다른 학생들 발소리가 오갔지만,"
    "우리 쪽 공기만은 이상하게 조금 느슨하고 따뜻했다."

    th "우리끼리만의 시간."
    th "그리고 그 바깥에서 잠깐 닿아 온 말 한마디."

    th "그 둘이 섞이니까."
    th "오늘은 이상하게 더 오래 남을 것 같다."

    play sound "audio/sfx_school_bell.ogg"

    "본종이 울렸다."
    "우리는 다시 각자 흩어졌다."

    "교실로 돌아가는 길."
    "방금 복도에서 들었던 그 짧은 말이 계속 귀에 남았다."

    th "예쁘다."

    th "……뭐."
    th "틀린 말은 아니었네."

    scene black with fade

    # ---------------------------------------------------------
    # Scene 27

    centered "{size=40}Scene 27{/size}\n\n{size=30}같이 고르는 사소한 것들{/size}" with dissolve
    pause 1.5

    scene bg old_library with fade
    play music "audio/bgm_lazy_afternoon.ogg" fadein 2.0

    play sound "audio/sfw_walking.ogg"
    "다음 날 점심시간."
    "준비실 문 앞에 서자, 안쪽에서부터 익숙한 웃음소리가 새어 나왔다."
    "낮고 조용한 웃음, 짧게 툭 튀는 말소리, 그리고 누가 종이를 정리하는 바스락거림."
    "그 소리들만으로도 안에 누가 있는지 조금은 알 것 같았다."

    th "이제는 문 열기 전부터 분위기가 상상된다."
    th "누가 먼저 와 있을지, 누가 또 무슨 말을 하고 있을지."
    th "그걸 생각하면서 문 앞에 멈추는 일도 이제는 꽤 자연스러워졌다."

    play sound "audio/sfx_Sliding_door.ogg"
    "서진이 문을 열었다."

    show harin normal at char_1, sway_soft
    show yuna smile at char_2, idle_bounce
    show seola normal at char_3, tiny_bounce
    show gaeun smile at char_4, soft_bounce, tiny_bounce
    with dissolve

    yn "왔네!"
    play sound "audio/sfw_cloth_moving.ogg"
    "유나는 의자에서 거의 튀어 오르듯 몸을 일으켰다."
    "정말로 폴짝, 하고 가벼운 탄력이 느껴질 정도였다."

    hr "아직 안 늦었어."
    hr "점심 끝나기 3분 전이니까."

    ge "딱 좋은 타이밍이네."

    sa "지금 중요한 거 고르는 중이야."

    sj "중요한 거?"

    play sound "audio/sfw_walking.ogg"
    "서진이 책상 쪽으로 다가가자 색지들이 한가득 펼쳐져 있는 게 보였다."
    "연분홍, 크림색, 연하늘, 연두색."
    "전부 봄 같고, 전부 준비실이랑 잘 어울릴 것 같은 색들이었다."

    yn "부스 앞에 놓을 작은 소개카드!"
    play sound "audio/sfx_paper_flutter.ogg"
    "유나는 두 손으로 카드들을 부채처럼 펼쳐 보였다."
    "잘 봐달라는 것처럼 손끝이 붕붕 신나 있었다."

    yn "근데 지금 색 조합 때문에 의견이 갈리고 있습니다."
    hr "정확히는 유나가 너무 많이 꺼내놔서 정리가 안 되는 거지."

    yn "이건 선택지를 풍부하게 한 거야."

    sa "보기는 예뻐."
    sa "그래서 더 못 고르겠어."

    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "설아는 카드 한 장을 살짝 끌어와 눈앞에서 가만히 비교했다."
    "동작은 작았는데, 괜히 집중하게 만드는 힘이 있었다."

    ge "나는 크림색도 좋고 연분홍도 좋더라."
    hr "나는 크림색."
    sa "나는 연하늘."

    yn "나는 다 좋아."
    sj "그건 의견이 아니잖아."

    "유나는 억울하다는 듯 입술을 조금 내밀더니, 금방 또 웃었다."

    yn "왜. 다 예쁘면 다 좋다고 할 수도 있지."
    yn "굳이 하나만 고르기 아깝단 말이야."

    hr "유나는 원래 아쉬운 걸 제일 싫어하잖아."

    sa "맞아."
    sa "좋은 게 많으면 다 잡고 싶어 해."

    yn "그건 부정 못 하겠다."

    play sound "audio/sfw_cloth_moving.ogg"
    "유나는 괜히 발뒤꿈치를 들썩였다."
    "가만히 있으려는 척은 하는데, 기분 좋은 건 몸이 먼저 말해 주는 사람 같았다."

    hr "서진, 너는?"
    hr "의견 하나 내봐."

    play sound "audio/sfw_walking.ogg"
    "서진이 책상 가까이 섰다."
    "색지들을 하나씩 내려다보자 다 비슷한 듯하면서도 미묘하게 분위기가 달랐다."

    th "크림색은 편안하고."
    th "연하늘은 맑고."
    th "연분홍은 눈에 더 들어오고."
    th "연두는 유나 같네."

    sj "크림색 바탕에 연하늘 포인트."
    sj "튀지는 않는데 너무 심심하지도 않고."
    sj "글씨도 제일 잘 보일 것 같은데."

    "잠깐 조용해졌다."
    "유나가 눈을 동그랗게 떴다가, 서진을 빤히 봤다."

    yn "어."
    yn "생각보다 엄청 멀쩡한 의견이 나왔어."

    sj "무슨 뜻이야."

    ge "유나야, 그건 칭찬이 아니지."

    hr "아니, 근데 진짜 괜찮네."
    hr "깔끔하고 보기 편할 것 같아."

    sa "응."
    sa "눈에 오래 남을 것 같아."

    "설아가 조용히 끄덕이자, 그걸로 거의 결정이 끝난 분위기가 났다."

    yn "좋아!"
    show yuna smile at char_2, excited_hop
    "유나는 진짜로 작게 폴짝 뛰었다."
    play sound "audio/sfx_paper_flutter.ogg"
    "그리고는 바로 카드 한 장을 집어 서진 쪽으로 쏙 내밀었다."

    yn "그럼 의견 낸 사람이 첫 장 써."
    yn "채택된 안의 책임자."

    sj "왜 내가."
    hr "의견 냈잖아."
    sa "써."
    ge "좋은 의견 냈으니까."

    "세 사람의 짧고 단단한 동의가 겹치자 서진은 결국 펜을 들었다."

    th "이상하게 여기선 빠져나가기 힘들다."
    th "아니, 꼭 빠져나가야 할 이유가 없어진 건가."

    play sound "audio/sfw_running.ogg" volume 0.8
    "유나는 서진 옆으로 쪼르르 다가와 카드 위를 내려다봤다."
    play sound "audio/sfw_cloth_moving.ogg"
    "하린도 반듯하게 카드들을 가지런히 밀어 주고, 설아는 조용히 옆에 서서 손끝으로 카드 모서리를 눌렀다."
    "가은 선배도 웃으며 책상 쪽으로 몸을 조금 기울였다."

    yn "문구는 이 셋 중 하나!"
    yn "첫 번째, 잠깐 쉬어 가도 괜찮은 곳."
    yn "두 번째, 천천히 보고 편하게 머물다 가는 곳."
    yn "세 번째, 오늘의 봄을 조금 가져갈 수 있는 곳."

    ge "세 번째, 예쁘다."

    hr "예쁘긴 한데 살짝 문학부 감성 같기도 하고."

    sa "그래도 좋아."
    sa "조금 남는 말이야."

    play sound "audio/sfx_pen_click.ogg"
    "서진은 펜 끝을 카드 위에 가볍게 톡 얹었다."

    sj "세 번째로 하자."
    sj "딱 우리 같아."

    "유나가 바로 활짝 웃었다."
    "좋아하는 말이 나오면 표정부터 먼저 환해지는 사람답게, 얼굴이 금방 밝아졌다."

    yn "봐."
    yn "나만 그렇게 생각한 거 아니잖아."

    hr "이번엔 인정."
    ge "그럼 첫 장은 그걸로 쓰자."

    "서진은 천천히 글씨를 써 내려갔다."

    "오늘의 봄을 조금 가져갈 수 있는 곳."

    "마지막 글자를 적고 펜을 떼자, 자연스럽게 모두의 시선이 카드 위로 모였다."
    "정말 조그만 카드 한 장인데도 다들 의외로 진지했다."
    "그 진지함이 웃기기보다 좋았다."

    ge "예쁘다."
    sa "응."
    hr "글씨도 괜찮네."
    yn "오."
    yn "서진, 너 글씨 좋네?"

    sj "왜 다들 놀라는 건데."

    yn "왠지 네 글씨는 좀 날아다닐 줄 알았어."

    "유나는 손으로 허공에 휙휙 이상한 궤적까지 그려 보였다."
    "서진은 어이없다는 듯 피식 웃었다."

    sj "나를 대체 뭘로 본 거야."
    sa "조금 그럴 줄 알긴 했어."
    hr "나도."
    ge "의외라서 더 좋은 거지."

    "괜히 억울한데, 다들 웃고 있으니까 같이 웃게 됐다."

    th "이제는 이런 식으로 놀려도 기분이 안 나쁘다."
    th "대충 던지는 말이 아니라, 그냥 같이 웃고 싶어서 하는 말이라는 걸 아니까."

    yn "좋아, 그럼 이제 글씨 릴레이!"
    play sound "audio/sfx_paper_flutter.ogg"
    "유나는 다음 카드를 번쩍 들어 올렸다."
    "손끝에 힘이 잔뜩 들어가 있어서 카드가 괜히 더 가볍게 펄럭였다."

    hr "결국 다 써야 하니까 돌아가면서 하는 거잖아."
    yn "맞아."
    yn "근데 릴레이라고 하면 더 재밌잖아."

    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "두 번째는 하린 차례였다."
    "하린은 카드를 자기 앞으로 슥 끌어오더니, 아주 반듯하게 각을 맞췄다."
    play sound "audio/sfx_pen_click.ogg"
    "그러고는 망설임 없이 글씨를 적기 시작했다."

    "획 하나, 간격 하나까지 흐트러짐이 없었다."

    ge "와, 진짜 단정하다."
    yn "이건 교본 글씨체야."
    sa "믿음직해 보여."

    hr "글씨가 왜 믿음직해."

    sa "왠지 틀린 말 안 적을 것 같아."

    "하린이 순간 웃음을 참지 못하고 입꼬리를 살짝 올렸다."
    "그 작은 변화가 이상하게 눈에 잘 들어왔다."

    th "처음엔 웃는 것도 아껴 쓰는 사람 같았는데."
    th "요즘은 저런 순간이 확실히 늘었다."

    "세 번째는 설아였다."
    "설아는 카드를 양손으로 조심히 잡고 한 번 가만히 내려다봤다."
    play sound "audio/sfx_pen_click.ogg"
    "그리고 느리지만 망설임 없는 손으로 글씨를 써 내려갔다."

    "얇고, 단정하고, 조용한 글씨였다."
    "크게 튀진 않는데 이상하게 오래 보게 되는 글씨."

    yn "설아 글씨 예쁘다."
    ge "응, 진짜."
    hr "사람이랑 비슷하네."
    sa "뭐가."
    hr "조용한데 남는 거."

    "설아가 눈을 깜빡이다가 작게 웃었다."
    "정말 잠깐, 배시시 스치는 정도였는데 그게 오히려 더 설아다웠다."

    yn "방금 웃었지."
    yn "이것도 기록해야 해."
    sa "하지 마."

    "네 번째는 가은 선배였다."
    "가은은 카드를 받아 들며 웃었고, 펜을 잡는 손에도 여유가 있었다."
    play sound "audio/sfx_pen_click.ogg"
    "글씨는 예상보다 훨씬 부드럽고 둥글었다."

    sj "선배 글씨 좀 의외네요."
    ge "어떤 쪽으로?"
    sj "좀 더 딱딱할 줄 알았어요."

    yn "맞아."
    yn "회의록 장인 느낌일 줄 알았는데."

    ge "너희 나를 대체 어떤 사람으로 보는 거야."

    hr "은근 다들 비슷하게 생각하고 있었네."

    sa "그래도 이 글씨 좋아."
    sa "보기 편해."

    ge "그 말이면 충분하다."

    "마지막은 유나 차례였다."
    "모두의 시선이 자연스럽게 유나에게 모였다."
    "유나는 괜히 헛기침을 한 번 하더니, 어깨를 들썩였다."

    yn "왜 다들 그렇게 쳐다봐."
    yn "나도 충분히 차분하게 쓸 수 있거든?"

    hr "불안해서 그래."
    sa "하트 넣을 것 같아."
    sj "꽃도 넣을 것 같은데."
    ge "둘 다 가능성 있어."

    yn "진짜 너무해!"

    "유나는 억울하다는 듯 외쳤지만, 이미 웃고 있었다."
    play sound "audio/sfx_pen_click.ogg"
    "그리고 카드를 자기 앞으로 끌어오더니 혀를 조금 내밀고 엄청 진지한 표정으로 글씨를 쓰기 시작했다."

    play sound "audio/sfx_paper_flutter.ogg"
    "다 적고 난 뒤, 유나는 의기양양하게 카드를 들었다."

    "그런데 문장 끝에 아주 조그만 꽃잎 무늬가 하나 붙어 있었다."

    hr "결국 넣었네."
    sa "못 참았네."
    sj "차분하게 쓴다며."
    ge "근데 유나답고 귀엽다."

    "유나는 카드로 입을 반쯤 가리면서 키득키득 웃었다."

    yn "이건 장식이지."
    yn "진짜 하트는 아니잖아."

    hr "그 논리 처음 듣는다."

    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "책상 위에는 어느새 다섯 장의 카드가 나란히 놓였다."
    "똑같은 문장을 적었는데도 전부 분위기가 달랐다."

    "하린의 카드는 반듯했고."
    "설아의 카드는 조용했고."
    "가은의 카드는 부드러웠고."
    "유나의 카드는 생기가 있었고."
    "서진의 카드는 생각보다 담백했다."

    ge "같은 문장인데도 다 다르네."
    sa "응."
    sa "누가 썼는지 보여."
    hr "통일감이 없는 게 아니라..."
    hr "오히려 그래서 더 좋네."

    yn "그치!"
    yn "우리 원래 다 다르잖아."
    yn "근데 같이 놓으면 또 어울리고."

    play sound "audio/sfw_walking.ogg" volume 0.7
    "유나는 카드들을 하나씩 세워 두고, 뒤로 한 걸음 물러났다."
    "그러고는 양손을 허리에 얹고 한참 바라보다가 만족스럽게 고개를 끄덕였다."

    yn "좋아."
    yn "이건 분명 손님들도 좋아할 거야."

    hr "확신이 빠르네."
    yn "좋은 건 빨리 확신해 줘야 해."
    sa "좋은 건 꽉 잡아야 하거든요."

    "설아가 예전 말을 아주 자연스럽게 꺼내자 유나가 바로 웃음을 터뜨렸다."
    "준비실 안에 작은 웃음이 퍼졌다."

    ge "이제는 다들 어록을 자연스럽게 쓰네."
    sj "그러게요."

    th "처음엔 조금 오글거린다고 생각했는데."
    th "이제는 그 말들이 이 준비실에 잘 어울린다."
    th "여기서만 통하는 말 같아서 더 그런지도 모르겠다."

    play sound "audio/sfx_school_bell.ogg"
    "복도에서 종이 울렸다."
    "점심시간이 끝나 간다는 뜻이었다."

    play sound "audio/sfw_cloth_moving.ogg"
    "하지만 누구도 바로 움직이지 않았다."
    "다들 한 번쯤은 카드들을 다시 보고, 책상을 다시 보고, 서로를 한 번 더 본 뒤에야 천천히 가방을 챙겼다."

    yn "아, 진짜 너무 짧다."
    play sound "audio/sfx_pen_click.ogg" volume 0.5
    "유나는 아쉬운 얼굴로 책상에 손끝을 톡톡 두드렸다."

    hr "점심시간은 원래 짧아."
    sa "여기는 더 짧아."
    ge "그건 맞아."

    "서진은 창가를 한 번 바라봤다."
    "별 장식이 바람에 아주 살짝 흔들리고 있었다."
    "그 아래에는 조금 전까지 다섯 사람이 머리를 맞대고 들여다보던 카드들이 가지런히 놓여 있었다."

    th "이런 건 나중에도 생각나겠지."
    th "누가 어떤 글씨를 썼는지."
    th "누가 또 장식을 못 참고 하나 더 붙였는지."
    th "별것 아닌 걸 고르는데도 다들 이상할 만큼 진심이었다는 것도."

    play sound "audio/sfx_paper_flutter.ogg"
    "하린이 카드를 조심히 한데 모아 들었다."

    hr "내가 서랍에 넣어 둘게."
    hr "구겨지면 아깝잖아."

    yn "역시 체크리스트 반장."
    hr "그 별명도 안 끝났어?"
    sa "굳었어."
    ge "여기선 한 번 붙은 건 잘 안 없어지네."
    sj "그러게요."

    "유나는 마지막 카드를 한 번 더 돌아봤다."
    "그리고는 괜히 만족스러운 얼굴로 생긋 웃었다."

    yn "오늘 것도 성공이다."
    sa "응."
    sa "성공."
    ge "완전."
    hr "인정."

    "서진도 작게 고개를 끄덕였다."

    sj "성공이네."

    "그 한마디에 유나 표정이 더 밝아졌다."
    "정작 본인은 숨기려는 것 같았지만, 기쁜 건 다 티가 났다."

    th "이상하게도 이제는 이런 사소한 합의가 좋다."
    th "누가 크게 말하지 않아도, 다들 비슷한 마음이라는 걸 알게 되는 순간들이."

    play sound "audio/sfw_walking.ogg"
    "준비실 문을 나서기 직전, 설아가 뒤를 돌아봤다."
    "책상 위의 색지와 펜, 창가의 별 장식, 그리고 조금 전까지 다섯 사람이 모여 있던 자리."

    sa "다음에도 이거 하자."

    yn "소개카드?"
    sa "아니."
    sa "이런 거."
    sa "같이 고르는 거."

    "잠깐 조용해졌다."
    "정말 별말 아닌데도, 다들 설아가 무슨 뜻으로 말했는지 바로 알아들었다."

    ge "좋지."
    hr "응."
    sj "그래."
    sj "계속 해도 되겠다."

    show yuna smile at char_2, excited_hop
    yn "좋아!"
    yn "그럼 결정!"
    yn "우리 팀은 앞으로도 사소한 것에 진심이기로!"

    hr "그건 이미 그렇지 않아?"
    sa "맞아."
    ge "이제 와서 선언할 필요도 없을 정도로."

    "다시 웃음이 번졌다."
    "준비실 안에 남아 있던 따뜻한 공기가, 문을 나서는 마지막 순간까지도 다섯 사람을 따라오는 것 같았다."

    play sound "audio/sfw_walking.ogg"
    "점심시간은 끝났고, 수업은 다시 시작될 거고, 오늘도 금방 지나갈 것이다."
    "그런데도 이상하게 괜찮았다."

    "방금 전까지 같이 고른 사소한 것들이, 남은 하루를 조금 더 다정하게 만들어 줄 것 같아서."

    stop music fadeout 2.0

    # ---------------------------------------------------------
    # Scene 28
    scene black with fade
    centered "{size=40}Scene 28{/size}

{size=30}끝나기 전에 한 번 더{/size}" with dissolve
    pause 1.5

    scene bg classroom with fade
    play music "audio/bgm_playful_bickering.ogg" fadein 2.0

    "종례가 끝난 뒤의 교실은 늘 비슷하다."
    "의자가 끌리는 소리, 가방 지퍼를 여닫는 소리, 오늘 하루를 다 털어낸 듯한 한숨과 웃음이 뒤섞이며 순식간에 어수선해진다."
    play sound "audio/sfw_school_crowd.ogg" volume 0.6
    "그 소란 속에서도 우리 반 창가 쪽에는 이상하리만치 익숙한 흐름이 생겨 있었다."
    stop sound fadeout 1.0
    "누가 먼저 말하지 않아도, 다섯 사람의 시선이 자연스럽게 한곳으로 모인다."

    show harin normal at center_lower with dissolve
    hr "오늘은 준비실 가기 전에 교실 뒤 게시판부터 정리해야 해."
    hr "축제 공지 종이가 모서리부터 들뜨기 시작했어. 저 상태면 내일 아침엔 반쯤 떨어져 있을 거야."

    show yuna smile at char_2 with dissolve
    yn "반장님 레이더 또 발동했다."
    yn "진짜 그런 건 어떻게 그렇게 제일 먼저 보여요?"

    show seola smile at char_4 with dissolve
    sa "하린은 그런 걸 보면 못 지나가."

    show gaeun smile at right_mid with dissolve
    ge "직업병 같은 거지. 반장병."

    hr "그런 이상한 병명 붙이지 마."
    hr "그리고 너희도 오늘은 그냥 지나갈 생각 아니지?"

    sj "이미 불려온 표정인데 뭘 새삼."
    th "요즘은 방과 후가 되면 각자 알아서 준비실로 가기 전에 한 번쯤 뭉친다."
    th "처음엔 누가 누구를 따라온다는 느낌이었는데, 이제는 그냥 원래 그런 순서처럼 굳어졌다."

    play sound "audio/sfx_paper_flutter.ogg" volume 0.5
    "하린은 들뜬 공지 종이의 모서리를 손끝으로 눌러보며 미세하게 인상을 찌푸렸다."
    "유나는 그런 하린의 옆얼굴을 보고 괜히 킥킥 웃더니 자기 가방을 책상 위에 턱 올려놓았다."

    yn "좋아, 그럼 오늘의 미션은 게시판 구조 작전!"
    yn "가은 선배는 높이 담당, 하린 선배는 정렬 담당, 설아 선배는 감성 감독, 서진 선배는 힘 담당."
    sj "나는 왜 늘 힘 담당이냐."
    yn "든든해 보이니까."
    ge "좋은 말 같은데 묘하게 잡일 배정 같다?"

    show yuna laugh with dissolve
    "유나는 그렇게 말하고는 맨 먼저 교실 뒤로 쪼르르 달려갔다."
    play sound "audio/sfw_running.ogg" volume 0.7
    "타닥타닥, 경쾌한 발소리 뒤로 봄 저녁의 공기가 얇게 흔들렸다."
    stop sound fadeout 0.7

    scene bg classroom with dissolve
    show harin sigh at left_mid with dissolve
    show yuna smile at char_2 with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    "결국 다 같이 게시판 앞에 모여들었다."
    "색이 바랜 공지 종이와 살짝 기울어진 장식 테이프 몇 줄을 손보는 것뿐인데도, 이상하게 다들 제법 진지했다."

    hr "유나, 테이프는 한 번에 길게 자르지 마."
    hr "끝이 접히면 보기 안 좋아."
    yn "아, 들켰다."
    yn "근데 이 정도는 티 안 나지 않아요?"

    hr "내 눈엔 보여."
    ge "그 말은 이미 끝났다는 뜻이네."

    play sound "audio/sfx_paper_cut.ogg" volume 0.6
    "설아가 조용히 가위를 들어 삐뚤어진 테이프 끝을 정리했다."
    "짧고 깔끔한 소리와 함께 접힌 부분이 반듯하게 잘려 나갔다."

    sa "이제 괜찮아."
    sa "하린이 화 안 나도 돼."

    show harin faint_smile with dissolve
    hr "…화 안 났어."
    sj "조금 났던 것 같은데."
    ge "조금보다 반 정도?"

    show harin annoyed with dissolve
    hr "안 났다니까."

    show yuna laugh at char_2, excited_hop
    yn "아하하, 표정이 이미 말해주는데?"

    "하린이 차갑게 노려보자 유나는 금방 입을 꾹 다물었지만, 눈웃음만은 전혀 숨기지 못했다."
    th "예전 같았으면 저 시선 하나에 교실 전체가 조용해졌을 텐데."
    th "이제는 다들 그 안에 진짜 화보다 익숙한 체념이 더 많다는 걸 안다."

    play sound "audio/sfw_cloth_moving.ogg" volume 0.6
    "가은 선배가 의자를 끌어다 게시판 앞에 섰다."
    "까치발을 들고 윗부분을 누르자, 노을빛이 들어온 교실 창문 쪽에서 긴 그림자가 천천히 기울었다."

    ge "이쯤?"
    hr "왼쪽 1센티만."
    ge "정확히 1센티?"
    hr "대충 말한 건데 진짜 딱 그 정도야."
    sj "무섭네."
    sa "하린은 눈금자가 몸에 들어 있는 것 같아."

    show harin smile with dissolve
    hr "그건 좀 웃긴 비유네."

    "설아의 담담한 한마디에 하린의 입가가 아주 잠깐 풀렸다."
    "유나는 그 작은 변화도 놓치지 않고 바로 손가락으로 허공을 콕 찔렀다."

    yn "방금 웃음 적립."
    yn "오늘도 성공."

    sj "그 적립 기준은 대체 누가 정하냐."
    yn "당연히 나지."
    ge "독재 국가네."

    play sound "audio/sfx_ui_click.ogg" volume 0.5
    "유나는 자기 혼자 만족스러운 얼굴로 허공에 도장을 찍듯 손을 툭 내렸다."

    "별것 아닌 정리가 끝났을 뿐인데 게시판은 묘하게 더 반듯해졌고, 교실 뒤편은 조금 더 우리 손을 탄 자리처럼 보였다."
    "다들 한 걸음 물러나 그 결과를 바라봤다."

    sa "조금 달라졌어."
    ge "응. 작은데 티 난다."
    hr "원래 이런 건 작은 차이가 커."
    yn "맞아."
    yn "우리도 맨 처음엔 이렇게 안 친했잖아."

    "순간 다들 조용해졌다."
    "유나는 별 생각 없이 툭 던진 말 같았지만, 그래서 더 진심처럼 들렸다."

    sj "그건 맞네."
    sj "처음엔 다들 이렇게 오래 같이 있을 줄 몰랐지."

    show seola smile with dissolve
    sa "지금은 안 이상해."
    sa "같이 있는 게."

    ge "그러게."
    ge "이제는 안 모이면 오히려 허전할 것 같은데?"

    show yuna smile with dissolve
    yn "봐봐!"
    yn "내가 말했잖아. 우리 팀 은근 잘 맞는다고."

    hr "은근이 아니라 이미 많이 맞아."

    "하린이 아주 자연스럽게 그렇게 말하자 유나가 잠깐 눈을 깜빡였다."
    "그리고는 곧바로 환하게 웃으며 두 손으로 자기 입을 가렸다."

    yn "서하린한테 방금 공식 인정 받았다…!"
    yn "오늘 일기장에 적어야지."
    hr "그런 건 또 적지 마."
    sa "이미 적었을 얼굴이야."
    ge "맞아, 지금 표정 완전 저장 완료인데."

    play sound "audio/sfx_school_bell.ogg" volume 0.7
    "멀리서 늦은 예비종 같은 소리가 작게 울렸다."
    "당장 뛰어가야 할 만큼 급한 시간은 아니었지만, 그래도 방과 후의 공기가 슬슬 다음 순서를 재촉하기 시작했다."

    sj "가자. 준비실도 가야지."
    yn "응!"

    play sound "audio/sfw_walking.ogg"
    "다섯 사람은 거의 동시에 몸을 돌렸다."
    "누가 먼저라고 할 것도 없이, 발걸음이 하나의 흐름처럼 복도로 이어졌다."
    stop sound fadeout 1.0

    # ---------------------------------------------------------
    # Scene 29
    scene black with fade
    centered "{size=40}Scene 29{/size}

{size=30}사서 먹는 시간{/size}" with dissolve
    pause 1.5

    scene bg store with fade
    play music "audio/bgm_comedic_yuna.ogg" fadein 2.0

    "준비실 작업은 생각보다 빨리 끝났다."
    "색지를 정리하고, 메모해 둔 목록을 다시 맞추고, 내일 쓸 것들을 한쪽에 모아두고 나니 아직 해가 완전히 지기 전의 애매한 여유가 남았다."
    "그 애매한 틈을 유나가 놓칠 리 없었다."

    show yuna grin at char_2 with dissolve
    yn "좋아, 오늘은 해산 전에 보급이다!"
    yn "다들 저녁 전이니까 애매하게 출출하죠?"

    show harin normal at left_mid with dissolve
    hr "애매하게라는 말이 제일 위험해."
    hr "그럴 때 군것질하면 저녁 망쳐."

    show gaeun laugh at right_mid with dissolve
    ge "근데 그 애매한 때 먹는 게 제일 맛있잖아."

    show seola smile at char_4 with dissolve
    sa "맞아."
    sa "애매해서 더 좋을 때 있어."

    sj "둘이 손잡고 유나 편 드네."

    "매점 앞 작은 냉장 진열장과 과자 선반 앞은 방과 후 특유의 달콤한 냄새로 가득했다."
    "유나는 이미 신난 얼굴로 이쪽저쪽을 훑고 있었고, 가은 선배는 뒤에서 여유롭게 웃으며 그걸 구경했다."

    play sound "audio/sfx_ui_hover.ogg" volume 0.4
    "유나의 손가락이 선반 위를 이리저리 훑을 때마다 포장지가 바스락거렸다."

    yn "오늘은 각자 하나씩 고르기 금지."
    yn "서로 하나씩 추천해 주기!"

    hr "왜 그런 룰이 또 생겨."
    yn "재밌잖아요."
    yn "자기 취향만 고르면 맨날 비슷한 것만 먹게 되니까, 오늘은 상대 취향 생각해서 고르는 거지."

    ge "오, 그거 괜찮다."
    ge "생각보다 성격 보이겠네."

    sa "누가 누구 거 고를지 정해야 해."
    sj "괜히 복잡해지는데."

    show yuna vivid with dissolve
    yn "이미 정했어요!"
    yn "하린 선배는 서진 선배 거, 서진 선배는 설아 선배 거, 설아 선배는 가은 선배 거, 가은 선배는 내 거, 나는 하린 선배 거!"

    hr "왜 제일 마지막에 네가 제일 신난 목소리야."
    yn "중요하니까!"

    "어이없다는 말이 여기저기서 나왔지만, 이상하게 아무도 진짜로 거절하지는 않았다."
    th "이제는 다들 안다."
    th "유나가 이런 걸 제안했을 때 가장 재밌는 결론은, 대충 따라가 주는 쪽에서 나온다는 걸."

    play sound "audio/sfw_walking.ogg" volume 0.7
    "각자 선반 앞에 흩어졌다."
    "하린은 성분표라도 볼 듯 진지한 얼굴로 포장을 뒤집어 보고 있었고, 설아는 냉장칸 앞에서 한참을 가만히 서 있었다."
    "가은 선배는 유나가 뭘 좋아할지 이미 감이 온다는 표정으로 음료 코너를 둘러봤고, 유나는 웬일로 장난을 줄이고 과자 봉지를 엄숙하게 들여다봤다."
    stop sound fadeout 0.8

    scene bg store with dissolve
    show harin normal at left_mid with dissolve
    show yuna normal at char_2 with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    "잠시 뒤, 다섯 사람은 계산대 옆 좁은 공간에 다시 모였다."
    "각자 고른 것들을 손에 들고 있는데, 그 조합이 묘하게 웃겼다."

    hr "이거."
    "하린은 내 쪽으로 지나치게 달지 않은 곡물 바 하나를 내밀었다."
    hr "네가 단 건 잘 안 먹고, 그렇다고 너무 퍽퍽한 것도 싫어하잖아."

    sj "…언제 그걸 다 파악했냐."
    hr "옆자리였잖아, 한동안."
    hr "그리고 너 은근 표정에 다 써 있어."

    ge "와, 관찰력 무섭다."
    yn "역시 체크리스트 반장답다. 먹는 취향도 데이터화돼 있어."

    show harin annoyed with dissolve
    hr "체크리스트 반장은 이제 별명이 된 거야?"
    sa "응."
    sa "안 없어질 것 같아."

    "하린은 체념한 듯 한숨을 쉬었지만, 입가에는 미세한 웃음이 걸려 있었다."

    sj "그럼 내 차례."
    "나는 설아에게 작게 흔드는 캔 음료 하나를 내밀었다."
    play sound "audio/sfx_can_open.ogg" volume 0.5
    sj "너 너무 단 건 별로 안 좋아하는 것 같아서. 탄산은 약한 걸로 골랐어."

    show seola surprise with dissolve
    sa "…기억했어?"
    sj "지난번 피자 파티 때 네가 제일 늦게 고른 거."
    sj "강한 맛은 좀 오래 보더라."

    show seola smile with dissolve
    sa "고마워."
    sa "맞아. 이거 좋아."

    "설아가 캔을 내려다보는 눈빛이 아주 조용하게 풀렸다."
    "말은 짧았지만, 만족한 건 확실히 보였다."

    ge "그럼 나는 유나 거."
    "가은 선배는 형광빛 포장이 귀여운 젤리와 딸기우유를 한꺼번에 내밀었다."
    ge "너는 하나만 주면 분명 아쉬워할 것 같아서 세트로."

    show yuna surprise at char_2 with dissolve
    yn "헐, 선배 천재예요?"
    yn "저 진짜 방금 딱 이 조합 상상했는데!"

    ge "봐봐, 내가 사람 보는 눈은 있다니까."
    yn "와, 이건 진짜 사랑이다."

    sj "과자 하나 받았다고 사랑까지 가냐."
    yn "먹는 거 앞에선 충분히 가능하거든요?"

    "다들 웃었다."
    "작고 환한 웃음이 매점 안의 달큰한 공기와 섞여 둥글게 퍼졌다."

    sa "내 차례."
    "설아는 가은 선배에게 작은 캔커피와 버터 쿠키를 내밀었다."
    sa "선배는 따뜻한 거 들고 있을 때 제일 편해 보여."
    sa "그리고 쿠키는… 그냥 어울려."

    ge "뭐야, 너무 다정한 해석인데?"
    ge "나 지금 괜히 감동했어."

    show gaeun laugh with dissolve
    "가은 선배가 웃으며 쿠키 상자를 가볍게 흔들었다."
    "노을빛이 투명한 포장 비닐에 반사되어 반짝였다."

    yn "마지막! 내 차례!"
    "유나는 두 손으로 아주 엄숙하게 작은 견과류 봉지와 무가당 요거트를 하린 앞에 바쳤다."

    hr "…의외네."
    yn "의외라는 표정 뭐예요."
    yn "저도 이제 하린 선배 취향 알아요."
    yn "달달한 것보다 안 부담스러운 거 좋아하고, 먹으면서도 죄책감 안 드는 거 선호하잖아요."

    show harin surprise with dissolve
    hr "그런 말은 좀 이상하지만… 틀리진 않았어."

    ge "유나도 사람 잘 본다니까."
    sj "의외로 이런 데선 세심하지."

    show yuna grin at char_2, excited_hop
    yn "의외로 빼요!"

    play sound "audio/sfx_eating.ogg" volume 0.5
    "그대로 매점 앞 좁은 벤치와 창틀 쪽에 걸터앉아 다 같이 포장을 뜯었다."
    "누군가는 한 입 먹고 고개를 끄덕였고, 누군가는 남의 손에 든 걸 슬쩍 다시 봤다."
    "추천이라는 이름을 붙였지만, 결국은 서로를 얼마나 보고 있었는지 확인하는 시간에 가까웠다."

    hr "생각보다 다들 잘 골랐네."
    sa "응."
    sa "진짜 다 어울려."
    ge "이 정도면 우리 이제 취향 데이터도 꽤 쌓였는데?"

    sj "듣기만 하면 연구 모임 같다."
    yn "좋지 않아요?"
    yn "서로를 오래 봐야만 아는 것들 있잖아."

    "유나는 젤리를 오물거리다가 문득 말을 멈추고, 차분해진 눈으로 다들 한 번씩 바라봤다."
    "평소처럼 왁 하고 튀어 오르는 장난기가 아니라, 그냥 순수하게 좋아서 확인하는 표정이었다."

    yn "진짜 신기하다."
    yn "처음엔 그냥 같이 축제 준비하는 사람들이었는데."
    yn "이제는 누가 뭘 고를지 대충 상상도 되고, 그게 맞아떨어지기도 하고."

    show harin smile with dissolve
    hr "계속 같이 있었으니까."

    show seola smile with dissolve
    sa "계속 같이 있었는데도 안 질렸고."

    ge "오히려 더 재밌어졌지."

    sj "부정할 수는 없네."

    "대답이 겹치자 잠깐 정적이 생겼다가, 이내 누가 먼저랄 것도 없이 또 웃음이 번졌다."
    "어색해서가 아니라, 너무 자연스러워서 나오는 웃음이었다."

    play sound "audio/sfx_stomach_growl.ogg" volume 0.6
    "그때, 정말 절묘한 타이밍에 누군가의 배에서 작게 꼬르륵 소리가 났다."
    "잠깐 정적. 그리고 바로, 고개를 푹 숙인 사람은 하린이었다."

    show harin flustered with dissolve
    hr "…못 들은 걸로 해."

    show yuna laugh at char_2, excited_hop
    yn "아하하하! 하린 선배도 배고프잖아!"
    ge "이건 귀한 장면인데."
    sa "오늘 최고다."
    sj "매점 오길 잘했네."

    "하린은 얼굴을 붉힌 채 요거트 뚜껑을 괜히 더 반듯하게 접었다."
    "그 모습이 너무 드물고 인간적이라, 다들 한참 웃다가 겨우 진정했다."

    show harin sigh with dissolve
    hr "웃을 거면 다 먹고 빨리 가."
    hr "…그래도, 오늘은 괜찮았어."

    "작고 낮은 목소리였지만 다들 들었다."
    "그래서 이번엔 놀리지 않고, 그냥 각자 자기 손에 든 것을 한 번 더 내려다보며 가볍게 웃었다."

    stop music fadeout 2.0

    # ---------------------------------------------------------
    # Scene 30
    scene black with fade
    centered "{size=40}Scene 30{/size}

{size=30}헤어지기 아쉬운 길{/size}" with dissolve
    pause 1.5

    scene bg school_road_dusk with fade
    play music "audio/bgm_stand_by_you.ogg" fadein 2.0

    "학교 밖으로 나오자, 하늘은 이미 낮과 밤의 사이에 걸쳐 있었다."
    "붉지도 푸르지도 않은 애매한 빛이 골목과 전신주, 멀리 이어지는 도로를 한 번 부드럽게 덮고 있었다."
    "봄 저녁 특유의 선선한 공기 속에서, 다섯 사람의 걸음은 이상하리만치 느렸다."

    play sound "audio/sfw_walking.ogg" volume 0.7
    "누가 먼저 속도를 늦췄는지는 모른다."
    "그런데 어느새 아무도 서두르지 않고 있었다."

    show yuna smile at char_2 with dissolve
    show harin normal at left_mid with dissolve
    show seola normal at char_4 with dissolve
    show gaeun smile at right_mid with dissolve

    yn "오늘 진짜 꽉 찼다."
    yn "교실도 정리하고, 준비실도 갔다가, 매점까지 성공했어."
    yn "이 정도면 완전 알찬 하루 인정?"

    sj "너 기준으론 하루에 이벤트 세 개는 기본 아닌가."
    yn "그래도 오늘은 더 좋았어요."

    ge "왜?"

    show yuna smile with dissolve
    yn "그냥요."
    yn "뭐 해도 다 같이 한 느낌이어서."

    "유나는 멋쩍은 듯 웃으며 운동화 끝으로 길바닥의 작은 돌멩이를 툭 찼다."
    "돌멩이는 멀리 가지도 못하고 몇 번 또르르 굴러가다 멈췄다."

    sa "나도."
    sa "오늘 이상하게 빨리 지나갔어."

    hr "시간이 빠른 건 대체로 바쁠 때인데."
    hr "오늘은 바쁘다기보다…"
    hr "계속 이어져 있었지."

    ge "맞아. 끊기는 데가 없었어."
    ge "누구 하나 먼저 빠지지도 않고, 중간에 어색하게 비는 순간도 없고."

    th "그 말이 이상하게 오래 남았다."
    th "끊기는 데가 없었다."
    th "하루를 돌아보면 정말 그랬다."
    th "아침엔 자연스럽게 웃었고, 점심엔 같이 고르고, 방과 후엔 같이 정리하고, 끝나고도 또 같이 걷고 있었다."
    th "별일이 있어서가 아니라, 같이 있는 흐름이 너무 자연스러워져서."

    play sound "audio/sfw_cloth_moving.ogg" volume 0.5
    "바람이 한 번 지나가자 유나의 반묶음 머리와 설아의 긴 머리카락이 동시에 살짝 흔들렸다."
    "가은 선배는 손에 든 빈 캔을 가볍게 굴렸고, 하린은 가방끈을 고쳐 잡으며 하늘을 한 번 올려다봤다."

    sj "축제 끝나도 이렇게 다닐까."

    "그 말은 생각보다 조용하게 떨어졌다."
    "농담처럼 던진 것도, 무겁게 꺼낸 것도 아니었는데 다들 바로 대답하지 못했다."

    show yuna surprise with dissolve
    yn "…어?"

    "먼저 반응한 건 유나였다."
    "눈을 동그랗게 뜬 얼굴에, 순간 아주 짧게 당황이 스쳤다."

    ge "뭐야, 갑자기 벌써 아쉬운 소리?"
    ge "그건 좀 이른데."

    sa "이르긴 한데."
    sa "생각은 해봤어."

    show harin faint_smile with dissolve
    hr "나도."
    hr "축제 준비 끝나면 이 핑계로 모이긴 어려울 테니까."

    "정말 사소한 현실적인 말이었다."
    "하지만 그래서 더 진짜처럼 들렸다."
    "지금 이 시간들이 끝이 있는 종류라는 걸, 다들 이미 어렴풋이 알고 있었던 셈이다."

    show yuna pout with dissolve
    yn "싫은데."
    yn "그냥 끝나면 끝, 이건 좀 싫어요."

    "유나는 입술을 살짝 내밀며 발끝으로 바닥을 한 번 더 툭 건드렸다."
    "장난을 칠 때의 삐죽임과는 조금 달랐다."
    "이번에는 진짜로 아쉬워하는 얼굴이었다."

    sj "나도 그냥 한 말은 아니었어."
    sj "요즘은 좀… 당연해졌거든."
    sj "점심 되면 준비실 갈 것 같고, 끝나면 또 어디선가 모일 것 같고."

    sa "응."
    sa "맞아."

    ge "아, 그 느낌 알아."
    ge "나도 수업 끝나면 오늘은 또 누가 먼저 와 있을까 생각하게 되더라."

    hr "솔직히 말하면."
    hr "이제는 네가 없으면 조용해서 이상하고."
    hr "네가 없으면 너무 시끄럽지도 않아서 이상해."

    "하린의 시선이 유나 쪽으로 향했다."
    "말은 여전히 담백했지만, 그 안에 담긴 익숙함만큼은 분명했다."

    show yuna surprise at char_2
    pause 0.2
    show yuna smile at char_2, excited_hop
    yn "뭐야, 그거 완전 고백 아니에요?"

    hr "아니거든."
    ge "들었지? 공식적으로 유나는 소음인데 필요한 소음이래."
    sa "중요한 소리네."
    sj "없으면 허전한 쪽."

    "유나는 잠깐 아무 말도 못 하더니, 결국 참지 못하고 웃어버렸다."
    "눈가가 반짝일 만큼 환한 웃음이었다."

    yn "진짜 이상하다."
    yn "맨날 놀리면서 왜 이렇게 다정해."

    hr "네가 놀릴 거리를 너무 많이 주니까."
    sa "근데 다정한 건 맞아."
    ge "응, 그건 맞지."

    play sound "audio/sfw_walking.ogg" volume 0.6
    "갈림길이 보이기 시작했다."
    "누군가는 여기서 버스를 타야 하고, 누군가는 오른쪽 골목으로, 누군가는 언덕 쪽으로 올라가야 했다."
    "매번 지나치는 자리인데도 오늘은 유난히 가까워 보였다."

    yn "벌써 여기야?"
    ge "천천히 왔는데도 결국 도착은 하네."

    sa "오늘 길이 짧다."

    th "설아 말이 딱 맞았다."
    th "분명 평소와 같은 거리인데도, 오늘은 이상할 만큼 짧았다."

    show gaeun smile with dissolve
    ge "그럼 하나 정하자."
    ge "축제 끝나도 그냥 끝내지 말기."
    ge "누가 먼저 말 안 해도, 가끔은 계속 같이 있기."

    show yuna vivid with dissolve
    yn "좋아!"
    yn "완전 좋아!"
    yn "그럼 우리… 음, 이유 없어도 모이는 걸로!"

    hr "이유 없는 모임은 너무 즉흥적이야."
    hr "적어도 명분은 하나 있어야지."

    sj "명분은 만들면 되잖아."
    sj "간식 먹기든, 산책이든, 사진 정리든."

    sa "사소한 것에 진심이기로 했으니까."

    "설아가 아주 담담하게 전에 했던 말을 다시 꺼냈다."
    "그 말이 이 저녁길에 유난히 잘 어울렸다."

    ge "좋네."
    ge "그럼 결정."
    ge "축제가 끝나도 우리는 사소한 핑계를 계속 만들기로."

    show harin smile with dissolve
    hr "그 정도면 나도 찬성."

    show yuna grin at char_2, excited_hop
    yn "됐다!"
    yn "와, 오늘 진짜 역사적인 날이다!"
    yn "공식 미래 약속 성립!"

    sj "네가 붙이는 이름은 왜 다 거창하냐."
    yn "중요하니까요."

    "유나는 아주 만족스러운 얼굴로 고개를 끄덕였다."
    "가은 선배는 그런 유나를 보며 작게 웃었고, 설아는 조용히 그 장면을 눈에 담았다."
    "하린은 아무 말 없이도 표정이 한결 부드러워져 있었다."

    play sound "audio/sfx_camera_click.ogg" volume 0.7
    "그때 유나가 갑자기 휴대폰을 번쩍 들었다."

    yn "잠깐, 이건 남겨야 해."
    yn "오늘 표정들 다 좋단 말이야."

    sj "또 사진이냐."
    ge "좋지, 찍자."
    sa "응. 오늘은 찍어도 돼."
    hr "갑자기 준비할 시간도 안 주고…"

    show harin flustered with dissolve
    "하린이 그렇게 말했지만 이미 늦었다."
    "유나는 갈림길 앞에 다섯 사람을 억지로 끌어 모으더니, 자기 키에 맞춰 휴대폰 각도를 몇 번 바꿨다."

    yn "좋아, 다들 조금만 붙어요!"
    yn "오늘은 자연스럽게, 너무 꾸미지 말고!"

    play sound "audio/sfw_cloth_moving.ogg" volume 0.6
    "어깨가 닿고, 소매가 스치고, 누군가의 웃음이 누군가의 숨결 가까이에서 섞였다."
    "그 거리감이 전혀 어색하지 않았다."

    ge "유나야, 너 지금 제일 꾸미고 있어."
    sa "맞아. 표정 제일 열심히 만들어."
    sj "입꼬리 너무 올라갔는데."

    show yuna pout with dissolve
    yn "아 진짜! 빨리 찍어요!"

    play sound "audio/sfx_camera_click.ogg" volume 0.9
    with flash
    "찰칵."
    "셔터음과 함께, 오늘의 끝자락이 한 장의 사진으로 고정되었다."

    "유나는 찍힌 화면을 확인하더니 그대로 한동안 말이 없었다."
    "다들 이상해서 유나를 보자, 녀석은 화면을 가슴 쪽으로 끌어안듯 붙들고 작게 웃었다."

    show yuna smile with dissolve
    yn "좋다."
    yn "진짜 좋다."

    "짧은 한마디였는데, 그 말 안에는 오늘 하루 전체가 다 들어 있는 것 같았다."

    hr "나중에 보내 줘."
    sa "나도."
    ge "나도 꼭."
    sj "원본 훼손하지 말고."

    show yuna laugh at char_2, excited_hop
    yn "저를 뭘로 보고!"
    yn "아주 예쁘게 보내드리겠습니다!"

    play sound "audio/sfw_walking.ogg" volume 0.7
    "결국 갈림길 앞에서 한참 더 머물렀다."
    "안녕을 말하고도 두세 마디씩 더 붙었고, 돌아서는 척하다가도 다시 손을 흔들었다."
    "정말로 떠나기 아쉬운 사람들처럼."

    ge "그럼 내일 봐, 얘들아."
    sa "내일 봐."
    hr "늦지 마."
    sj "들어가다가 연락하고."

    show yuna smile with dissolve
    yn "응."
    yn "내일도 같이 있어요."

    "그 말은 약속이라기보다 이미 정해진 사실처럼 들렸다."
    "그래서 누구도 대답을 망설이지 않았다."

    sj "그래."
    hr "응."
    sa "같이 있어."
    ge "당연하지."

    "저녁길 위로 웃음이 한 번 더 번졌다."
    "그리고 그제야, 다섯 사람은 각자의 방향으로 천천히 흩어졌다."
    "멀어지는 발걸음 속에서도 이상하게 마음은 가벼웠다."

    th "이제는 안다."
    th "이 관계가 단순히 축제 준비 때문에 묶인 건 아니라는 걸."
    th "사소한 말, 사소한 약속, 사소한 같이 걷는 길 같은 것들이 어느새 우리를 여기까지 데려왔다는 걸."
    th "그래서 더 오래 붙잡고 싶어진다는 것도."

    stop sound fadeout 1.0
    stop music fadeout 2.0

    return
