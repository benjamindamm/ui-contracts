package uxshared
import rego.v1
# One shared experimental library requirement; no automatic inheritance.
applicable if {
 input.library == "example"
 input.componentId == "ui-contracts:Autocomplete"
}
requirement := "met" if { input.mandatoryMet == true } else := "unmet"
