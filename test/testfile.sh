#! /bin/bash

# this script parses command line arguments and creates a test file for imputation

 gzip -cd $1 | head -n 1000 > test/$2
