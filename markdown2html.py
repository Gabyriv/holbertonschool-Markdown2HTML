#!/usr/bin/python3
"""
Module that converts a markdown file to HTML
"""

import sys
import os

def main():
    """
    Converts markdown file to HTML
    Returns:
        None
    """
    # Check number of arguments
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} README.md README.html", file=sys.stderr)
        sys.exit(1)
        
    md_file = sys.argv[1]
    output_filename = sys.argv[2]
    
    if not os.path.exists(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)
    
    # If all checks pass
    sys.exit(0)

if __name__ == "__main__":
    main()
