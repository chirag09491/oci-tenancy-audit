# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421

from .scm_configuration import ScmConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalScmConfiguration(ScmConfiguration):
    """
    An external SCM configuration extends a SCM Configuration with necessary data to reach and use the Source Code Management tool/platform used by a Remediation Recipe.
    An external SCM in ADM refers to GitHub, or GitLab.
    """

    #: A constant which can be used with the external_scm_type property of a ExternalScmConfiguration.
    #: This constant has a value of "GITHUB"
    EXTERNAL_SCM_TYPE_GITHUB = "GITHUB"

    #: A constant which can be used with the external_scm_type property of a ExternalScmConfiguration.
    #: This constant has a value of "GITLAB"
    EXTERNAL_SCM_TYPE_GITLAB = "GITLAB"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalScmConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.adm.models.ExternalScmConfiguration.scm_type` attribute
        of this class is ``EXTERNAL_SCM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scm_type:
            The value to assign to the scm_type property of this ExternalScmConfiguration.
            Allowed values for this property are: "OCI_CODE_REPOSITORY", "EXTERNAL_SCM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scm_type: str

        :param branch:
            The value to assign to the branch property of this ExternalScmConfiguration.
        :type branch: str

        :param build_file_location:
            The value to assign to the build_file_location property of this ExternalScmConfiguration.
        :type build_file_location: str

        :param is_automerge_enabled:
            The value to assign to the is_automerge_enabled property of this ExternalScmConfiguration.
        :type is_automerge_enabled: bool

        :param external_scm_type:
            The value to assign to the external_scm_type property of this ExternalScmConfiguration.
            Allowed values for this property are: "GITHUB", "GITLAB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type external_scm_type: str

        :param repository_url:
            The value to assign to the repository_url property of this ExternalScmConfiguration.
        :type repository_url: str

        :param username:
            The value to assign to the username property of this ExternalScmConfiguration.
        :type username: str

        :param pat_secret_id:
            The value to assign to the pat_secret_id property of this ExternalScmConfiguration.
        :type pat_secret_id: str

        """
        self.swagger_types = {
            'scm_type': 'str',
            'branch': 'str',
            'build_file_location': 'str',
            'is_automerge_enabled': 'bool',
            'external_scm_type': 'str',
            'repository_url': 'str',
            'username': 'str',
            'pat_secret_id': 'str'
        }

        self.attribute_map = {
            'scm_type': 'scmType',
            'branch': 'branch',
            'build_file_location': 'buildFileLocation',
            'is_automerge_enabled': 'isAutomergeEnabled',
            'external_scm_type': 'externalScmType',
            'repository_url': 'repositoryUrl',
            'username': 'username',
            'pat_secret_id': 'patSecretId'
        }

        self._scm_type = None
        self._branch = None
        self._build_file_location = None
        self._is_automerge_enabled = None
        self._external_scm_type = None
        self._repository_url = None
        self._username = None
        self._pat_secret_id = None
        self._scm_type = 'EXTERNAL_SCM'

    @property
    def external_scm_type(self):
        """
        **[Required]** Gets the external_scm_type of this ExternalScmConfiguration.
        The type of External Source Code Management.

        Allowed values for this property are: "GITHUB", "GITLAB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The external_scm_type of this ExternalScmConfiguration.
        :rtype: str
        """
        return self._external_scm_type

    @external_scm_type.setter
    def external_scm_type(self, external_scm_type):
        """
        Sets the external_scm_type of this ExternalScmConfiguration.
        The type of External Source Code Management.


        :param external_scm_type: The external_scm_type of this ExternalScmConfiguration.
        :type: str
        """
        allowed_values = ["GITHUB", "GITLAB"]
        if not value_allowed_none_or_none_sentinel(external_scm_type, allowed_values):
            external_scm_type = 'UNKNOWN_ENUM_VALUE'
        self._external_scm_type = external_scm_type

    @property
    def repository_url(self):
        """
        **[Required]** Gets the repository_url of this ExternalScmConfiguration.
        The repository URL for the SCM.
        For Non-Enterprise GitHub the expected format is https://github.com/[owner]/[repoName]
        For Enterprise GitHub the expected format is http(s)://[hostname]/api/v3/repos/[owner]/[repoName]
        For GitLab the expected format is https://gitlab.com/[groupName]/[repoName]


        :return: The repository_url of this ExternalScmConfiguration.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this ExternalScmConfiguration.
        The repository URL for the SCM.
        For Non-Enterprise GitHub the expected format is https://github.com/[owner]/[repoName]
        For Enterprise GitHub the expected format is http(s)://[hostname]/api/v3/repos/[owner]/[repoName]
        For GitLab the expected format is https://gitlab.com/[groupName]/[repoName]


        :param repository_url: The repository_url of this ExternalScmConfiguration.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def username(self):
        """
        Gets the username of this ExternalScmConfiguration.
        The username for the SCM (to perform operations such as cloning or pushing via HTTP).


        :return: The username of this ExternalScmConfiguration.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ExternalScmConfiguration.
        The username for the SCM (to perform operations such as cloning or pushing via HTTP).


        :param username: The username of this ExternalScmConfiguration.
        :type: str
        """
        self._username = username

    @property
    def pat_secret_id(self):
        """
        **[Required]** Gets the pat_secret_id of this ExternalScmConfiguration.
        The Oracle Cloud Identifier (`OCID`__) of the Private Access Token (PAT) Secret.
        The secret provides the credentials necessary to authenticate against the SCM.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The pat_secret_id of this ExternalScmConfiguration.
        :rtype: str
        """
        return self._pat_secret_id

    @pat_secret_id.setter
    def pat_secret_id(self, pat_secret_id):
        """
        Sets the pat_secret_id of this ExternalScmConfiguration.
        The Oracle Cloud Identifier (`OCID`__) of the Private Access Token (PAT) Secret.
        The secret provides the credentials necessary to authenticate against the SCM.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param pat_secret_id: The pat_secret_id of this ExternalScmConfiguration.
        :type: str
        """
        self._pat_secret_id = pat_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
