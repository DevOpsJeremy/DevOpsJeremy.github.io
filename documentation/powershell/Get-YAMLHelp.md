---
layout: documentation
module:
  - name: Documentation
    path: https://github.com/DevOpsJeremy/Documentation
category:
  - powershell
  - documentation
---
# Get-YAMLHelp
## Syntax
```powershell
Get-YAMLHelp
    [-Path] <FileInfo>
```
## Description
This function takes a YAML file and captures the "comment-based help" information from the file, then returns it as an object with those keywords.

The function accepts the following comment-based help keywords:
    - SYNOPSIS
    - DESCRIPTION
    - EXAMPLE
    - INPUTS
    - OUTPUTS
    - NOTES
    - LINK
    - COMPONENT
    - FUNCTIONALITY
    - ROLE
## Examples
### Example 1
```powershell
Get-YAMLHelp -Path file.yml `
Synopsis    : Creates a new EC2 instance `
Description : {This playbook creates a new EC2 instance.} `
Examples    : {Get-YAMLHelp.YAMLExample} `
Inputs      : {region, instance_name} `
Outputs     : `
Notes       : `
Link        : `
Role        :
```

## Parameters
### **-Path**
&ensp;&ensp;&ensp;&ensp;Path of the YAML file.


| Attribute | Value |
| --- | --- |
| Type | FileInfo |
| Position | 1 |
| Default value | None |
| Accept pipeline input | False |
## Inputs
#### [**FileInfo**](https://learn.microsoft.com/en-us/dotnet/api/System.IO.FileInfo)
## Outputs
#### **None**
## Notes
Version: 0.0
## Related Links
