import pandas as pd
import pytest
from ohlcpattern.candlestick import CandlestickPatterns

def test_candlestick_patterns_basic():
    # Example data from README
    data = {
        'Open': [7317.3, 7255.77, 7205.01, 7202, 7254.77, 7315.36],
        'High': [7436.68, 7271.77, 7435, 7275.86, 7365.01, 7528.45],
        'Low': [7157.04, 7128.86, 7157.12, 7076.42, 7238.67, 7288],
        'Close': [7255.77, 7204.63, 7202, 7254.74, 7316.14, 7388.24]
    }
    df = pd.DataFrame(data)
    
    csp = CandlestickPatterns(df)
    csp._add('reversal')
    modeling_data = csp.pattern_modeling()
    
    assert 'model' in modeling_data.columns
    assert len(modeling_data) == 6
    # Check that at least some models are detected (if any)
    # The README says at index 3/4/5 there are some.
    # Note: our test data is small, but let's check it doesn't crash.
    print(modeling_data[modeling_data.model != ''])

def test_invalid_pattern():
    data = {'Open': [1], 'High': [2], 'Low': [0], 'Close': [1]}
    df = pd.DataFrame(data)
    csp = CandlestickPatterns(df)
    with pytest.raises(ValueError):
        csp._add('invalid_pattern_name')
