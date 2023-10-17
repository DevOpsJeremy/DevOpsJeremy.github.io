---
layout: post
title: Getting Assigned Parameters in PowerShell
categories: powershell
author:
- Jeremy Watkins
---
Have you ever needed to pass a number of parameter values from one function into another function with some (but not all) of the same parameters? I've run into this particular pain point multiple times when writing functions in the past so I decided to find somewhat of a workaround.

# $PSBoundParameters
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
Now that we understand how `$PSBoundParameters` works, let's examine the issue
Where `$PSBoundParameters` falls short, however, is that it only contains _bound_ parameters (as the name suggests). This means that if a parameter has a default value the default value will never be included in the `$PSBoundParameters`