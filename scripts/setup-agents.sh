#!/bin/bash
# Script para criar a estrutura agnostica de agentes de IA (Mac/Linux)

set -euo pipefail

PROFILE="${1:-minimal}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

print_usage() {
  cat <<'EOF'
Usage:
  bash scripts/setup-agents.sh [minimal|standard|full]
  bash scripts/setup-agents.sh --help

Profiles:
  minimal   cria a base agnostica minima
  standard  adiciona docs operacionais, tools, images e extensoes de .agents
  full      adiciona templates opinativos para colaboracao e governanca
EOF
}

if [ "$PROFILE" = "--help" ] || [ "$PROFILE" = "-h" ] || [ "$PROFILE" = "help" ]; then
  print_usage
  exit 0
fi

if [ "$PROFILE" != "minimal" ] && [ "$PROFILE" != "standard" ] && [ "$PROFILE" != "full" ]; then
  print_usage
  exit 1
fi

ensure_file() {
  if [ ! -e "$1" ]; then
    touch "$1"
  fi
}

ensure_link() {
  local target="$1"
  local path="$2"

  if [ -e "$path" ] || [ -L "$path" ]; then
    echo "Ja existe: $path"
    return
  fi

  ln -s "$target" "$path"
}

ensure_file_with_content() {
  local path="$1"
  local content="$2"

  if [ ! -e "$path" ]; then
    printf "%s" "$content" > "$path"
  fi
}

copy_template_if_missing() {
  local source="$1"
  local destination="$2"

  if [ ! -e "$destination" ]; then
    cp "$source" "$destination"
  fi
}

copy_template_if_empty() {
  local source="$1"
  local destination="$2"

  if [ ! -s "$destination" ]; then
    cp "$source" "$destination"
  fi
}

echo "[1/4] Criando estrutura de pastas unificada ($PROFILE)..."
mkdir -p .agents/agents .agents/commands .agents/skills .agents/rules
mkdir -p docs src

if [ "$PROFILE" = "standard" ] || [ "$PROFILE" = "full" ]; then
  mkdir -p docs/decisions docs/runbooks tools/scripts tools/prompts images .agents/hooks .agents/settings
fi

echo "[2/4] Criando arquivos base..."
ensure_file docs/architecture.md
ensure_file AGENTS.md

if [ "$PROFILE" = "standard" ] || [ "$PROFILE" = "full" ]; then
  ensure_file docs/PRD.md
  ensure_file docs/Plan.md
  ensure_file docs/Napkin.md
fi

if [ "$PROFILE" = "full" ]; then
  copy_template_if_missing "$SCRIPT_DIR/templates/full/docs/decisions/0001-template.md" "docs/decisions/0001-template.md"
  copy_template_if_missing "$SCRIPT_DIR/templates/full/docs/runbooks/onboarding.md" "docs/runbooks/onboarding.md"
  copy_template_if_missing "$SCRIPT_DIR/templates/full/.agents/agents/reviewer.md" ".agents/agents/reviewer.md"
  copy_template_if_missing "$SCRIPT_DIR/templates/full/.agents/rules/code-review.md" ".agents/rules/code-review.md"
fi

copy_template_if_empty "$SCRIPT_DIR/templates/common/AGENTS.md" "AGENTS.md"

echo "[3/4] Criando links de compatibilidade..."
ensure_link .agents .claude
ensure_link .agents .codex
ensure_link AGENTS.md CLAUDE.md

echo "[4/4] Estrutura pronta."
