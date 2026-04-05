################################################################################
## 초기화
################################################################################

## 이 파일에서 init offset 문을 사용하면 이 파일의 초기화 문이 다른 파일의 init
## 코드보다 먼저 실행됩니다.
init offset = -2

## gui.init의 호출은 스타일을 합리적인 기본값으로 재설정하고, 게임의 너비(width)
## 와 높이(height)를 설정합니다.
init python:
    gui.init(1920, 1080)

## 화면 또는 트랜스폼에서 유효하지 않거나 불안정한 프로퍼티 검사 활성화
define config.check_conflicting_properties = True


################################################################################
## GUI 설정 변수
################################################################################


## 색상 ##########################################################################
##
## 인터페이스에서 글자의 색상입니다.
## 강조 색상은 레이블(label)과 강조된 글자로 인터페이스 전체에서 사용됩니다.
define gui.accent_color = '#cc0066'

## 텍스트 버튼(text button)이 선택(selected)됐거나 커서를 올리지(hovered) 않았을
## 때 사용됩니다.
define gui.idle_color = '#707070'

## 작은(small) 색상은 같은 효과를 내기 위해 더 밝거나 어두워야 하는 작은 글자에
## 사용됩니다.
define gui.idle_small_color = '#606060'

## 버튼(button)과 막대(bar)에 커서를 올렸을 때(hovered) 사용됩니다.
define gui.hover_color = '#cc0066'

## 텍스트 버튼(text button)에 선택됐지만(selected) 포커스되지(focused) 않았을 때
## 사용됩니다.
define gui.selected_color = '#555555'

## 텍스트 버튼(text button)이 선택되지(selected) 않았을 때 사용됩니다.
define gui.insensitive_color = '#7070707f'

## 채워지지 않은 빈 막대(bar)에 사용됩니다.
define gui.muted_color = '#e066a3'
define gui.hover_muted_color = '#ea99c1'

## 대사(dialogue)와 선택지(menu choice)의 글자에서 사용됩니다.
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'


## 글자와 글자 크기 ###################################################################

## 인-게임 글자에 사용됩니다. (프리텐다드 적용)
define gui.text_font = "Pretendard-Regular.ttf" 

## 캐릭터의 이름에 사용됩니다.
define gui.name_text_font = "Pretendard-Regular.ttf"

## 인터페이스에 사용됩니다.
define gui.interface_text_font = "Pretendard-Regular.ttf"

## 일반 대사의 글자 크기입니다.
define gui.text_size = 33

## 캐릭터 이름의 글자 크기입니다.
define gui.name_text_size = 45

## 게임의 유저 인터페이스에서 글자의 크기입니다.
define gui.interface_text_size = 33

## 게임의 유저 인터페이스에서 레이블(label)들의 글자 크기입니다.
define gui.label_text_size = 36

## 통지(notify) 화면의 글자 크기입니다.
define gui.notify_text_size = 24

## 게임의 타이틀(title) 글자의 크기입니다.
define gui.title_text_size = 75


## 메인과 게임 메뉴들 ##################################################################

## 이미지들은 메인(main)과 게임 메뉴(game menu)에 사용됩니다.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## 대사 ##########################################################################

## 대사를 포함하는 텍스트 박스의 높이입니다.
define gui.textbox_height = 278

## 화면에 텍스트박스를 세로로 배치합니다. (1.0은 최하단)
define gui.textbox_yalign = 1.0

## 말하는 캐릭터의 이름을 텍스트 박스를 기준으로 배치합니다.
define gui.name_xpos = 360
define gui.name_ypos = 0

## 캐릭터들의 이름을 수평으로 정렬합니다.
define gui.name_xalign = 0.0

## 캐릭터들의 이름이 들어 있는 박스의 너비, 높이, 그리고 테두리입니다.
define gui.namebox_width = None
define gui.namebox_height = None

## 네임박스의 테두리 설정입니다.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## 네임박스 배경 설정입니다.
define gui.namebox_tile = False


## 텍스트박스에서 대사의 위치입니다.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## 대사의 최대 너비입니다.
define gui.dialogue_width = 1116

## 대사 글자의 수평 정렬입니다.
define gui.dialogue_text_xalign = 0.0


## 버튼들 #########################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## 선택 버튼들 (인-게임 메뉴) #########################################################

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#707070'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#7070707f'


## 저장 슬롯 버튼 ####################################################################

define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 384
define config.thumbnail_height = 216
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 위치와 간격 ######################################################################

define gui.navigation_xpos = 60
define gui.skip_ypos = 15
define gui.notify_ypos = 68
define gui.choice_spacing = 33
define gui.navigation_spacing = 6
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15
define gui.main_menu_text_xalign = 1.0


## 프레임들 ########################################################################

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False


## 막대, 스크롤바, 슬라이더 ##############################################################

define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)
define gui.unscrollable = "hide"


## 대사록 #########################################################################

define config.history_length = 250
define gui.history_height = 210
define gui.history_spacing = 0
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-모드 ######################################################################

define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_list_length = 6
define gui.nvl_height = 173
define gui.nvl_spacing = 15
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## 현지화 #########################################################################

define gui.language = "unicode"


################################################################################
## 모바일 기기
################################################################################

init python:

    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)

    @gui.variant
    def small():
        ## 글자 크기들.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## 텍스트박스의 위치를 조정합니다.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## 다양한 사물의 크기와 간격을 변경합니다.
        gui.slider_size = 54
        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15
        gui.history_height = 285
        gui.history_text_width = 1035
        gui.quick_button_text_size = 30

        ## 파일 버튼 레이아웃.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-모드.
        gui.nvl_height = 255
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30