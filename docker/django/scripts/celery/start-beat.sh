#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

celery -A dj_template beat -l INFO
