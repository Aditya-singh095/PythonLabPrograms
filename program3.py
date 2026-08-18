import pandas as pd


def inspect_csv(filename):
    # Read CSV file
    if filename.endswith(".tsv"):
        df = pd.read_csv(filename, sep="\t")
    else:
        df = pd.read_csv(filename)

    # Display basic information
    print("\n--- CSV File Information ---")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nSummary:")
    print(df.describe())


def main():
    filename = input("Enter CSV/TSV file name: ")

    try:
        # Read file
        if filename.endswith(".tsv"):
            df = pd.read_csv(filename, sep="\t")
        else:
            df = pd.read_csv(filename)

        # Inspect data
        inspect_csv(filename)

        # Ask user for filtering
        column = input("\nEnter column name for filtering: ")
        value = float(input("Enter minimum value: "))

        # Filter rows
        filtered_data = df[df[column] >= value]

        print("\n--- Filtered Data ---")
        print(filtered_data)

        # Save filtered data
        output_file = input("\nEnter output file name: ")

        filtered_data.to_csv(output_file, index=False)

        print("\nFiltered data saved successfully!")

    except FileNotFoundError:
        print("Error: File not found.")

    except KeyError:
        print("Error: Column name not found.")

    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
