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
