package uxprobe
import rego.v1

# Own UX experiment profile. Missing/null must be guarded before typed evaluation.
candidate if {
 input.existingEntriesOnly == true
 input.singleSelection == true
}

decision := "unknown" if {
 object.get(input, "existingEntriesOnly", null) == null
} else := "unknown" if {
 object.get(input, "singleSelection", null) == null
} else := "invalid-input" if {
 not is_boolean(input.existingEntriesOnly)
} else := "invalid-input" if {
 not is_boolean(input.singleSelection)
} else := "candidate" if {
 candidate
} else := "unsuitable"
