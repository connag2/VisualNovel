## quick menu를 선에 가리지 않게 살짝 위로 올리는 패치
screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -18

            textbutton _("되감기") action Rollback()
            textbutton _("대사록") action ShowMenu('history')
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("저장하기") action ShowMenu('save')
            textbutton _("Q.저장하기") action QuickSave()
            textbutton _("Q.불러오기") action QuickLoad()
            textbutton _("설정") action ShowMenu('preferences')
