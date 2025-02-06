[CmdletBinding()]
param (
    [string[]] $Modules
)
Install-PSResource platyPS -TrustRepository -PassThru | Format-List
Import-Module platyPS -Force
Import-Module $Modules -Force
foreach ($module in $Modules) {
    Get-Command -Module [IO.Path]::GetFileNameWithoutExtension($module)
}
