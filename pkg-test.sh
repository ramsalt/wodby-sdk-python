#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_test() {
    local dir="${1}"
    local stored_dir=$(pwd)

    cp ./tests/test.py "${dir}"/
    cd "${dir}"

    if [[ "${TRAVIS}" ]]; then
        python setup.py install
    fi

    python test.py
    rm -f test.py

    cd "${stored_dir}"
}

if [[ "${TRAVIS}" ]]; then
    pkg_test ./src-master

    if [[ "${TRAVIS_TAG}" ]]; then
        pkg_test ./src-tag
    fi
else
    pkg_test ./src
fi