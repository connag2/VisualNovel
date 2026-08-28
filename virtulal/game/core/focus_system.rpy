# focus_system.rpy
init -1 python:
    # 화자 포커스 시스템 (추후 로직 연동용 더미 함수)
    def speaker(name):
        def callback(event, interact=True, **kwargs):
            if not interact:
                return
            if event == "begin":
                pass
        return callback
