# 🧬 Awesome AI4Biology

[English](./README.md) | 中文

A curated list of AI tools, models, and resources for biology and life sciences. Covering protein design, genomics, drug discovery, single-cell analysis, and beyond.

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0](https://img.shields.io/badge/License-CC0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Artificial intelligence is transforming every corner of biology — from predicting protein structures with atomic accuracy to decoding the regulatory grammar of genomes. This repository aims to be a comprehensive, community-driven collection of AI for Biology skills, tools, models, and platforms across all major sub-fields.

## 📋 Table of Contents

- [Protein Structure Prediction and Design](#protein-structure-prediction)
- [Protein Language Models](#protein-language-models)
- [Protein Function Prediction and Annotation](#protein-function-prediction)
- [Protein-Protein Interaction Prediction](#protein-protein-interaction)
- [Antibody Design and Immunology](#antibody-design)
- [Molecular Dynamics and Simulation](#molecular-dynamics)
- [Genomics and Variant Analysis](#genomics)
- [Transcriptomics and Single-Cell Analysis](#single-cell)
- [Epigenetics](#epigenetics)
- [RNA Structure and Function Prediction](#rna)
- [CRISPR and Gene Editing](#crispr)
- [Multi-Omics Integration](#multi-omics)
- [Drug Discovery and Molecular Generation](#drug-discovery)
- [Biomedical NLP](#biomedical-nlp)
- [Biological Image Analysis](#bio-image)
- [Synthetic Biology](#synthetic-biology)
- [Metabolomics and Systems Biology](#metabolomics)
- [Evolution and Phylogenetics](#evolution)
- [Emerging Directions](#emerging)
- [AI Biology Agents & Frameworks](#ai-agents)
- [Benchmarks & Datasets](#benchmarks)
- [Skill Libraries & Frameworks](#skill-libraries)
- [Foundation Models Overview](#foundation-models-overview)
- [Spatial Transcriptomics](#spatial-transcriptomics)
- [Cell Biology & Virtual Cell](#virtual-cell)
- [Ecology & Metagenomics](#ecology-metagenomics)
- [Genome Annotation & Evolution](#genome-annotation)
- [Clinical & Biomedical AI](#clinical-biomedical-ai)
- [Supporting Tools & Databases](#databases-apis)

---

## 🧬 Protein Structure Prediction and Design

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| AlphaFold (v2/v3) | A revolutionary AI system by Google DeepMind that predicts a protein's 3D structure from its amino acid sequence with near-experimental accuracy. | [GitHub](https://github.com/deepmind/alphafold) | Nature (2021) |
| RoseTTAFold / RoseTTAFold-All-Atom | A deep learning tool that rapidly and accurately predicts protein structures and their interactions with other molecules (DNA, RNA, small molecules). | [GitHub](https://github.com/RosettaCommons/RoseTTAFold) | Science (2021) |
| ESMFold | A fast protein structure prediction model from Meta AI that uses large-scale protein language models (ESM-2) to predict structures directly from sequences without MSAs. | [GitHub](https://github.com/facebookresearch/esm) | Science (2023) |
| RFdiffusion | A generative diffusion model for de novo protein design, capable of creating novel protein backbones for a wide range of functional challenges. | [GitHub](https://github.com/RosettaCommons/RFdiffusion) | Nature (2023) |
| ProteinMPNN | A robust deep learning tool for protein sequence design (inverse folding) that generates sequences folding into a given target backbone structure. | [GitHub](https://github.com/davehtp/proteinmpnn) | Science (2022) |
| Chroma | A programmable generative model for protein structures and complexes, enabling design of proteins with specific geometric and functional properties. | [GitHub](https://github.com/generatebio/chroma) | Nature (2023) |
| FrameFlow | A generative model for protein structure design using SE(3) flow matching on frames, improving the efficiency and quality of de novo protein generation. | [GitHub](https://github.com/frameflow/frameflow) | arXiv (2023) |
| OmegaFold | A high-resolution protein structure prediction tool that does not require MSAs, relying solely on a single primary sequence. | [GitHub](https://github.com/HeliXon/OmegaFold) | bioRxiv (2022) |

---

## 🔤 Protein Language Models

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| ESM (Evolutionary Scale Modeling) | A suite of transformer-based models (ESM-1b, ESM-2) trained on hundreds of millions of protein sequences to capture evolutionary and structural information. | [GitHub](https://github.com/facebookresearch/esm) | PNAS (2021) |
| ProtTrans | A collection of massive protein language models (ProtBERT, ProtT5) trained using various architectures to provide state-of-the-art protein representations. | [GitHub](https://github.com/agemagician/ProtTrans) | IEEE TPAMI (2021) |
| ProGen / ProGen2 | LLMs for protein generation that can be controlled by specifying protein properties or families, enabling the design of functional artificial proteins. | [GitHub](https://github.com/salesforce/ProGen) | Nature Biotechnology (2023) |
| ProtGPT2 | An autoregressive transformer model trained on the entire protein sequence space, capable of generating de novo protein sequences following natural principles. | [Link](https://huggingface.co/nateraw/protgpt2) | Nature Communications (2022) |
| Ankh | An optimized protein language model focusing on general-purpose protein modeling with high efficiency. | [GitHub](https://github.com/calico/anKh) | arXiv (2023) |
| xTrimoPGLM | A unified 100B-scale pre-trained transformer designed to decipher the language of proteins, supporting both representation and generation tasks. | [GitHub](https://github.com/gaoeason/xTrimoPGLM) | arXiv (2024) |

---

## 🎯 Protein Function Prediction and Annotation

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| DeepFRI | A Graph Convolutional Network (GCN) method for predicting protein functions (GO terms) by integrating sequence and structural information. | [GitHub](https://github.com/flat逆/DeepFRI) | Nature Communications (2021) |
| DeepGOPlus | Combines deep CNNs with sequence similarity-based predictions to provide accurate Gene Ontology (GO) annotations. | [GitHub](https://github.com/bio-ontology-research-group/deepgoplus) | Bioinformatics (2020) |
| NetGO | A web server for high-accuracy protein function prediction that integrates multiple network-based and sequence-based features. | [Link](http://cadd.gsu.edu.tw/NetGO) | Nucleic Acids Research (2019) |
| ProteinBERT | A universal deep-learning model for protein sequence and function prediction using a unique architecture to handle very long sequences. | [GitHub](https://github.com/nadavbra/protein_bert) | Bioinformatics (2022) |
| CleanProtein | A framework for protein function prediction that focuses on cleaning and denoising protein data to improve AI-driven annotations. | [GitHub](https://github.com/nannadm/cleanprotein) | arXiv (2022) |

---

## 🔗 Protein-Protein Interaction Prediction

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| AlphaFold-Multimer | An extension of AlphaFold v2 specifically trained to predict the 3D structures of multi-chain protein complexes. | [GitHub](https://github.com/deepmind/alphafold) | bioRxiv (2021) |
| RoseTTAFold2-PPI | A fast and accurate deep learning method for large-scale protein-protein interaction screening and complex structure prediction. | [GitHub](https://github.com/RosettaCommons/RoseTTAFold) | bioRxiv (2023) |
| MaSIF | A geometric deep learning framework to learn representations of protein surfaces, used for predicting PPI sites and docking. | [GitHub](https://github.com/LPDI-EPFL/masif) | Nature Methods (2019) |
| PIPR | A deep learning framework using a Siamese residual RCNN architecture to predict PPIs from protein sequences alone. | [GitHub](https://github.com/ziyuang/PIPR) | Bioinformatics (2019) |
| D-PPI | A deep learning model for predicting protein-protein interactions by leveraging evolutionary information and deep neural networks. | [GitHub](https://github.com/xiuyiyang/D-PPI) | IEEE (2018) |

---

## 💉 Antibody Design and Immunology

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| IgFold | A fast and accurate antibody structure prediction tool using a pre-trained language model to predict structures from sequences in seconds. | [GitHub](https://github.com/m到手酸/IgFold) | Nature Communications (2023) |
| DiffAb | A diffusion-based generative model for antigen-specific antibody design, generating both sequences and structures of CDRs. | [GitHub](https://github.com/Accuranker/DiffAb) | NeurIPS (2022) |
| AntiFold | A tool for antibody structure-based sequence design, predicting sequences that fit into given antibody variable domain structures. | [GitHub](https://github.com/RefAb/AntiFold) | bioRxiv (2023) |
| AbDesign | A computational framework for the de novo design of antibody variable domains, integrating Rosetta-based energy functions and AI. | [GitHub](https://github.com/RosettaCommons/AbDesign) | Nature Chemical Biology (2016) |
| DeepAb | A deep learning method for predicting antibody Fv structures, utilizing a recurrent neural network with attention mechanisms. | [GitHub](https://github.com/rosettatype/DeepAb) | Patterns (2022) |

---

## ⚛️ Molecular Dynamics and Simulation

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| DeePMD-kit | A deep learning package for many-body potential energy representation and molecular dynamics, achieving ab initio accuracy with empirical potential efficiency. | [GitHub](https://github.com/deepmodeling/deepmd-kit) | Computer Physics Communications (2018) |
| SchNet / SchNetPack | A continuous-filter convolutional neural network designed to model quantum-mechanical properties of molecules and materials. | [GitHub](https://github.com/atomistic-machine-learning/schnet) | NeurIPS (2017) |
| TorchMD | A framework for molecular simulations using PyTorch, enabling the integration of machine learning potentials and differentiable simulations. | [GitHub](https://github.com/torchmd/torchmd) | JCTC (2021) |
| NeuralMD | A tool for performing molecular dynamics simulations with neural network potentials, focusing on high-performance and scalability. | [GitHub](https://github.com/masironbed/NeuralMD) | arXiv (2020) |
| GNN-MD | Using Graph Neural Networks to accelerate molecular dynamics simulations by predicting forces and energies directly from molecular graphs. | [GitHub](https://github.com/gnnmd/gnn-md) | arXiv (2022) |
| MACE | A fast and accurate machine learning force field based on the Atomic Cluster Expansion (ACE) and equivariant message passing. | [GitHub](https://github.com/ACEsuit/mace) | NeurIPS (2022) |

---

## 🧬 Genomics and Variant Analysis

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| DeepVariant | Uses deep CNNs to call genetic variants from NGS data, greatly improving variant detection accuracy. | [GitHub](https://github.com/google/deepvariant) | Nature Biotechnology (2018) |
| SpliceAI | A deep learning tool by Illumina that predicts splice sites from DNA sequences, identifying cryptic splicing variants causing diseases. | [GitHub](https://github.com/Illumina/SpliceAI) | Cell (2019) |
| Enformer | A Transformer-based architecture that predicts gene expression and chromatin states using long-range genomic interactions up to 100kb. | [GitHub](https://github.com/Interverse/Enformer) | Nature (2021) |
| CADD | Combined Annotation Dependent Depletion — uses machine learning to integrate multiple annotations for scoring the deleteriousness of human genetic variants. | [Link](https://cadd.gs.washington.edu) | Nature Genetics (2014) |
| Sei | A deep learning framework predicting the effects of sequence alterations on 21,907 genomic features and classifying them into regulatory sequence categories. | [GitHub](https://github.com/FunctionFuture/sei) | Nature Genetics (2022) |
| Clair3 | A variant calling tool optimized for long-read sequencing (e.g., Oxford Nanopore), combining neural networks and ensemble learning. | [GitHub](https://github.com/HKU-BAL/Clair3) | Nature Communications (2022) |
| AlphaGenome | A unified DNA sequence model (2025) that predicts thousands of functional genomic features from 1Mb input sequences. | [Link](https://google.com/alphagenome) | Nature (2025) |
| popEVE | An AI model (2025) for predicting the disease-causing potential of rare variants in patient genomes. | [Link](https://popeve.org) | Nature Genetics (2025) |

---

## 🔬 Transcriptomics and Single-Cell Analysis

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| scGPT | A Transformer-based single-cell foundation model pre-trained on millions of cells, applicable to cell type annotation, batch correction, and gene network inference. | [GitHub](https://github.com/bowang-lab/scGPT) | Nature Methods (2024) |
| Geneformer | A context-aware attention model pre-trained on large-scale single-cell transcriptomic data, excelling at predicting gene network perturbation effects. | [GitHub](https://github.com/CompCy-lab/Geneformer) | Nature (2023) |
| scVI | A VAE-based probabilistic framework for single-cell RNA-seq dimensionality reduction, clustering, and differential expression analysis. | [GitHub](https://github.com/YosefLab/scVI-tools) | Nature Methods (2018) |
| CellTypist | An automated cell type annotation tool based on logistic regression and massive reference datasets, suitable for cross-tissue and cross-species single-cell data. | [GitHub](https://github.com/ijuric-app/CellTypist) | Science (2022) |
| scBERT | Uses BERT architecture for single-cell cell type prediction, capturing gene-gene interactions through pre-training. | [GitHub](https://github.com/bids-lab/scBERT) | Nature Machine Intelligence (2022) |
| scFoundation | A 100M-parameter large-scale single-cell foundation model supporting cell embedding, gene expression prediction, and drug response prediction. | [GitHub](https://github.com/MyronQiu/scFoundation) | Nature Methods (2024) |
| scPRINT | A model (2025) pre-trained on over 50 million cells, capable of robust gene network inference. | [GitHub](https://github.com/cerebrate-lab/scPRINT) | Nature Communications (2025) |

---

## 🧪 Epigenetics

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| DeepSEA | A deep learning sequence model that directly predicts chromatin features (TF binding, histone modifications) from DNA sequences. | [Link](http://deepsea.princeton.edu) | Nature Methods (2015) |
| ChromHMM | An HMM-based tool for automatically learning and characterizing chromatin states from multiple histone modification datasets. | [Link](https://egg2.russelllab.org) | Nature Methods (2012) |
| DeepCpG | Uses deep neural networks to predict single-cell DNA methylation states, integrating local sequence and neighboring methylation information. | [GitHub](https://github.com/PMBio/deepcpg) | Genome Biology (2017) |
| Basenji | A deep CNN for predicting genome-wide DNA regulatory activity (DNase-seq, ChIP-seq signals). | [GitHub](https://github.com/calico/basenji) | Genome Research (2018) |
| EpiMap | Integrates thousands of epigenomic maps and uses deep learning to predict enhancer activity across tissues and cell types. | [Link](https://www.biolincc.org/epimap) | Nature (2021) |
| DeepChrome | Uses CNN to predict gene expression levels from histone modification features in promoter regions. | [GitHub](https://github.com/QQ517/DeePromo) | Bioinformatics (2016) |

---

## 📜 RNA Structure and Function Prediction

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| SPOT-RNA | Uses ensemble deep learning and transfer learning to predict RNA secondary structures, significantly improving non-canonical base pair prediction. | [GitHub](https://github.com/cyanobacterium/SPOT-RNA) | Nature Communications (2019) |
| EternaFold | An RNA secondary structure prediction model trained through multi-task learning and crowdsourced data (Eterna game) with strong generalization. | [GitHub](https://github.com/eternagame/EternaFold) | PLOS Computational Biology (2020) |
| RNAfold | A classic RNA secondary structure prediction tool (part of ViennaRNA), based on thermodynamic models and commonly used as a benchmark for AI models. | [Link](https://www.tbi.univie.ac.at/RNA) | Algorithms for Molecular Biology (2011) |
| E2Efold | An end-to-end deep learning model that directly predicts RNA secondary structures from sequences without relying on traditional thermodynamic parameters. | [GitHub](https://github.com/MLforBio/ECOFOLD) | ICLR (2020) |
| MXfold2 | Combines deep learning with thermodynamic constraints for RNA secondary structure prediction through a differentiable learning framework. | [GitHub](https://github.com/mxfold/mxfold2) | Bioinformatics (2020) |
| BigRNA | A foundation model by Deep Genomics that predicts multiple RNA regulatory processes including splicing, translation, and degradation. | [Link](https://www.deepgenomics.com) | bioRxiv (2024) |

---

## ✂️ CRISPR and Gene Editing

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| DeepCRISPR | A unified deep learning framework for predicting CRISPR/Cas9 off-target effects and on-target efficiency. | [GitHub](https://github.com/biodatalab/deepcrispr) | Genome Biology (2018) |
| CRISPR-Net | Uses RNN and CNN to predict CRISPR/Cas9 off-target activity, performing well on imbalanced datasets. | [GitHub](https://github.com/crisprnet/crisprnet) | Bioinformatics (2020) |
| DeepHF | A deep learning model optimized for high-fidelity Cas9 variants, predicting sgRNA on-target efficiency. | [GitHub](https://github.com/MyronQiu/DeepHF) | Nature Communications (2019) |
| Pythia | An AI tool (2025) that predicts how cells repair their DNA after CRISPR cutting, enabling precise editing. | [Link](https://pythia-biology.com) | Nature Communications (2025) |
| CCTop | A classic CRISPR/Cas on-target and off-target prediction tool, now integrating multiple AI algorithms for improved accuracy. | [Link](https://cctop.cos.uni-heidelberg.de) | PLOS ONE (2015) |
| BE-Hive | A machine learning model specifically designed for base editing, predicting editing product distributions and efficiency. | [GitHub](https://github.com/natab/BE-Hive) | Nature (2020) |

---

## 🔀 Multi-Omics Integration

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| MOFA+ | Multi-Omics Factor Analysis — an unsupervised framework for integrating different omics data from the same set of samples. | [GitHub](https://github.com/bioFAM/MOFA) | Genome Biology (2020) |
| MultiVI | Part of the scvi-tools framework, for joint analysis of single-cell RNA-seq and ATAC-seq data, supporting both paired and unpaired data. | [GitHub](https://github.com/YosefLab/scvi-tools) | Nature Methods (2023) |
| MultiVelo | Combines single-cell transcriptomics and chromatin accessibility data to infer gene regulatory dynamics. | [GitHub](https://github.com/bioFAM/MultiVelo) | Nature Communications (2022) |
| Flexynesis | A deep learning toolkit (2025) for bulk multi-omics data integration, advancing precision oncology research. | [GitHub](https://github.com/rsinghlab/Flexynesis) | Nature Communications (2025) |
| scJoint | Uses transfer learning and neural networks to integrate heterogeneous single-cell multi-omics data, transferring labels across modalities. | [GitHub](https://github.com/bendeng-b略/sCJoint) | Nature Computational Science (2022) |
| MOGONET | A GCN-based multi-omics integration method for classification and biomarker discovery, capturing complex inter-omics relationships. | [GitHub](https://github.com/txWang/MOGONET) | Nature Communications (2021) |

---

## 💊 Drug Discovery and Molecular Generation

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| MolBERT | A BERT-based molecular representation learning model pre-trained on large-scale chemical libraries for property prediction and drug screening. | [GitHub](https://github.com/bp-kelley/molbert) | JCIM (2020) |
| MegaMolBART | A large-scale generative model by NVIDIA using Transformer architecture on SMILES strings for molecular generation, optimization, and property prediction. | [GitHub](https://github.com/NVIDIA/MegaMolBART) | JCIM (2022) |
| DrugGPT | A GPT-based strategy for designing potential ligands targeting specific proteins by learning protein-ligand interactions. | [GitHub](https://github.com/BenevolentAI/DrugGPT) | bioRxiv (2023) |
| DiffDock | A diffusion model-based molecular docking tool that predicts 3D binding structures of small molecule ligands with protein receptors. | [GitHub](https://github.com/gabib/biobombe) | arXiv (2023) |
| TankBind | A deep learning model for protein-ligand binding affinity prediction and binding site identification, handling multiple potential binding pockets. | [GitHub](https://github.com/DeepGraphLearning/TankBind) | bioRxiv (2022) |
| REINVENT | A reinforcement learning framework for de novo drug design, automatically optimizing molecules with specific bioactivity through generative models and scoring functions. | [GitHub](https://github.com/MolecularAI/ReInvent) | Journal of Cheminformatics (2024) |
| MolGPT | A GPT-based molecular generation model that learns the probability distribution of SMILES strings to generate chemically valid novel molecules. | [GitHub](https://github.com/s snappedbad/MolGPT) | JCIM (2022) |

---

## 📚 Biomedical NLP

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| PubMedBERT | A domain-specific language model by Microsoft, fully pre-trained on PubMed full-text and abstracts, achieving SOTA on multiple biomedical NLP tasks. | [Link](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) | arXiv (2020) |
| BioGPT | A generative pre-trained Transformer by Microsoft for biomedical text generation and mining, supporting QA and summarization tasks. | [GitHub](https://github.com/microsoft/BioGPT) | Briefing in Bioinformatics (2022) |
| GatorTron | A large-scale clinical language model by UF and NVIDIA, trained on massive EHR data to enhance clinical decision support. | [Link](https://huggingface.co/UFNLP/gatorgrader) | npj Digital Medicine (2022) |
| Med-PaLM / Med-PaLM 2 | Google's medical-specific large model achieving near-expert-level performance on medical exams and clinical QA through instruction fine-tuning. | [Link](https://ai.google/research/teams/medalm) | Nature (2023) |
| BioBERT | The first BERT model fine-tuned on large-scale biomedical corpora, widely used for NER and relation extraction. | [GitHub](https://github.com/dmis-lab/biobert) | Bioinformatics (2019) |
| BioMedLM (PubMedGPT) | A 2.7B parameter model by Stanford CRFM and MosaicML, optimized for biomedical literature with balanced performance and inference efficiency. | [Link](https://huggingface.co/stanford-crnm/pubmedgpt) | Stanford CRFM (2022) |

---

## 🖼️ Biological Image Analysis

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| CellPose | A generalist deep learning-based cell segmentation algorithm that handles various microscopy images with strong generalization. | [GitHub](https://github.com/MouseLand/cellpose) | Nature Methods (2021) |
| StarDist | A deep learning tool for segmenting cell nuclei and other star-convex objects by predicting radial distances. | [GitHub](https://github.com/stardist/stardist) | arXiv (2018) |
| DeepCell | A software library for large-scale biological image analysis, providing deep learning models for cell segmentation, tracking, and lineage analysis. | [GitHub](https://github.com/vanvalenlab/deepcell-tf) | Cell Systems (2016) |
| Segment Anything for Microscopy | Adapts Meta's SAM model to microscopy images, supporting prompt-based (points, boxes) rapid segmentation of complex biological structures. | [GitHub](https://github.com/computational-cell-analytics/dl-for-micro) | Nature Methods (2025) |
| nnU-Net | A self-configuring biomedical image segmentation framework that automatically adapts network architecture and training parameters based on dataset characteristics. | [GitHub](https://github.com/MIC-DKFZ/nnUNet) | Nature Methods (2021) |
| Ilastik | An interactive image classification and segmentation tool combining classical ML and deep learning workflows, suitable for biologists without programming backgrounds. | [Link](https://www.ilastik.org) | Nature Methods (2019) |

---

## 🧬 Synthetic Biology

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| ProteinMPNN | A powerful protein sequence design tool (inverse folding) that predicts optimal amino acid sequences for given backbone structures. | [GitHub](https://github.com/davehtp/proteinmpnn) | Science (2022) |
| RFdiffusion | A diffusion model-based protein backbone design tool for de novo design of novel protein structures with specific functions or binding properties. | [GitHub](https://github.com/RosettaCommons/RFdiffusion) | Nature (2023) |
| ART | Automated Recommendation Tool — uses ML and probabilistic modeling to guide synthetic biology experiment design, optimizing metabolic pathways and gene expression. | [GitHub](https://github.com/Isomorphic-Bio/ART) | Nature Communications (2020) |
| ESM-2 / ESMFold | Meta's protein language model that predicts protein structure and function from sequence alone, greatly accelerating component design in synthetic biology. | [GitHub](https://github.com/facebookresearch/esm) | Science (2023) |
| PromoterCAD | An AI tool for synthetic promoter design, using deep learning to predict and optimize gene expression regulatory sequences. | [GitHub](https://github.com/anAnac/PromoterCAD) | bioRxiv (2021) |

---

## 🔄 Metabolomics and Systems Biology

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| Asari | A high-performance LC-MS metabolomics data processing tool providing more accurate peak detection and annotation. | [GitHub](https://github.com/MesnageClaire/ASARI) | Nature Communications (2023) |
| DeepMetabolism | Combines deep learning with metabolic network constraints for predicting cellular phenotypes and metabolic fluxes. | [GitHub](https://github.com/LoLab-MRU/DeepMetabolism) | bioRxiv (2018) |
| MetaboAnalyst | A widely-used metabolomics analysis platform with integrated ML modules for biomarker discovery and pathway analysis. | [Link](https://www.metaboanalyst.ca) | Nucleic Acids Research (2024) |
| PCPFM | A cloud-native metabolomics processing framework supporting automated processing and quality control for large-scale datasets. | [GitHub](https://github.com/shuzhao/PCPFM) | Nucleic Acids Research (2024) |
| COBRApy | A core Python library for constraint-based metabolic network modeling in systems biology, supporting FBA and other analysis algorithms. | [GitHub](https://github.com/opencobra/cobrapy) | BMC Systems Biology (2013) |

---

## 🌳 Evolution and Phylogenetics

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| Fusang | A deep learning-based phylogenetic tree inference framework achieving performance comparable to maximum likelihood methods with higher computational efficiency. | [Link](https://www.fusang.bio) | Nucleic Acids Research (2023) |
| MyESL | A software tool for evolutionary sparse learning in molecular phylogenetics and genomics. | [GitHub](https://github.com/rocscience/myESL) | bioRxiv (2024) |
| Phyloformer | Uses Transformer architecture for phylogenetic tree prediction by learning evolutionary relationships between sequences. | [GitHub](https://github.com/genbio/phyloformer) | arXiv (2023) |
| DeepEvolve | A deep learning framework for simulating and inferring evolutionary dynamics, identifying natural selection signals and population history. | [GitHub](https://github.com/dnaer/deepevolve) | Evolution Letters (2026) |
| PyPop7 | A pure-Python library of population-based randomized optimization algorithms, commonly used in evolutionary computation and complex biological parameter optimization. | [GitHub](https://github.com/pypop7/pypop7) | arXiv (2023) |

---

## 🚀 Emerging Directions

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| Edge AI for Conservation | Leverages edge computing and AI for wildlife monitoring and ecosystem science, supporting real-time analysis on field devices. | [GitHub](https://github.com/ai-conservation) | Trends in Ecology & Evolution (2025) |
| Awesome Neuro-AI | A curated resource list at the intersection of deep learning and neuroscience, covering brain modeling, neural decoding, and more. | [GitHub](https://github.com/ebony buckle/awesome-neuro-AI) | Neuron (2023) |
| AI in Agriculture | A survey and toolset of deep learning techniques for crops, fisheries, and livestock, aiming to improve agricultural productivity and sustainability. | [GitHub](https://github.com/zzh2000122/awesome-AI-agriculture) | Computers and Electronics in Agriculture (2025) |
| AI-Assisted Bio-Curation | Uses AI to extract, structure, and standardize morphological trait data from published literature, advancing biodiversity research. | [GitHub](https://github.com/biocuration/bioai) | bioRxiv (2025) |
| Awesome Green AI | Focuses on AI applications in environmental impact assessment and carbon footprint reduction, particularly modeling biological system responses to climate change. | [GitHub](https://github.com/kstanescu/awesome-green-ai) | Communications of the ACM (2020) |

---

## 🤖 AI Biology Agents & Frameworks

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| Robin | FutureHouse's end-to-end scientific discovery agent — first AI-generated drug discovery identifying ripasudil as novel dry AMD therapeutic (2025). | [Link](https://futurehouse.ai) | Nature (2025) |
| Aviary | Language agent gymnasium for DNA manipulation, literature search, and protein engineering tasks. | [GitHub](https://github.com/evanyl/aviary) | arXiv (2024) |
| Curie | Automated and rigorous experiment agent for scientific discovery. | [Link](https://curie.ai) | arXiv (2024) |
| ChemCrow | LLM agent augmented with chemistry tools for autonomous research (NeurIPS 2023). | [GitHub](https://github.com/urakagi/ChemCrow) | NeurIPS (2023) |
| POPPER | Automated hypothesis testing with agentic sequential falsifications. | [GitHub](https://github.com/popper-ml/popper) | arXiv (2024) |
| autoresearch | Andrej Karpathy's autonomous LLM research framework — overnight experiments with auto code editing. | [GitHub](https://github.com/autoresearch/autora) | GitHub (2024) |
| GeneClaw | Enterprise AI agent for genome annotation and biopharmaceutical R&D. | [Link](https://geneclaw.ai) | Website (2024) |
| OpenClaw / Hermes | Open-source AI agent framework with Skills ecosystem; WeChat/Feishu integrations. | [Link](https://openclaw.ai) | GitHub (2024) |

---

## 📊 Benchmarks & Datasets

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| ProteinGym | Large-scale benchmarks for protein design and fitness prediction. | [Link](https://protein.ai/proteingym) | Nature Biotechnology (2023) |
| TAPE | Tasks Assessing Protein Embeddings — evaluating protein transfer learning across five tasks. | [GitHub](https://github.com/songlab-gem/TAPE) | Science (2019) |
| BioProBench | Evaluation of LLMs on biological protocols and procedural understanding. | [GitHub](https://github.com/biotender/bioprobench) | arXiv (2024) |
| MedAgentGym | Scalable agentic training environment for code-centric medical reasoning. | [GitHub](https://github.com/medagent/medagentgym) | arXiv (2024) |
| Tahoe-100M | Giga-scale single-cell perturbation atlas for context-dependent gene function (2025). | [Link](https://tahoe.allen.ai) | Nature (2025) |
| Tahoe-x1 | Scaling perturbation-trained single-cell foundation models to 3B parameters. | [Link](https://tahoe.allen.ai) | Nature (2025) |
| OpenBioMed | Benchmark for multi-modal biomedical AI (molecule + text + protein). | [GitHub](https://github.com/bytedance/openbiomed) | KDD (2023) |
| BioSimulations | Repository and API for computational models of biological systems. | [Link](https://biosimulations.org) | Nucleic Acids Research (2021) |

---

## 📚 Skill Libraries & Frameworks

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| OpenClaw Medical Skills | 200+ production-ready SKILL.md files across biology, pharmacology, medicine, omics, and literature search. Largest open-source bio AI skill library. | [Link](https://openclaw.ai/skills) | GitHub (2024) |
| K-Dense | 136 ready-to-use skills covering cancer genomics, drug-target binding, molecular dynamics, RNA velocity, 78+ scientific databases. | [GitHub](https://github.com/K-Dense/kdense) | GitHub (2024) |
| LabClaw | 211 production-ready SKILL.md files across 7 domains (biology, pharmacology, medicine). Stanford LabOS-compatible. | [GitHub](https://github.com/openclaw/labclaw) | GitHub (2024) |
| Dynamic Skills (OpenSpace) | MCP-based self-evolving Skills plugin for OpenClaw — agents write and store new Skills as they encounter new tasks. | [Link](https://openclaw.ai/openspace) | GitHub (2024) |
| MCP Servers | Model Context Protocol servers for biological data — UniProt, PDB, Ensembl, KEGG, and more. | [Link](https://modelcontextprotocol.ai) | GitHub (2024) |

---

## 🏗️ Foundation Models Overview

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| Evo / Evo 2 | Arc Institute's 40B-parameter genome foundation model trained on 9T nucleotides from all domains of life; 1M bp context (Nature 2026). | [Link](https://evo.ai) | Nature (2026) |
| DNABERT-2 | Efficient foundation model and benchmark for multi-species genome understanding. | [GitHub](https://github.com/facebookresearch/DNABERT_2) | arXiv (2023) |
| LucaOne | Generalized biological foundation model with unified nucleic acid and protein language (Nature MI 2025). | [GitHub](https://github.com/tencentAILab/LucaOne) | Nature Machine Intelligence (2025) |
| GET (Genome Foundation Model) | Foundation model of transcription across human cell types. | [GitHub](https://get-model.github.io) | Nature (2024) |
| ESM-3 | Generalist protein language model for sequence, structure, and function from EvolutionaryScale (2024). | [Link](https://evolutionscale.ai/esm) | Science (2024) |
| Boltz-1 | First fully open-source model achieving AlphaFold3-level accuracy for biomolecular interaction modeling (bioRxiv 2024). | [GitHub](https://github.com/microsoft/Boltz-1) | bioRxiv (2024) |
| Chai-1 | Biomolecular structure prediction model from Chai Discovery. | [Link](https://chai.bio) | bioRxiv (2024) |
| Protenix | Open reproduction of AlphaFold3 from Bytedance for biomolecular structure prediction. | [GitHub](https://github.com/bytedance/protenix) | bioRxiv (2024) |
| Cell2Sentence | Teaching LLMs the language of biology through single-cell transcriptomics (ICML 2024). | [GitHub](https://github.com/YosefLab/Cell2Sentence) | ICML (2024) |
| scMulan | Multitask generative pre-trained language model for single-cell analysis. | [GitHub](https://github.com/txWang/scMulan) | Nature Methods (2024) |
| GeneCompass | Knowledge-informed cross-species foundation model for gene regulatory mechanisms. | [Link](https://genecompass.net) | Nature Computational Science (2024) |
| RNA-FM | RNA foundation model for structure and function prediction. | [GitHub](https://github.com/ML4Bio/RNA-FM) | Nature Communications (2022) |
| Nucleotide Transformer | InstaDeep/EMBL-EBI genome foundation model for DNA sequences. | [Link](https://huggingface.co/InstaDeepAI/nucleotide-transformer) | Nature Methods (2023) |
| BioT5 / BioT5+ | Cross-modal integration of biology and chemistry knowledge. | [GitHub](https://github.com/kangyuan/bioT5) | ICLR (2024) |
| NatureLM | Deciphering the language of nature for scientific discovery. | [Link](https://www.nature.com/naturelm) | Nature (2024) |

---

## 🗺️ Spatial Transcriptomics

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| ChatSpatial | MCP server enabling spatial transcriptomics analysis via natural language; integrates 60+ methods (SpaGCN, Cell2location, LIANA+, CellRank) for Visium/Xenium/MERFISH. | [Link](https://chatspatial.ai) | bioRxiv (2024) |
| SUICA | Super-high dimensional sparse implicit neural representations for spatial transcriptomics (2025). | [GitHub](https://github.com/xliu-ai/SUICA) | Nature Methods (2025) |
| stDiff | Diffusion model for imputing spatial transcriptomics via single-cell data. | [GitHub](https://github.com/biomedia-祁/stDiff) | Nature Methods (2024) |
| SpaGCN | Graph convolutional network for spatial gene expression and tissue structure. | [GitHub](https://github.com/jianhuupenn/SpaGCN) | Nature Methods (2022) |
| Cell2location | Bayesian model for cell type mapping in spatial transcriptomics. | [GitHub](https://github.com/vitrior/cell2location) | Nature Methods (2022) |
| LIANA+ | Cell-cell communication inference from spatial and single-cell data. | [GitHub](https://github.com/saezlab/liana) | bioRxiv (2024) |

---

## 🔮 Cell Biology & Virtual Cell

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| VCWorld | Biological world model for virtual cell simulation (bioRxiv 2025). | [Link](https://vcworld.ai) | bioRxiv (2025) |
| scDiffusion | Conditional generation of high-quality single-cell data using diffusion models. | [GitHub](https://github.com/beduffy/scDiffusion) | Nature Methods (2023) |
| CellPLM | Pre-training of cell language model beyond single cells. | [GitHub](https://github.com/baidu/CellPLM) | NeurIPS (2023) |
| scDiffEq | Drift-diffusion modeling of single-cell dynamics with neural stochastic differential equations. | [GitHub](https://github.com/AnnaKull/scdiffeq) | Nature Computational Science (2024) |
| Cellpose 4 | Cell segmentation and morphometry for microscopy images. | [GitHub](https://github.com/MouseLand/cellpose) | Nature Methods (2024) |
| scDART | Integrating unmatched scRNA-seq and scATAC-seq data via deep learning. | [GitHub](https://github.com/COST-group/scdart) | Nature Methods (2024) |
| SIMBA | Single-cell embedding along with features for multi-modal epigenomics. | [GitHub](https://github.com/parklab/SIMBA) | Nature Methods (2024) |

---

## 🌍 Ecology & Metagenomics

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| Kraken2 / MetaPhlAn | Taxonomic classification and profiling of metagenomic sequences. | [Link](https://ccb.jhu.edu/software/kraken2) | Genome Biology (2019) |
| HUMAnN3 | Functional profiling of metagenomic and metatranscriptomic sequences. | [Link](https://huttenhower.org/humann) | Nature Methods (2020) |
| Qiime2 | Microbiome bioinformatics with a plugin architecture. | [Link](https://qiime2.org) | Nature Methods (2019) |
| MetaStorm | Metagenomic sequence analysis and visualization. | [GitHub](https://github.com/LANL-Bioinformatics/MetaStorm) | Bioinformatics (2016) |
| EviCor | Ecological co-occurrence analysis and correlation networks. | [GitHub](https://github.com/microbiome/evicor) | mSystems (2022) |

---

## 🧬 Genome Annotation & Evolution

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| AUGUSTUS / Braker | Ab initio gene prediction; evidence-based genome annotation. | [Link](https://bioinf.uni-greifswald.de/augustus) | Nucleic Acids Research (2006) |
| Prokka | Rapid prokaryotic genome annotation. | [GitHub](https://github.com/tseemann/prokka) | Bioinformatics (2014) |
| BUSCO | Benchmarking universal single-copy orthologs for genome quality assessment. | [Link](https://busco.ezlab.org) | Briefings in Bioinformatics (2020) |
| OrthoFinder | Phylogenomics and gene family evolution analysis. | [GitHub](https://github.com/davidemms/OrthoFinder) | PLOS Computational Biology (2020) |
| MAKER | Portable and scalable genome annotation pipeline. | [Link](https://www.yandell-lab.org/maker) | Genome Research (2014) |
| Funannotate | Eukaryotic genome annotation pipeline. | [GitHub](https://github.com/nextgenusfs/funannotate) | GitHub (2023) |

---

## 🏥 Clinical & Biomedical AI

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| MedAgents | Multi-disciplinary collaboration framework for zero-shot medical reasoning (ACL 2024). | [GitHub](https://github.com/medagents/medagents) | ACL (2024) |
| H-optimus-0 | Powerful feature extraction from histology images for downstream pathology tasks. | [GitHub](https://github.com/biomedia/h-optimus) | Nature (2024) |
| ClinAgents | Clinical multi-agent system for medical decision support. | [GitHub](https://github.com/xxx/ClinAgents) | arXiv (2024) |
| MedEmbed | Medical embedding model for EHR data integration. | [GitHub](https://github.com/medical-ai/medembed) | Journal of Biomedical Informatics (2024) |

---

## 🗄️ Supporting Tools & Databases

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| UniProt | Protein sequences and function — Direct REST API access for protein search, FASTA retrieval, ID mapping. | [Link](https://rest.uniprot.org) | Nucleic Acids Research (2023) |
| RCSB PDB | 3D protein structures — Search, download coordinates, retrieve metadata for drug discovery. | [Link](https://www.rcsb.org) | Nucleic Acids Research (2023) |
| AlphaFold DB | AI-predicted protein structures (200M+ proteins). | [Link](https://alphafold.ebi.ac.uk) | Nature (2021) |
| STRING | Protein-protein interactions — 59M proteins, 20B interactions, 5000+ species. | [Link](https://string-db.org) | Nucleic Acids Research (2023) |
| KEGG / Reactome | Pathway databases for systems biology. | [Link](https://www.genome.jp/kegg) | Nucleic Acids Research (2023) |
| Open Targets | Systematic identification and prioritisation of targets for drug discovery. | [Link](https://opentargets.org) | Nucleic Acids Research (2024) |
| ChEMBL | Bioactivity data for drug discovery — compounds, targets, activities. | [Link](https://www.ebi.ac.uk/chembl) | Nucleic Acids Research (2024) |
| HMDB | Human metabolome database — 220k+ metabolites. | [Link](https://hmdb.ca) | Nucleic Acids Research (2023) |
| NCBI / Ensembl | Genomic reference databases. | [Link](https://www.ncbi.nlm.nih.gov) | Nucleic Acids Research (2023) |
| BioPython | Primary Python toolkit for molecular biology — NCBI queries, sequence manipulation, file parsing. | [Link](https://biopython.org) | Bioinformatics (2009) |
| Nextflow / Snakemake | Reproducible bioinformatics workflow management. | [Link](https://www.nextflow.io) | Nature Biotechnology (2020) |
| Bioconductor | R-based genomics and statistics ecosystem. | [Link](https://bioconductor.org) | Genome Biology (2015) |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## 📄 License

This list is released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

---

<p align="center">
  <strong>⭐ If you find this repository useful, please consider giving it a star! ⭐</strong>
</p>
