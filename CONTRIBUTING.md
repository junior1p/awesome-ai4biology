# Contributing to Awesome AI4Biology

Thank you for your interest in contributing! This repository follows a **skills-first, curated** approach rather than just collecting links. Please read this guide carefully.

## 📋 Quality Standards

### Source Priority (in order)
1. **Official documentation / official GitHub repository**
2. **Peer-reviewed papers** (prefer Nature/Science/Cell tier)
3. **Authoritative data portals** (UniProt, RCSB PDB, EBI, NCBI)
4. **High-quality tutorials** from maintainers
5. **Community-recommended resources**

❌ **Do not submit**:二手转载、无官方链接、已停止维护的资源

### Required Fields for Every Resource

When adding a resource, you MUST provide:

| Field | Description | Example |
|-------|-------------|---------|
| `category` | Main domain | `Protein`, `Omics`, `Drug discovery` |
| `resource_name` | Official name | `AlphaFold`, `RDKit` |
| `type` | Resource type | `GitHub repo`, `dataset portal`, `paper` |
| `link` | Official URL | `https://github.com/...` |
| `license` | License or terms | `MIT`, `CC0-1.0`, `Non-commercial ToS` |
| `difficulty` | `Beginner`, `Intermediate`, or `Advanced` |
| `notes` | Additional info, restrictions | `Non-commercial use only` |

### ⚠️ Compliance Requirements

**You MUST flag**:
- **Controlled access data**: dbGaP, DUC, TCGA — add note: `Requires dbGaP authorization`
- **Non-commercial restrictions**: AlphaFold Server, AlphaFold3 — add note: `Non-commercial use only`
- **Redistribution prohibited**: PDBbind, some ZINC subsets — add note: `Redistribution prohibited`
- **Custom licenses**: Rosetta, some commercial tools — clarify academic vs commercial

## 🚀 How to Contribute

### Option 1: Add to resources.csv

Edit `resources/registry/resources.csv` and add your resource with all required fields.

### Option 2: Add to a domain file

Edit the relevant file in `resources/by-domain/` or `resources/by-method/`.

### Option 3: Create an Issue

Use the issue template to suggest new categories, tools, or learning paths.

## 🔍 Review Checklist

Before submitting a PR, verify:

- [ ] Link is to official source (not a mirror or third-party copy)
- [ ] License/terms are verified from official page
- [ ] Restrictions are noted in `notes` field
- [ ] Entry follows CSV format exactly
- [ ] No duplicate entries (check by name and link)
- [ ] Content is relevant to AI × Biology

## 📁 File Structure

```
awesome-ai4biology/
├── resources/
│   ├── registry/
│   │   └── resources.csv    # Single source of truth (machine-readable)
│   ├── by-domain/           # Human-readable domain pages
│   └── by-method/          # Human-readable method pages
├── skills/
│   └── skill-matrix.md     # Cross-domain skill framework
├── learning-paths/         # Curated learning journeys
└── scripts/                # Automation (lint, validate, generate)
```

## 💬 Getting Help

- Open an Issue for questions
- Join the discussion at [scverse Discourse](https://discourse.scverse.org/) for single-cell topics
- For general bioinformatics: [Image.sc Forum](https://forum.image.sc/)

## 🙏 Acknowledgements

Contributors are listed in the GitHub commit history. Thank you to all who have contributed!
