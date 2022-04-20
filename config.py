#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    # LUIS_APP_ID = os.environ.get("LuisAppId", "606dbc00-24c4-4f47-9af4-e0992e633784")
    # LUIS_API_KEY = os.environ.get("LuisAPIKey", "")
    # # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    # LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "")
