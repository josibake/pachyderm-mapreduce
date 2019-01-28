#!/bin/bash

PROJECT_ROOT=`pwd`
echo "Deploying pipelines for ${PROJECT_ROOT}"

pachctl create-repo text-files
pachctl create-pipeline -f ${PROJECT_ROOT}/pipeline-spec.json