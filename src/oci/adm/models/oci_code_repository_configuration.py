# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421

from .scm_configuration import ScmConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciCodeRepositoryConfiguration(ScmConfiguration):
    """
    An OCI Code repository configuration extends a SCM Configuration with necessary data to reach and use the OCI DevOps Code Repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciCodeRepositoryConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.adm.models.OciCodeRepositoryConfiguration.scm_type` attribute
        of this class is ``OCI_CODE_REPOSITORY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scm_type:
            The value to assign to the scm_type property of this OciCodeRepositoryConfiguration.
            Allowed values for this property are: "OCI_CODE_REPOSITORY", "EXTERNAL_SCM"
        :type scm_type: str

        :param branch:
            The value to assign to the branch property of this OciCodeRepositoryConfiguration.
        :type branch: str

        :param build_file_location:
            The value to assign to the build_file_location property of this OciCodeRepositoryConfiguration.
        :type build_file_location: str

        :param is_automerge_enabled:
            The value to assign to the is_automerge_enabled property of this OciCodeRepositoryConfiguration.
        :type is_automerge_enabled: bool

        :param oci_code_repository_id:
            The value to assign to the oci_code_repository_id property of this OciCodeRepositoryConfiguration.
        :type oci_code_repository_id: str

        """
        self.swagger_types = {
            'scm_type': 'str',
            'branch': 'str',
            'build_file_location': 'str',
            'is_automerge_enabled': 'bool',
            'oci_code_repository_id': 'str'
        }

        self.attribute_map = {
            'scm_type': 'scmType',
            'branch': 'branch',
            'build_file_location': 'buildFileLocation',
            'is_automerge_enabled': 'isAutomergeEnabled',
            'oci_code_repository_id': 'ociCodeRepositoryId'
        }

        self._scm_type = None
        self._branch = None
        self._build_file_location = None
        self._is_automerge_enabled = None
        self._oci_code_repository_id = None
        self._scm_type = 'OCI_CODE_REPOSITORY'

    @property
    def oci_code_repository_id(self):
        """
        **[Required]** Gets the oci_code_repository_id of this OciCodeRepositoryConfiguration.
        The Oracle Cloud Identifier (`OCID`__) of the OCI DevOps repository.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The oci_code_repository_id of this OciCodeRepositoryConfiguration.
        :rtype: str
        """
        return self._oci_code_repository_id

    @oci_code_repository_id.setter
    def oci_code_repository_id(self, oci_code_repository_id):
        """
        Sets the oci_code_repository_id of this OciCodeRepositoryConfiguration.
        The Oracle Cloud Identifier (`OCID`__) of the OCI DevOps repository.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param oci_code_repository_id: The oci_code_repository_id of this OciCodeRepositoryConfiguration.
        :type: str
        """
        self._oci_code_repository_id = oci_code_repository_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
