#!/usr/bin/env bash
set -e

clean_and_compile() {
	test -f "$1/CMakeCache.txt" && rm -r "$1"
	mkdir -p "$1"
	pushd "$1"
	command "cmake-for-cheribsd-cheriabi-$1.sh" -G Ninja .. -DCMAKE_BUILD_TYPE=Debug
	ninja
	popd
}

clean_and_compile dynamic
clean_and_compile dynamic-with-lld
clean_and_compile static
clean_and_compile static-with-lld
