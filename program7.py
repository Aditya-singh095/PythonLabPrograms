# Functional Data Filtering & Matrix Transformation Suite


def remove_negative(matrix):
    """Replace negative values with 0."""
    return list(
        map(
            lambda row: list(map(lambda x: max(x, 0), row)),
            matrix
        )
    )


def filter_positive(matrix):
    """Keep only positive values from the matrix."""
    return list(
        map(
            lambda row: list(filter(lambda x: x > 0, row)),
            matrix
        )
    )


def sort_matrix(matrix):
    """Sort each row in ascending order."""
    return list(
        map(
            lambda row: sorted(row),
            matrix
        )
    )


def sort_by_sum(matrix):
    """Sort rows according to their sum."""
    return sorted(matrix, key=lambda row: sum(row))


def transform_matrix(matrix):
    """Square every element."""
    return list(
        map(
            lambda row: list(map(lambda x: x * x, row)),
            matrix
        )
    )


# -------------------------
# Example
# -------------------------

matrix = [
    [5, -2, 8],
    [-4, 3, 1],
    [7, -6, 2]
]

print("Original Matrix:")
print(matrix)

print("\nNegative values removed:")
print(remove_negative(matrix))

print("\nOnly positive values:")
print(filter_positive(matrix))

print("\nSorted rows:")
print(sort_matrix(matrix))

print("\nRows sorted by sum:")
print(sort_by_sum(matrix))

print("\nSquared matrix:")
print(transform_matrix(matrix))
