import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--command')

    args = parser.parse_args()

    if args.command == 'codes':
        from console.tdx.workers.code_list import run
        run()
    
