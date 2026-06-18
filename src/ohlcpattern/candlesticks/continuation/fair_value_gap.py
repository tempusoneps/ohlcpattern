from ... import BLACK_CS, WHITE_CS


def is_fair_value_rising_gap(htd):
    if len(htd) < 3:
        raise Exception("Sorry, fair value gap model requires minimum 3 bars")
    _current_bar = htd.iloc[-1]
    _prev_1_bar = htd.iloc[-2]
    _prev_2_bar = htd.iloc[-3]
    _1st_condition = is_passed_1st_rising_condition(_current_bar, _prev_1_bar, _prev_2_bar)
    _2nd_condition = is_passed_2nd_rising_condition(_current_bar, _prev_1_bar, _prev_2_bar)
    return bool(_1st_condition and _2nd_condition)


def is_fair_value_falling_gap(htd):
    if len(htd) < 3:
        raise Exception("Sorry, fair value gap model requires minimum 3 bars")
    _current_bar = htd.iloc[-1]
    _prev_1_bar = htd.iloc[-2]
    _prev_2_bar = htd.iloc[-3]
    _1st_condition = is_passed_1st_falling_condition(_current_bar, _prev_1_bar, _prev_2_bar)
    _2nd_condition = is_passed_2nd_falling_condition(_current_bar, _prev_1_bar, _prev_2_bar)
    return bool(_1st_condition and _2nd_condition)


# -----------------------------------------------Conditions------------------------------------------------------------
def is_passed_1st_rising_condition(_current_bar, _prev_1_bar, _prev_2_bar):
    """
    Idea:
        1. current_color = white
        2. _prev_1_bar_color = white
        3. _prev_2_bar_color = white
    :param _current_bar:
    :param _prev_1_bar:
    :param _prev_2_bar:
    :return:
    """
    return bool(_current_bar['color'] == WHITE_CS and _prev_1_bar['color'] == WHITE_CS and _prev_2_bar['color'] == WHITE_CS)


def is_passed_2nd_rising_condition(_current_bar, _prev_1_bar, _prev_2_bar):
    """
        Idea:
            1. _prev_2_bar_high < current_low
        :param _current_bar:
        :param _prev_1_bar:
        :param _prev_2_bar:
        :return:
        """
    return _current_bar['Low'] > _prev_2_bar['High']


def is_passed_1st_falling_condition(_current_bar, _prev_1_bar, _prev_2_bar):
    """
    Idea:
        1. current_color = black
        2. _prev_1_bar_color = black
        3. _prev_2_bar_color = black
    :param _current_bar:
    :param _prev_1_bar:
    :param _prev_2_bar:
    :return:
    """
    return bool(_current_bar['color'] == BLACK_CS and _prev_1_bar['color'] == BLACK_CS and _prev_2_bar['color'] == BLACK_CS)


def is_passed_2nd_falling_condition(_current_bar, _prev_1_bar, _prev_2_bar):
    """
        Idea:
            1. _prev_2_bar_low > current_high
        :param _current_bar:
        :param _prev_1_bar:
        :param _prev_2_bar:
        :return:
        """
    return _current_bar['High'] < _prev_2_bar['Low']
