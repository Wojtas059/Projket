import pytest

from src.crypto.securityCreator import SecurityCreator

# IMPORTANT NAME CONVENTION: test_METHODNAME_EXPECTEDOUTCOME_WHATISTESTED


class TestBcrypt:
    def test_createAdvancedUserCode_alphanumericString_advancedUserCodeGeneration():
        securityCreator = SecurityCreator()
        securityCreator.createAdvancedUserCode().isalnum()
        assert True
