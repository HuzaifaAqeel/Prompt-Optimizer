# ✂️ Prompt Optimizer

Minimize your LLM token usage to cut API costs — plug-and-play prompt optimizers with token metrics.

> **Attribution:** This project is based on [vaibkumr/prompt-optimizer](https://github.com/vaibkumr/prompt-optimizer) (MIT License). I made the heavy optional dependencies lazy so the lightweight optimizers work without torch/transformers.

## What it does

- 🧹 Strip stopwords, punctuation, and more from prompts
- 📏 Measure token counts before/after with `TokenMetric`
- 🔗 Chain optimizers with `SequentialOptim`
- 🧠 Entropy-based optimization with masked LMs (needs torch + transformers)

## What changed from the original

- Made `BERTScoreMetric` and `EntropyOptim` imports **lazy** — the original forced torch/transformers on every import, so now lightweight optimizers install and run without them

## Quick start

```python
from prompt_optimizer.metric import TokenMetric
from prompt_optimizer.poptim import StopWordOptim, PunctuationOptim
from prompt_optimizer.poptim.sequential import Sequential

seq = Sequential([StopWordOptim(), PunctuationOptim()], verbose=False, metrics=[TokenMetric()])
result = seq("Who is the president of the United States of America?")
print(result.content)  # fewer tokens, same meaning
```

## License

MIT — see [LICENSE](LICENSE) (original license by Vaibhav Kumar, preserved).
