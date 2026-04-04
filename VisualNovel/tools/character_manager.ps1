param(
    [string]$BasePath = (Resolve-Path "$PSScriptRoot\..").Path,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
        Write-Host "폴더 생성: $Path"
    }
}

function Write-Utf8File {
    param([string]$Path, [string]$Content, [switch]$Overwrite)
    if ((Test-Path $Path) -and (-not $Overwrite)) {
        Write-Host "유지: $Path"
        return
    }
    $parent = Split-Path $Path -Parent
    Ensure-Directory $parent
    [System.IO.File]::WriteAllText($Path, $Content, [System.Text.UTF8Encoding]::new($false))
    Write-Host "파일 작성: $Path"
}

function Get-CharactersReadme {
@"
# 히로인 캐릭터 문서 안내

이 폴더는 각 히로인별 개별 설정 문서를 관리하는 공간이다.

## 문서 목록
- harin.md : 서하린
- yuna.md : 유나
- seola.md : 설아
- gaeun.md : 민가은

한국어로 출력할 것.
"@
}

function Get-HarinContent {
@"
# 서하린
## 한 줄 콘셉트
차갑고 완벽해 보이는 우등생, 하지만 무너지는 것을 누구보다 두려워하는 소녀.
한국어로 출력할 것.
"@
}

function Get-YunaContent {
@"
# 유나
## 한 줄 콘셉트
귀엽고 밝고 사랑스러워 보이지만, 혼자 남겨질까 봐 두려워하는 소녀.
한국어로 출력할 것.
"@
}

function Get-SeolaContent {
@"
# 설아
## 한 줄 콘셉트
하얀 머리와 붉은 눈을 가진 몽환적인 소녀. 상처받기 싫어 스스로 벽을 치는 사람.
한국어로 출력할 것.
"@
}

function Get-GaeunContent {
@"
# 민가은
## 한 줄 콘셉트
여유롭고 다정하지만, 과거의 상처 때문에 묘한 거리감을 유지하는 선배.
한국어로 출력할 것.
"@
}

$charactersPath = Join-Path $BasePath "characters"
Ensure-Directory $charactersPath

Write-Utf8File -Path (Join-Path $charactersPath "README.md") -Content (Get-CharactersReadme) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "harin.md") -Content (Get-HarinContent) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "yuna.md") -Content (Get-YunaContent) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "seola.md") -Content (Get-SeolaContent) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "gaeun.md") -Content (Get-GaeunContent) -Overwrite:$Force

Write-Host "
캐릭터 문서 준비 완료
기준 경로: $BasePath"