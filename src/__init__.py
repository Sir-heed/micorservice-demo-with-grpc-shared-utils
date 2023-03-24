import os
import sys

# Get the path to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directory containing the protobuf-generated module to the sys.path
protobuf_dir = os.path.join(current_dir, 'microservice_demo_with_grpc_shared_utils')
sys.path.append(protobuf_dir)