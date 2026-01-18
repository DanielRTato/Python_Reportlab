#!/usr/bin/env bash
set -e

# setup_conda_gtk.sh - Create conda env with GTK and reportlab (Unix/WSL)
if ! command -v conda >/dev/null 2>&1; then
  echo "Conda not found; please install Miniconda/Anaconda and re-run."
  exit 1
fi

echo "Creating conda env 'gtk'..."
conda create -n gtk -c conda-forge python=3.11 pygobject pycairo gtk3 reportlab -y

echo "Activating environment..."
# Ensure conda activate is available in non-login shells
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate gtk

echo "Verifying installation..."
python -c "import gi; print('gi', gi.__version__); import reportlab; print('reportlab OK')"

echo "Done."
