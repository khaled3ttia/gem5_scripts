#!/bin/bash

programs=(rb_tree hash_table)
args=("32 64" "64 256" "64 1024" "128 4096")

for prog in ${programs[@]}; do	
  	for ((i=0; i<${#args[@]}; ++i)); do
#		echo ${prog}_${i}_pcm
    		mkdir ${prog}_${i}_pcm
		./build/X86/gem5.opt -d ${prog}_${i}_pcm configs/learning_gem5/part1/pcm_new.py ${prog} ${args[i]}  > ${prog}_${i}_pcm/terminal_output.txt&
		sleep 50
#		ls
#		mkdir ${prog}_${i}_ddr
#		./build/X86/gem5.opt -d ${prog}_${i}_ddr configs/learning_gem5/part1/ddr.py ${prog}  ${args[i]} &
#		sleep 50
  done
done


