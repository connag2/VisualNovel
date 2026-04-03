$ErrorActionPreference = "Stop"

$root = (Resolve-Path "$PSScriptRoot\..").Path

powershell -ExecutionPolicy Bypass -File "$root\tools\character_manager.ps1"
powershell -ExecutionPolicy Bypass -File "$root\tools\route_manager.ps1"

Write-Host ""
Write-Host "전체 초기화 완료"