---
layout: documentation
toc: true
source: https://github.com/DevOpsJeremy/ConvertTo-Module
feedback: true
module:
  - name: ConvertTo-Module
    path: https://github.com/DevOpsJeremy/ConvertTo-Module
category:
  - powershell
  - documentation
---
# ConvertTo-Module
## Syntax
```powershell
ConvertTo-Module
    [-Source] <String>
    [[-Destination] <String>]
    [[-Name] <String>]
    [-FileList <String[]>]
    [-ModuleList <Object[]>]
    [-FunctionsToExport <String[]>]
    [-AliasesToExport <String[]>]
    [-VariablesToExport <String[]>]
    [-CmdletsToExport <String[]>]
    [-DscResourcesToExport <String[]>]
    [-Tags <String[]>]
    [-RequiredAssemblies <String[]>]
    [-ProjectUri <Uri>]
    [-LicenseUri <Uri>]
    [-IconUri <Uri>]
    [-ReleaseNotes <String>]
    [-Prerelease <String>]
    [-ExternalModuleDependencies <String[]>]
    [-PrivateData <Object>]
    [-ScriptsToProcess <String[]>]
    [-TypesToProcess <String[]>]
    [-HelpInfoUri <String>]
    [-PrivateFunctions <String[]>]
    [-CompatiblePSEditions <String[]>]
    [-NestedModules <Object[]>]
    [-Guid <Guid>]
    [-Author <String>]
    [-CompanyName <String>]
    [-Copyright <String>]
    [-FormatsToProcess <String[]>]
    [-ModuleVersion <Version>]
    [-ProcessorArchitecture <ProcessorArchitecture>]
    [-PowerShellVersion <Version>]
    [-CLRVersion <Version>]
    [-DotNetFrameworkVersion <Version>]
    [-PowerShellHostName <String>]
    [-PowerShellHostVersion <Version>]
    [-RequiredModules <Object[]>]
    [-Description <String>]
    [-DefaultCommandPrefix <String>]
```
## Description
This function takes a simple PowerShell script (.ps1) of functions, creates the directory structure for a PowerShell module, generates the module manifest (`.psd1) and script module (`.psm1), and populates the module directories with the functions.

The directory structure is as follows:
    <Module Name>\
        private\
            functions\
                <Private Function Files (`.ps1`)>
            Types.ps1
        public\
            functions\
                <Public Function Files (`.ps1`)>
        <Module Name>.psd1
        <Module Name>.psm1
## Examples
### Example 1
```powershell
ConvertTo-Module -Name Confluence -Source Confluence.ps1 -PrivateFunctions ConfluenceExpandPropertyArgumentCompleter -Author 'Jeremy Watkins'
```
This command creates the Confluence PowerShell module and directory structure. It exports the private function(s) (ConfluenceExpandPropertyArgumentCompleter) into the Confluence\private\functions directory and sets the author as 'Jeremy Watkins'.
### Example 2
```powershell
ConvertTo-Module -Name ConfiForms -Source ConfiForms.ps1 -Author 'Jeremy Watkins' -Description 'ConfiForms functions' `
Import-Module ConfiForms\ConfiForms.psd1
```
These commands create the ConfiForms PowerShell module and directory structure, sets the author and description, then imports the module.
## Parameters
### **-Source**
&ensp;&ensp;&ensp;&ensp;Source script from which to create the module.


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | 1 |
| Default value | None |
| Accept pipeline input | False |
### **-Destination**
&ensp;&ensp;&ensp;&ensp;Destination directory. A new sub-directory will be created using the name provided to the `-Name` parameter. Default is the current directory.


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | 2 |
| Default value | $PWD.Path |
| Accept pipeline input | False |
### **-Name**
&ensp;&ensp;&ensp;&ensp;The name of the module. This will be used as the directory, mainifest, and module script names.


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | 3 |
| Default value | None |
| Accept pipeline input | False |
### **-FileList**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-filelist


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-ModuleList**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-modulelist


| Attribute | Value |
| --- | --- |
| Type | Object[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-FunctionsToExport**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-functionstoexport


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-AliasesToExport**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-aliasestoexport


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-VariablesToExport**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-variablestoexport


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-CmdletsToExport**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-cmdletstoexport


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-DscResourcesToExport**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-dscresourcestoexport


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Tags**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-tags


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-RequiredAssemblies**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-requiredassemblies


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-ProjectUri**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-projecturi


| Attribute | Value |
| --- | --- |
| Type | Uri |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-LicenseUri**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-licenseuri


| Attribute | Value |
| --- | --- |
| Type | Uri |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-IconUri**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-iconuri


| Attribute | Value |
| --- | --- |
| Type | Uri |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-ReleaseNotes**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-releasenotes


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Prerelease**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-prerelease


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-ExternalModuleDependencies**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-externalmoduledependencies


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-PrivateData**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-privatedata


| Attribute | Value |
| --- | --- |
| Type | Object |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-ScriptsToProcess**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-scriptstoprocess


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-TypesToProcess**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-typestoprocess


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-HelpInfoUri**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-helpinfouri


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-PrivateFunctions**
&ensp;&ensp;&ensp;&ensp;Any functions from the `-Source` script which do not need to be exported for use. This is typically for any functions which are only used by other functions in the module and do not need to be available to users at the console, etc.


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-CompatiblePSEditions**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-compatiblepseditions


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | @(
            'Destkop',
            'Core'
        ) |
| Accept pipeline input | False |
### **-NestedModules**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-nestedmodules


| Attribute | Value |
| --- | --- |
| Type | Object[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Guid**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-guid


| Attribute | Value |
| --- | --- |
| Type | Guid |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Author**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-author


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-CompanyName**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-companyname


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Copyright**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-copyright


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-FormatsToProcess**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-formatstoprocess


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-ModuleVersion**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-moduleversion


| Attribute | Value |
| --- | --- |
| Type | Version |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-ProcessorArchitecture**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-processorarchitecture


| Attribute | Value |
| --- | --- |
| Type | ProcessorArchitecture |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-PowerShellVersion**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-powershellversion


| Attribute | Value |
| --- | --- |
| Type | Version |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-CLRVersion**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-clrversion


| Attribute | Value |
| --- | --- |
| Type | Version |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-DotNetFrameworkVersion**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-dotnetframeworkversion


| Attribute | Value |
| --- | --- |
| Type | Version |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-PowerShellHostName**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-powershellhostname


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-PowerShellHostVersion**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-powershellhostversion


| Attribute | Value |
| --- | --- |
| Type | Version |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-RequiredModules**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-requiredmodules


| Attribute | Value |
| --- | --- |
| Type | Object[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Description**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-description


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-DefaultCommandPrefix**
&ensp;&ensp;&ensp;&ensp;Pass-through parameter for `New-ModuleManifest`. See Microsoft documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest#-defaultcommandprefix


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
## Inputs
#### [**String**](https://learn.microsoft.com/en-us/dotnet/api/System.String)
#### [**String[]**](https://learn.microsoft.com/en-us/dotnet/api/System.String)
#### [**Object[]**](https://learn.microsoft.com/en-us/dotnet/api/System.Object)
#### [**Guid**](https://learn.microsoft.com/en-us/dotnet/api/System.Guid)
#### [**Version**](https://learn.microsoft.com/en-us/dotnet/api/System.Version)
#### [**ProcessorArchitecture**](https://learn.microsoft.com/en-us/dotnet/api/System.Reflection.ProcessorArchitecture)
#### [**Object**](https://learn.microsoft.com/en-us/dotnet/api/System.Object)
#### [**Uri**](https://learn.microsoft.com/en-us/dotnet/api/System.Uri)
## Outputs
#### **None**
## Notes
Version: 1.0.0.0
## Related Links
- [ConvertTo-Module](https://devopsjeremy.github.io/documentation/powershell/ConvertTo-Module.html)
- [Source](https://github.com/DevOpsJeremy/ConvertTo-Module)
- [About PowerShell Modules](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_modules)
- [New-ModuleManifest](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/new-modulemanifest)