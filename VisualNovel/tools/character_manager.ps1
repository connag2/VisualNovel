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
    param(
        [string]$Path,
        [string]$Content,
        [switch]$Overwrite
    )

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
- `yuna.md` : 유나
- `shiroha.md` : 시로하
- `seoyeon.md` : 서연
- `harin.md` : 하린

한국어로 출력할 것.
"@
}

function Get-YunaContent {
@"
# 유나

## 한 줄 콘셉트
귀엽고 밝고 사랑스러워 보이지만, 누구에게도 완전히 선택받지 못할까 봐 두려워하는 소녀.

한국어로 출력할 것.
"@
}

function Get-ShirohaContent {
@"
# 시로하

## 한 줄 콘셉트
하얀 머리와 붉은 눈을 가진 비현실적인 소녀. 차갑고 멀어 보이지만 누구보다 깊게 상처받기 쉬운 사람.

한국어로 출력할 것.
"@
}

function Get-SeoyeonContent {
@"
# 서연

## 한 줄 콘셉트
다정하고 포근하지만 자기 아픔은 늘 뒤로 미루는 소녀.

한국어로 출력할 것.
"@
}

function Get-HarinContent {
@"
# 하린

## 한 줄 콘셉트
늘 밝고 반짝이지만, 혼자 남겨지는 순간 가장 깊은 공허를 마주하는 소녀.

한국어로 출력할 것.
"@
}

$charactersPath = Join-Path $BasePath "characters"
Ensure-Directory $charactersPath

Write-Utf8File -Path (Join-Path $charactersPath "README.md") -Content (Get-CharactersReadme) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "yuna.md") -Content (Get-YunaContent) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "shiroha.md") -Content (Get-ShirohaContent) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "seoyeon.md") -Content (Get-SeoyeonContent) -Overwrite:$Force
Write-Utf8File -Path (Join-Path $charactersPath "harin.md") -Content (Get-HarinContent) -Overwrite:$Force

Write-Host ""
Write-Host "캐릭터 문서 준비 완료"
Write-Host "기준 경로: $BasePath"