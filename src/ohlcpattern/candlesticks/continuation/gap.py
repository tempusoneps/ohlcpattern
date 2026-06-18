from ... import BLACK_CS, WHITE_CS


def is_bullish_gap(htd):
    if len(htd) < 2:
        raise Exception("Sorry, gap model requires minimum 2 bars")
    _current_bar = htd.iloc[-1]
    _prev_bar = htd.iloc[-2]
    _1st_condition = bullish_gap_cond_1(_current_bar, _prev_bar)
    _2nd_condition = bullish_gap_cond_2(_current_bar, _prev_bar)
    return bool(_1st_condition and _2nd_condition)


def is_bearish_gap(htd):
    if len(htd) < 2:
        raise Exception("Sorry, gap model requires minimum 2 bars")
    _current_bar = htd.iloc[-1]
    _prev_bar = htd.iloc[-2]
    _1st_condition = bearish_gap_cond_1(_current_bar, _prev_bar)
    _2nd_condition = bearish_gap_cond_2(_current_bar, _prev_bar)
    return bool(_1st_condition and _2nd_condition)


# -----------------------------------------------Conditions------------------------------------------------------------
def bullish_gap_cond_1(_current_bar, _prev_bar):
    """
    Idea:
        1. current_color = white
        2. prev_color = white
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return bool(_current_bar['color'] == WHITE_CS and _prev_bar['color'] == WHITE_CS)


def bullish_gap_cond_2(_current_bar, _prev_bar):
    """
    Idea:
        1. prev_high < current_low
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return _prev_bar['High'] < _current_bar['Low']


def bearish_gap_cond_1(_current_bar, _prev_bar):
    """
    Idea:
        1. current_color = black
        2. prev_color = black
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return bool(_current_bar['color'] == BLACK_CS and _prev_bar['color'] == BLACK_CS)


def bearish_gap_cond_2(_current_bar, _prev_bar):
    """
    Idea:
        1. prev_low > current_high
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return _prev_bar['Low'] > _current_bar['High']
