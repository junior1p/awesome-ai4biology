# Skill Matrix for AI × Biology

A cross-domain skill framework that applies across Omics, Protein, Drug Discovery, Single-Cell, Imaging, and Synthetic Biology.

## 🏗️ Core Competency Layers

### Layer 1: Foundations (All Domains)

| Skill | Tools | Difficulty |
|-------|-------|------------|
| Python/R programming | Python, R, Jupyter | Beginner |
| Linux CLI & scripting | bash, GNU coreutils | Beginner |
| Version control | Git, GitHub | Beginner |
| Reproducible environments | Conda, Docker, Singularity | Intermediate |
| Workflow management | Nextflow, Snakemake, Galaxy | Intermediate |
| Container orchestration | Docker, Singularity, HPC | Intermediate |

### Layer 2: ML/AI Methods

| Skill | Tools | Difficulty |
|-------|-------|------------|
| Deep learning basics | PyTorch, TensorFlow | Intermediate |
| Transformer architectures | Hugging Face Transformers | Intermediate |
| Graph neural networks | PyTorch Geometric, DGL | Advanced |
| Generative models (VAE/Flow/Diffusion) | PyTorch, DeepChem | Advanced |
| Protein language models | ESM, ProtTrans, ProGen | Advanced |
| Single-cell foundation models | scGPT, Geneformer, scVI | Advanced |

### Layer 3: Data Engineering

| Skill | Tools | Difficulty |
|-------|-------|------------|
| Sequence data formats | FASTQ, BAM, CRAM, VCF, GTF | Beginner |
| Omics formats | AnnData, Seurat object | Intermediate |
| Imaging formats | OME-Zarr/NGFF, BioImage.IO | Intermediate |
| Chemical formats | SMILES, SDF, PDBQT | Beginner |
| Data versioning | DVC, Git LFS | Intermediate |
| Cloud storage | AWS S3, GCP, Azure | Intermediate |

---

## 📊 Domain-Specific Skill Trees

### Omics (Genomics/Transcriptomics/Proteomics/Metabolomics)

```
Beginner
├── FASTA/FASTQ/BAM handling (samtools, bedtools)
├── Sequence alignment & QC (FastQC, Bowtie2)
├── Differential expression (DESeq2, edgeR)
└── Reference genomes (GRCh38, GRCm38)
    │
    ▼
Intermediate
├── Variant calling (GATK, DeepVariant)
├── Regulatory genomics (DeepSEA, Enformer)
├── RNA-seq pipelines (nf-core, Salmon)
└── Multi-omics integration (MOFA+, MultiVI)
    │
    ▼
Advanced
├── Foundation models (DNABERT-2, Evo, LucaOne)
├── Single-cell multi-omics (scJoint, scMulan)
└── Population genomics & selection (pool-seq)
```

### Protein Structure & Design

```
Beginner
├── PDB structure viewing (PyMOL, Chimera)
├── Sequence analysis (BLAST, ClustalOmega)
├── UniProt & RCSB PDB usage
└── Basic protein properties (MW, pI, instability)
    │
    ▼
Intermediate
├── Structure prediction (AlphaFold2, ESMFold)
├── Sequence-structure visualization (PyMOL)
├── Molecular dynamics intro (OpenMM basics)
└── Protein language models (ESM, ProtTrans)
    │
    ▼
Advanced
├── De novo design (RFdiffusion, Chroma)
├── Sequence design (ProteinMPNN, ProGen)
├── Multi-state modeling (Rosetta, AlphaFold-Multimer)
└── Experimental validation & feedback loops
```

### Drug Discovery & Molecular ML

```
Beginner
├── SMILES & molecular representations
├── RDKit basics (fingerprinting, descriptors)
├── Molecular visualization (PyMOL, RDKit)
└── Basic ADMET concepts
    │
    ▼
Intermediate
├── Graph neural networks for molecules (PyG, DGL)
├── Property prediction (DeepChem, MoleculeNet)
├── Molecular docking (AutoDock Vina, DiffDock)
└── Dataset navigation (ChEMBL, PubChem, ZINC)
    │
    ▼
Advanced
├── Generative design (Junction Tree VAE, GraphNVP)
├── Multi-target optimization
├── Physics-based refinement (OpenMM, FEP)
└── Virtual screening at scale
```

### Single-Cell & Spatial Omics

```
Beginner
├── scRNA-seq analysis (Scanpy, Seurat)
├── QC, normalization, clustering
├── Cell type annotation (CellTypist)
└── Trajectory analysis (Monocle3, PAGA)
    │
    ▼
Intermediate
├── Multi-omics integration (scvi-tools, MultiVI)
├── Perturbation modeling (scGen, scRNA-seq+)
├── Spatial transcriptomics (SpaGCN, Cell2location)
└── Foundation models (scGPT, scFoundation)
    │
    ▼
Advanced
├── Cell-cell communication (CellPhoneDB, LIANA+)
├── Virtual cell models (VCWorld, scDiffEq)
├── Generative single-cell models (scDiffusion)
└── Perturbation atlases (Tahoe-100M)
```

---

## 📈 Evaluation & Reproducibility (Cross-Domain)

| Skill | Description | Tools |
|-------|-------------|-------|
| Cross-validation | Holdout, k-fold, stratified splits | scikit-learn |
| OOD evaluation | Distribution-shifted test sets | Custom |
| Uncertainty quantification | BayesianNNs, MC dropout, ensemble | PyTorch |
| Benchmarking | Standardized benchmarks per domain | TAPE, ProteinGym, etc. |
| Reproducibility | Environment pinning, containerization | Docker, Singularity, conda |
| Workflow reproducibility | Pipeline frameworks | Nextflow, Snakemake |
| License compliance | Data/model terms tracking | SPDX, this registry |

---

## ⚠️ Compliance & Ethics (Required for All Domains)

### Data Access Levels

| Level | Examples | Requirements |
|-------|----------|-------------|
| Open/CC0 | RCSB PDB, UniProt, PubChem | Cite source |
| CC BY | ChEMBL, HCA releases | Cite + attribution |
| Restricted | TCGA, dbGaP controlled data | DUC/DUA, authorization |
| Embargoed | Some medical datasets | Follow embargo terms |

### Model/Service Restrictions

| Model | Restriction | Notes |
|-------|-------------|-------|
| AlphaFold Server | Non-commercial only | Cannot use for commercial drug discovery without license |
| AlphaFold3 weights | Non-commercial + output restrictions | Read WEIGHTS_TERMS_OF_USE carefully |
| Evo 2 | Research use | Check Arc Institute terms |
| RCSB PDB | CC0 | Very permissive, good for practice |

---

## 🛠️ Quick Reference: Tool → Skill Mapping

| Tool | Primary Skills |
|------|----------------|
| PyTorch | DL basics, model development |
| Biopython | Sequence handling, NCBI queries |
| RDKit | Molecule parsing, fingerprinting, reactions |
| Scanpy | Single-cell analysis workflows |
| AlphaFold | Protein structure prediction |
| DeepChem | Molecule ML, GNN, generative models |
| Nextflow | Pipeline reproducibility |
| Snakemake | Workflow management |
| Docker | Environment reproducibility |
