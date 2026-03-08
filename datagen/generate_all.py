#!/usr/bin/env python
"""
Master runner: generate all CordovaOS demo XML data.

Civil Registry runs first (populates PERSONS), then all other domains.
"""
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


def main():
    print("=" * 60)
    print("CordovaOS Demo Data Generator")
    print("=" * 60)

    # Phase 1: Foundation (must be first — populates PERSONS)
    civil_registry.generate()
    vital_statistics.generate()

    # Phase 2: Institutional
    business_registry.generate()
    property_registry.generate()
    education_record.generate()

    # Phase 3: Economic
    employment_record.generate()
    tax_revenue.generate()

    # Phase 4: Operational
    maritime.generate()
    healthcare.generate()
    law_enforcement.generate()

    print("=" * 60)
    print("All domains generated.")
    print("=" * 60)


if __name__ == "__main__":
    main()
