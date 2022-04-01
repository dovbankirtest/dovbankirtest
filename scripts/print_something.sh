#!/usr/bin/env bash

echo "💡💡💡💡💡💡💡💡💡💡💡💡💡💡 tttttttttttttttttttttttttttttttttttttttr"
echo "$BRANCH"
echo "$REBUILD_BRANCH"

if [ "$REBUILD_BRANCH" = true ]; then
  echo '1 trrue'
fi

if [ "$REBUILD_BRANCH" == "true" ]; then
  echo '2 trrue'
fi

if "$REBUILD_BRANCH"; then
  echo '3 trrue'
fi
