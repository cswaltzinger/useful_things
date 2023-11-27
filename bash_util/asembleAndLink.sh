# assemble and link a stand along c file 
function aal(){
  FILE=$1
  as $FILE.s -o $FILE.o &&
   ld $FILE.o -o $FILE &&
    ./$FILE
}
