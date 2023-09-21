#!/bin/bash
              
              a=2
              b=2
              c=$((a + b))
	      
              echo "Bash says: Hello, World!"
              echo "$a + $b = $c"
	      mylist=("user1" "user2" "user3")
	      len=${#mylist[@]}
	      for list in ${mylist[@]};
	      do
		      echo $list
	      done


