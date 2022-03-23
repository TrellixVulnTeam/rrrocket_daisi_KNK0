import subprocess
import json

import pandas as pd

from rrrocket_retriever import get_latest_rrrocket_release
from rrrocket_processor import process_match_overview, proccess_match_overview_raw


def process_replay_dataframe(file_path: pd.DataFrame):
    bin_path = get_latest_rrrocket_release()

    result = subprocess.check_output([bin_path, '-n', file_path])
    result = json.loads(result.decode('utf-8'))

    blue, orange = process_match_overview(result['properties'])

    return [{'type': 'dataframe', 'label': 'Blue Team', 'data': blue},
            {'type': 'dataframe', 'label': 'Orange Team', 'data': orange}]


def process_replay_raw(file_path: pd.DataFrame):
    bin_path = get_latest_rrrocket_release()

    result = subprocess.check_output([bin_path, '-n', file_path])
    result = json.loads(result.decode('utf-8'))
    blue, orange = proccess_match_overview_raw(result['properties'])

    return [{'type': 'json', 'label': 'Blue Team', 'data': blue},
            {'type': 'json', 'label': 'Orange Team', 'data': orange}]
