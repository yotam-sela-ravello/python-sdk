# Copyright 2012-2014 Ravello Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

if sys.version_info[:2] < (3,3):
    sys.stderr.write('This driver requires Python >= 3.3\n')
    sys.stderr.write('Please use "nosetests" instead.\n')
    sys.exit(1)

from unittest import TestLoader, TextTestRunner

testdir = os.path.split(os.path.abspath(__file__))[0]
os.chdir(testdir)

loader = TestLoader()
tests = loader.discover('.', 'flow_*.py')

runner = TextTestRunner(verbosity=2, buffer=True)
runner.run(tests)
