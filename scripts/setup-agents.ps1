# Script para criar a estrutura agnostica de agentes de IA (Windows/PowerShell)
# Se a execucao direta falhar por ExecutionPolicy, use scripts\setup-agents.cmd.

param(
    [ValidateSet("minimal", "standard", "full")]
    [string]$Profile = "minimal",
    [switch]$Help
)

function Show-Usage {
    Write-Host "Usage:"
    Write-Host "  powershell -ExecutionPolicy Bypass -File .\scripts\setup-agents.ps1 [-Profile minimal|standard|full]"
    Write-Host "  powershell -ExecutionPolicy Bypass -File .\scripts\setup-agents.ps1 -Help"
    Write-Host ""
    Write-Host "Profiles:"
    Write-Host "  minimal   cria a base agnostica minima"
    Write-Host "  standard  adiciona docs operacionais, tools, images e extensoes de .agents"
    Write-Host "  full      adiciona templates opinativos para colaboracao e governanca"
}

if ($Help) {
    Show-Usage
    exit 0
}

function New-LinkWithFallback {
    param(
        [string]$Path,
        [string]$Target,
        [string]$PrimaryType,
        [string]$FallbackType
    )

    if (Test-Path -LiteralPath $Path) {
        Write-Host "Ja existe: $Path" -ForegroundColor DarkYellow
        return
    }

    try {
        New-Item -ItemType $PrimaryType -Path $Path -Target $Target -ErrorAction Stop | Out-Null
        Write-Host "Criado: $Path ($PrimaryType)" -ForegroundColor Green
        return
    } catch {
        $canFallback = $_.Exception -is [System.UnauthorizedAccessException] -or $_.FullyQualifiedErrorId -like "*ElevationRequired*"
        if (-not $canFallback) {
            throw
        }
    }

    New-Item -ItemType $FallbackType -Path $Path -Target $Target -ErrorAction Stop | Out-Null
    Write-Host "Criado: $Path ($FallbackType)" -ForegroundColor Yellow
}

function Ensure-File {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType File -Path $Path | Out-Null
    }
}

function Ensure-FileWithContent {
    param(
        [string]$Path,
        [string]$Content
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        Set-Content -Path $Path -Value $Content
    }
}

function Copy-TemplateIfMissing {
    param(
        [string]$Source,
        [string]$Destination
    )

    if (-not (Test-Path -LiteralPath $Destination)) {
        Copy-Item -Path $Source -Destination $Destination
    }
}

function Copy-TemplateIfEmpty {
    param(
        [string]$Source,
        [string]$Destination
    )

    if (-not (Test-Path -LiteralPath $Destination) -or (Get-Item $Destination).Length -eq 0) {
        Copy-Item -Path $Source -Destination $Destination -Force
    }
}

Write-Host "[1/4] Criando estrutura de pastas unificada ($Profile)..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path ".agents\agents", ".agents\commands", ".agents\skills", ".agents\rules", "docs", "src" | Out-Null

if ($Profile -eq "standard" -or $Profile -eq "full") {
    New-Item -ItemType Directory -Force -Path "docs\decisions", "docs\runbooks", "tools\scripts", "tools\prompts", "images", ".agents\hooks", ".agents\settings" | Out-Null
}

Write-Host "[2/4] Criando arquivos base..." -ForegroundColor Cyan
Ensure-File -Path "docs\architecture.md"
Ensure-File -Path "AGENTS.md"

if ($Profile -eq "standard" -or $Profile -eq "full") {
    Ensure-File -Path "docs\PRD.md"
    Ensure-File -Path "docs\Plan.md"
    Ensure-File -Path "docs\Napkin.md"
}

if ($Profile -eq "full") {
    Copy-TemplateIfMissing -Source "$PSScriptRoot\templates\full\docs\decisions\0001-template.md" -Destination "docs\decisions\0001-template.md"
    Copy-TemplateIfMissing -Source "$PSScriptRoot\templates\full\docs\runbooks\onboarding.md" -Destination "docs\runbooks\onboarding.md"
    Copy-TemplateIfMissing -Source "$PSScriptRoot\templates\full\.agents\agents\reviewer.md" -Destination ".agents\agents\reviewer.md"
    Copy-TemplateIfMissing -Source "$PSScriptRoot\templates\full\.agents\rules\code-review.md" -Destination ".agents\rules\code-review.md"
}

Write-Host "[3/4] Preparando AGENTS.md..." -ForegroundColor Cyan
if ((Get-Item "AGENTS.md").Length -eq 0) {
    Copy-TemplateIfEmpty -Source "$PSScriptRoot\templates\common\AGENTS.md" -Destination "AGENTS.md"
} else {
    Write-Host "Ja existe: AGENTS.md" -ForegroundColor DarkYellow
}

Write-Host "[4/4] Criando links para compatibilidade com ferramentas..." -ForegroundColor Cyan
try {
    New-LinkWithFallback -Path ".claude" -Target ".agents" -PrimaryType "SymbolicLink" -FallbackType "Junction"
    New-LinkWithFallback -Path ".codex" -Target ".agents" -PrimaryType "SymbolicLink" -FallbackType "Junction"
    New-LinkWithFallback -Path "CLAUDE.md" -Target "AGENTS.md" -PrimaryType "SymbolicLink" -FallbackType "HardLink"
    Write-Host "Estrutura preparada com sucesso." -ForegroundColor Green
} catch {
    Write-Host "Erro ao criar os links de compatibilidade: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
