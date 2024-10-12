from argparse import ArgumentParser

from markpoint import MarkParser, PointGenerator


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-o", "--outfile", type=str, help="Outfile for the powerpoint presentation"
    )
    parser.add_argument(
        "-i",
        "--inputfile",
        type=str,
        help="Input markdown file for the powerpoint presentation",
    )
    args = parser.parse_args()

    with open(args.inputfile, "r") as f:
        text = f.read()

    mp = MarkParser(text)
    pg = PointGenerator(mp.slides)
    pg.generate(args.outfile)


if __name__ == "__main__":
    main()
