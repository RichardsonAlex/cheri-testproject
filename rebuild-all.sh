#!/usr/bin/env bash
set -e

clean_and_compile() {
	local builddir="$(uname -s)-$1"
	test -f "$builddir/CMakeCache.txt" && rm -r "$builddir"
	mkdir -p "$builddir"
	pushd "$builddir"
	command "cmake-for-cheribsd-cheriabi-$1.sh" -G Ninja .. -DCMAKE_BUILD_TYPE=Debug
	ninja
	popd
}

clean_and_compile dynamic
clean_and_compile dynamic-with-lld
clean_and_compile static
clean_and_compile static-with-lld
