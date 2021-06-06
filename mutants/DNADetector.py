from typing import List, Optional

from mutants.constants import DNA_LETTERS, MAX_MUTANT_SEQUENCE, MIN_ROW_LENGTH
from mutants.exceptions import (
    ExceptionInvalidDnaLetters,
    ExceptionMatrixNotIsSquare,
    ExceptionMinimumRowLen
)


class DNADetector:
    def __init__(self, *, dna: List[str]):
        self.dna = dna
        self.max_len_matrix = len(self.dna[0])
        self.dna_matrix = self.parse_dna_to_matrix()

    @staticmethod
    def check_minimum_row_len(
        *,
        row: str
    ) -> Optional[ExceptionMinimumRowLen]:
        if len(row) <= MIN_ROW_LENGTH:
            raise ExceptionMinimumRowLen(
                f'check_minimum_matrix_len :: '
                f'size from {row} <= {MIN_ROW_LENGTH}'
            )
        return

    @staticmethod
    def check_strict_dna_letters(
        *,
        letter: str
    ) -> Optional[ExceptionInvalidDnaLetters]:
        if letter not in DNA_LETTERS:
            raise ExceptionInvalidDnaLetters(
                f'check_strict_dna_letters :: '
                f'dna letter {letter} not in strict {DNA_LETTERS}'
            )
        return

    def check_if_matrix_is_square(
        self,
        *,
        len_row: int
    ) -> Optional[ExceptionMatrixNotIsSquare]:
        if len_row != self.max_len_matrix:
            raise ExceptionMatrixNotIsSquare(
                f'check_if_matrix_is_square :: '
                f'matrix will be square'
            )
        return

    def parse_dna_to_matrix(self) -> List[List[str]]:
        _matrix = []
        for str_item in self.dna:
            self.check_minimum_row_len(row=str_item)
            self.check_if_matrix_is_square(len_row=len(str_item))
            _matrix.append(list(str_item))
        self.check_if_matrix_is_square(len_row=len(_matrix))
        return _matrix

    # Main Method
    def is_mutant(self) -> bool:
        mutant_dna_found = 0
        dna_matrix = self.dna_matrix
        for row in range(len(dna_matrix)):
            for column in range(len(dna_matrix[row])):
                pivot_letter = dna_matrix[row][column]
                self.check_strict_dna_letters(letter=pivot_letter)

                if mutant_dna_found > 1:
                    return True

                # Check Right direction
                if (
                        column + MAX_MUTANT_SEQUENCE < self.max_len_matrix and
                        self.check_right(
                            row=row,
                            column=column,
                            actual_letter=pivot_letter
                        )
                ):
                    mutant_dna_found += 1

                # Check the other directions
                if row + MAX_MUTANT_SEQUENCE < self.max_len_matrix:
                    # Check Down direction
                    if self.check_down(
                        row=row,
                        column=column,
                        actual_letter=pivot_letter
                    ):
                        mutant_dna_found += 1
                    # Check Right-Diagonal direction
                    if (
                        column + MAX_MUTANT_SEQUENCE < self.max_len_matrix and
                        self.check_right_diagonal(
                            row=row,
                            column=column,
                            actual_letter=pivot_letter
                        )
                    ):
                        mutant_dna_found += 1
                    # Check Left-Diagonal direction
                    if (
                            column - MAX_MUTANT_SEQUENCE >= 0 and
                            self.check_left_diagonal(
                                row=row,
                                column=column,
                                actual_letter=pivot_letter
                            )
                    ):
                        mutant_dna_found += 1

        return False

    def check_right(
        self,
        *,
        row: int,
        column: int,
        actual_letter: str
    ) -> bool:
        loop_begin = column + 1
        loop_end = loop_begin + MAX_MUTANT_SEQUENCE
        for index_column in range(loop_begin, loop_end):
            if self.dna_matrix[row][index_column] != actual_letter:
                return False
        return True

    def check_down(
        self,
        *,
        row: int,
        column: int,
        actual_letter: str
    ) -> bool:
        loop_begin = row + 1
        loop_end = loop_begin + MAX_MUTANT_SEQUENCE
        for index_row in range(loop_begin, loop_end):
            if self.dna_matrix[index_row][column] != actual_letter:
                return False
        return True

    def check_right_diagonal(
        self,
        *,
        row: int,
        column: int,
        actual_letter: str
    ) -> bool:
        loop_begin = row + 1
        loop_end = loop_begin + MAX_MUTANT_SEQUENCE
        index_column = column + 1
        for index_row in range(loop_begin, loop_end):
            if self.dna_matrix[index_row][index_column] != actual_letter:
                return False
            index_column += 1
        return True

    def check_left_diagonal(
        self,
        *,
        row: int,
        column: int,
        actual_letter: str
    ) -> bool:
        loop_begin = row + 1
        loop_end = loop_begin + MAX_MUTANT_SEQUENCE
        index_column = column - 1
        for index_row in range(loop_begin, loop_end):
            if self.dna_matrix[index_row][index_column] != actual_letter:
                return False
            index_column -= 1
        return True
