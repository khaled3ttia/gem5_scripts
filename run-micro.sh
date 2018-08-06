#!/bin/bash

if [ $# != 1 ]; then
  echo "Usage: #0 [FACTOR]"
  exit 1
fi

factor=$1

RD=$((32 * factor))
ST=$((96 * factor))
SL=$((3 * factor))

programs=(array_rand \
    array_strm \
    array_slid)

args=("16 $RD 49152" "$ST" "16 $SL 2 2048")

for ((i=0; i<${#programs[@]}; ++i)); do
	mkdir ${programs[i]}_${factor}_ddr
        ./build/X86/gem5.opt -d ${programs[i]}_${factor}_ddr configs/learning_gem5/part1/ddr.py  ${programs[i]}  ${args[i]} > ${programs[i]}_${factor}_ddr/terminal_out.txt &
    	sleep 20
done

