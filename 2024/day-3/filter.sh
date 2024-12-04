#!/bin/bash

grep -Po "mul\(\d{1,3},\d{1,3}\)" input | grep -Po "\d{1,3},\d{1,3}" > filtered_input
