#!/bin/sh

CURRENT_DIR=$PWD
cd $CURRENT_DIR/domain_lang && ./runtests.sh
cd $CURRENT_DIR/java_gen && ./runtests.sh