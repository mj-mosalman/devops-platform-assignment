#!/bin/bash
set -e

curl -f http://localhost:8010/health || exit 1

echo
