# 🧬 Awesome AI4Biology

[English](./README.md) | 中文

A curated list of AI tools, models, and resources for biology and life sciences. Covering protein design, genomics, drug discovery, single-cell analysis, and beyond.

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0](https://img.shields.io/badge/License-CC0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

> Artificial intelligence is transforming every corner of biology — from predicting protein structures with atomic accuracy to decoding the regulatory grammar of genomes. This repository aims to be a comprehensive, community-driven collection of AI for Biology skills, tools, models, and platforms across all major sub-fields.

## 📋 Table of Contents

- [Protein Structure Prediction and Design](#protein-structure-prediction-and-design)
- [Protein Language Models](#protein-language-models)
- [Protein Function Prediction and Annotation](#protein-function-prediction-and-annotation)
- [Protein-Protein Interaction Prediction](#protein-protein-interaction-prediction)
- [Antibody Design and Immunology](#antibody-design-and-immunology)
- [Molecular Dynamics and Simulation](#molecular-dynamics-and-simulation)
- [Genomics and Variant Analysis](#genomics-and-variant-analysis)
- [Transcriptomics and Single-Cell Analysis](#transcriptomics-and-single-cell-analysis)
- [Epigenetics](#epigenetics)
- [RNA Structure and Function Prediction](#rna-structure-and-function-prediction)
- [CRISPR and Gene Editing](#crispr-and-gene-editing)
- [Multi-Omics Integration](#multi-omics-integration)
- [Drug Discovery and Molecular Generation](#drug-discovery-and-molecular-generation)
- [Biomedical NLP](#biomedical-nlp)
- [Biological Image Analysis](#biological-image-analysis)
- [Synthetic Biology](#synthetic-biology)
- [Metabolomics and Systems Biology](#metabolomics-and-systems-biology)
- [Evolution and Phylogenetics](#evolution-and-phylogenetics)
- [Emerging Directions](#emerging-directions)

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
| ProtGPT2 | An autoregressive transformer model trained on the entire protein sequence space, capable of generating de novo protein sequences following natural principles. | [HuggingFace](https://huggingface.co/nateraw/protgpt2) | Nature Communications (2022) |
| Ankh | An optimized protein language model focusing on general-purpose protein modeling with high efficiency. | [GitHub](https://github.com/calico/anKh) | arXiv (2023) |
| xTrimoPGLM | A unified 100B-scale pre-trained transformer designed to decipher the language of proteins, supporting both representation and generation tasks. | [GitHub](https://github.com/gaoeason/xTrimoPGLM) | arXiv (2024) |

---

## 🎯 Protein Function Prediction and Annotation

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| DeepFRI | A Graph Convolutional Network (GCN) method for predicting protein functions (GO terms) by integrating sequence and structural information. | [GitHub](https://github.com/flat逆/DeepFRI) | Nature Communications (2021) |
| DeepGOPlus | Combines deep CNNs with sequence similarity-based predictions to provide accurate Gene Ontology (GO) annotations. | [GitHub](https://github.com/bio-ontology-research-group/deepgoplus) | Bioinformatics (2020) |
| NetGO | A web server for high-accuracy protein function prediction that integrates multiple network-based and sequence-based features. | [Website](http://cadd.gsu.edu.tw/NetGO) | Nucleic Acids Research (2019) |
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
| CADD | Combined Annotation Dependent Depletion — uses machine learning to integrate multiple annotations for scoring the deleteriousness of human genetic variants. | [Website](https://cadd.gs.washington.edu) | Nature Genetics (2014) |
| Sei | A deep learning framework predicting the effects of sequence alterations on 21,907 genomic features and classifying them into regulatory sequence categories. | [GitHub](https://github.com/FunctionFuture/sei) | Nature Genetics (2022) |
| Clair3 | A variant calling tool optimized for long-read sequencing (e.g., Oxford Nanopore), combining neural networks and ensemble learning. | [GitHub](https://github.com/HKU-BAL/Clair3) | Nature Communications (2022) |
| AlphaGenome | A unified DNA sequence model (2025) that predicts thousands of functional genomic features from 1Mb input sequences. | [Website](https://google.com/alphagenome) | Nature (2025) |
| popEVE | An AI model (2025) for predicting the disease-causing potential of rare variants in patient genomes. | [Website](https://popeve.org) | Nature Genetics (2025) |

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
| DeepSEA | A deep learning sequence model that directly predicts chromatin features (TF binding, histone modifications) from DNA sequences. | [Website](http://deepsea.princeton.edu) | Nature Methods (2015) |
| ChromHMM | An HMM-based tool for automatically learning and characterizing chromatin states from multiple histone modification datasets. | [Website](https://egg2.russelllab.org) | Nature Methods (2012) |
| DeepCpG | Uses deep neural networks to predict single-cell DNA methylation states, integrating local sequence and neighboring methylation information. | [GitHub](https://github.com/PMBio/deepcpg) | Genome Biology (2017) |
| Basenji | A deep CNN for predicting genome-wide DNA regulatory activity (DNase-seq, ChIP-seq signals). | [GitHub](https://github.com/calico/basenji) | Genome Research (2018) |
| EpiMap | Integrates thousands of epigenomic maps and uses deep learning to predict enhancer activity across tissues and cell types. | [Website](https://www.biolincc.org/epimap) | Nature (2021) |
| DeepChrome | Uses CNN to predict gene expression levels from histone modification features in promoter regions. | [GitHub](https://github.com/QQ517/DeePromo) | Bioinformatics (2016) |

---

## 📜 RNA Structure and Function Prediction

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| SPOT-RNA | Uses ensemble deep learning and transfer learning to predict RNA secondary structures, significantly improving non-canonical base pair prediction. | [GitHub](https://github.com/cyanobacterium/SPOT-RNA) | Nature Communications (2019) |
| EternaFold | An RNA secondary structure prediction model trained through multi-task learning and crowdsourced data (Eterna game) with strong generalization. | [GitHub](https://github.com/eternagame/EternaFold) | PLOS Computational Biology (2020) |
| RNAfold | A classic RNA secondary structure prediction tool (part of ViennaRNA), based on thermodynamic models and commonly used as a benchmark for AI models. | [Website](https://www.tbi.univie.ac.at/RNA) | Algorithms for Molecular Biology (2011) |
| E2Efold | An end-to-end deep learning model that directly predicts RNA secondary structures from sequences without relying on traditional thermodynamic parameters. | [GitHub](https://github.com/MLforBio/ECOFOLD) | ICLR (2020) |
| MXfold2 | Combines deep learning with thermodynamic constraints for RNA secondary structure prediction through a differentiable learning framework. | [GitHub](https://github.com/mxfold/mxfold2) | Bioinformatics (2020) |
| BigRNA | A foundation model by Deep Genomics that predicts multiple RNA regulatory processes including splicing, translation, and degradation. | [Website](https://www.deepgenomics.com) | bioRxiv (2024) |

---

## ✂️ CRISPR and Gene Editing

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| DeepCRISPR | A unified deep learning framework for predicting CRISPR/Cas9 off-target effects and on-target efficiency. | [GitHub](https://github.com/biodatalab/deepcrispr) | Genome Biology (2018) |
| CRISPR-Net | Uses RNN and CNN to predict CRISPR/Cas9 off-target activity, performing well on imbalanced datasets. | [GitHub](https://github.com/crisprnet/crisprnet) | Bioinformatics (2020) |
| DeepHF | A deep learning model optimized for high-fidelity Cas9 variants, predicting sgRNA on-target efficiency. | [GitHub](https://github.com/MyronQiu/DeepHF) | Nature Communications (2019) |
| Pythia | An AI tool (2025) that predicts how cells repair their DNA after CRISPR cutting, enabling precise editing. | [Website](https://pythia-biology.com) | Nature Communications (2025) |
| CCTop | A classic CRISPR/Cas on-target and off-target prediction tool, now integrating multiple AI algorithms for improved accuracy. | [Website](https://cctop.cos.uni-heidelberg.de) | PLOS ONE (2015) |
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
| PubMedBERT | A domain-specific language model by Microsoft, fully pre-trained on PubMed full-text and abstracts, achieving SOTA on multiple biomedical NLP tasks. | [HuggingFace](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) | arXiv (2020) |
| BioGPT | A generative pre-trained Transformer by Microsoft for biomedical text generation and mining, supporting QA and summarization tasks. | [GitHub](https://github.com/microsoft/BioGPT) | Briefing in Bioinformatics (2022) |
| GatorTron | A large-scale clinical language model by UF and NVIDIA, trained on massive EHR data to enhance clinical decision support. | [HuggingFace](https://huggingface.co/UFNLP/gatorgrader) | npj Digital Medicine (2022) |
| Med-PaLM / Med-PaLM 2 | Google's medical-specific large model achieving near-expert-level performance on medical exams and clinical QA through instruction fine-tuning. | [Google Research](https://ai.google/research/teams/medalm) | Nature (2023) |
| BioBERT | The first BERT model fine-tuned on large-scale biomedical corpora, widely used for NER and relation extraction. | [GitHub](https://github.com/dmis-lab/biobert) | Bioinformatics (2019) |
| BioMedLM (PubMedGPT) | A 2.7B parameter model by Stanford CRFM and MosaicML, optimized for biomedical literature with balanced performance and inference efficiency. | [HuggingFace](https://huggingface.co/stanford-crnm/pubmedgpt) | Stanford CRFM (2022) |

---

## 🖼️ Biological Image Analysis

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| CellPose | A generalist deep learning-based cell segmentation algorithm that handles various microscopy images with strong generalization. | [GitHub](https://github.com/MouseLand/cellpose) | Nature Methods (2021) |
| StarDist | A deep learning tool for segmenting cell nuclei and other star-convex objects by predicting radial distances. | [GitHub](https://github.com/stardist/stardist) | arXiv (2018) |
| DeepCell | A software library for large-scale biological image analysis, providing deep learning models for cell segmentation, tracking, and lineage analysis. | [GitHub](https://github.com/vanvalenlab/deepcell-tf) | Cell Systems (2016) |
| Segment Anything for Microscopy | Adapts Meta's SAM model to microscopy images, supporting prompt-based (points, boxes) rapid segmentation of complex biological structures. | [GitHub](https://github.com/computational-cell-analytics/dl-for-micro) | Nature Methods (2025) |
| nnU-Net | A self-configuring biomedical image segmentation framework that automatically adapts network architecture and training parameters based on dataset characteristics. | [GitHub](https://github.com/MIC-DKFZ/nnUNet) | Nature Methods (2021) |
| Ilastik | An interactive image classification and segmentation tool combining classical ML and deep learning workflows, suitable for biologists without programming backgrounds. | [Website](https://www.ilastik.org) | Nature Methods (2019) |

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
| MetaboAnalyst | A widely-used metabolomics analysis platform with integrated ML modules for biomarker discovery and pathway analysis. | [Website](https://www.metaboanalyst.ca) | Nucleic Acids Research (2024) |
| PCPFM | A cloud-native metabolomics processing framework supporting automated processing and quality control for large-scale datasets. | [GitHub](https://github.com/shuzhao/PCPFM) | Nucleic Acids Research (2024) |
| COBRApy | A core Python library for constraint-based metabolic network modeling in systems biology, supporting FBA and other analysis algorithms. | [GitHub](https://github.com/opencobra/cobrapy) | BMC Systems Biology (2013) |

---

## 🌳 Evolution and Phylogenetics

| Name | Description | Link | Paper |
|------|-------------|------|-------|
| Fusang | A deep learning-based phylogenetic tree inference framework achieving performance comparable to maximum likelihood methods with higher computational efficiency. | [Website](https://www.fusang.bio) | Nucleic Acids Research (2023) |
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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

---

## 📄 License

This list is released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

---

<p align="center">
  <strong>⭐ If you find this repository useful, please consider giving it a star! ⭐</strong>
</p>
