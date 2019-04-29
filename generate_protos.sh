#!/usr/bin/env bash
proto_path=$1
proto_files=$2
python -m grpc_tools.protoc -I ${proto_path} --python_out=frater/core/proto/ ${proto_files}