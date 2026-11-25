#!/usr/bin/env bash
set -euo pipefail

input=${1:-spotifycharts.csv}
output=${2:-spotifycharts_track_id.csv}

ruby -rcsv -e '
  input, output = ARGV
  CSV.open(input, "r") do |source|
    headers = source.shift
    abort "Input CSV is missing the url column" unless headers&.include?("url")
    url_index = headers.index("url")
    headers[url_index] = "track_id"

    CSV.open(output, "w") do |out|
      out << headers
      source.each do |fields|
        url = fields[url_index].to_s
        fields[url_index] = url.split("/track/", 2).last.to_s.split(/[?\/#]/, 2).first
        out << fields
      end
    end
  end
' "$input" "$output"
