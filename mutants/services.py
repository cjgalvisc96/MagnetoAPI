import logging
from typing import Dict, List

from mutants import selectors as mutants_selectors
from mutants.DNADetector import DNADetector
from mutants.models import Stats

logger = logging.getLogger(__name__)


def is_mutant(
    *,
    dna: List[str]
) -> bool:
    try:
        dna_detector = DNADetector(dna=dna)
        response = dna_detector.is_mutant()
    except Exception as error:
        logger.error(error)
        response = False

    if response:
        update_stats(count_mutant_dna=1, count_human_dna=0)
    else:
        update_stats(count_mutant_dna=0, count_human_dna=1)

    return response


def get_stats() -> Dict:
    response = dict(
        count_mutant_dna=0,
        count_human_dna=0,
        ratio=0.0
    )
    stats = mutants_selectors.get_stats()
    if stats.exists():
        stats = stats.first()
        response['count_mutant_dna'] = stats.count_mutant_dna
        response['count_human_dna'] = stats.count_human_dna
        response['ratio'] = stats.ratio

    return response


def update_stats(
    *,
    count_mutant_dna: int,
    count_human_dna: int
) -> None:
    stats = mutants_selectors.get_stats()
    if stats.exists():
        stats = stats.first()
        new_count_mutant_dna = stats.count_mutant_dna + count_mutant_dna
        new_count_human_dna = stats.count_human_dna + count_human_dna
        stats.count_mutant_dna = new_count_mutant_dna
        stats.count_human_dna = new_count_human_dna
        try:
            new_ratio = new_count_mutant_dna / new_count_human_dna
        except ZeroDivisionError:
            new_ratio = 0.0
        stats.ratio = new_ratio
        stats.save()
        return

    try:
        ratio = count_mutant_dna/count_human_dna
    except ZeroDivisionError:
        ratio = 0.0

    stats = dict(
        count_mutant_dna=count_mutant_dna,
        count_human_dna=count_human_dna,
        ratio=ratio
    )
    create_stats(stats=stats)


def create_stats(
    *,
    stats: Dict
) -> None:
    try:
        Stats.objects.create(
            count_mutant_dna=stats['count_mutant_dna'],
            count_human_dna=stats['count_human_dna'],
            ratio=stats['ratio']
        )
    except Exception as error:
        logger.error(f'create_stats :: {error}')
