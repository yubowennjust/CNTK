#!/bin/bash
set -e -o pipefail

CNTK_PATH="$1"
LIB_PATH="$2"
cd $CNTK_PATH/Examples/Image/Classification/ResNet/Java
javac -cp $CNTK_PATH/bindings/java/Swig src/*.java
export LD_LIBRARY_PATH=$LIB_PATH:$LD_LIBRARY_PATH
java -classpath "$CNTK_PATH/Examples/Image/Classification/ResNet/Java/src:$CNTK_PATH/bindings/java/Swig" Main
