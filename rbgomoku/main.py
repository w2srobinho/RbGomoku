import argparse

def main():
    parser = argparse.ArgumentParser(description='The RbGomoku game is console based.')
    parser.add_argument('size_table',
                        metavar='N',
                        type=int,
                        help='table size NxN, MIN=3 and MAX=19')
    args = parser.parse_args()


if __name__ == '__main__':
    main()