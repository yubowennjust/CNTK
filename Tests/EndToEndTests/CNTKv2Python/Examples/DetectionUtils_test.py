# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import os
import pytest
import sys

abs_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(abs_path)
sys.path.append(os.path.join(abs_path, "..", "..", "..", "..", "Examples", "Image", "Detection", "utils"))

pytest.mark.skipif(((sys.platform == 'win32' and sys.version_info[:2] != (3,5)) or (sys.platform == 'linux' and sys.version_info[:2] != (3,4))), reason="it runs only on linux-py34 and windows-py35 due to cython modules")
def test_rpn_component():
    from unit_tests import test_proposal_layer, test_proposal_target_layer, test_anchor_target_layer
    test_proposal_layer()
    test_proposal_target_layer()
    test_anchor_target_layer()
