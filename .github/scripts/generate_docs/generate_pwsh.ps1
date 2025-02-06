[CmdletBinding()]
param (
    [string[]] $Files
)
Install-PSResource platyPS -TrustRepository -PassThru
"--- Files ---"
$Files
