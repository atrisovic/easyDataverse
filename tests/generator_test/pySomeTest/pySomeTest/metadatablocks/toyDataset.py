# generated by datamodel-codegen:
#   filename:  toyDataset.json
#   timestamp: 2022-07-21T17:20:41+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from easyDataverse.core import DataverseBase
from pydantic import Field


class SomeEnum(Enum):
    """
    Some enum field
    """

    enum = 'enum'


class Compound(DataverseBase):
    bar: Optional[str] = Field(
        None,
        description='Another primitive field',
        multiple=False,
        typeClass='primitive',
        typeName='fooCompoundField',
    )


class ToyDataset(DataverseBase):
    compound: List[Compound] = Field(
        default_factory=list,
        description='Some compound field',
        multiple=False,
        typeClass='compound',
        typeName='fooCompound',
    )
    foo: Optional[str] = Field(
        None,
        description='Some primitive field',
        multiple=False,
        typeClass='primitive',
        typeName='fooField',
    )
    some_enum: Optional[SomeEnum] = Field(
        None,
        description='Some enum field',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='fooEnum',
    )
    _metadatablock_name: Optional[str] = 'toyDataset'


    def add_compound(
        self,
        bar: Optional[str] = None,
    ):
        """Function used to add an instance of Compound to the metadatablock.

        Args:
        
            bar (string): Another primitive field

        """

        self.compound.append(
            Compound(
                bar=bar
            )
        )
