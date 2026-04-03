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
    param(
        [string]$Path,
        [object]$Data,
        [switch]$Overwrite
    )

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

$yuna = [ordered]@{
    characterId = "yuna"
    name = "유나"
    routeType = "heroine"
}

$shiroha = [ordered]@{
    characterId = "shiroha"
    name = "시로하"
    routeType = "heroine"
}

$seoyeon = [ordered]@{
    characterId = "seoyeon"
    name = "서연"
    routeType = "heroine"
}

$harin = [ordered]@{
    characterId = "harin"
    name = "하린"
    routeType = "heroine"
}

Write-JsonFile -Path (Join-Path $routesPath "yuna.route.json") -Data $yuna -Overwrite:$Force
Write-JsonFile -Path (Join-Path $routesPath "shiroha.route.json") -Data $shiroha -Overwrite:$Force
Write-JsonFile -Path (Join-Path $routesPath "seoyeon.route.json") -Data $seoyeon -Overwrite:$Force
Write-JsonFile -Path (Join-Path $routesPath "harin.route.json") -Data $harin -Overwrite:$Force

Write-Host ""
Write-Host "루트 JSON 파일 생성 완료"
Write-Host "생성 위치: $routesPath"