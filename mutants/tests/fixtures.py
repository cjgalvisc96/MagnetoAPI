from rest_framework import status

mutants = [
    (
        [
            "CCGGGC", "CAAAGT", "CAATGT", "TAAATG", "ACCTTA", "TCTTTT"
        ], status.HTTP_200_OK
    ),
    (
        [
            "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"
        ], status.HTTP_200_OK
    ),
    (
        [
            "CCCCCAGT", "GTCAGTCA", "CAGTCAGT", "TTCAGTCG", "GAGTCAGA",
            "GTCAGTCA", "GAGTCAGG", "GTCCAGAA"
        ], status.HTTP_200_OK
    ),
    (
        [
            "AAAA", "AAAA", "AAAA", "AAAA"
         ], status.HTTP_200_OK
    )
]
humans = [
    (
        [
            "ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"
        ], status.HTTP_403_FORBIDDEN
    ),
    (
        [
            "CAGT", "AGTC", "CCCC", "CCAG"
        ], status.HTTP_403_FORBIDDEN
    ),
    (
        [
            "AAAACC", "GTGTGT", "ACACAC", "GTGTGT", "ACACAC", "GTGTGT"
        ], status.HTTP_403_FORBIDDEN
    )
]
invalid_entries = [
    (  # Incorrect square one
        [
            "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACT"
        ], status.HTTP_403_FORBIDDEN
    ),
    (  # Incorrect square two
        [
            "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG"
        ], status.HTTP_403_FORBIDDEN
    ),
    (  # incorrect_characters_dna
        [
            "ATGCGA", "CAGTGC", "TTATPT", "AGAAGG", "CCXCTA", "TCACTG"
        ], status.HTTP_403_FORBIDDEN
    ),
    (  # incorrect_small_dna
        [
            "AAA", "CCC", "GGG"
        ], status.HTTP_403_FORBIDDEN
    )
]
