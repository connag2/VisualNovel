# 🌌 [프로젝트 이름] (Visual Novel)

## 📖 소개 (Overview)
매력적인 세계관과 캐릭터들이 이끌어가는 비주얼 노벨 프로젝트입니다. 플레이어의 선택에 따라 스토리가 분기되며, 다채로운 결말을 경험할 수 있습니다. 

## ✨ 주요 기능 (Features)
* **다중 분기 시스템:** 플레이어의 선택이 캐릭터와의 관계 및 스토리에 직접적인 영향을 미칩니다.
* **입체적인 캐릭터:** 세밀하게 설정된 페르소나와 배경 스토리를 가진 캐릭터들이 등장합니다.
* **고품질 일러스트:** 정교한 AI 프롬프트를 활용하여 기획된 배경 및 캐릭터 스탠딩 일러스트를 제공합니다.

---

## 🛠 프로젝트 초기 세팅 (PowerShell 자동 생성)
프로젝트 구동에 필요한 기본 폴더(`game`, `images`, `audio`)와 필수 가이드라인 문서, 기본 스크립트 파일을 자동으로 생성합니다.

**실행 방법:**
VS Code 등의 터미널(PowerShell)을 열고 아래 코드를 그대로 복사하여 붙여넣기 한 후 엔터를 누르세요.

```powershell
# 1. 필수 디렉토리 생성
New-Item -ItemType Directory -Force -Path "game", "images", "audio" | Out-Null
Write-Host "✅ 폴더 생성 완료 (game, images, audio)" -ForegroundColor Green

# 2. AI_GUIDE.md 파일 생성 (AI 작업용 지침서)
$aiGuideContent = @"
# 🤖 AI 개발 및 작업 가이드 (AI_GUIDE)

이 프로젝트에서 AI를 활용해 코드를 작성하거나 스토리를 기획할 때 반드시 지켜야 하는 규칙입니다.
AI는 작업을 시작하기 전 **무조건 이 파일을 먼저 읽고** 아래 규칙을 적용해야 합니다.

## 📌 핵심 규칙
1. **모든 대화와 출력은 한국어로 할 것.**
2. 코드를 작성할 때는 각 줄이나 블록에 명확한 한글 주석을 달아줄 것.
3. 비주얼 노벨의 특성을 살려 캐릭터의 페르소나와 세계관 설정을 일관성 있게 유지할 것.
"@
Set-Content -Path "AI_GUIDE.md" -Value $aiGuideContent -Encoding UTF8
Write-Host "✅ AI_GUIDE.md 생성 완료" -ForegroundColor Green

# 3. 기본 게임 스크립트 파일 생성 (game/script.rpy)
$gameScriptContent = @"
# 이 파일은 게임의 메인 스크립트입니다. (Ren'Py 엔진 기준)

# 캐릭터 선언 예시
define e = Character("에일린", color="#c8ffc8")

# 게임 시작점
label start:
    scene bg room # 배경 이미지 호출 (images 폴더에 bg room.jpg 필요)
    
    "비주얼 노벨 프로젝트가 성공적으로 세팅되었습니다!"
    
    e "이제 여기서부터 새로운 이야기를 만들어 나가면 돼."
    e "어떤 선택을 할지 기대하고 있을게."

    return
"@
Set-Content -Path "game/script.rpy" -Value $gameScriptContent -Encoding UTF8
Write-Host "✅ game/script.rpy 생성 완료" -ForegroundColor Green
