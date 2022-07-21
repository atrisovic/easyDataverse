# generated by datamodel-codegen:
#   filename:  codeMeta.json
#   timestamp: 2022-07-20T14:10:53+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from easyDataverse.core import DataverseBase
from pydantic import Field


class DevelopmentStatus(Enum):
    """
    Description of development status, e.g. work in progress (wip), active, inactive, suspended. See repostatus.org for more information.
    """

    concept = 'concept'
    wip = 'wip'
    active = 'active'
    inactive = 'inactive'
    unsupported = 'unsupported'
    moved = 'moved'
    suspended = 'suspended'
    abandoned = 'abandoned'


class SoftwareRequirements(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Name or title of the required software/library',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaSoftwareRequirementsTitle',
    )
    url: Optional[str] = Field(
        None,
        description='Link to required software/library',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaSoftwareRequirementsUrl',
    )


class SoftwareSuggestions(DataverseBase):
    name: Optional[str] = Field(
        None,
        description='Name or title of the optional software/library',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaSoftwareSuggestionsTitle',
    )
    url: Optional[str] = Field(
        None,
        description='Link to optional software/library',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaSoftwareSuggestionsUrl',
    )


class CodeMeta(DataverseBase):
    software_requirements: List[SoftwareRequirements] = Field(
        default_factory=list,
        description='Required software dependencies',
        multiple=True,
        typeClass='compound',
        typeName='codeMetaSoftwareRequirements',
    )
    software_version: Optional[str] = Field(
        None,
        description='Version of the software instance, usually following some convention like SemVer etc.',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaSoftwareVersion',
    )
    development_status: Optional[DevelopmentStatus] = Field(
        None,
        description='Description of development status, e.g. work in progress (wip), active, inactive, suspended. See repostatus.org for more information.',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='codeMetaDevelopmentStatus',
    )
    code_repository: Optional[List] = Field(
        None,
        description='Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex, institutional GitLab instance, etc.).',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaCodeRepository',
    )
    programming_language: Optional[List] = Field(
        None,
        description='The programming language(s) used to implement the software (e.g. Python, C++, Matlab, Fortran, Java, Julia,default_factory=list)',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaProgrammingLanguage',
    )
    operating_systems: Optional[List] = Field(
        None,
        description='Operating systems supported (e.g. Windows 10, OSX 11.3, Android 11).',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaOperatingSystem',
    )
    application_category: Optional[List] = Field(
        None,
        description='Type of software application, e.g. Simulation, Analysis, Visualisation.',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaApplicationCategory',
    )
    application_subcategory: Optional[List] = Field(
        None,
        description='Subcategory of the application, e.g. Arcade Game.',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaApplicationSubCategory',
    )
    software_help_documentation: Optional[List] = Field(
        None,
        description='Link to help texts or documentation',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaSoftwareHelp',
    )
    build_instructions: Optional[str] = Field(
        None,
        description='Link to installation instructions/documentation',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaBuildInstructions',
    )
    runtime_platform: Optional[List] = Field(
        None,
        description='Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0). Supersedes runtime.',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaRuntimePlatform',
    )
    target_product: Optional[List] = Field(
        None,
        description='Target Operating System / Product to which the code applies. If applies to several versions, just the product name can be used.',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaTargetProduct',
    )
    permissions: Optional[List] = Field(
        None,
        description='Permission(s) required to run the code (for example, a mobile app may require full internet access or may run only on wifi).',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaPermissions',
    )
    memory_requirements: Optional[List] = Field(
        None,
        description='Minimum memory requirements.',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaMemoryRequirements',
    )
    processor_requirements: Optional[List] = Field(
        None,
        description='Processor architecture required to run the application (e.g. IA64).',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaProcessorRequirements',
    )
    storage_requirements: Optional[str] = Field(
        None,
        description='Storage requirements (e.g. free space required).',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaStorageRequirements',
    )
    release_notes: Optional[str] = Field(
        None,
        description='Link to release notes',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaReleaseNotes',
    )
    continous_integration: Optional[List] = Field(
        None,
        description='Link to continuous integration service',
        multiple=True,
        typeClass='primitive',
        typeName='codeMetaContIntegration',
    )
    issue_tracker: Optional[str] = Field(
        None,
        description='Link to software bug reporting or issue tracking system',
        multiple=False,
        typeClass='primitive',
        typeName='codeMetaIssueTracker',
    )
    software_suggestions: List[SoftwareSuggestions] = Field(
        default_factory=list,
        description='Optional dependencies , e.g. for optional features, code development, etc.',
        multiple=True,
        typeClass='compound',
        typeName='codeMetaSoftwareSuggestions',
    )
    _metadatablock_name: Optional[str] = 'codeMeta'


    def add_software_requirements(
        self,
        name: Optional[str] = None,
        url: Optional[str] = None,
    ):
        """Function used to add an instance of SoftwareRequirements to the metadatablock.

        Args:
        
            name (string): Name or title of the required software/library
            url (string): Link to required software/library

        """

        self.software_requirements.append(
            SoftwareRequirements(
                name=name, url=url
            )
        )


    def add_software_suggestions(
        self,
        name: Optional[str] = None,
        url: Optional[str] = None,
    ):
        """Function used to add an instance of SoftwareSuggestions to the metadatablock.

        Args:
        
            name (string): Name or title of the optional software/library
            url (string): Link to optional software/library

        """

        self.software_suggestions.append(
            SoftwareSuggestions(
                name=name, url=url
            )
        )
