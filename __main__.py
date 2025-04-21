import sys

if __name__ == "__main__":
    # check arguments
    if len(sys.argv) != 2:
        print("Usage: python -m actions_parser <story.json>")
        sys.exit(1)
    # run story