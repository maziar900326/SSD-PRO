from src.models.structure import Structure

from tests.factories.swing_factory import (
    make_high_swing,
    make_low_swing,
)


def make_structure(
    structure_type=Structure.HH,
    swing=None
):
    """
    Creates a Structure object for tests.
    """

    if swing is None:

        if structure_type in (
            Structure.HH,
            Structure.LH
        ):
            swing = make_high_swing()

        else:
            swing = make_low_swing()

    return Structure(
        structure_type,
        swing
    )


def make_hh(**kwargs):

    return make_structure(
        Structure.HH,
        make_high_swing(**kwargs)
    )


def make_hl(**kwargs):

    return make_structure(
        Structure.HL,
        make_low_swing(**kwargs)
    )


def make_lh(**kwargs):

    return make_structure(
        Structure.LH,
        make_high_swing(**kwargs)
    )


def make_ll(**kwargs):

    return make_structure(
        Structure.LL,
        make_low_swing(**kwargs)
    )