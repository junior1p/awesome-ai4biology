#!/usr/bin/env python3
"""
Validate resources.csv for completeness and correctness.
Checks:
- Required fields present
- License field is not empty
- Links are valid URLs
- No duplicate entries
- Difficulty values are valid
"""

import csv
import sys
import re
from pathlib import Path

VALID_TYPES = [
    "official docs", "GitHub repo", "platform", "dataset portal",
    "paper", "model", "framework", "agent", "benchmark",
    "reference", "video", "course", "community hub", "spec/docs"
]
VALID_DIFFICULTIES = ["Beginner", "Intermediate", "Advanced"]
VALID_CATEGORIES = [
    "Foundations", "Omics", "Single-cell", "Protein", "Drug discovery",
    "Imaging", "Synthetic Biology", "AI Agents", "Benchmarks"
]

def validate_link(url):
    """Basic URL validation"""
    if not url:
        return False, "Link is empty"
    pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not pattern.match(url):
        return False, f"Invalid URL format: {url}"
    return True, ""

def lint_registry(csv_path):
    """Main validation function"""
    issues = []
    warnings = []
    seen_entries = set()
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    if not rows:
        issues.append("CSV is empty")
        return issues, warnings
    
    # Check headers
    required = ['category', 'resource_name', 'type', 'link', 'license', 'difficulty']
    missing_headers = [h for h in required if h not in rows[0].keys()]
    if missing_headers:
        issues.append(f"Missing required columns: {missing_headers}")
    
    # Check each row
    for i, row in enumerate(rows, 2):  # +2 for header row and 1-indexing
        entry_key = (row.get('resource_name', ''), row.get('link', ''))
        
        # Duplicate check
        if entry_key[0] and entry_key[1]:
            if entry_key in seen_entries:
                warnings.append(f"Row {i}: Duplicate entry: {entry_key[0]}")
            seen_entries.add(entry_key)
        
        # Required fields
        for field in required:
            if not row.get(field, '').strip():
                issues.append(f"Row {i}: Missing required field '{field}'")
        
        # Type validation
        if row.get('type', '').strip() and row['type'] not in VALID_TYPES:
            warnings.append(f"Row {i}: Unknown type '{row['type']}' - consider adding to schema")
        
        # Difficulty validation
        if row.get('difficulty', '').strip() and row['difficulty'] not in VALID_DIFFICULTIES:
            issues.append(f"Row {i}: Invalid difficulty '{row['difficulty']}' - must be one of {VALID_DIFFICULTIES}")
        
        # Link validation
        link = row.get('link', '').strip()
        if link:
            valid, msg = validate_link(link)
            if not valid:
                issues.append(f"Row {i}: {msg}")
        
        # Compliance warnings for restricted resources
        notes = row.get('notes', '').lower()
        license_val = row.get('license', '').lower()
        if any(x in license_val for x in ['non-commercial', 'proprietary', 'restricted']):
            if 'non-commercial' not in notes and 'restrict' not in notes:
                warnings.append(f"Row {i}: License has restrictions but notes don't mention them")
    
    return issues, warnings

if __name__ == "__main__":
    csv_path = Path(__file__).parent.parent / "resources" / "registry" / "resources.csv"
    
    if len(sys.argv) > 1:
        csv_path = Path(sys.argv[1])
    
    if not csv_path.exists():
        print(f"❌ Error: {csv_path} not found")
        sys.exit(1)
    
    issues, warnings = lint_registry(csv_path)
    
    print(f"📋 Validating: {csv_path}")
    print("-" * 50)
    
    if warnings:
        print(f"⚠️  {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  - {w}")
    
    if issues:
        print(f"❌ {len(issues)} error(s):")
        for i in issues:
            print(f"  - {i}")
        sys.exit(1)
    else:
        print("✅ Validation passed!")
        sys.exit(0)
