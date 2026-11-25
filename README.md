# SmartVision AI

**Status:** teaching and portfolio project. It measures image statistics; it does not contain a trained neural network.

A beginner-friendly Python + Streamlit computer-vision dashboard.

## Features
- Upload JPG, JPEG and PNG images
- Image dimensions, brightness and contrast analysis
- RGB channel statistics
- Rule-based demo classification workflow
- Local analysis history with clear-history option

## Important limitation
This starter project does **not** contain a trained neural network and does not identify real objects. The demo category is based only on manually selected brightness and contrast values. For a genuine classification research project, add a labelled dataset and train/evaluate a model before describing it as an AI image classifier.

## Requirements
- Python 3.10 or newer
- Visual Studio Code
- Python extension for VS Code

## Run on Windows
Open this folder in VS Code, then open Terminal → New Terminal:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

## Run on macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown in the terminal, normally `http://localhost:8501`.

## Tests

```bash
python -m pip install pytest
python -m pytest -q
```

## Folder structure
```text
SmartVision_AI/
├── app.py
├── requirements.txt
├── README.md
├── analysis_history.json  (created at run time, not in git)
├── tests/
└── src/
    ├── __init__.py
    ├── vision.py
    └── history.py
```

## Suggested academic extensions
1. Train a CNN or transfer-learning classifier on a documented, licensed dataset.
2. Add train/validation/test splits and reproducible random seeds.
3. Report precision, recall, macro-F1 and a confusion matrix.
4. Evaluate inference latency and calibration.
5. Test on images from a different source to measure generalization.

## How to cite

```bibtex
@software{hussain2026smartvision,
  author = {Hussain, Muzammal},
  title  = {{SmartVision: image statistics dashboard}},
  year   = {2026},
  url    = {https://github.com/MHKhan50/SmartVision-AI-DeepLearning}
}
```

## Author

Muzammal Hussain, independent researcher, Glasgow, United Kingdom.
ORCID: [0009-0001-2570-5686](https://orcid.org/0009-0001-2570-5686)

## Licence

MIT. See `LICENSE`.

