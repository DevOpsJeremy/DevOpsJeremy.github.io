# New-Documentation
## Syntax
```powershell
New-Documentation
    [-Name] <String>
    [-OutputType <String>]
    [-LoremIpsum]
    [-HeadingLevel <Int32>]
```
```powershell
New-Documentation
    -File <FileInfo>
    [-OutputType <String>]
    [-LoremIpsum]
    [-HeadingLevel <Int32>]
```
```powershell
New-Documentation
    -Cmdlet <CmdletInfo>
    [-OutputType <String>]
    [-LoremIpsum]
    [-HeadingLevel <Int32>]
```
```powershell
New-Documentation
    -Function <FunctionInfo>
    [-OutputType <String>]
    [-LoremIpsum]
    [-HeadingLevel <Int32>]
```
## Description
New-Documentation generates documentation for a cmdlet, function, script, or YAML file in any of the following formats: Confluence HTML, Confluence Wiki markup, Markdown language. This utilizes PowerShell's comment-based help system to pull help information from an object such as Synopsis, Description, Examples, Parameters, etc.
## Examples
### Example 1
```powershell
New-Documentation -Name New-Item -OutputType ConfluenceHtml -LoremIpsum
Generates documentation for New-Item and returns the output in Confluence HTML format. The `-LoremIpsum` switch parameter populates any missing information with filler-text.
```

### Example 2
```powershell
Get-Item MyScript.ps1 | New-Documentation -OutputType Markdown
Generates documentation for the MyScript.ps1 script and returns the output in Markdown format.
```

### Example 3
```powershell
Get-Item MyPlaybook.yml | New-Documentation -OutputType ConfluenceWiki -HeadingLevel 2
Generates documentation for the MyPlaybook.yml YAML file and returns the output in Confluence Wiki markup format, with all headings starting at level 2.
```

### Example 4
```powershell
Get-Command Get-Service | New-Documentation -LoremIpsum | Out-File Get-Service.md
Generates documentation for the Get-Service cmdlet and returns the output in the default format of Markdown. The `-LoremIpsum` switch parameter populates any missing information with filler-text. Outputs the results to the Get-Service.md Markdown file.
```

### Example 5
```powershell
Get-Command MyFunction | New-Documentation -OutputType ConfluenceHtml -HeadingLevel 2
Generates documentation for the MyFunction function and returns the output in Confluence HTML format, with all headings starting at level 2.
```

## Parameters
### **-Name**
&ensp;&ensp;&ensp;&ensp;Name of an object for which to generate documentation. Any Name that can be used with `Get-Help`.


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | 1 |
| Default value | None |
| Accept pipeline input | False |
### **-File**
&ensp;&ensp;&ensp;&ensp;A File from which to generate documentation. This can be a PowerShell script (.ps1) or a YAML file (.yml/.yaml). This parameter accepts pipeline input; see examples.


| Attribute | Value |
| --- | --- |
| Type | FileInfo |
| Position | named |
| Default value | None |
| Accept pipeline input | True |
### **-Cmdlet**
&ensp;&ensp;&ensp;&ensp;A Cmdlet from which to generate documentation. Must be a System.Management.Automation.CmdletInfo object. This parameter accepts pipeline input; see examples.


| Attribute | Value |
| --- | --- |
| Type | CmdletInfo |
| Position | named |
| Default value | None |
| Accept pipeline input | True |
### **-Function**
&ensp;&ensp;&ensp;&ensp;A Function from which to generate documentation. Must be a System.Management.Automation.FunctionInfo object. This parameter accepts pipeline input; see examples.


| Attribute | Value |
| --- | --- |
| Type | FunctionInfo |
| Position | named |
| Default value | None |
| Accept pipeline input | True |
### **-OutputType**
&ensp;&ensp;&ensp;&ensp;The format of the returned output. Options are Markdown, ConfluenceWiki, and ConfluenceHtml. Default is Markdown.


| Attribute | Value |
| --- | --- |
| Type | String |
| Position | named |
| Default value | Markdown |
| Accept pipeline input | False |
### **-LoremIpsum**
&ensp;&ensp;&ensp;&ensp;A switch parameter for enabling Lorem Ipsum text. Lorem Ipsum is auto-generated filler text to used to populate the output. This is useful for if the object doesn't already contain the help text (e.g.: Synopsis, Description, etc.), but the user wants to get the general structure of the end result.


| Attribute | Value |
| --- | --- |
| Type | SwitchParameter |
| Position | named |
| Default value | False |
| Accept pipeline input | False |
### **-HeadingLevel**
&ensp;&ensp;&ensp;&ensp;The Heading Level from which to start. All subsequent headings are incremented accordingly. Options are 1, 2, or 3. Default is 1.


| Attribute | Value |
| --- | --- |
| Type | Int32 |
| Position | named |
| Default value | 1 |
| Accept pipeline input | False |
## Inputs
#### [**String**](https://learn.microsoft.com/en-us/dotnet/api/System.String)
#### [**FileInfo**](https://learn.microsoft.com/en-us/dotnet/api/System.IO.FileInfo)
#### [**CmdletInfo**](https://learn.microsoft.com/en-us/dotnet/api/System.Management.Automation.CmdletInfo)
#### [**FunctionInfo**](https://learn.microsoft.com/en-us/dotnet/api/System.Management.Automation.FunctionInfo)
#### [**SwitchParameter**](https://learn.microsoft.com/en-us/dotnet/api/System.Management.Automation.SwitchParameter)
#### [**Int32**](https://learn.microsoft.com/en-us/dotnet/api/System.Int32)
## Outputs
#### **None**
## Notes
Version: 0.0
## Related Links
- [New-Documentation](https://jerdub1993.github.io/documentation/powershell/new-documentation.html)
- [Confluence Wiki syntax](https://confluence.atlassian.com/doc/confluence-wiki-markup-251003035.html)
- [Markdown syntax](https://www.markdownguide.org/cheat-sheet/)
- [PowerShell Comment-Based Help](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comment_based_help)
