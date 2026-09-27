from prompt_optimizer.metric import Metric, TokenMetric
from prompt_optimizer.poptim import (
    LemmatizerOptim,
    NameReplaceOptim,
    PromptOptim,
    PulpOptim,
    PunctuationOptim,
    StemmerOptim,
    StopWordOptim,
)
from prompt_optimizer.visualize import StringDiffer


def __getattr__(name):
    # BERTScoreMetric needs torch + transformers; import lazily so the
    # rest of the library works without those heavy optional deps.
    if name == "BERTScoreMetric":
        from prompt_optimizer.metric.bertscore_metric import BERTScoreMetric
        return BERTScoreMetric
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "StringDiffer",
    "Metric",
    "BERTScoreMetric",
    "TokenMetric",
    "PromptOptim",
    "LemmatizerOptim",
    "StopWordOptim",
    "NameReplaceOptim",
    "PunctuationOptim",
    "PulpOptim",
    "StemmerOptim",
    "AutocorrectOptim",
    "SynonymReplaceOptim",
    "EntropyOptim",
]
