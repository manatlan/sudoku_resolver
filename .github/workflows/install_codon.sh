#!/usr/bin/env bash
set -e
set -o pipefail

CODON_INSTALL_DIR=~/.codon
OS=$(uname -s | awk '{print tolower($0)}')
ARCH=$(uname -m)

if [ "$OS" != "linux" ] && [ "$OS" != "darwin" ]; then
  echo "error: Pre-built binaries only exist for Linux and macOS." >&2
  exit 1
fi

CODON_BUILD_ARCHIVE=codon-$OS-$ARCH.tar.gz

mkdir -p $CODON_INSTALL_DIR
cd $CODON_INSTALL_DIR
curl -L https://github.com/exaloop/codon/releases/latest/download/"$CODON_BUILD_ARCHIVE" | tar zxvf - --strip-components=1

EXPORT_COMMAND="export PATH=$(pwd)/bin:\$PATH"
echo "$(pwd)/bin" >> $GITHUB_PATH

echo "Codon successfully installed at: $(pwd)"
echo "Open a new terminal session or update your PATH to use codon"
