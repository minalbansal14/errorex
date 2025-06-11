# errorex

**Explain errors better.**

`errorex` is a Python library that automatically explains and logs runtime errors in your code by capturing:
- Code traceback (excluding library noise)
- Local variable snapshots
- Suggestions for common errors
- LLM-ready GPT prompts

# errorex

[![PyPI version](https://img.shields.io/pypi/v/errorex.svg)](https://pypi.org/project/errorex/)
[![Python Versions](https://img.shields.io/pypi/pyversions/errorex.svg)](https://pypi.org/project/errorex/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Explain errors better.**  
> `errorex` is a Python library that automatically captures and explains runtime errors in ML/data pipelines — complete with filtered traceback, local variables, fix suggestions, and GPT-ready prompts.

---

## 🔧 Installation

```bash
pip install errorex


from errorex import explain_errors

@explain_errors(log=True, suggest=True)
def run_pipeline():
    import pandas as pd
    from sklearn.linear_model import LogisticRegression

    df = pd.DataFrame({
        'feature': [1, 2, 3, 4],
        'label': [1, 0, 1, None]  # NaN will cause crash
    })

    X = df[['feature']]
    y = df['label']
    model = LogisticRegression()
    model.fit(X, y)

run_pipeline()

📝 What You Get in the Markdown Report
Full filtered traceback

All in-scope local variables at crash line

Smart suggestions like:

“y contains NaNs — use dropna()”

GPT-pasteable prompt for debugging:

## 🤖 LLM Debug Prompt
I encountered the following error in my script:
ValueError: Input y contains NaN

Code:
model.fit(X, y)

Variables:
- y: 0    1.0
     1    0.0
     3    NaN

What does this error mean and how can I fix it?

🧠 Features
📍 Clean traceback (excludes noisy site-packages)

🧠 Local variable snapshots

💡 Fix suggestions (NaNs, KeyErrors, shape mismatch)

📤 Markdown reports + GPT-ready prompts

🎛️ Configurable decorator: @explain_errors(log=True, suggest=False, raise_error=False)

🧪 Testing

pytest tests/


🙌 Contributing
Found a bug or want to add more auto-suggestions?
You're welcome to submit a pull request or open an issue.

📄 License
MIT © Minal Bansal


---

Let me know when you’ve added it — and I’ll help you with the next step: GitHub Actions or CLI entry point!
