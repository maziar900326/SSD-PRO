from src.models.bos import BOS

from tests.factories.structure_factory import (
    make_hh,
    make_ll,
)


def make_bos(
    direction=BOS.BULLISH,
    broken_structure=None,
    candle_index=10
):
    """
    Creates a BOS object for tests.
    """

    if broken_structure is None:

        if direction == BOS.BULLISH:
            broken_structure = make_hh()

        else:
            broken_structure = make_ll()

    return BOS(
        direction=direction,
        broken_structure=broken_structure,
        candle_index=candle_index
    )


def make_bullish_bos(**kwargs):

    defaults = dict(
        direction=BOS.BULLISH
    )

    defaults.update(kwargs)

    return make_bos(**defaults)


def make_bearish_bos(**kwargs):

    defaults = dict(
        direction=BOS.BEARISH
    )

    defaults.update(kwargs)

    return make_bos(**defaults)