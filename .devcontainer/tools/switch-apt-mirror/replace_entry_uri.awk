# Usage: awk -v type_match=TYPE -v suite_match=SUITE -v new_uri=URI -f replace_entry_uri.awk <file>

function has_suite(dist) {
  return (dist ~ /-(updates|backports|security)$/)
}
{
  # Skip empty lines
  if (NF == 0) { print; next }

  # Skip commented lines
  if ($0 ~ /^#/) { print; next }

  # Parse type (field 1)
  entry_type = $1

  # Handle optional [options] in field 2
  if ($2 ~ /^\[/) {
    entry_options = $2
    entry_uri = $3
    entry_dist = $4
  } else {
    entry_options = ""
    entry_uri = $2
    entry_dist = $3
  }

  # Type match logic
  type_ok = (type_match == "all" || entry_type == type_match)

  # Suite match logic
  suite_ok = 0
  if (suite_match == "all") {
    suite_ok = 1
  } else if (has_suite(entry_dist)) {
    split(entry_dist, arr, "-")
    suite_ok = (arr[2] == suite_match)
  } else if (suite_match == "main") {
    suite_ok = !has_suite(entry_dist)
  }

  # If both match, replace URI
  if (type_ok && suite_ok) {
    if (entry_options != "") {
      $3 = new_uri
    } else {
      $2 = new_uri
    }
  }

  # Print the modified or unmodified line
  print
}
