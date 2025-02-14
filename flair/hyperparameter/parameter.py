from enum import Enum


class Parameter(Enum):
    EMBEDDINGS = "embeddings"
    HIDDEN_SIZE = "hidden_size"
    USE_CRF = "use_crf"
    USE_RNN = "use_rnn"
    RNN_LAYERS = "rnn_layers"
    DROPOUT = "dropout"
    WORD_DROPOUT = "word_dropout"
    LOCKED_DROPOUT = "locked_dropout"
    LEARNING_RATE = "learning_rate"
    MINI_BATCH_SIZE = "mini_batch_size"
    ANNEAL_FACTOR = "anneal_factor"
    ANNEAL_WITH_RESTARTS = "anneal_with_restarts"
    PATIENCE = "patience"
    OPTIMIZER = "optimizer"
    MOMENTUM = "momentum"
    DAMPENING = "dampening"
    WEIGHT_DECAY = "weight_decay"
    NESTEROV = "nesterov"
    AMSGRAD = "amsgrad"
    BETAS = "betas"
    EPS = "eps"
    TRANSFORMER_MODEL = "model"
    LAYERS = "layers"
    #--- Sanctify additions ---#
    LAYER_MEAN = "layer_mean"
    POOLING = "cls_pooling"
    WARMUP_FRACTION = "warmup_fraction"
    SCHEDULER = "scheduler"

TRAINING_PARAMETERS = [
    Parameter.LEARNING_RATE.value,
    Parameter.MINI_BATCH_SIZE.value,
    Parameter.OPTIMIZER.value,
    Parameter.ANNEAL_FACTOR.value,
    Parameter.PATIENCE.value,
    Parameter.ANNEAL_WITH_RESTARTS.value,
    Parameter.MOMENTUM.value,
    Parameter.DAMPENING.value,
    Parameter.WEIGHT_DECAY.value,
    Parameter.NESTEROV.value,
    Parameter.AMSGRAD.value,
    Parameter.BETAS.value,
    Parameter.EPS.value,
    Parameter.WARMUP_FRACTION.value, # Sanctify additions
    Parameter.SCHEDULER.value,  # Sanctify additions

]
SEQUENCE_TAGGER_PARAMETERS = [
    Parameter.EMBEDDINGS.value,
    Parameter.HIDDEN_SIZE.value,
    Parameter.RNN_LAYERS.value,
    Parameter.USE_CRF.value,
    Parameter.USE_RNN.value,
    Parameter.DROPOUT.value,
    Parameter.LOCKED_DROPOUT.value,
    Parameter.WORD_DROPOUT.value,
]
TEXT_CLASSIFICATION_PARAMETERS = [
    Parameter.LAYERS.value,
    Parameter.TRANSFORMER_MODEL.value,
    Parameter.LAYER_MEAN.value, # Sanctify additions
    Parameter.POOLING.value, # Sanctify additions
]
