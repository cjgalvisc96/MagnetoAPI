# Mutants
mutant_zero = (
    [
        "CCGGGC", "CAAAGT", "CAATGT", "TAAATG", "ACCTTA", "TCTTTT"
    ], True
)
mutant_one = (
    [
        "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"
    ], True
)
mutant_two = (
    [
        "CCCCCAGT", "GTCAGTCA", "CAGTCAGT", "TTCAGTCG", "GAGTCAGA",
        "GTCAGTCA", "GAGTCAGG", "GTCCAGAA"
    ], True
)
mutant_three = (["AAAA", "AAAA", "AAAA", "AAAA"], True)
# Humans
human_one = (
    [
        "ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"
    ], False
)
human_two = (["CAGT", "AGTC", "CCCC", "CCAG"], False)
human_three = (
    [
        "AAAACC", "GTGTGT", "ACACAC", "GTGTGT", "ACACAC", "GTGTGT"
    ], False
)
# Invalid entries
incorrect_square_one = (
    [
        "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACT"
    ], False
)
incorrect_square_two = (["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG"], False)
incorrect_characters_dna = (
    [
        "ATGCGA", "CAGTGC", "TTATPT", "AGAAGG", "CCXCTA", "TCACTG"
    ], False
)
incorrect_small_dna = (["AAA", "CCC", "GGG"], False)
