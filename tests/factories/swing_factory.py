from datetime import datetime

from src.models.swing import Swing


def make_swing(
    index=0,
    time=None,
    price=100.0,
    swing_type=Swing.HIGH
):
    """
    Creates a Swing object for tests.
    """

    return Swing(
        index=index,
        time=time or datetime.now(),
        price=price,
        swing_type=swing_type
    )


def make_high_swing(**kwargs):
    """
    Creates a HIGH swing.
    """

    defaults = dict(
        swing_type=Swing.HIGH,
        price=100
    )

    defaults.update(kwargs)

    return make_swing(**defaults)


def make_low_swing(**kwargs):
    """
    Creates a LOW swing.
    """

    defaults = dict(
        swing_type=Swing.LOW,
        price=100
    )

    defaults.update(kwargs)

    return make_swing(**defaults)