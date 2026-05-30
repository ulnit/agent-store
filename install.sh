#!/bin/bash
set -e
echo "Installing AI Agent Toolkit..."
pip install --user ai-agent-toolkit || pip install ai-agent-toolkit
echo "✅ Done! Run: agent-tools --help"
