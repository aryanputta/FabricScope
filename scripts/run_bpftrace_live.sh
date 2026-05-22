#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_FILE="${1:-${ROOT_DIR}/results/live_tcp_retrans.log}"

if ! command -v bpftrace >/dev/null 2>&1; then
  echo "bpftrace not found" >&2
  exit 1
fi

sudo bpftrace "${ROOT_DIR}/probes/tcp_retrans.bt" > "${OUTPUT_FILE}"

