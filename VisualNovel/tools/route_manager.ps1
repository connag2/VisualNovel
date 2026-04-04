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

function Write-JsonFile {
    param([string]$Path, [object]$Data, [switch]$Overwrite)
    if ((Test-Path $Path) -and (-not $Overwrite)) {
        Write-Host "유지: $Path"
        return
    }
    $parent = Split-Path $Path -Parent
    Ensure-Directory $parent
    $json = $Data | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($Path, $json, [System.Text.UTF8Encoding]::new($false))
    Write-Host "파일 작성: $Path"
}

$routesPath = Join-Path $BasePath "data\routes"
Ensure-Directory $routesPath

$harin = [ordered]@{ characterId = "harin"; name = "서하린"; routeType = "heroine" }
$yuna = [ordered]@{ characterId = "yuna"; name = "유나"; routeType = "heroine" }
$seola = [ordered]@{ characterId = "seola"; name = "설아"; routeType = "heroine" }
$gaeun = [ordered]@{ characterId = "gaeun"; name = "민가은"; routeType = "heroine" }

Write-JsonFile -Path (Join-Path $routesPath "harin.route.json") -Data $harin -Overwrite:$Force
Write-JsonFile -Path (Join-Path $routesPath "yuna.route.json") -Data $yuna -Overwrite:$Force
Write-JsonFile -Path (Join-Path $routesPath "seola.route.json") -Data $seola -Overwrite:$Force
Write-JsonFile -Path (Join-Path $routesPath "gaeun.route.json") -Data $gaeun -Overwrite:$Force

Write-Host "
루트 JSON 파일 생성 완료
생성 위치: $routesPath"