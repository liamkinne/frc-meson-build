#!/bin/bash

rm -r build
mkdir build
cp edu.* ./build
meson build --cross-file cross_file.txt
