# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from .discovery_details import DiscoveryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoacsDiscoveryDetails(DiscoveryDetails):
    """
    Specifies the credentials to access the source SOACS instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SoacsDiscoveryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.SoacsDiscoveryDetails.type` attribute
        of this class is ``SOACS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SoacsDiscoveryDetails.
            Allowed values for this property are: "JCS", "SOACS", "OIC", "OAC", "ICS", "PCS"
        :type type: str

        :param weblogic_user:
            The value to assign to the weblogic_user property of this SoacsDiscoveryDetails.
        :type weblogic_user: str

        :param weblogic_password:
            The value to assign to the weblogic_password property of this SoacsDiscoveryDetails.
        :type weblogic_password: str

        """
        self.swagger_types = {
            'type': 'str',
            'weblogic_user': 'str',
            'weblogic_password': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'weblogic_user': 'weblogicUser',
            'weblogic_password': 'weblogicPassword'
        }

        self._type = None
        self._weblogic_user = None
        self._weblogic_password = None
        self._type = 'SOACS'

    @property
    def weblogic_user(self):
        """
        **[Required]** Gets the weblogic_user of this SoacsDiscoveryDetails.
        The SOACS instance weblogic admin user


        :return: The weblogic_user of this SoacsDiscoveryDetails.
        :rtype: str
        """
        return self._weblogic_user

    @weblogic_user.setter
    def weblogic_user(self, weblogic_user):
        """
        Sets the weblogic_user of this SoacsDiscoveryDetails.
        The SOACS instance weblogic admin user


        :param weblogic_user: The weblogic_user of this SoacsDiscoveryDetails.
        :type: str
        """
        self._weblogic_user = weblogic_user

    @property
    def weblogic_password(self):
        """
        **[Required]** Gets the weblogic_password of this SoacsDiscoveryDetails.
        The SOACS instance weblogic admin password


        :return: The weblogic_password of this SoacsDiscoveryDetails.
        :rtype: str
        """
        return self._weblogic_password

    @weblogic_password.setter
    def weblogic_password(self, weblogic_password):
        """
        Sets the weblogic_password of this SoacsDiscoveryDetails.
        The SOACS instance weblogic admin password


        :param weblogic_password: The weblogic_password of this SoacsDiscoveryDetails.
        :type: str
        """
        self._weblogic_password = weblogic_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other