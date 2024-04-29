import argparse
import pandas
def main():
    parser = argparse.ArgumentParser(description="Load and display information about CSV files.")
    parser.add_argument("dbow", help="Path to the first CSV file")
    parser.add_argument("dm", help="Path to the second CSV file")
    parser.add_argument("out")
    args = parser.parse_args()

    print("./data/" + args.dbow)
    dbow = pandas.read_csv("./data/" + args.dbow)
    print(dbow.columns)
    dm = pandas.read_csv("./data/" + args.dm)

    print(dbow.head(10))
    print(dm.head(10))

    combine = pandas.DataFrame()
    id = 0
    for col in dbow.columns:
        id += 1
        combine["dim"+str(id)] = dbow[col]
    for col in dm.columns:
        id += 1
        combine["dim" + str(id)] = dm[col]

    combine.to_csv("./data/" + args.out, index=False)

if __name__ == "__main__":
    main()