from prompt_optimizer.metric.base import Metric
from prompt_optimizer.metric.token_metric import TokenMetric


def __getattr__(name):
    # BERTScoreMetric needs torch + transformers; import lazily so the
    # rest of the library works without those heavy optional deps.
    if name == "BERTScoreMetric":
        from prompt_optimizer.metric.bertscore_metric import BERTScoreMetric
        return BERTScoreMetric
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = ["Metric", "BERTScoreMetric", "TokenMetric"]
