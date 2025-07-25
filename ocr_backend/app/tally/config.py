"""
Tally Configuration

Configuration settings for Tally connector library.
"""

import os
from pathlib import Path


class TallyConfig:
    """Configuration class for Tally connector settings."""
    
    # Tally Connection Settings
    DEFAULT_VERSION = "legacy"  # or "latest"
    DEFAULT_HOST = "http://localhost:9000"
    
    # Alternative library directories for different versions
    # _PARENT = Path(__file__).parent
    _PARENT = "/Users/vaibhavholani/development/business/OCR-Platform/ocr_backend/app/tally"

    LEGACY_LIB_DIR = os.path.join(_PARENT, "tally_dll_files", "lib")
    LATEST_LIB_DIR = os.path.join(_PARENT, "tally_dll_files", "lib_new_name_space")


    DEFAULT_LIB_DIR = LEGACY_LIB_DIR  # Default to legacy
    
    # Default values for entity creation
    DEFAULT_LEDGER_GROUP = "Sundry Debtors"
    DEFAULT_SUPPLIER_GROUP = "Sundry Creditors"
    DEFAULT_STOCK_GROUP = "Primary"
    DEFAULT_UNIT = "PCS"
    DEFAULT_GODOWN = "Main Location"
    DEFAULT_BATCH = "Primary Batch"
    
    # Sales and Purchase ledger defaults
    DEFAULT_SALES_LEDGER = "Sales Account"
    DEFAULT_PURCHASE_LEDGER = "Imported Goods"
    
    # Voucher defaults
    DEFAULT_VOUCHER_VIEW = "Invoice Voucher View"
    
    @classmethod
    def get_lib_dir(cls, version: str = None) -> str:
        """Get the appropriate library directory based on version."""
        if version == "latest":
            return cls.LATEST_LIB_DIR
        elif version == "legacy":
            return cls.LEGACY_LIB_DIR
        else:
            return cls.DEFAULT_LIB_DIR
    
    @classmethod
    def get_default_ledger_group(cls, ledger_type: str = "customer") -> str:
        """Get default ledger group based on type."""
        if ledger_type.lower() in ["supplier", "vendor", "creditor"]:
            return cls.DEFAULT_SUPPLIER_GROUP
        else:
            return cls.DEFAULT_LEDGER_GROUP
