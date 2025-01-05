---
title: Getting Assigned Parameters in PowerShell
status: new
date:
  created: 2023-10-16
authors:
  - jeremy
tags:
  - powershell
---
Have you ever needed to pass a number of parameter values from one function into another function with some (but not all) of the same parameters? I've run into this particular pain point multiple times when writing functions in the past so I decided to find somewhat of a workaround.

# `$PSBoundParameters`
If you've spent some time writing PowerShell functions, you may be familiar with the [`$PSBoundParameters`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables#psboundparameters) automatic variable. As Microsoft defines it, this variable

> Contains a dictionary of the parameters that are passed to a script or function and their current values.

Let's take a look at the below example. We'll write a simple function to return the contents of the `$PSBoundParameters` variable:

```powershell
PS > function Get-BoundParameters {
    param (
        $Parameter1,
        $Parameter2,
        $Parameter3
    )
    $PSBoundParameters
}
PS > Get-BoundParameters -Parameter1 'this is param1' -Parameter3 'this is param3'

Key        Value
---        -----
Parameter1 this is param1
Parameter3 this is param3
```

As you can see, the `$PSBoundParameters` variable contains the parameters `Parameter1` and `Parameter3` and their contents, but does _not_ contain `Parameter2` since I never used that parameter.

`$PSBoundParameters` comes in handy quite often for things like checking whether a certain parameter has been used:

```powershell
PS > function Get-Foods {
    param (
        [Parameter(Mandatory)]
        $Fruits,
        $Vegetables
    )
    $message = "Here are the fruits"
    if ($PSBoundParameters.ContainsKey('Vegetables')){
        $message += " and vegetables"
    }
    Write-Output $message
    $Fruits + $Vegetables | ForEach-Object { "- $_" }
}
PS > Get-Foods -Fruits apple, orange -Vegetables carrot, celery
Here are the fruits and vegetables
- apple
- orange
- carrot
- celery
```
In this example, we use `$PSBoundParameters` to check if it contains the key 'Vegetables' (meaning the `$Vegetables` parameter was used), and if it does we add the phrase " and vegetables" to the end of the return message.

Now that we understand how `$PSBoundParameters` works, let's examine where it falls short.

# Default Values
While `$PSBoundParameters` is great, the issue is that it only contains _bound_ parameters (as the name suggests). This means that if a parameter has a default value the default value will never be included in the `$PSBoundParameters` dictionary.

I've run into this situation many times when writing functions that pass certain parameter key/values to other commands, such as this example:

```powershell
PS > function Get-UserItems {
    param (
        $Name,
        $Items
    )
    Write-Output "$Name has the following items:"
    foreach ($Item in $Items){
        "- $Item"
    }
}
PS > function Get-UserItemsParent {
    param (
        $Name = "Bob",
        $Items
    )
    Get-UserItems @PSBoundParameters
}
PS > Get-UserItemsParent -Items apple, orange, carrot, celery
 has the following items:
- apple
- orange
- carrot
- celery
```
In the above example you'll notice that, while the fruits and vegetables in the `$Items` variable were passed on from the `Get-UserItemsParent` function to the `Get-UserItems` function via the `$PSBoundParameters` variable, the name Bob was not because "Bob" is the default value of the `$Name` parameter, but that parameter wasn't actually used by the user and as such is not part of `$PSBoundParameters`. This is the dilemma we're here to solve.
> ## Splatting
> As an aside, I'll briefly explain what splatting is and how it works.
> 
> In the `Get-UserItemsParent` function, we used a method called **splatting** when calling the `Get-UserItems` function. Splatting is a way to pass all parameters and values to a command as a dictionary instead of writing them out the long way. As an example, this:
> ```powershell
> $parameters = @{
>    Name = 'Get-UserItems'
>    CommandType = 'Function'
> }
> Get-Command @parameters
> ```
> Is the same as this:
> ```powershell
> Get-Command -Name 'Get-UserItems' -CommandType 'Function'
> ```
> Note that when splatting, the dictionary variable (in this case, `$parameters`) is written with an `@` sign instead of a `$`.
>
> If you're unfamiliar with splatting, I highly recommend reading [the documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting) to learn how you can take advantage of it in your scripts. I'll likely cover it and more ways to use it in a future post but for now, back to the article.


# Getting _Assigned_ Parameters

What we're really looking for is akin to a `$PSAssignedParameters` variable, which in theory would contain _assigned_ parameters (i.e. any parameters with values, whether from the user or from default values). Unfortunately, this isn't a real variable (at least [not yet](https://github.com/PowerShell/PowerShell/issues/3285)), but the below code snippet is a suitable workaround:

```powershell
$PSAssignedParameters = @{}
[System.Management.Automation.CommandMetaData]::new(
    $MyInvocation.MyCommand
).Parameters.GetEnumerator() | ForEach-Object {
    $var = Get-Variable -Name $_.key -ValueOnly
    if ($var){
        $PSAssignedParameters[$_.key] = $var
    }
}
```
Here's the breakdown of what we're doing:
```powershell
$PSAssignedParameters = @{}
```
Here we create the `$PSAssignedParameters` hashtable to which we'll be adding the assigned parameters.
```powershell
[System.Management.Automation.CommandMetaData]::new($MyInvocation.MyCommand).Parameters.GetEnumerator()
```
The `$MyInvocation` automatic variable and its `MyCommand` property represents the command that's currently running. Creating a new `[CommandMetaData]` object with the current command allows us to find _all_ parameters available for the command by accessing the `Parameters` property. These parameters and information about the parameters are stored as a dictionary. Finally, `GetEnumerator()` allows us to iterate ("loop") through each of the parameters in the dictionary.
```powershell
$var = Get-Variable -Name $_.key -ValueOnly
```
While looping through the parameters, we use the `Get-Variable` cmdlet to get the value of each parameter.
```powershell
if ($var){
    $PSAssignedParameters[$_.key] = $var
}
```
If the parameter value (`$var`) is not empty, add it to the `$PSAssignedParameters` hashtable.

And that's it! All we need are 7 lines to get all parameters with assigned values. In the next section I'll discuss how we can build this into a function for reusability.

# `Get-AssignedParameter` Function

We can use this `Get-AssignedParameter` function in our scripts as a replacement for the missing `$PSAssignedParameters` variable.
```powershell
function Get-AssignedParameter {
    param (
        [System.Management.Automation.InvocationInfo] $Invocation
    )
    $PSAssignedParameters = @{}
    [System.Management.Automation.CommandMetaData]::new($Invocation.MyCommand).Parameters.GetEnumerator() | ForEach-Object {
        $var = Get-Variable -Name $_.key -ValueOnly 
        if ($var){
            $PSAssignedParameters[$_.key] = $var
        }
    }
    $PSAssignedParameters.Clone()
}
```
The function can be used as-is, but let's see if we can improve it. It occurred to me that, while getting the assigned parameters is the goal, there are times when we may want to include or exclude specific parameters. Instead of repeatedly writing code in our scripts to remove unwanted keys from `$PSAssignedParameters`, let's add that functionality to the function.

```powershell
function Get-AssignedParameter {
    param (
        [System.Management.Automation.InvocationInfo] $Invocation,
        [string[]] $Include,
        [string[]] $Exclude
    )
    $PSAssignedParameters = @{}
    [System.Management.Automation.CommandMetaData]::new($Invocation.MyCommand).Parameters.GetEnumerator() | ForEach-Object {
        if ($Include){
            if ($_.key -in $Include){
                $var = Get-Variable -Name $_.key -ValueOnly 
                if ($var){
                    $PSAssignedParameters[$_.key] = $var
                }
            }
        } elseif ($_.key -notin $Exclude){
            $var = Get-Variable -Name $_.key -ValueOnly 
            if ($var){
                $PSAssignedParameters[$_.key] = $var
            }
        }
    }
    $PSAssignedParameters.Clone()
}
```
Here I added the `$Include` and `$Exclude` parameters along with the corresponding logic:
- If `$Include` is used, only return parameters in the `$Include` array
- If `$Exclude` is used, only return parameters _not_ in the `$Exclude` array

While we'd hope nobody would try to use the `$Include` and `$Exclude` parameters at the same time, we'll want to follow PowerShell [best practices](https://github.com/PoshCode/PowerShellPracticeAndStyle/blob/master/Style-Guide/Function-Structure.md) and ensure our function can't be used in unintended ways. To accomplish this, we'll use [Parameter Sets](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_parameter_sets):

```powershell
param (
    [System.Management.Automation.InvocationInfo] $Invocation,
    [Parameter(
        ParameterSetName = 'Include'
    )]
    [string[]] $Include,
    [Parameter(
        ParameterSetName = 'Exclude'
    )]
    [string[]] $Exclude
)
```
By defining the `$Include` and `$Exclude` parameters as two different parameter sets, we allow PowerShell to do the work for us. As we can see when we run `Get-Help` against our function:

```powershell
NAME
    Get-AssignedParameter

SYNTAX
    Get-AssignedParameter [-Invocation <InvocationInfo>] [-Include <string[]>]

    Get-AssignedParameter [-Invocation <InvocationInfo>] [-Exclude <string[]>]
```
The two parameters are part of separate parameter sets and thus it's impossible to use both parameters at the same time.

Finally, we'll add our `CmdletBinding` and some comments:

```powershell
function Get-AssignedParameter {
    <#
    .SYNOPSIS
        Gets all parameters with assigned values.
    .DESCRIPTION
        This function returns any parameters from a provided invocation with assigned values--whether that be bound parameter values provided by the user, or default values.
    .PARAMETER Invocation
        The invocation from which to find the parameters. Typically this will be the automatic variable `$MyInvocation` within a function or script.
    .PARAMETER Include
        A string array of parameter names to include in the returned result. If this parameter is used, only parameters in this list will be returned.
    .PARAMETER Exclude
        A string array of parameter names to exclude from the returned result. If this parameter is used, any parameters in this list will not be returned.
    .OUTPUTS
        System.Collections.Hashtable
    .LINK
        https://DevOpsJeremy.github.io/documentation/powershell/Get-AssignedParameter.html
    .LINK
        Getting Assigned Parameters in PowerShell: https://devopsjeremy.github.io/powershell/2023/10/16/getting-assigned-parameters.html
    .EXAMPLE
        Get-AssignedParameter -Invocation $MyInvocation

        Gets any assigned parameter key/values.
    .EXAMPLE
        Get-AssignedParameter -Invocation $MyInvocation -Include Name,Status

        Gets the 'Name' and 'Status' parameter key/values if they are assigned.
    .EXAMPLE
        Get-AssignedParameter -Invocation $MyInvocation -Exclude ComputerName

        Gets any parameter key/values which are assigned, excluding the 'ComputerName' parameter.
    #>
    [CmdletBinding(
        DefaultParameterSetName = 'Exclude'
    )]
    param (
        [System.Management.Automation.InvocationInfo] $Invocation,
        [Parameter(
            ParameterSetName = 'Include'
        )]
        [string[]] $Include,
        [Parameter(
            ParameterSetName = 'Exclude'
        )]
        [string[]] $Exclude
    )
    $PSAssignedParameters = @{}
    [System.Management.Automation.CommandMetaData]::new($Invocation.MyCommand).Parameters.GetEnumerator() | ForEach-Object {
        if ($Include){
            if ($_.key -in $Include){
                $var = Get-Variable -Name $_.key -ValueOnly 
                if ($var){
                    $PSAssignedParameters[$_.key] = $var
                }
            }
        } elseif ($_.key -notin $Exclude){
            $var = Get-Variable -Name $_.key -ValueOnly 
            if ($var){
                $PSAssignedParameters[$_.key] = $var
            }
        }
    }
    $PSAssignedParameters.Clone()
}
```
<sup>[Gist](https://gist.github.com/DevOpsJeremy/db0b082b39ac10533de09a83b43640e0)</sup>

And now our function is complete! Let's test it out using our function from earlier:

```powershell
PS > function Get-UserItems {
    param (
        $Name,
        $Items
    )
    Write-Output "$Name has the following items:"
    foreach ($Item in $Items){
        "- $Item"
    }
}
PS > function Get-UserItemsParent {
    param (
        $Name = "Bob",
        $Items
    )
    $PSAssignedParameters = Get-AssignedParameters -Invocation $MyInvocation
    Get-UserItems @PSAssignedParameters
}
PS > Get-UserItemsParent -Items apple, orange, carrot, celery
Bob has the following items:
- apple
- orange
- carrot
- celery
```

As we can see, not only did the `$Items` parameter get passed to the child function, but so did the default value of `$Name`. I hope you found this article helpful--be sure to subscribe to the RSS feed and the socials below to keep up with future posts.

For further information, check out [the documentation](/documentation/powershell/Get-AssignedParameter.html) for this function.

#### Jeremy Watkins