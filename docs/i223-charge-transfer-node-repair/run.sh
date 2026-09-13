#!/usr/bin/env bash
# I-223 measurement runner: one probe, both streams persisted, environment pinned.
#
#   ./run.sh <tag> <probe.py> [extra python args]
#
# Runs from the RMG-Py worktree so that rmgpy.settings picks up ITS rmgrc, which
# pins database.directory to this database worktree.  Every probe prints the
# resolved path as its first line; check it in the log before trusting anything.
set -uo pipefail

TAG="$1"; shift
PROBE="$1"; shift

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RMGPY="${RMGPY_ROOT:-/home/alon/Code/RMG-Py-i223-ct-node-repair}"
LOGS="$HERE/logs"
mkdir -p "$LOGS"

# shellcheck disable=SC1091
source ~/anaconda3/etc/profile.d/conda.sh
conda activate rmg_env

: > "$LOGS/$TAG.stdout.log"
: > "$LOGS/$TAG.stderr.log"

cd "$RMGPY" || exit 1
PYTHONPATH="$RMGPY" MPLCONFIGDIR="${TMPDIR:-/tmp}/mpl" \
    python "$HERE/$PROBE" "$@" \
    > >(tee -a "$LOGS/$TAG.stdout.log") \
    2> >(tee -a "$LOGS/$TAG.stderr.log" >&2)
status=$?
echo "exit status: $status" | tee -a "$LOGS/$TAG.stdout.log"
exit $status
