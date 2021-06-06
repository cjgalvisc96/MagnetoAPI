mutants = [
    (
        [
            "CCGGGC", "CAAAGT", "CAATGT", "TAAATG", "ACCTTA", "TCTTTT"
        ], 200
    ),
    (
        [
            "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"
        ], 200
    ),
    (
        [
            "CCCCCAGT", "GTCAGTCA", "CAGTCAGT", "TTCAGTCG", "GAGTCAGA",
            "GTCAGTCA", "GAGTCAGG", "GTCCAGAA"
        ], 200
    ),
    (
        [
            "AAAA", "AAAA", "AAAA", "AAAA"
         ], 200
    )
]
humans = [
    (
        [
            "ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"
        ], 403
    ),
    (
        [
            "CAGT", "AGTC", "CCCC", "CCAG"
        ], 403
    ),
    (
        [
            "AAAACC", "GTGTGT", "ACACAC", "GTGTGT", "ACACAC", "GTGTGT"
        ], 403
    )
]
invalid_entries = [
    (  # Incorrect square one
        [
            "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACT"
        ], 403
    ),
    (  # Incorrect square two
        [
            "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG"
        ], 403
    ),
    (  # incorrect_characters_dna
        [
            "ATGCGA", "CAGTGC", "TTATPT", "AGAAGG", "CCXCTA", "TCACTG"
        ], 403
    ),
    (  # incorrect_small_dna
        [
            "AAA", "CCC", "GGG"
        ], 403
    )
]
