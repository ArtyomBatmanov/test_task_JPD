from collections import Counter

list_version = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]


def group_versions(list_version) -> list:
    tuples_list = [tuple(pair) for pair in list_version]

    counts = Counter(tuples_list)

    result = [[id_version[0], id_version[1], count] for id_version, count in counts.items()]

    return result


result = group_versions(list_version)
print(result)
