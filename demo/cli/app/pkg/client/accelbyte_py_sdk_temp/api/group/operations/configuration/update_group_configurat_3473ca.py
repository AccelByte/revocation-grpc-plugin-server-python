# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: ags_py_codegen

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

# AccelByte Gaming Services Group Service (2.16.3)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HeaderStr
from .....core import HttpResponse

from ...models import ModelsUpdateGroupConfigurationGlobalRulesRequestV1
from ...models import ModelsUpdateGroupConfigurationResponseV1
from ...models import ResponseErrorResponse


class UpdateGroupConfigurationGlobalRuleAdminV1(Operation):
    """update existing configuration global rule (updateGroupConfigurationGlobalRuleAdminV1)

    Required permission 'ADMIN:NAMESPACE:{namespace}:GROUP:CONFIGURATION [UPDATE]'




    This endpoint is used to update existing global rule configuration based on the allowed action. It will replace the permission with the request




    Action Code: 73106

    Required Permission(s):
        - ADMIN:NAMESPACE:{namespace}:GROUP:CONFIGURATION [UPDATE]

    Properties:
        url: /group/v1/admin/namespaces/{namespace}/configuration/{configurationCode}/rules/{allowedAction}

        method: PUT

        tags: ["Configuration"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        body: (body) REQUIRED ModelsUpdateGroupConfigurationGlobalRulesRequestV1 in body

        allowed_action: (allowedAction) REQUIRED str in path

        configuration_code: (configurationCode) REQUIRED str in path

        namespace: (namespace) REQUIRED str in path

    Responses:
        200: OK - ModelsUpdateGroupConfigurationResponseV1 (OK)

        400: Bad Request - ResponseErrorResponse (20019: unable to parse request body | 20002: validation error)

        401: Unauthorized - ResponseErrorResponse (20001: unauthorized access)

        403: Forbidden - ResponseErrorResponse (20013: insufficient permissions | 20022: token is not user token)

        404: Not Found - ResponseErrorResponse (73131: global configuration not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
    """

    # region fields

    _url: str = "/group/v1/admin/namespaces/{namespace}/configuration/{configurationCode}/rules/{allowedAction}"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BEARER_AUTH"]]
    _location_query: str = None

    body: ModelsUpdateGroupConfigurationGlobalRulesRequestV1  # REQUIRED in [body]
    allowed_action: str  # REQUIRED in [path]
    configuration_code: str  # REQUIRED in [path]
    namespace: str  # REQUIRED in [path]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def securities(self) -> List[List[str]]:
        return self._securities

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        if not hasattr(self, "body") or self.body is None:
            return None
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "allowed_action"):
            result["allowedAction"] = self.allowed_action
        if hasattr(self, "configuration_code"):
            result["configurationCode"] = self.configuration_code
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_body(
        self, value: ModelsUpdateGroupConfigurationGlobalRulesRequestV1
    ) -> UpdateGroupConfigurationGlobalRuleAdminV1:
        self.body = value
        return self

    def with_allowed_action(
        self, value: str
    ) -> UpdateGroupConfigurationGlobalRuleAdminV1:
        self.allowed_action = value
        return self

    def with_configuration_code(
        self, value: str
    ) -> UpdateGroupConfigurationGlobalRuleAdminV1:
        self.configuration_code = value
        return self

    def with_namespace(self, value: str) -> UpdateGroupConfigurationGlobalRuleAdminV1:
        self.namespace = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelsUpdateGroupConfigurationGlobalRulesRequestV1()
        if hasattr(self, "allowed_action") and self.allowed_action:
            result["allowedAction"] = str(self.allowed_action)
        elif include_empty:
            result["allowedAction"] = ""
        if hasattr(self, "configuration_code") and self.configuration_code:
            result["configurationCode"] = str(self.configuration_code)
        elif include_empty:
            result["configurationCode"] = ""
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[
        Union[None, ModelsUpdateGroupConfigurationResponseV1],
        Union[None, HttpResponse, ResponseErrorResponse],
    ]:
        """Parse the given response.

        200: OK - ModelsUpdateGroupConfigurationResponseV1 (OK)

        400: Bad Request - ResponseErrorResponse (20019: unable to parse request body | 20002: validation error)

        401: Unauthorized - ResponseErrorResponse (20001: unauthorized access)

        403: Forbidden - ResponseErrorResponse (20013: insufficient permissions | 20022: token is not user token)

        404: Not Found - ResponseErrorResponse (73131: global configuration not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(
            code=code, content_type=content_type, content=content
        )
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return (
                ModelsUpdateGroupConfigurationResponseV1.create_from_dict(content),
                None,
            )
        if code == 400:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 401:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 403:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 404:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 500:
            return None, ResponseErrorResponse.create_from_dict(content)

        return self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelsUpdateGroupConfigurationGlobalRulesRequestV1,
        allowed_action: str,
        configuration_code: str,
        namespace: str,
        **kwargs,
    ) -> UpdateGroupConfigurationGlobalRuleAdminV1:
        instance = cls()
        instance.body = body
        instance.allowed_action = allowed_action
        instance.configuration_code = configuration_code
        instance.namespace = namespace
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> UpdateGroupConfigurationGlobalRuleAdminV1:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = (
                ModelsUpdateGroupConfigurationGlobalRulesRequestV1.create_from_dict(
                    dict_["body"], include_empty=include_empty
                )
            )
        elif include_empty:
            instance.body = ModelsUpdateGroupConfigurationGlobalRulesRequestV1()
        if "allowedAction" in dict_ and dict_["allowedAction"] is not None:
            instance.allowed_action = str(dict_["allowedAction"])
        elif include_empty:
            instance.allowed_action = ""
        if "configurationCode" in dict_ and dict_["configurationCode"] is not None:
            instance.configuration_code = str(dict_["configurationCode"])
        elif include_empty:
            instance.configuration_code = ""
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "allowedAction": "allowed_action",
            "configurationCode": "configuration_code",
            "namespace": "namespace",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "body": True,
            "allowedAction": True,
            "configurationCode": True,
            "namespace": True,
        }

    # endregion static methods
