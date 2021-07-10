# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '6a1a63ef-b919-4a74-b75e-9369e10ad67d'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '804134ae-f211-41ea-8faa-a12fa8ec4874'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    #TENANT_ID = '7f565ca3-52a4-4afb-bd01-742df1734cf4'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'bddcb30f-fb47-4f19-b2a4-14b2540cf535'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    #CLIENT_SECRET = 'uX.R~oigrcMIJ2j1BMEsR6e4j3B-64D-Ti'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations/'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'Kris2pisz@kris1piszczyahoo.onmicrosoft.com'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'Pikdata55'