from src.detector import detect_bruteforce
import pandas as pd


def test_failed_detection():
    df = pd.DataFrame({
        'status': ['failed', 'success']
    })

    result = detect_bruteforce(df)

    assert len(result) == 1
