from ... import BLACK_CS, WHITE_CS


def is_bullish_neck(htd):
    if len(htd) < 2:
        raise Exception("Sorry, neck model requires minimum 2 bars")
    _current_bar = htd.iloc[-1]
    _prev_bar = htd.iloc[-2]
    _1st_condition = bullish_neck_cond_1(_current_bar, _prev_bar)
    _2nd_condition = neck_cond_2(_current_bar, _prev_bar)
    _3rd_condition = bullish_neck_cond_3(_current_bar, _prev_bar)
    return bool(_1st_condition and _2nd_condition and _3rd_condition)


def is_bearish_neck(htd):
    if len(htd) < 2:
        raise Exception("Sorry, neck model requires minimum 2 bars")
    _current_bar = htd.iloc[-1]
    _prev_bar = htd.iloc[-2]
    _1st_condition = bearish_neck_cond_1(_current_bar, _prev_bar)
    _2nd_condition = neck_cond_2(_current_bar, _prev_bar)
    _3rd_condition = bearish_neck_cond_3(_current_bar, _prev_bar)
    return bool(_1st_condition and _2nd_condition and _3rd_condition)


# -----------------------------------------------Conditions------------------------------------------------------------
def bullish_neck_cond_1(_current_bar, _prev_bar):
    """
    Idea:
        1. current_color = black
        2. prev_color = white
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return bool(_current_bar['color'] == BLACK_CS and _prev_bar['color'] == WHITE_CS)


def neck_cond_2(_current_bar, _prev_bar):
    """
    Idea:
        1. prev_body > 2 * current_body
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return _prev_bar['body'] > 2 * _current_bar['body']


def bullish_neck_cond_3(_current_bar, _prev_bar):
    """
    Idea:
        1. current_close > (prev_close + prev_open) / 2
        2. current_open > prev_close
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return bool(_current_bar['Open'] > _prev_bar['Close'] and _current_bar['Close'] > (_prev_bar['Close'] + _prev_bar['Open']) / 2)


def bearish_neck_cond_1(_current_bar, _prev_bar):
    """
    Idea:
        1. current_color = white
        2. prev_color = black
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return bool(_current_bar['color'] == WHITE_CS and _prev_bar['color'] == BLACK_CS)


def bearish_neck_cond_3(_current_bar, _prev_bar):
    """
    Idea:
        1. current_close < (prev_close + prev_open) / 2
        2. current_open < prev_close
    :param _current_bar:
    :param _prev_bar:
    :return:
    """
    return bool(_prev_bar['Close'] > _current_bar['Open'] and _current_bar['Close'] < (_prev_bar['Close'] + _prev_bar['Open']) / 2)
