#! /bin/bash

 gzip -cd $1 | head -n 1000 > $2
