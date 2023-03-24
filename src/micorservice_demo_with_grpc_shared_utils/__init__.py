import os
import sys

# Get the path to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the directory containing the protobuf-generated module to the sys.path
sys.path.append(current_dir)