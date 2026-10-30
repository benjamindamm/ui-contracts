package uxprobe
import rego.v1

# Own experimental UX policy; not a built-in Rego component vocabulary.
candidate if {
 input.existingEntriesOnly == true
 input.singleSelection == true
}

decision := "unknown" if {
 not is_boolean(input.existingEntriesOnly)
} else := "unknown" if {
 not is_boolean(input.singleSelection)
} else := "candidate" if {
 candidate
} else := "unsuitable"

# Opposite rule conclusions are both retained; no hidden override policy.
conclusions contains "recommend" if { input.existingEntriesOnly == true }
conclusions contains "exclude" if { input.existingEntriesOnly == true }
