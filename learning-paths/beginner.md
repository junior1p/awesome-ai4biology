# Learning Paths: Beginner → Advanced

A structured journey from foundations to research-level skills in AI × Biology.

---

## 🎯 Overview

This repository provides **5 learning tracks**, each with 3 difficulty levels:

| Track | Time to Proficiency | Target Skills |
|-------|-------------------|---------------|
| [Omics](#omics-track) | 12-16 weeks | Genomics, variant analysis, RNA-seq |
| [Protein](#protein-track) | 10-14 weeks | Structure prediction, design, MD |
| [Drug Discovery](#drug-discovery-track) | 10-14 weeks | Molecule ML, docking, virtual screening |
| [Single-Cell](#single-cell-track) | 8-12 weeks | scRNA-seq, integration, spatial |
| [Imaging](#imaging-track) | 6-10 weeks | Bioimage analysis, segmentation |

---

## 📅 12-Week Foundation Sprint

**Recommended for**: All tracks (complete first)

```
Weeks 1-2:  Python + Linux + Git
├── Python basics (functions, classes, numpy, pandas)
├── Jupyter notebooks for exploration
├── Linux CLI (ls, grep, awk, sed, piping)
└── Git + GitHub (commit, branch, PR)

Weeks 3-4:  Reproducible Computing
├── Conda environments + conda-forge
├── Docker basics (pull, run, build)
├── Jupyter → script conversion
└── Basic R (optional, for Bioconductor users)

Weeks 5-6:  ML Foundations
├── PyTorch basics (tensors, autograd, modules)
├── scikit-learn (train/test splits, basic classifiers)
├── Deep learning fundamentals (MLP, CNN basics)
└── Evaluation basics (accuracy, precision, recall, ROC)
```

---

## 🧬 Omics Track

```
Duration: 12-16 weeks | Prerequisite: Foundation Sprint

├── Week 7-8: Sequencing Data Fundamentals
│   ├── FASTQ format + FastQC quality control
│   ├── Alignment basics (Bowtie2, STAR)
│   ├── SAM/BAM manipulation (samtools)
│   └── Variant calling intro (GATK basics)
│
├── Week 9-10: RNA-Seq & Expression Analysis
│   ├── Alignment + quantification (Salmon, featureCounts)
│   ├── DESeq2 / edgeR for differential expression
│   ├── Pathway analysis (g:Profiler, Enrichr)
│   └── nf-core RNA-seq pipeline
│
├── Week 11-12: Regulatory Genomics & Foundation Models
│   ├── Noncoding variant effects (DeepSEA)
│   ├── Sequence-to-expression (Enformer)
│   ├── DNABERT fine-tuning basics
│   └── Advanced: Evo, LucaOne exploration
│
├── Week 13-16: Capstone Projects (choose one)
│   ├── [ ] Rerun RNA-seq pipeline on GEO dataset
│   ├── [ ] Train DNABERT on species-specific task
│   ├── [ ] Reproduce Enformer predictions + compare
│   └── [ ] Build variant effect predictor
```

---

## 🧪 Protein Track

```
Duration: 10-14 weeks | Prerequisite: Foundation Sprint

├── Week 7-8: Protein Data & Structure Basics
│   ├── UniProt: searching, downloading, API
│   ├── RCSB PDB: structure viewing (PyMOL/Chimera)
│   ├── AlphaFold DB: accessing predictions
│   └── Protein properties (Expasy tools)
│
├── Week 9-10: Structure Prediction
│   ├── AlphaFold2 usage (ColabFold, local)
│   ├── ESMFold for fast prediction
│   ├── Interpreting confidence scores (pLDDT, PAE)
│   └── Structural alignment (TM-align)
│
├── Week 11-12: Protein Design & Generation
│   ├── RFdiffusion for backbone generation
│   ├── ProteinMPNN for sequence design
│   ├── ProtGPT2 for de novo sequence exploration
│   └── Design validation (AlphaFold refinement)
│
├── Week 13-14: Molecular Dynamics (Optional Deep Dive)
│   ├── OpenMM basics: energy minimization, MD
│   ├── Force fields and parameters
│   ├── Analysis: RMSD, RMSF, hydrogen bonds
│   └── Advanced: FEP+, relative binding free energy
│
├── Week 15-16: Capstone Projects (choose one)
│   ├── [ ] Predict structure of a novel protein family
│   ├── [ ] Design a mini-protein (e.g., 50 aa) with RFdiffusion
│   ├── [ ] Compare AlphaFold2 vs ESMFold on a dataset
│   └── [ ] Build a protein stability predictor
```

---

## 💊 Drug Discovery Track

```
Duration: 10-14 weeks | Prerequisite: Foundation Sprint

├── Week 7-8: Chemistry Foundations
│   ├── SMILES, RDKit molecule parsing
│   ├── Molecular fingerprints (Morgan, MACCS)
│   ├── RDKit descriptors and properties
│   └── Basic molecular visualization
│
├── Week 9-10: Molecule Machine Learning
│   ├── DeepChem tutorials (MoleculeNet)
│   ├── Graph neural networks (PyG LifeSci)
│   ├── Property prediction models
│   └── Dataset exploration: ChEMBL, PubChem, ZINC
│
├── Week 11-12: Molecular Docking & Virtual Screening
│   ├── AutoDock Vina basics
│   ├── DiffDock for pose prediction
│   ├── Virtual screening workflow
│   └── Scoring functions and refinement
│
├── Week 13-14: Generative Design (Advanced)
│   ├── Junction Tree VAE
│   ├── GuacaMol for molecular generation benchmarks
│   ├── Multi-objective optimization
│   └── Retrosynthesis planning (AiZynthFinder)
│
├── Week 15-16: Capstone Projects (choose one)
│   ├── [ ] Build a solubility predictor on MoleculeNet
│   ├── [ ] Virtual screen a ZINC subset against a target
│   ├── [ ] Generate novel molecules with DeepChem
│   └── [ ] Reproduce a binding affinity benchmark
```

---

## 🔬 Single-Cell Track

```
Duration: 8-12 weeks | Prerequisite: Foundation Sprint

├── Week 7-8: scRNA-seq Analysis Fundamentals
│   ├── Scanpy: from count matrix to clusters
│   ├── Seurat (R): alternative workflow
│   ├── QC, normalization, PCA, UMAP
│   └── Cell type annotation (CellTypist)
│
├── Week 9-10: Integration & Advanced Analysis
│   ├── Batch correction (Harmony, BBKNN)
│   ├── Trajectory analysis (Monocle3, PAGA)
│   ├── Gene set enrichment (scanpy.tl.rank_features_groups)
│   └── CellPhoneDB for cell-cell communication
│
├── Week 11-12: Foundation Models & Spatial
│   ├── scGPT: transfer learning for new datasets
│   ├── scvi-tools: probabilistic modeling
│   ├── Spatial transcriptomics (SpaGCN, Cell2location)
│   └── Multi-omics integration (scJoint)
│
├── Week 13-16: Capstone Projects (choose one)
│   ├── [ ] Analyze a public HCA dataset end-to-end
│   ├── [ ] Fine-tune scGPT on a disease dataset
│   ├── [ ] Compare trajectory methods on developmental data
│   └── [ ] Integrate scRNA-seq + spatial data
```

---

## 🏥 Imaging Track

```
Duration: 6-10 weeks | Prerequisite: Foundation Sprint

├── Week 7-8: Bioimage Analysis Basics
│   ├── napari: interactive visualization
│   ├── Cellpose: cell segmentation
│   ├── ImageJ/Fiji basics
│   └── OME-Zarr format for large images
│
├── Week 9-10: Deep Learning for Images
│   ├── StarDist for nuclei segmentation
│   ├── Cellpose 4 (trainable models)
│   ├── ilastik for pixel classification
│   └── BioImage.IO model zoo usage
│
├── Week 11-12: Advanced Topics
│   ├── 3D segmentation and tracking
│   ├── Multi-channel analysis
│   ├── Morphometric analysis
│   └── Building reproducible imaging workflows
│
├── Week 13-14: Capstone Projects (choose one)
│   ├── [ ] Segment cells in a fluorescence image dataset
│   ├── [ ] Train Cellpose on a custom cell type
│   ├── [ ] Analyze morphology in a drug screening dataset
│   └── [ ] Build an analysis pipeline with napari plugins
```

---

## 📊 Skill Assessment Rubrics

### Beginner ✓
- Can run existing tools/scripts without modification
- Can interpret basic outputs (plots, tables)
- Understands file formats (FASTA, FASTQ, PDB)
- Can follow tutorials and documentation

### Intermediate ✓
- Can adapt tools to new datasets
- Can troubleshoot common errors
- Can chain tools into simple pipelines
- Understands data structures (AnnData, Seurat)

### Advanced ✓
- Can fine-tune foundation models
- Can build custom ML models for domain problems
- Can evaluate OOD generalization and uncertainty
- Can design and execute research-grade projects

---

## ⚠️ Data & License Checklist

Before starting any project, verify:

| Data Type | License | Can I use it? |
|-----------|---------|---------------|
| RCSB PDB | CC0 | ✅ Yes, cite source |
| UniProt | CC BY 4.0 | ✅ Yes, cite + attribute |
| ChEMBL | CC BY-SA | ✅ Yes, cite + shareAlike |
| AlphaFold DB | CC BY 4.0 | ✅ Yes, cite |
| AlphaFold Server | Non-commercial | ⚠️ Academic OK, commercial ❌ |
| AlphaFold3 weights | Non-commercial | ⚠️ Academic OK, commercial ❌ |
| TCGA | dbGaP controlled | ❌ Requires authorization |
| PDBbind | Redistribution prohibited | ⚠️ Access but don't redistribute |

---

## 🚀 Quick Links

- [Skill Matrix](../skills/skill-matrix.md) — Cross-domain skills reference
- [Resource Registry](../resources/registry/resources.csv) — Full resource list
- [By Domain](../resources/by-domain/) — Domain-specific pages
- [By Method](../resources/by-method/) — Method-specific pages
