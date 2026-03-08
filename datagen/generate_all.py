#!/usr/bin/env python
"""
Master runner: generate all CordovaOS demo XML data.

Civil Registry runs first (populates PERSONS), then all other domains.
Generates ~100K XML instances for a 25,000-resident nation.
"""
import os
import time
import glob

import civil_registry
import vital_statistics
import business_registry
import property_registry
import education_record
import employment_record
import tax_revenue
import maritime
import healthcare
import law_enforcement


def count_xml(directory):
    """Count XML files in a directory."""
    pattern = os.path.join(directory, "*.xml")
    return len(glob.glob(pattern))


def clear_xml(directory):
    """Remove all XML files from a directory."""
    pattern = os.path.join(directory, "*.xml")
    files = glob.glob(pattern)
    for f in files:
        os.remove(f)
    return len(files)


def main():
    t_start = time.time()
    print("=" * 60)
    print("CordovaOS Demo Data Generator — 25,000 Population")
    print("=" * 60)

    base = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data")

    # Clear existing XML files
    print("\nClearing existing XML files...")
    total_cleared = 0
    for subdir in os.listdir(base):
        dirpath = os.path.join(base, subdir)
        if os.path.isdir(dirpath):
            n = clear_xml(dirpath)
            if n:
                total_cleared += n
    print(f"  Removed {total_cleared} existing files.\n")

    phases = [
        ("Phase 1: Foundation", [
            ("Civil Registry", civil_registry),
            ("Vital Statistics", vital_statistics),
        ]),
        ("Phase 2: Institutional", [
            ("Business Registry", business_registry),
            ("Property Registry", property_registry),
            ("Education Record", education_record),
        ]),
        ("Phase 3: Economic", [
            ("Employment Record", employment_record),
            ("Tax & Revenue", tax_revenue),
        ]),
        ("Phase 4: Operational", [
            ("Maritime", maritime),
            ("Healthcare", healthcare),
            ("Law Enforcement", law_enforcement),
        ]),
    ]

    total_records = 0
    for phase_name, generators in phases:
        print(f"\n{'─' * 40}")
        print(f"  {phase_name}")
        print(f"{'─' * 40}")
        t_phase = time.time()
        for gen_name, gen_module in generators:
            t_gen = time.time()
            gen_module.generate()
            elapsed = time.time() - t_gen
            print(f"    ↳ {elapsed:.1f}s")
        phase_elapsed = time.time() - t_phase
        print(f"  Phase total: {phase_elapsed:.1f}s")

    # Count final totals
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    for subdir in sorted(os.listdir(base)):
        dirpath = os.path.join(base, subdir)
        if os.path.isdir(dirpath):
            n = count_xml(dirpath)
            if n:
                total_records += n
                print(f"  {subdir:<30} {n:>8,}")
    print(f"  {'─' * 40}")
    print(f"  {'TOTAL':<30} {total_records:>8,}")

    total_elapsed = time.time() - t_start
    print(f"\nCompleted in {total_elapsed:.1f}s ({total_elapsed/60:.1f} minutes)")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
