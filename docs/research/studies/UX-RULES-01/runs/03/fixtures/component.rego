package uxcomponent
import rego.v1
recommendation := "met" if { input.preferenceMet == true } else := "excepted" if {
 input.exceptionApproved == true
 input.exceptionComponent == input.componentId
} else := "unmet"
assessment := {"applicable": true, "permitted": input.mandatoryMet, "requirement": data.uxshared.requirement, "recommendation": recommendation} if {
 data.uxshared.applicable
} else := {"applicable": false, "permitted": null, "requirement": "not-applicable", "recommendation": "not-applicable"}
