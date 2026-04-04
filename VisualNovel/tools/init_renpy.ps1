param(
    [switch]$Force = $true
)

$ErrorActionPreference = "Stop"

# 현재 스크립트 위치를 기준으로 상위 폴더(VisualNovel)를 찾습니다.
$BasePath = (Resolve-Path "$PSScriptRoot\..").Path

Write-Host "====================================="
Write-Host " 랜파이 프로젝트 자동 생성 시작..."
Write-Host " 대상 경로: $BasePath"
Write-Host "====================================="

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
        Write-Host " [생성됨] 폴더: $Path"
    }
}

function Write-Utf8File {
    param([string]$Path, [string]$Content)
    $parent = Split-Path $Path -Parent
    Ensure-Directory $parent
    [System.IO.File]::WriteAllText($Path, $Content, [System.Text.UTF8Encoding]::new($false))
    Write-Host " [작성됨] 파일: $Path"
}

# 랜파이 game 폴더 경로 지정
$gamePath = Join-Path $BasePath "game"
Ensure-Directory $gamePath
Ensure-Directory (Join-Path $gamePath "routes")

# 1. 캐릭터 정의 파일 (characters.rpy)
$charactersRpy = @"
# 캐릭터 정의
define sj = Character('서진', color='#cccccc')
define hr = Character('하린', color='#7eb2e6')
define yn = Character('유나', color='#ffa6c9')
define sa = Character('설아', color='#f2f2f2')
define ge = Character('가은', color='#dcb27e')
"@

# 2. 메인 스크립트 및 공통 루트 (script.rpy)
$scriptRpy = @"
# 게임 시작점
label start:
    scene bg room
    
    sj "조용히 학교생활을 마치고 별 탈 없이 졸업하는 것. 그것만이 내 목표였다."
    
    # 공통 루트 진행
    call common_route
    
    return

label common_route:
    "어느 날, 일상적인 학교생활 속에서 네 명의 사람들과 얽히기 시작했다."
    
    menu:
        "누구에게 다가갈까?"
        
        "창가에서 멍하니 있는 하린에게 말을 건다.":
            jump route_harin
            
        "장난을 치며 다가오는 유나를 받아준다.":
            jump route_yuna
            
        "비 오는 날 창가에 앉아있는 설아의 곁으로 간다.":
            jump route_seola
            
        "도서관에서 높은 곳의 책을 꺼내주는 가은 선배에게 감사 인사를 한다.":
            jump route_gaeun
"@

# 3. 개별 히로인 루트 뼈대 생성 함수
function Get-RouteContent {
    param([string]$Name, [string]$Id)
    return @"
label route_${Id}:
    "$Name 루트에 진입했습니다."
    
    # $Name 스토리 전개
    
    return
"@
}

# 파일 생성 실행
Write-Utf8File -Path (Join-Path $gamePath "characters.rpy") -Content $charactersRpy
Write-Utf8File -Path (Join-Path $gamePath "script.rpy") -Content $scriptRpy

Write-Utf8File -Path (Join-Path $gamePath "routes\route_harin.rpy") -Content (Get-RouteContent "서하린" "harin")
Write-Utf8File -Path (Join-Path $gamePath "routes\route_yuna.rpy") -Content (Get-RouteContent "유나" "yuna")
Write-Utf8File -Path (Join-Path $gamePath "routes\route_seola.rpy") -Content (Get-RouteContent "설아" "seola")
Write-Utf8File -Path (Join-Path $gamePath "routes\route_gaeun.rpy") -Content (Get-RouteContent "민가은" "gaeun")

Write-Host "====================================="
Write-Host " 렌파이 파일 세팅이 완료되었습니다!"
Write-Host " VisualNovel/game 폴더 안에 script.rpy가 있는지 확인해 주세요."
Write-Host "====================================="