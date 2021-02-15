# Copyright 2020-2021 Sebastian Ramacher <sebastian.ramacher@ait.ac.at>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Optional, Tuple, Mapping

class PrivateKey:
    def __init__(self, buf: Optional[bytes] = None) -> None: ...
    @property
    def param(self) -> int: ...
    @property
    def pk(self) -> "PublicKey": ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __neq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class PublicKey:
    def __init__(self, buf: Optional[bytes] = None) -> None: ...
    @property
    def param(self) -> int: ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __neq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

Picnic_L1_FS: int
Picnic_L1_UR: int
Picnic_L3_FS: int
Picnic_L3_UR: int
Picnic_L5_FS: int
Picnic_L5_UR: int
Picnic3_L1: int
Picnic3_L3: int
Picnic3_L5: int
Picnic_L1_full: int
Picnic_L3_full: int
Picnic_L5_full: int

ALL_PARAMETERS: Tuple[int]
SUPPORTED_PARAMETERS: Tuple[int]
PARAMETER_NAMES: Mapping[int, str]
PRIVATE_KEY_SIZE: Mapping[int, int]
PUBLIC_KEY_SIZE: Mapping[int, int]

def keygen(param: int) -> Tuple[PrivateKey, PublicKey]: ...
def validate_keypair(sk: PrivateKey, pk: PublicKey) -> bool: ...
def sign(sk: PrivateKey, message: bytes) -> bytes: ...
def verify(pk: PublicKey, message: bytes, signature: bytes) -> bool: ...
