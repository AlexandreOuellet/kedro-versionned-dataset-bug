from typing import Any, Dict
import logging

import pandas as pd
import numpy as np

import time

logger = logging.getLogger(__name__)


def A(parameters: Dict[str, Any]):
    time.sleep(parameters["sleep"])

    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    print(df.head())
    return df


def B(versionned_dataset):
    print(versionned_dataset.head())
    pass
