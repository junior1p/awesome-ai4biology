# 🧬 Awesome AI4Biology Skills

[English](./README.md) | 中文

> A curated, **skills-first** map of AI × Biology: tools, models, tutorials, datasets, papers, and learning paths — designed for sustainability and long-term maintainability.

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0](https://img.shields.io/badge/License-CC0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 What This Repo Is

This repository is **not just a list of links**. It's a structured, curated collection of AI for Biology resources organized by:

- **Skills taxonomy** — cross-domain competencies and how they build on each other
- **Resource registry** — machine-readable CSV with license, difficulty, and compliance info
- **Learning paths** — beginner → advanced tracks for 5 major domains
- **Quality standards** — official sources preferred, compliance flags for restricted data/models

## 👤 Who It's For

- Undergraduates/graduates in bioinformatics, computational biology, ML/CS
- Researchers transitioning to AI × Biology
- Practitioners in pharma, biotech, clinical informatics
- Educators building curricula

> **Default user**: Knows Python or R, but depth in biology and AI varies.

## 📁 Repository Structure

```
awesome-ai4biology/
├── README.md                    # This file
├── LICENSE                      # MIT (code) + CC BY 4.0 (docs)
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md              # Contribution guidelines
│
├── resources/
│   ├── registry/
│   │   ├── resources.csv        # ⭐ Single source of truth (machine-readable)
│   │   └── schema.json          # CSV schema definition
│   ├── by-domain/               # Human-readable domain pages (planned)
│   └── by-method/               # Human-readable method pages (planned)
│
├── skills/
│   └── skill-matrix.md          # Cross-domain skill framework
│
├── learning-paths/
│   ├── beginner.md              # Foundation + domain tracks
│   └── tracks/                  # Per-domain learning paths (planned)
│
└── scripts/
    ├── validate_resources.py    # CSV validation
    └── build_indexes.py         # Auto-generate domain pages (planned)
```

## 🚀 Quick Start

### 1. Pick a Track

| Track | Time | What You'll Learn |
|-------|------|-------------------|
| [Omics](./learning-paths/beginner.md#-omics-track) | 12-16 weeks | Genomics, variant analysis, RNA-seq, foundation models |
| [Protein](./learning-paths/beginner.md#-protein-track) | 10-14 weeks | Structure prediction, design, molecular dynamics |
| [Drug Discovery](./learning-paths/beginner.md#-drug-discovery-track) | 10-14 weeks | Molecule ML, docking, virtual screening, generative design |
| [Single-Cell](./learning-paths/beginner.md#-single-cell-track) | 8-12 weeks | scRNA-seq, integration, spatial, foundation models |
| [Imaging](./learning-paths/beginner.md#-imaging-track) | 6-10 weeks | Bioimage analysis, segmentation, deep learning |

### 2. Follow the Learning Path

Start with the **Foundation Sprint** (Weeks 1-6), then pick a domain track.

See [Learning Paths](./learning-paths/beginner.md) for detailed week-by-week plans.

### 3. Find Resources

Browse the **[Resource Registry](./resources/registry/resources.csv)** (CSV) to filter by:
- `category` — Omics, Protein, Drug discovery, etc.
- `license` — MIT, CC0, Non-commercial ToS, etc.
- `difficulty` — Beginner, Intermediate, Advanced

## 📊 Repository Stats

| Metric | Count |
|--------|-------|
| Total Categories | 9 |
| Total Resources | 60+ |
| Learning Tracks | 5 |
| Skill Areas | 25+ |

**Resource Distribution** (from registry):

```
Omics           ████████████████  15
Foundations     █████████████     13
Protein         ███████████       11
Single-cell     █████████          9
Drug discovery  █████████          9
Imaging         ██████             6
Synthetic Bio   █████              5
AI Agents       ████               4
Benchmarks      ████               3
```

## 🛠️ Skill Matrix Highlights

### Foundations (All Domains)
- Python/R + Jupyter + Git
- Conda/Docker for reproducibility
- Nextflow/Snakemake workflows

### Domain-Specific

| Domain | Key Skills |
|--------|-----------|
| **Omics** | FASTQ/BAM/VCF handling, variant calling, regulatory genomics, DNABERT/Evo |
| **Protein** | AlphaFold, ESMFold, RFdiffusion, ProteinMPNN, OpenMM |
| **Drug Discovery** | RDKit, DeepChem, molecular docking, virtual screening |
| **Single-Cell** | Scanpy, Seurat, scvi-tools, scGPT, spatial methods |
| **Imaging** | napari, Cellpose, OME-Zarr, BioImage.IO |

See full [Skill Matrix](./skills/skill-matrix.md) for detailed skill trees.

## ⚠️ Compliance & Licensing

**Every resource in this repo includes license/terms info.** Key points:

### Open / Free to Use ✓
| Resource | License | Notes |
|----------|---------|-------|
| RCSB PDB | CC0 | ✅ Cite, good for practice |
| UniProt | CC BY 4.0 | ✅ Cite + attribute |
| AlphaFold DB | CC BY 4.0 | ✅ Academic use |
| PubChem | Public domain | ✅ Very permissive |

### Restricted ⚠️
| Resource | Restriction | Action Required |
|----------|-------------|-----------------|
| AlphaFold Server | Non-commercial only | Don't use for commercial drug discovery |
| AlphaFold3 weights | Non-commercial + output restrictions | Read WEIGHTS_TERMS_OF_USE |
| TCGA / dbGaP data | Controlled access | Requires authorization |
| PDBbind | Redistribution prohibited | Access OK, don't mirror |

See [Learning Paths](./learning-paths/beginner.md#⚠️-data--license-checklist) for full compliance checklist.

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- Quality standards (official sources only)
- Required fields for each entry
- Compliance requirements
- Review checklist

**Quick PR process**:
1. Edit `resources/registry/resources.csv`
2. Run `python scripts/validate_resources.py` to check
3. Submit PR with description of why the resource belongs

## 📚 Related Resources

- [awesome-ai-for-science](https://github.com/helix Inst/awesome-ai-for-science) — Broader AI for science
- [Awesome-Bio-Foundation-Models](https://github.com.com/GenePhysics/awesome-bio-foundation-models) — Bio foundation model papers
- [OpenClaw Medical Skills](https://openclaw.ai/skills) — 200+ bio AI skills
- [K-Dense](https://github.com/K-Dense/kdense) — 136 bio skills

## 📄 License

- **Code & scripts**: MIT License
- **Documentation & curated content**: CC BY 4.0
- **Note**: Individual resources have their own licenses — always check before using

**Important**: This repository does NOT re-license any external data/models. It provides links and terms guidance only.

---

<p align="center">
  <strong>⭐ If you find this repository useful, please consider giving it a star! ⭐</strong>
</p>
