# Get-LoremIpsum
## Syntax
```powershell
Get-LoremIpsum
    [-Paragraphs <Int32>]
```
```powershell
Get-LoremIpsum
    [-Sentences <Int32>]
```
```powershell
Get-LoremIpsum
    [-Words <Int32>]
```
## Description
Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document without relying on meaningful content. This cmdlet generates the filler text in varying amounts--words, sentences, or paragraphs.
## Examples
### Example 1
```powershell
Get-LoremIpsum
Generates filler text. The default is 1 paragraph of 2 to 6 sentences.
```

### Example 2
```powershell
Get-LoremIpsum -Sentences 3
Generates 3 sentences of filler text.
```

### Example 3
```powershell
Get-LoremIpsum -Paragraphs 2
Generates 2 paragraphs of filler text.
```

### Example 4
```powershell
Get-LoremIpsum -Words 10
Generates 10 words of filler text.
```

## Parameters
### **-Paragraphs**
&ensp;&ensp;&ensp;&ensp;Number of paragraphs to generate.


| Attribute | Value |
| --- | --- |
| Type | Int32 |
| Position | named |
| Default value | 1 |
| Accept pipeline input | False |
### **-Sentences**
&ensp;&ensp;&ensp;&ensp;Number of sentences to generate.


| Attribute | Value |
| --- | --- |
| Type | Int32 |
| Position | named |
| Default value | 1 |
| Accept pipeline input | False |
### **-Words**
&ensp;&ensp;&ensp;&ensp;Number of words to generate.


| Attribute | Value |
| --- | --- |
| Type | Int32 |
| Position | named |
| Default value | 1 |
| Accept pipeline input | False |
## Inputs
#### [**Int32**](https://learn.microsoft.com/en-us/dotnet/api/System.Int32)
## Outputs
#### **None**
## Notes
Version: 0.0
## Related Links
