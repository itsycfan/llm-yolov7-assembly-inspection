# llm-yolov7-assembly-inspection

Multimodal manual-assembly guidance and error-inspection system combining
GPT-4 (reasoning) and YOLOv7 (component/tool/step detection), with speech
recognition and text-to-speech feedback for operators. Developed as part
of a PhD research project at Politecnico di Torino; accompanies a paper
presented at CIRP ICME 2025 (see [Citation](#citation)).

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
- `docs/paper/` — CIRP ICME 2025 paper details, figures, and case-study
  material (pump assembly, steps S15-S22)
- `assets/demo/` — small sample outputs (images/audio/logs) for
  demonstration; full raw experiment data is archived separately
- `archive/` — pre-git development history snapshots (reference only)

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"   # do not hardcode it in any file
```

Download the YOLOv7 weights per `models/README.md` before running
`notebooks/main_pipeline.ipynb`.

## Citation

If you use this code, please cite:

> Y. Fan, M. Borgia, A. Simeone, D. Antonelli, P. C. Priarone, L. Settineri,
> "A video-driven LLM framework for assembly error detection and corrective
> guidance in manual manufacturing tasks," *Procedia CIRP*, 19th CIRP
> Conference on Intelligent Computation in Manufacturing Engineering
> (CIRP ICME 2025), Gulf of Naples, Italy, 16-18 July 2025.

```bibtex
@inproceedings{fan2025videodriven,
  title     = {A video-driven {LLM} framework for assembly error detection and corrective guidance in manual manufacturing tasks},
  author    = {Fan, Yuchen and Borgia, Mara and Simeone, Alessandro and Antonelli, Dario and Priarone, Paolo C. and Settineri, Luca},
  booktitle = {Procedia CIRP},
  series    = {19th CIRP Conference on Intelligent Computation in Manufacturing Engineering (CIRP ICME 2025)},
  year      = {2025},
  publisher = {Elsevier},
  note      = {Gulf of Naples, Italy, 16--18 July 2025},
  doi       = {TBD}
}
```

Full details and abstract: see [`docs/paper/README.md`](docs/paper/README.md).
