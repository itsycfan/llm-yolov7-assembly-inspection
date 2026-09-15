# llm-yolov7-assembly-inspection

Multimodal manual-assembly guidance and error-inspection system combining
GPT-4 (reasoning) and YOLOv7 (component/tool/step detection), with speech
recognition and text-to-speech feedback for operators. Developed as part
of a PhD research project; supports a CIRP 2024 submission.

## Pipeline overview

1. **Detection** — YOLOv7 (`third_party/yolov7`, weights in `models/`)
   detects components, tools, and assembly steps from camera/video input.
2. **Reasoning** — GPT-4 (`notebooks/main_pipeline.ipynb`, prompts in
   `configs/gpt_prompt.xlsx`) checks detected state against
   `configs/assembly_tasks.xlsx` and `configs/error_templates.xlsx` to
   flag assembly errors.
3. **Interaction** — Speech recognition transcribes operator speech;
   text-to-speech (`src/GUI.py`) reads back guidance/warnings.
4. **Logging** — Errors and session transcripts are logged for review.

## Repository layout

- `configs/` — task definitions, error templates, GPT prompt templates
- `notebooks/` — main pipeline notebooks + data-table builder notebooks
- `src/` — GUI and case-study runner scripts
- `third_party/yolov7/` — vendored YOLOv7 detector (see its README)
- `models/` — trained weights (not committed; see `models/README.md`)
- `simulation/` — RoboDK simulation project (`Yuchen_2024.rdk`)
- `docs/paper/` — CIRP 2024 paper figures and case-study material
- `assets/demo/` — small sample outputs (images/audio/logs) for
  demonstration; full raw experiment data is archived separately
- `archive/` — pre-git development history snapshots (reference only)

## Setup

```bash
pip install -r requirements.txt
```

Download the YOLOv7 weights per `models/README.md` before running
`notebooks/main_pipeline.ipynb`.

## Citation

TODO: add paper title, authors, and BibTeX citation once available.
