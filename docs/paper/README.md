# Paper Materials

This repository accompanies the following publication:

**A video-driven LLM framework for assembly error detection and corrective
guidance in manual manufacturing tasks**

Yuchen Fan, Mara Borgia, Alessandro Simeone*, Dario Antonelli, Paolo C.
Priarone, Luca Settineri

*Department of Management and Production Engineering, Politecnico di
Torino, Italy*

Presented at the **19th CIRP Conference on Intelligent Computation in
Manufacturing Engineering (CIRP ICME 2025)**, 16-18 July 2025, Gulf of
Naples, Italy. Published in Procedia CIRP (Elsevier), open access under
CC BY-NC-ND 4.0.

DOI / volume / page numbers: TBD (not yet assigned at time of writing —
update once the final Procedia CIRP record is online).

## Abstract

Current AI-driven assembly assistance systems rely on static visual
inputs, limiting their ability to capture dynamic assembly operations.
This study presents a video-driven framework leveraging large language
models (LLMs) for automated error detection and corrective guidance in
manual assembly tasks. The methodology employs video sequences of
reference procedures and operator executions with structured prompts
for LLM comparative analysis. The framework incorporates
machine-in-the-loop for real-time correction and human-in-the-loop for
system refinement. An experimental validation on assembly tasks
analyses the framework capability in deviation detection, error
classification, and corrective instruction generation.

## Case study

Manual assembly of a centrifugal pump unit (22 operational steps,
S1-S22); this repository's experiments focus on the six most
error-prone steps (S15, S16, S17, S18, S21, S22). Two fixed HD cameras
(top view + side view) recorded reference and operator-execution
videos; ChatGPT-4.0 (OpenAI API) was used as the LLM assessment engine.

## Contents in this folder

- `figures/` — system screenshots (Capture1.PNG, Capture2.PNG)
- `case_study_figures/` — annotated case-study figures by category
  (component / operation / result / tool), for steps 6 and 9

## Citation

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
