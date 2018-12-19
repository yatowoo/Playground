#!/bin/bash -

# Script to update by self

set -v
cp $0 $0.bak
echo -e "\n# Updated: "$(date -R) >> $0.bak
rm $0
mv $0.bak $0
set +v