import argparse
import pandas
def main():
    parser = argparse.ArgumentParser(description="Load and display information about CSV files.")
    parser.add_argument("dbow", help="Path to the first CSV file")
    parser.add_argument("dm", help="Path to the second CSV file")
    args = parser.parse_args()

    print("./data/" + args.dbow)
    dbow = pandas.read_csv("./data/" + args.dbow)
    dm = pandas.read_csv("./data/" + args.dm)

    print(dbow.head(10))

    print(dm.head(10))


if __name__ == "__main__":
    main()