---
layout: documentation
category:
  - powershell
  - documentation
---
# Get-AssignedParameter
Gets all parameters with assigned values.
## Syntax
```powershell
Get-AssignedParameter
    [-Invocation <InvocationInfo>]
    [-Exclude <String[]>]
```
```powershell
Get-AssignedParameter
    [-Invocation <InvocationInfo>]
    [-Include <String[]>]
```
## Description
This function returns any parameters from a provided invocation with assigned values--whether that be bound parameter values provided by the user, or default values.
## Examples
### Example 1
```powershell
Get-AssignedParameter -Invocation $MyInvocation
```
Gets any assigned parameter key/values.
### Example 2
```powershell
Get-AssignedParameter -Invocation $MyInvocation -Include Name,Status
```
Gets the 'Name' and 'Status' parameter key/values if they are assigned.
### Example 3
```powershell
Get-AssignedParameter -Invocation $MyInvocation -Exclude ComputerName
```
Gets any parameter key/values which are assigned, excluding the 'ComputerName' parameter.
## Parameters
### **-Invocation**
&ensp;&ensp;&ensp;&ensp;The invocation from which to find the parameters. Typically this will be the automatic variable `$MyInvocation` within a function or script.


| Attribute | Value |
| --- | --- |
| Type | InvocationInfo |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Include**
&ensp;&ensp;&ensp;&ensp;A string array of parameter names to include in the returned result. If this parameter is used, only parameters in this list will be returned.


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
### **-Exclude**
&ensp;&ensp;&ensp;&ensp;A string array of parameter names to exclude from the returned result. If this parameter is used, any parameters in this list will not be returned.


| Attribute | Value |
| --- | --- |
| Type | String[] |
| Position | named |
| Default value | None |
| Accept pipeline input | False |
## Inputs
#### [**InvocationInfo**](https://learn.microsoft.com/en-us/dotnet/api/System.Management.Automation.InvocationInfo)
#### [**String[]**](https://learn.microsoft.com/en-us/dotnet/api/System.String)
## Outputs
#### [**Hashtable**](https://learn.microsoft.com/en-us/dotnet/api/System.Collections.Hashtable)
## Notes
## Related Links
- [Get-AssignedParameter](https://DevOpsJeremy.github.io/documentation/powershell/Get-AssignedParameter.html)
- [Getting Assigned Parameters in PowerShell](https://devopsjeremy.github.io/powershell/2023/10/16/getting-assigned-parameters.html)