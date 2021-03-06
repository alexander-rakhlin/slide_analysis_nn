import os
from pathlib import Path

from slide_analysis_nn.tile import TILE_SIZE

PROJECT_PATH = Path(os.path.abspath(os.path.dirname(__file__)))

TRAIN_TEST_DATASET_PERCENT = 0.7
NUMBER_OF_SAMPLES_PER_SLIDE = 1000

EPOCHS = 30
BATCH_SIZE = 128
TRAIN_STEPS = None
VALIDATION_STEPS = None
MIN_DELTA = 1e-4
PATIENCE = 5

NETWORK_INPUT_SHAPE = (224, 224, 3)
HEALTHY_MASK_NUM_OF_DILLATIONS = 5

SNAPSHOTS_DIR = PROJECT_PATH / 'snapshots'
TF_BOARD_LOGS_DIR = PROJECT_PATH / 'logs'
