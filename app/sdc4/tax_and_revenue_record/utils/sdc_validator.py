"""
SDC Validator wrapper with automatic ExceptionalValue recovery.

This module provides validation for SDC4 XML instances using sdcvalidator,
with automatic recovery of invalid components using ISO 21090 ExceptionalValues.
"""
import logging
from pathlib import Path
from typing import Tuple, List, Optional
from dataclasses import dataclass, field

try:
    from sdcvalidator import SDC4Validator, ExceptionalValueType
    HAS_SDCVALIDATOR = True
except ImportError:
    HAS_SDCVALIDATOR = False

logger = logging.getLogger(__name__)


@dataclass
class ValidationResult:
    """Result of XML validation with optional ExceptionalValue recovery."""
    is_valid: bool
    errors: list = field(default_factory=list)
    recovered_xml: Optional[str] = None
    report: Optional[dict] = None
    auto_corrected_fields: List[str] = field(default_factory=list)


class SDCValidator:
    """
    Wrapper around sdcvalidator.SDC4Validator with convenience methods.

    Validates XML instances against XSD schema and can automatically
    apply ExceptionalValues to invalid components using the SDC4
    quarantine-and-tag pattern.

    ExceptionalValue types use ISO 21090 NULL Flavor codes:
        INV  - Invalid (type violations, pattern mismatches)
        OTH  - Other (value not in coding system)
        NI   - No Information (missing/omitted value)
        NA   - Not Applicable (unexpected content)
        UNC  - Unencoded (encoding/format errors)
        UNK  - Unknown
        ASKU - Asked but Unknown
        ASKR - Asked and Refused
        NASK - Not Asked
        NAV  - Not Available
        MSK  - Masked (privacy/security)
        DER  - Derived
        PINF - Positive Infinity
        NINF - Negative Infinity
        TRC  - Trace
    """

    def __init__(self, xsd_path: str):
        """
        Initialize validator with XSD schema path.

        Args:
            xsd_path: Path to the XSD schema file
        """
        self.xsd_path = xsd_path
        if HAS_SDCVALIDATOR:
            self.validator = SDC4Validator(xsd_path)
        else:
            self.validator = None
            logger.warning(
                "sdcvalidator not installed. Validation will be skipped. "
                "Install with: pip install sdcvalidator==4.0.7"
            )

    def validate(self, xml_content: str) -> ValidationResult:
        """
        Validate XML content against XSD schema.

        Args:
            xml_content: XML string to validate

        Returns:
            ValidationResult with validation status and errors
        """
        if self.validator is None:
            return ValidationResult(is_valid=True)

        try:
            report = self.validator.validate_and_report(xml_content)
            return ValidationResult(
                is_valid=report['valid'],
                errors=report.get('errors', []),
                report=report,
            )
        except Exception as e:
            logger.error("Validation failed: %s", e)
            return ValidationResult(
                is_valid=False,
                errors=[{'reason': str(e), 'xpath': '/', 'exceptional_value_type': 'INV'}],
            )

    def auto_correct_with_evs(
        self,
        xml_content: str,
        errors: list,
    ) -> Tuple[str, List[str]]:
        """
        Validate and recover XML with ExceptionalValue injection.

        Uses sdcvalidator's validate_with_recovery to automatically
        insert ExceptionalValue elements for validation errors.

        Args:
            xml_content: Original XML content with validation errors
            errors: List of error dicts from validate() (used for field labeling)

        Returns:
            Tuple of (recovered_xml_string, list_of_corrected_field_xpaths)
        """
        if self.validator is None:
            return xml_content, []

        try:
            from sdcvalidator import etree_tostring
            recovered_tree = self.validator.validate_with_recovery(xml_content)
            recovered_xml = etree_tostring(recovered_tree, namespaces=True)

            corrected_fields = [
                error.get('xpath', 'unknown')
                for error in errors
            ]

            return recovered_xml, corrected_fields
        except Exception as e:
            logger.error("ExceptionalValue recovery failed: %s", e)
            return xml_content, []

    def validate_and_recover(self, xml_content: str) -> ValidationResult:
        """
        Validate XML and automatically recover with ExceptionalValues.

        Combines validate() and auto_correct_with_evs() in a single call.

        Args:
            xml_content: XML string to validate

        Returns:
            ValidationResult with recovered XML if errors were found
        """
        result = self.validate(xml_content)

        if not result.is_valid and result.errors:
            recovered_xml, corrected_fields = self.auto_correct_with_evs(
                xml_content, result.errors
            )
            result.recovered_xml = recovered_xml
            result.auto_corrected_fields = corrected_fields

        return result
